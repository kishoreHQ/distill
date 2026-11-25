"""Phase 1 checks. The committed tree is the fixture for repo-level tests."""

from __future__ import annotations

import json

from distilllib import (
    DISCLAIMER,
    OPPORTUNITY_DISCLAIMER,
    ROOT,
    SECTION_HEADINGS,
    load_json,
    load_registry,
    score_dimensions,
    weights,
)
from import_research_bundle import evidence_to_posts, parse_evidence
from refresh_profiles import rows_from_payload, select_profiles


def test_weights_match_the_brief():
    table = weights()
    assert table == {
        "market_pull": 25,
        "evidence_strength": 20,
        "fit_with_kishore_skills": 15,
        "time_to_value": 15,
        "competition_gap": 10,
        "monetization_clarity": 10,
        "risk_inverse": 5,
    }
    assert sum(table.values()) == 100


def test_score_formula():
    dimensions = {
        name: {"score": 10, "note": "ceiling"}
        for name in weights()
    }
    assert score_dimensions(dimensions)["total"] == 100.0
    half = {name: {"score": 5, "note": "mid"} for name in weights()}
    assert score_dimensions(half)["total"] == 50.0
    # infra-cost-audit hand scores: 7, 8, 9, 8, 5, 7, 6
    sample = {
        "market_pull": {"score": 7, "note": "n"},
        "evidence_strength": {"score": 8, "note": "n"},
        "fit_with_kishore_skills": {"score": 9, "note": "n"},
        "time_to_value": {"score": 8, "note": "n"},
        "competition_gap": {"score": 5, "note": "n"},
        "monetization_clarity": {"score": 7, "note": "n"},
        "risk_inverse": {"score": 6, "note": "n"},
    }
    assert score_dimensions(sample)["total"] == 74.0


def test_registry_counts():
    registry = load_registry()
    active = [row for row in registry["profiles"] if row["registry_status"] == "active"]
    excluded = [row for row in registry["profiles"] if row["registry_status"] == "excluded"]
    assert len(active) == 32
    assert len(excluded) == 1
    assert excluded[0]["id"] == "x-aravind"
    assert excluded[0]["replaced_by"] == "aravind-srinivas"
    ids = {row["id"] for row in active}
    assert "aravind-srinivas" in ids
    assert "arnav-gupta" in ids
    assert "x-aravind" not in ids
    assert registry["counts"]["posts_imported"] == sum(row["posts_imported"] for row in registry["profiles"])
    assert registry["counts"]["posts_imported"] > 2900


def test_people_are_not_merged():
    registry = load_registry()
    user_ids = [row["x_user_id"] for row in registry["profiles"]]
    assert len(user_ids) == len(set(user_ids))
    by_id = {row["id"]: row for row in registry["profiles"]}
    assert by_id["x-aravind"]["x_user_id"] != by_id["aravind-srinivas"]["x_user_id"]


def test_briefing_has_eight_sections_and_names_the_snapshot():
    text = (ROOT / "intelligence" / "daily" / "2026-11-24.md").read_text(encoding="utf-8")
    for _key, heading in SECTION_HEADINGS:
        assert f"## {heading}" in text
    assert "2026-11-24" in text
    assert "snapshot" in text.lower()
    assert DISCLAIMER in text
    assert OPPORTUNITY_DISCLAIMER in text


def test_boards_are_simulated():
    boards = list((ROOT / "boards").glob("*/board.yaml"))
    assert len(boards) == 5
    for path in boards:
        text = path.read_text(encoding="utf-8")
        deliberation = next(path.parent.glob("deliberations/*.md")).read_text(encoding="utf-8")
        assert "SIMULATED ADVISORY BOARD" in text
        assert DISCLAIMER in deliberation
        assert "x-aravind" not in deliberation or "not" in deliberation


def test_scores_file_matches_formula():
    payload = load_json(ROOT / "opportunities" / "scores.json")
    assert payload["weight_sum"] == 100
    assert 3 <= len(payload["opportunities"]) <= 6
    assert payload["opportunities"][0]["id"] == "infra-cost-audit"
    assert payload["opportunities"][0]["total"] == 74.0


