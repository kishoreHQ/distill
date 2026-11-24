#!/usr/bin/env python3
"""Score opportunity YAML files with config/scoring.yaml. Does not change the hypotheses."""

from __future__ import annotations

import argparse
from pathlib import Path

from distilllib import OPPORTUNITY_DISCLAIMER, ROOT, dump_json, load_schema, load_yaml, score_dimensions, validate_instance, weights


def load_opportunities(root: Path) -> list[dict]:
    folder = root / "opportunities"
    rows = []
    for path in sorted(folder.glob("*.yaml")):
        data = load_yaml(path)
        validate_instance(data, load_schema("opportunity.schema.json"))
        if OPPORTUNITY_DISCLAIMER not in data["disclaimer"]:
            raise SystemExit(f"{path.name} disclaimer does not match the standard text")
        scored = score_dimensions(data["dimensions"])
        rows.append(
            {
                "id": data["id"],
                "title": data["title"],
                "file": f"opportunities/{path.name}",
                "as_of": data["as_of"],
                "status": data["status"],
                "domains": data["domains"],
                "disclaimer": data["disclaimer"],
                "total": scored["total"],
                "scale_max": scored["scale_max"],
                "breakdown": scored["breakdown"],
                "evidence": data["evidence"],
                "non_claims": data["non_claims"],
            }
        )
    rows.sort(key=lambda row: (-row["total"], row["id"]))
    for index, row in enumerate(rows, start=1):
        row["rank"] = index
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    weight_sum = sum(weights().values())
    if weight_sum != 100:
        raise SystemExit(f"scoring weights sum to {weight_sum}, expected 100")
    rows = load_opportunities(args.root)
    payload = {
        "disclaimer": OPPORTUNITY_DISCLAIMER,
        "weight_sum": weight_sum,
        "method": "sum((dimension score / scale_max) * weight)",
        "opportunities": rows,
    }
    dump_json(payload, args.root / "opportunities" / "scores.json")
    print(f"scored {len(rows)} opportunities; top={rows[0]['id']} total={rows[0]['total']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
