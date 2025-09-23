from __future__ import annotations

import json
from typing import Dict, List

import requests


def fetch_data() -> List[Dict[str, str]]:
    try:
        resp = requests.get("https://httpbin.org/json", timeout=5)
        resp.raise_for_status()
        return [
            {
                "id": "remote",
                "content": resp.json().get("slideshow", {}).get("title", ""),
            }
        ]
    except Exception:
        # Fallback synthetic data if offline
        return [{"id": f"local-{i}", "content": f"synthetic-{i}"} for i in range(3)]


def main() -> int:
    data = fetch_data()
    print(json.dumps({"count": len(data), "sample": data[0]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
