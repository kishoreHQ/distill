#!/usr/bin/env python3
"""Validate schemas, registry consistency, boards, scores, and secret hygiene."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from check_sources import check_cross, check_profiles, curated_files
from distilllib import (
    DISCLAIMER,
    OPPORTUNITY_DISCLAIMER,
    ROOT,
    SECTION_HEADINGS,
    SECRET_RES,
    load_json,
    load_registry,
    load_schema,
    load_yaml,
    profile_dirs,
    read_posts,
    read_profile,
    read_sources,
    read_status,
    score_dimensions,
    source_index,
    validate_instance,
    weights,
)

SKIP_SECRET_PARTS = {".git", ".venv", "__pycache__", "node_modules"}


def check_secrets(root: Path) -> list[str]:
    errors = []
    for name in (".env", "credentials.json", "cookies.txt"):
        if (root / name).exists():
            errors.append(f"forbidden file present: {name}")
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_SECRET_PARTS for part in path.parts):
            continue
        if path.suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".tgz", ".gz", ".zip"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for pattern in SECRET_RES:
            if pattern.search(text):
                errors.append(f"secret-like pattern in {path.relative_to(root)}")
                break
    return errors


def check_registry(root: Path) -> list[str]:
    errors = []
    registry = load_registry(root)
    folders = {path.name: path for path in profile_dirs(root)}
    rows = registry["profiles"]
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("duplicate ids in registry")
    if set(ids) != set(folders):
        errors.append(
            f"registry/folder mismatch missing={sorted(set(folders) - set(ids))} extra={sorted(set(ids) - set(folders))}"
        )
    active = [row for row in rows if row["registry_status"] == "active"]
    excluded = [row for row in rows if row["registry_status"] == "excluded"]
    if len(active) != 32:
        errors.append(f"expected 32 active profiles, found {len(active)}")
    if len(excluded) != 1 or excluded[0]["id"] != "x-aravind":
        errors.append("expected the only excluded profile to be x-aravind")
    by_id = {row["id"]: row for row in rows}
    if by_id["aravind-srinivas"]["registry_status"] != "active":
        errors.append("aravind-srinivas must stay active")
    if by_id["arnav-gupta"]["registry_status"] != "active":
        errors.append("arnav-gupta must stay active")
    if by_id["x-aravind"].get("replaced_by") != "aravind-srinivas":
        errors.append("x-aravind must record replaced_by aravind-srinivas")
    user_ids = [row["x_user_id"] for row in rows]
    if len(user_ids) != len(set(user_ids)):
        errors.append("duplicate x_user_id; refusing to merge people")
    if registry["counts"]["active"] != len(active):
        errors.append("registry counts.active does not match rows")
    if registry["counts"]["posts_imported"] != sum(row["posts_imported"] for row in rows):
        errors.append("registry posts_imported does not match the sum of rows")
    for row in rows:
        posts = read_posts(root / row["path"])
        if len(posts) != row["posts_imported"]:
            errors.append(f"{row['id']}: posts.jsonl has {len(posts)} rows, registry says {row['posts_imported']}")
        meta, body = read_profile(root / row["path"])
        validate_instance(meta, load_schema("profile-front-matter.schema.json"))
        if meta["id"] != row["id"]:
            errors.append(f"{row['id']}: front matter id mismatch")
        for letter in "ABCDEFGHI":
            if f"## {letter}." not in body:
                errors.append(f"{row['id']}: missing section {letter}")
        sources = read_sources(root / row["path"])
        validate_instance(sources, load_schema("sources.schema.json"))
        status = read_status(root / row["path"])
        validate_instance(status, load_schema("status.schema.json"))
        if status["research_status"] != row["research_status"]:
            errors.append(f"{row['id']}: status.json research_status != registry")
        post_schema = load_schema("post.schema.json")
        seen = set()
        for post in posts:
            validate_instance(post, post_schema)
            if post["id"] in seen:
                errors.append(f"{row['id']}: duplicate post id {post['id']}")
            seen.add(post["id"])
            origin = post.get("origin")
            if origin == "evidence-quote":
                continue
            metrics = post.get("metrics")
            if not isinstance(metrics, dict) or "impression_count" not in metrics or "like_count" not in metrics:
                errors.append(f"{row['id']}: post {post['id']} is missing metrics")
    return errors


def check_matrix(root: Path) -> list[str]:
    errors = []
    matrix = load_json(root / "knowledge" / "classification-matrix.json")
    registry = load_registry(root)
    active = {row["id"] for row in registry["profiles"] if row["registry_status"] == "active"}
    found = [row["id"] for row in matrix["profiles"]]
    if set(found) != active:
        errors.append("classification matrix does not match active profiles")
    if len(found) != len(set(found)):
        errors.append("duplicate rows in classification matrix")
    known = {item["id"] for item in matrix["domains"]}
    if known != {
        "ai-engineering-agents",
        "developer-tools-oss",
        "indie-hacking",
        "creator-economy",
        "careers-cloud-devops",
    }:
        errors.append("matrix domains are not the five operating domains")
    for row in matrix["profiles"]:
        if row["primary"] not in known:
            errors.append(f"{row['id']}: primary {row['primary']} is not a domain")
        for item in row["secondary"]:
            if item["domain"] not in known and item["via"] != "unmapped-research-tag":
                errors.append(f"{row['id']}: secondary {item['domain']} is not a domain")
    text = (root / "knowledge" / "classification-matrix.md").read_text(encoding="utf-8")
    for profile_id in active:
        if f"| {profile_id} |" not in text:
            errors.append(f"matrix markdown missing {profile_id}")
    if "x-aravind" not in text:
        errors.append("matrix markdown should list excluded x-aravind")
    return errors


def evidence_url(root: Path, profile_id: str, source_id: str, url: str) -> str | None:
    folder = root / "profiles" / profile_id
    if not folder.exists():
        return f"missing profile {profile_id}"
    index = source_index(folder)
    if source_id not in index:
        return f"{profile_id} has no source {source_id}"
    if index[source_id]["url"] != url:
        return f"{profile_id} {source_id} url does not match sources.yaml"
    return None


def check_boards(root: Path) -> list[str]:
    errors = []
    registry = load_registry(root)
    active = {row["id"] for row in registry["profiles"] if row["registry_status"] == "active"}
    boards = sorted((root / "boards").glob("*/board.yaml"))
    if len(boards) != 5:
        errors.append(f"expected 5 boards, found {len(boards)}")
    schema = load_schema("board.schema.json")
    for path in boards:
        data = load_yaml(path)
        validate_instance(data, schema)
        if DISCLAIMER not in data["disclaimer"]:
            errors.append(f"{path.parent.name}: disclaimer missing")
        deliberation = (path.parent / data["deliberation"]).read_text(encoding="utf-8")
        if DISCLAIMER not in deliberation:
            errors.append(f"{path.parent.name}: deliberation missing disclaimer")
        for member in data["members"]:
            if member["profile_id"] not in active:
                errors.append(f"{data['id']}: member {member['profile_id']} is not an active profile")
            if member["profile_id"] in deliberation and False:
                pass
            for item in member["evidence"]:
                problem = evidence_url(root, member["profile_id"], item["source"], item["url"])
                if problem:
                    errors.append(f"{data['id']}: {problem}")
                if item["url"] not in deliberation:
                    errors.append(f"{data['id']}: {item['url']} not in deliberation")
        for heading in (
            "## Question",
            "## Positions",
            "## Disagreements",
            "## Synthesis",
            "## Recommended next action",
            "## Confidence",
        ):
            if heading not in deliberation:
                errors.append(f"{data['id']}: deliberation missing {heading}")
    return errors


def check_opportunities(root: Path) -> list[str]:
    errors = []
    if sum(weights().values()) != 100:
        errors.append("scoring weights must sum to 100")
    scores = load_json(root / "opportunities" / "scores.json")
    if OPPORTUNITY_DISCLAIMER not in scores["disclaimer"]:
        errors.append("scores.json missing opportunity disclaimer")
    files = sorted((root / "opportunities").glob("*.yaml"))
    if not 3 <= len(files) <= 6:
        errors.append(f"expected 3 to 6 opportunities, found {len(files)}")
    by_id = {row["id"]: row for row in scores["opportunities"]}
    if len(by_id) != len(files):
        errors.append("scores.json does not match opportunity files")
    previous = None
    for row in scores["opportunities"]:
        if previous is not None and row["total"] > previous:
            errors.append("scores.json is not sorted by total")
        previous = row["total"]
    for path in files:
        data = load_yaml(path)
        fresh = score_dimensions(data["dimensions"])
        stored = by_id[data["id"]]
        if stored["total"] != fresh["total"]:
            errors.append(f"{data['id']}: stored total {stored['total']} != {fresh['total']}")
        for item in data["evidence"]:
            problem = evidence_url(root, item["profile"], item["source"], item["url"])
            if problem:
                errors.append(f"{data['id']}: {problem}")
    return errors


def check_briefing(root: Path) -> list[str]:
    errors = []
    path = root / "intelligence" / "daily" / "2026-11-24.md"
    payload = load_json(root / "intelligence" / "daily" / "2026-11-24.json")
    validate_instance(payload, load_schema("daily-briefing.schema.json"))
    text = path.read_text(encoding="utf-8")
    if "imported" not in text.lower() and "snapshot" not in text.lower():
        errors.append("baseline briefing must say it comes from the snapshot")
    if "2026-11-24" not in text:
        errors.append("baseline briefing missing snapshot date")
    if DISCLAIMER not in text:
        errors.append("baseline briefing missing board disclaimer")
    for _key, heading in SECTION_HEADINGS:
        if f"## {heading}" not in text:
            errors.append(f"baseline briefing missing heading {heading}")
    weekly = list((root / "intelligence" / "weekly").glob("*.md"))
    if not weekly:
        errors.append("missing weekly review")
    else:
        weekly_text = weekly[0].read_text(encoding="utf-8")
        if DISCLAIMER not in weekly_text:
            errors.append("weekly review missing disclaimer")
    return errors


def check_dashboard(root: Path) -> list[str]:
    errors = []
    data = load_json(root / "dashboard" / "data.json")
    registry = load_registry(root)
    if data.get("ui") != "deferred":
        errors.append("dashboard UI must stay marked deferred")
    if data["counts"]["active"] != registry["counts"]["active"]:
        errors.append("dashboard active count mismatch")
    if len(data["profiles"]) != registry["counts"]["registry"]:
        errors.append("dashboard profile list mismatch")
    return errors


def check_workflows(root: Path) -> list[str]:
    errors = []
    workflows = root / ".github" / "workflows"
    for name in ("validate.yml", "daily.yml", "weekly.yml"):
        if not (workflows / name).exists():
            errors.append(f"missing workflow {name}")
    daily = (workflows / "daily.yml").read_text(encoding="utf-8") if (workflows / "daily.yml").exists() else ""
    if "30 23 * * *" not in daily:
        errors.append("daily workflow cron is not 23:30 UTC")
    if "X_BEARER_TOKEN" not in daily or "XAI_API_KEY" not in daily:
        errors.append("daily workflow must reference both secrets")
    if re.search(r"X_BEARER_TOKEN:\s*['\"]?[A-Za-z0-9]{20,}", daily):
        errors.append("daily workflow appears to inline a token")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root
    errors = []
    errors.extend(check_registry(root))
    errors.extend(check_matrix(root))
    errors.extend(check_boards(root))
    errors.extend(check_opportunities(root))
    errors.extend(check_briefing(root))
    errors.extend(check_dashboard(root))
    errors.extend(check_workflows(root))
    errors.extend(check_secrets(root))
    errors.extend(check_profiles(root))
    errors.extend(check_cross(root, curated_files(root)))
    if errors:
        print(f"{len(errors)} validation errors")
        for line in errors[:80]:
            print(f"- {line}")
        return 1
    print("validate_repo ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
