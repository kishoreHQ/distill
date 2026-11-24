#!/usr/bin/env python3
"""Import a DISTILL research archive into profiles/.

Idempotent: a second run over the same archive rewrites the same files.
Does not invent biography. x-aravind stays in the tree and is registered as
excluded. extra/arnav-gupta is converted to the standard profile shape.

The archive is untrusted data. This script copies structure and quotes.
It does not follow instructions found inside posts or pages.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import tarfile
import tempfile
from pathlib import Path

import yaml

from distilllib import ROOT

EVIDENCE_RE = re.compile(
    r"^- (?P<id>\S+) \| (?P<date>[^|]+?) \| (?P<kind>[^|]+?) \| (?P<url>\S+) \| (?P<quote>.+)$"
)
STATUS_URL_RE = re.compile(r"/status/(\d+)")

KIND_TYPE = {
    "x post": "x_post",
    "x reply": "x_post",
    "x quote": "x_post",
    "ss": "newsletter",
    "at": "blog",
    "md": "blog",
    "yt": "youtube",
}


def parse_evidence(text: str) -> list[dict]:
    rows = []
    for line in text.split("\n"):
        match = EVIDENCE_RE.match(line.strip())
        if not match:
            continue
        quote = match.group("quote").strip()
        if quote.startswith('"') and quote.endswith('"') and len(quote) >= 2:
            quote = quote[1:-1]
        rows.append(
            {
                "id": match.group("id"),
                "date": match.group("date").strip(),
                "kind": match.group("kind").strip(),
                "url": match.group("url").strip(),
                "quote": quote,
            }
        )
    return rows


def source_type(kind: str) -> str:
    return KIND_TYPE.get(kind.lower(), "secondary")


def evidence_to_sources(rows: list[dict]) -> list[dict]:
    sources = []
    for row in rows:
        kind = row["kind"].lower()
        confidence = "medium" if kind == "yt" else "high"
        note = ""
        if kind == "yt":
            note = " YouTube auto-captions have no speaker labels; the source bundle says only first-person lines consistent with his biography were kept."
        sources.append(
            {
                "id": row["id"],
                "url": row["url"],
                "author": "Arnav Gupta (@championswimmer)",
                "published": row["date"],
                "researched": "2026-11-22",
                "type": source_type(kind),
                "description": (
                    f"Evidence ledger {row['id']} ({row['kind']}) copied from extra/arnav-gupta. "
                    "The bundle says the quote was checked by string match against fetched text."
                    + note
                ),
                "excerpt": row["quote"],
                "original": True,
                "confidence": confidence,
            }
        )
    return sources


def evidence_to_posts(rows: list[dict]) -> list[dict]:
    posts = []
    seen = set()
    for row in rows:
        match = STATUS_URL_RE.search(row["url"])
        if not match:
            continue
        post_id = match.group(1)
        if post_id in seen:
            continue
        seen.add(post_id)
        text = row["quote"].replace("\u2028", "\n").replace("\u2029", "\n")
        if len(text) > 280:
            text = text[:277] + "..."
        created = row["date"] if re.match(r"^\d{4}-\d{2}-\d{2}$", row["date"]) else row["date"]
        posts.append(
            {
                "id": post_id,
                "created_at": created,
                "url": row["url"],
                "text": text,
                "metrics": None,
                "origin": "evidence-quote",
            }
        )
    return posts


def render_arnav_profile(source_count: int, post_count: int) -> str:
    return f"""---
