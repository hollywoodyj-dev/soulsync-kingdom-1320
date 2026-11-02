#!/usr/bin/env python3
"""Build a JS map of the four hash-checked official fixture totems."""
from __future__ import annotations

import base64
import hashlib
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "assets" / "official-1320-fixture"
MANIFEST = FIXTURE / "official-1320-fixture-totems.manifest.json"
OUT = ROOT / "src" / "current" / "_official_totem_uri.inc.js"


def main() -> int:
    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    lines = ["const OFFICIAL_TOTEM_URI={"]
    for code, info in man["assets"].items():
        data = (FIXTURE / info["file"]).read_bytes()
        digest = hashlib.sha256(data).hexdigest()
        if digest != info["sha256"]:
            raise SystemExit(f"hash mismatch {code}: {digest}")
        uri = "data:image/webp;base64," + base64.b64encode(data).decode("ascii")
        lines.append(f"  {json.dumps(code)}:{json.dumps(uri)},")
        print(f"{code} {len(data)} ok")
    lines.append("};")
    OUT.write_text("\n".join(lines) + "\n", encoding="ascii")
    print(f"wrote {OUT} bytes={OUT.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