def test_matrix_covers_active_profiles():
    matrix = load_json(ROOT / "knowledge" / "classification-matrix.json")
    registry = load_registry()
    active = {row["id"] for row in registry["profiles"] if row["registry_status"] == "active"}
    assert {row["id"] for row in matrix["profiles"]} == active
    assert len(matrix["domains"]) == 5


def test_parse_evidence_and_posts_do_not_invent_metrics():
    sample = "\n".join(
        [
            '- O-ENG-1 | 2022-09-10 | ss | https://example.com/post | "Postgres."',
            "- O-AI-1 | 2025-05-27 | X post | https://x.com/championswimmer/status/1927371303326974136 | Code is now cheap too.",
        ]
    )
    rows = parse_evidence(sample)
    assert [row["id"] for row in rows] == ["O-ENG-1", "O-AI-1"]
    posts = evidence_to_posts(rows)
    assert len(posts) == 1
    assert posts[0]["metrics"] is None
    assert posts[0]["origin"] == "evidence-quote"
    assert posts[0]["text"] == "Code is now cheap too."


def test_refresh_payload_mapping():
    payload = {
        "data": [
            {
                "id": "99",
                "text": "hello",
                "created_at": "2026-11-24T00:00:00.000Z",
                "public_metrics": {"like_count": 1, "impression_count": 2},
            }
        ]
    }
    rows = rows_from_payload(payload, "someone")
    assert rows[0]["url"] == "https://x.com/someone/status/99"
    assert rows[0]["origin"] == "refresh"
    assert rows[0]["metrics"]["like_count"] == 1
    assert rows[0]["metrics"]["retweet_count"] is None


def test_refresh_rotation_is_stable():
    registry = {
        "profiles": [
            {"id": "b", "registry_status": "active", "account_type": "person"},
            {"id": "a", "registry_status": "active", "account_type": "person"},
            {"id": "c", "registry_status": "active", "account_type": "aggregator"},
            {"id": "d", "registry_status": "excluded", "account_type": "person"},
            {"id": "e", "registry_status": "active", "account_type": "person"},
        ]
    }
    import datetime as dt

    chosen = select_profiles(registry, dt.date(2026, 1, 1), limit=2)
    assert [row["id"] for row in chosen] == [row["id"] for row in select_profiles(registry, dt.date(2026, 1, 1), limit=2)]
    assert all(row["account_type"] == "person" for row in chosen)
    assert "d" not in {row["id"] for row in chosen}
    assert "c" not in {row["id"] for row in chosen}


def test_no_token_files():
    assert not (ROOT / ".env").exists()
    daily = (ROOT / ".github" / "workflows" / "daily.yml").read_text(encoding="utf-8")
    assert "secrets.X_BEARER_TOKEN" in daily
    assert "secrets.XAI_API_KEY" in daily
    assert "30 23 * * *" in daily


def test_arnav_posts_keep_quote_rows_and_record_the_gap():
    registry = load_registry()
    row = next(item for item in registry["profiles"] if item["id"] == "arnav-gupta")
    posts = [
        json.loads(line)
        for line in (ROOT / "profiles" / "arnav-gupta" / "posts.jsonl").read_text(encoding="utf-8").split("\n")
        if line.strip()
    ]
    quotes = [post for post in posts if post.get("origin") == "evidence-quote"]
    refreshed = [post for post in posts if post.get("origin") == "refresh"]
    assert row["posts_imported"] == len(posts)
    assert len(quotes) == 57
    assert all(post["metrics"] is None for post in quotes)
    assert refreshed
    assert all(
        isinstance(post.get("metrics"), dict) and "impression_count" in post["metrics"]
        for post in refreshed
    )
    status = json.loads((ROOT / "profiles" / "arnav-gupta" / "status.json").read_text(encoding="utf-8"))
    assert status["posts_read"] == len(posts)
    assert status["posts_in_repo"] == len(posts)
    assert "did not include those posts" in status["posts_read_note"]
    assert "200" in status["posts_read_note"]