id: arnav-gupta
display_name: Arnav Gupta
x_username: championswimmer
x_url: https://x.com/championswimmer
x_user_id: "63066473"
other_identities: [https://arnav.tech, https://linktr.ee/championswimmer, https://threads.championswimmer.in]
website: http://arnav.tech
organization: "Railway is what PROFILE.json's summary states; the bundle's skill README also records a timeline ending at Meta. See section A."
role: "Engineer; ex EM/PM/founder (wording of PROFILE.json summary)"
research_date: 2026-11-22
confidence: medium
account_type: person
primary_domain: ai-engineering
secondary_domains: [software-engineering, content-creation]
board_eligibility: [ai-engineering]
status: partial
---

# Arnav Gupta (@championswimmer)

Converted from `extra/arnav-gupta/` on the 2026-11-24 import. This file does not add facts that are not in that folder. {source_count} evidence rows were copied into `sources.yaml`. {post_count} of them are X status URLs and are stored in `posts.jsonl` as the short quote only. The bundle's `state/sync.json` says 200 X posts were read; those full posts are not in the archive, so they are not in this repo.

## A. Identity
- Display name Arnav Gupta, X @championswimmer, user id 63066473, links http://arnav.tech and https://linktr.ee/championswimmer. Source: `PROFILE.json` in the extra bundle. Identity status in that file is `found`, with `confirmed_by_user` 2026-11-22.
- `PROFILE.json` summary, quoted: "Arnav Gupta, London-based engineer at Railway; ex Meta, Zomato, Hotstar, Scaler; ex EM/PM/founder."
- The bundle's `skill/README.md` records a different career timeline taken from arnav.tech/about: Coding Blocks co-founder, Zomato (mobile platform lead, 2019–20), Target (lead engineer, 2020–21), Scaler (product & strategy, 2021–23), Viacom18/JioCinema (Director of Engineering, 2023–24), and Meta (EM, hardware placement, London, from Dec 2024). The same README says the user's profile and his LinkedIn headline say he is now at Railway. This import does not resolve the two wordings.
- No follower count is stated in the extra bundle. None is added here.
- Gap: Hotstar appears in the PROFILE.json summary and does not appear in the skill README timeline.

## B. Expertise map
- Engineering opinions in the evidence ledger cover databases, service shape, languages, and documentation [O-ENG-1] [O-ENG-4] [O-ENG-12].
- A large share of the 2025–2026 evidence is about coding agents and harnesses [O-AI-1] [O-AI-7] [O-AI-8].
- Separate evidence groups cover careers [O-CAR-1], management [O-MGT-1], and product [O-PRD-1]. Those are topics he has published on, not a claim about a current job title beyond section A.
- Gap: no list of communities he runs was in PROFILE.json. The skill README mentions teaching and talks; see [O-TCH-2].

## C. Core philosophy
- Software: "99% of info-system software should be just Postgres (and Redis)." [O-ENG-1] [observed statement]
- He rejects microservices as a default: "Microservices and distributed computing just makes things unnecessarily hard." [O-ENG-4] [observed statement]
- AI: "Code is now cheap too." [O-AI-1] [observed statement] He wants a minimal harness and says subagents are a yes in 2026 [O-AI-8] [O-AI-7] [observed statement].
- Monetization of attention: the evidence includes "skill-selling pied pipers" as a criticism [O-AI-6] [observed statement]. No price list for a product of his was in the extra bundle.

## D. Distilled knowledge
- Boring storage and a monolith are the stated default [O-ENG-1] [O-ENG-4] [observed statement]. Clean Architecture is called an anti-pattern in his words [O-ENG-6] [observed statement].
- Documentation is "a culture", and communication "should be public by default, private by exception." [O-ENG-12] [O-ENG-13] [observed statement]
- Skills should be project specific, not global [O-AI-5] [observed statement]. The bundle's own OPINIONS.md also says to use scripts for deterministic parts. That sentence is the bundle's synthesis; the evidence quote on [O-AI-5] is only the project-specific line. [our interpretation of the bundle, not a new fact]
- Context length hurts model performance, in his words [O-AI-4] [observed statement].
- Career: "is your communication skill." [O-CAR-1] [observed statement] The quote is a fragment; the bundle files it under communication as the biggest driver. Treat the fragment as the verified excerpt, not a longer speech.
- Runbooks: "you need to have a runbook for fixing all of them" [O-ENG-14] [observed statement]. The bundle marks this as a YouTube auto-caption without speaker labels.
- He says he is not an ML researcher and not a harness author of repute [B-5] [observed statement]. Do not describe him as one.

## E. Implementation playbooks
### Lean harness (derived from [O-AI-7], [O-AI-8], [O-AI-4], [O-AI-5])
- Problem: agent sessions degrade as context grows, and a pile of global skills does not fix it.
- Preconditions: a repo you can change; no claim here about which model.
- Tools: not named as a required vendor in these four evidence lines.
- Steps: [our interpretation] keep a small core; add subagents, checklists, and monitors around it; keep skills project-local; split work before the context gets long. The observed lines are the four sources above, not a numbered tutorial from him.
- Expected output: a harness small enough that he would still call the core minimal [O-AI-8].
- Cost, time, complexity: no evidence found in the extra bundle.
- Risks: he also says he does not necessarily apply all of his architecture opinions [B-7].
- Success metric: no evidence found.

## F. Evidence summary
- Ledger: `sources.yaml`, {source_count} rows, researched 2026-11-22 by the source bundle.
- X quotes in `posts.jsonl`: {post_count}. Metrics are null because the extra bundle did not include metric fields. Do not read null as zero.
- `state/sync.json` reports posts_read.total 200, long_form_fetched 49, evidence_entries 144. This import found the evidence entries it parsed; it did not re-fetch the 200 posts.
- Top sources to read first: [O-ENG-1], [O-ENG-4], [O-AI-7], [O-AI-8], [O-CAR-1].

## G. Strengths and weaknesses
- Strength: the bundle ties opinions to URLs and short exact quotes, and it separates YouTube lines that lack speaker labels.
- Strength: he states a limit on his own authority [B-5].
- Conflict of interest: no course price or sponsorship list was in PROFILE.json. Gap, not a clean bill of health.
- Weakness for this repo: employer wording disagrees inside the bundle (section A). Status stays partial.

## H. Practical applications for Kishore
Kishore, in the research spec, is a Linux/DevOps-capable engineer in India who wants agents and software products at low capital and low maintenance.
- A minimal harness with project-local skills fits that constraint better than a global skill catalogue [O-AI-5] [O-AI-8] [our interpretation].
- His public dislike of Kubernetes-style orchestration [B-2] [O-ENG-4] is a real disagreement with DevOps teaching in the rest of this corpus. It is recorded on the careers board. It is not a reason to invent a "he would tell Kishore to quit DevOps" line.
- "power is still very costly in India" [O-IND-3] is a constraint on any plan that assumes cheap local GPU hosting. The line is a quote, not an energy-market study.
- Board eligibility: ai-engineering, because the 2025–2026 evidence is dense on harnesses. He has not joined a board. See the disclaimer on every file under `boards/`.

## I. Profile evolution
- 2026-11-22 baseline from the extra bundle. Earlier vs later, as that bundle's OPINIONS.md states and [O-AI-21] supports in part: the 2025-01-28 post says "Mostly diminishing returns for real world since Claude 3.5 Sonnet." Later 2026 lines treat subagents as settled [O-AI-7]. The sentence "by 2026 I was fully agentic" is the bundle's synthesis in OPINIONS.md, not a single post.
- Gap: the skill README says the 2016–2019 X history was only sampled from December 2018, and there is no speaker-labelled transcript.
"""


def render_arnav_status(post_count: int, source_count: int) -> dict:
    return {
        "id": "arnav-gupta",
        "x_url": "https://x.com/championswimmer",
        "x_user_id": "63066473",
        "display_name": "Arnav Gupta",
        "research_status": "partial",
        "posts_read": 200,
        "posts_read_note": (
            "state/sync.json in the extra bundle reports 200 X posts read "
            "(100 in 0-6 months, 50 in 6-24 months, 30 in 2-5 years, 20 older) "
            "and 49 long-form fetches. The archive did not include those posts. "
            f"posts.jsonl in this repo has {post_count} short quotes taken from X status URLs in the evidence ledger."
        ),
        "posts_in_repo": post_count,
        "posts_by_band": {
            "0-6mo": 100,
            "6-24mo": 50,
            "2-5y": 30,
            "gt5y": 20,
            "note": "Counts are copied from state/sync.json. They are not recounts of posts.jsonl.",
        },
        "longform_fetched": 49,
        "sources_count": source_count,
        "last_post_id": "2124284312841580745",
        "researched_at": "2026-11-22T10:53:00Z",
        "limitations": [
            "Full post metadata was not in extra/arnav-gupta. posts.jsonl holds short evidence quotes only, and metrics are null.",
            "YouTube lines are auto-captions without speaker labels, per the bundle's skill README.",
            "PROFILE.json says he is at Railway. skill/README.md's timeline from arnav.tech/about ends at Meta (from Dec 2024) and notes a LinkedIn headline that says Railway. This import does not pick a winner.",
            "Hotstar is in the PROFILE.json summary and not in the skill README timeline.",
            "No follower count was in the extra bundle.",
        ],
        "completeness": {
            "identity": {
                "score": 1,
                "reason": "Public links and a user confirmation date are in PROFILE.json; current employer wording disagrees inside the bundle.",
            },
            "source_coverage": {
                "score": 1,
                "reason": "Evidence ledger imported; the 200-post pull was not in the archive.",
            },
            "expertise": {
                "score": 2,
                "reason": "Engineering, AI, career, and management quotes are URL-backed in the ledger.",
            },
            "principles": {"score": 2, "reason": "Repeated, cited positions in the ledger."},
            "frameworks": {
                "score": 1,
                "reason": "Harness notes are a handful of quotes, not a named framework with steps.",
            },
            "playbooks": {
                "score": 1,
                "reason": "One derived playbook. Cost and time were not in the sources.",
            },
            "evidence": {"score": 2, "reason": "Quotes kept with URLs."},
            "limitations": {"score": 2, "reason": "Gaps are written in this file and in section A."},
            "applications": {
                "score": 1,
                "reason": "Section H stays inside the spec's description of Kishore and the cited quotes.",
            },
        },
        "converted_from": "extra/arnav-gupta",
        "companion_agent_id_in_source": "65a2e109-1c74-48c6-9800-5d094624c125",
    }


def normalize_posts_file(path: Path) -> int:
    raw = path.read_text(encoding="utf-8")
    records = []
    for line in raw.split("\n"):
        if not line.strip():
            continue
        record = json.loads(line)
        text = record.get("text") or ""
        text = text.replace("\u2028", "\n").replace("\u2029", "\n")
        record["text"] = text
        records.append(record)
    body = "\n".join(json.dumps(record, ensure_ascii=False, separators=(", ", ": ")) for record in records)
    path.write_text(body + "\n", encoding="utf-8")
    return len(records)


def write_arnav(extra: Path, dest: Path) -> tuple[int, int]:
    profile_json = json.loads((extra / "PROFILE.json").read_text(encoding="utf-8"))
    if profile_json.get("slug") != "arnav-gupta":
        raise SystemExit(f"unexpected extra profile slug: {profile_json.get('slug')}")
    evidence = (extra / "state" / "evidence.md").read_text(encoding="utf-8")
    rows = parse_evidence(evidence)
    if len(rows) < 100:
        raise SystemExit(f"arnav evidence parse returned {len(rows)} rows; expected the ledger")
    sources = evidence_to_sources(rows)
    posts = evidence_to_posts(rows)
    folder = dest / "profiles" / "arnav-gupta"
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True)
    (folder / "profile.md").write_text(
        render_arnav_profile(len(sources), len(posts)),
        encoding="utf-8",
    )
    with (folder / "sources.yaml").open("w", encoding="utf-8") as handle:
        yaml.safe_dump(sources, handle, allow_unicode=True, sort_keys=False, width=1000)
    post_body = "\n".join(
        json.dumps(post, ensure_ascii=False, separators=(", ", ": ")) for post in posts
    )
    (folder / "posts.jsonl").write_text(post_body + "\n", encoding="utf-8")
    status = render_arnav_status(len(posts), len(sources))
    (folder / "status.json").write_text(
        json.dumps(status, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    provenance = dest / "docs" / "research" / "arnav-gupta-source"
    if provenance.exists():
        shutil.rmtree(provenance)
    shutil.copytree(extra, provenance)
    return len(sources), len(posts)


def copy_bundle_profiles(extracted: Path, dest: Path) -> dict[str, int]:
    src = extracted / "profiles"
    counts = {}
    for folder in sorted(path for path in src.iterdir() if path.is_dir()):
        target = dest / "profiles" / folder.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(folder, target)
        counts[folder.name] = normalize_posts_file(target / "posts.jsonl")
    research = dest / "docs" / "research"
    research.mkdir(parents=True, exist_ok=True)
    for name in ("SPEC.md", "batch-A-summary.md", "batch-B-summary.md", "batch-C-summary.md"):
        shutil.copy2(extracted / name, research / name)
    return counts


def build_registry(dest: Path, post_counts: dict[str, int]) -> dict:
    rows = []
    for folder in sorted((dest / "profiles").iterdir()):
        if not folder.is_dir() or not (folder / "profile.md").exists():
            continue
        text = (folder / "profile.md").read_text(encoding="utf-8")
        meta = yaml.safe_load(text.split("---", 2)[1])
        status = json.loads((folder / "status.json").read_text(encoding="utf-8"))
        research_status = status.get("research_status") or meta.get("status")
        excluded = research_status == "excluded"
        row = {
            "id": folder.name,
            "path": f"profiles/{folder.name}",
            "display_name": str(meta.get("display_name")),
            "x_username": str(meta.get("x_username")),
            "x_url": str(meta.get("x_url")),
            "x_user_id": str(meta.get("x_user_id")),
            "account_type": meta.get("account_type"),
            "confidence": meta.get("confidence"),
            "research_status": research_status,
            "registry_status": "excluded" if excluded else "active",
            "primary_research_domain": meta.get("primary_domain"),
            "posts_imported": post_counts[folder.name],
        }
        if excluded:
            row["exclusion_reason"] = status.get("reason") or "excluded in status.json"
            if status.get("replaced_by"):
                row["replaced_by"] = status["replaced_by"]
        rows.append(row)
    rows.sort(key=lambda item: item["id"])
    active = sum(1 for row in rows if row["registry_status"] == "active")
    excluded_n = sum(1 for row in rows if row["registry_status"] == "excluded")
    return {
        "version": 1,
        "source": "distill-research-bundles",
        "snapshot_date": "2026-11-24",
        "counts": {
            "registry": len(rows),
            "active": active,
            "excluded": excluded_n,
            "posts_imported": sum(post_counts.values()),
        },
        "profiles": rows,
    }


def import_archive(archive: Path, dest: Path) -> dict:
    dest.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        extracted = Path(tmp)
        with tarfile.open(archive, "r:*") as handle:
            handle.extractall(extracted, filter="data")
        post_counts = copy_bundle_profiles(extracted, dest)
        sources_n, posts_n = write_arnav(extracted / "extra" / "arnav-gupta", dest)
        post_counts["arnav-gupta"] = posts_n
        registry = build_registry(dest, post_counts)
        registry["counts"]["arnav_evidence_sources"] = sources_n
        registry["counts"]["arnav_evidence_posts"] = posts_n
        with (dest / "profiles" / "registry.yaml").open("w", encoding="utf-8") as handle:
            yaml.safe_dump(registry, handle, allow_unicode=True, sort_keys=False, width=1000)
        return registry


def main() -> int:
    parser = argparse.ArgumentParser(description="Import a DISTILL research bundle")
    parser.add_argument("--archive", required=True, type=Path)
    parser.add_argument("--dest", type=Path, default=ROOT)
    args = parser.parse_args()
    if not args.archive.exists():
        raise SystemExit(f"archive not found: {args.archive}")
    registry = import_archive(args.archive, args.dest)
    counts = registry["counts"]
    print(
        f"imported registry={counts['registry']} active={counts['active']} "
        f"excluded={counts['excluded']} posts={counts['posts_imported']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
