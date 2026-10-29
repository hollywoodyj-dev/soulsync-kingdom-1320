# Gate A closeout against Acceptance Review v1.0

**Review file:** `docs/cursor/SoulSync_Kingdom_1320_Cursor_Handoff_Acceptance_Review_v1.0.md`  
**Date:** 2026-10-30  
**Workspace:** `C:\Users\hugoz\soulsync-kingdom-1320`

The review’s verdict remains **ACCEPT WITH CONDITIONS — local Cursor handoff only**. This closeout records what Cursor has now executed in this environment. It does **not** authorize Preview, deploy, production, or public launch, and it does **not** accept official 1320 algorithm or content.

## 1. Review matrix vs Cursor re-run

| Area | Review status | Cursor now |
|---|---|---|
| ZIP contents (120 entries) | PASS | Confirmed. ZIP SHA-256 `A5D22ED23B47153957E80112E3062C64A4F4E72A0314A439219DF4A2C9BEAEFB` |
| SHA-256 (119 files) | PASS | Reconfirmed OK |
| `START_HERE.md` | PASS | Followed |
| Frozen baseline structure | PASS (structure) | Hash-guarded; read-only |
| Source + selftest exist | PASS (existence) | Unmodified |
| Smoke tests | NOT EXECUTED (missing Chromium) | **ALL PASS** current + frozen |
| Full interaction regression | OPEN | **Rebuilt and ALL PASS** (see gaps below) |
| Design docs | PASS (existence) | Unchanged |
| 1320 computation | HOLD FOR INTEGRATION | Unchanged; DEMO only; `Adapter1320.compute()` not edited |
| Official totems | PARTIAL | Fixtures hashed only; not wired into the game |
| Nova contract | OPEN | Waiting on Nova |
| Privacy / consent copy | OPEN | 6-key whitelist enforced in tests; formal copy still missing |
| Device tests | OPEN | Not run |
| Publish permission | PASS (governance) | Preview / deploy / launch still forbidden |

## 2. P0 items from §4

| P0 | Evidence | Status |
|---|---|---|
| Independent baseline tests + logs | `docs/cursor/evidence/smoke-current-v0.2.3-2026-10-30.txt`, `…smoke-frozen-v0.2.2-2026-10-30.txt`; Playwright 1.64.1 + Chromium 156; Python 3.13.5 | **Closed** |
| Git baseline + immutable ZIP | commit `b0761015f884a2c178371602f474264f17052243`; ZIP hash in `handoff-immutable/ZIP_SHA256.txt`; ZIP kept on disk | **Closed** |
| Retracted-formula rule + static check | `.cursor/rules/1320-local-handoff.mdc`, `tools/guard_retracted_formulas.py` PASS | **Closed** |
| Rebuild interaction regression | `tools/interaction_regression.py` + `docs/cursor/evidence/interaction-regression-2026-10-30.txt` ALL PASS | **Closed for Chromium/local P0 scope** |

Remaining inside the regression script (not required to close local P0, still listed): leap-day official asserts, adapter error/contract tests, iPhone/Android.

## 3. What the rebuilt regression now covers (§3.4)

Dream catch 4 lights → gate skip → wrong PIN then `1320` → sample birth → four realms → gather → blueprint → bottle (empty / snippet-only / URL blocked) → preview → consent / alias regen revoke → meteor → wall → sample-star gesture.

Also: unfinished leave, redo+leave restore, `#shell.inert` + Tab trap + Escape, visible controls ≥44px, walker vs labels, reduced-motion mid-flow overflow on map/blueprint/preview/wall, public payload exactly 6 keys, birth and gate answers not in payload.

## 4. Gate readout after this closeout

| Gate | Status |
|---|---|
| A — Local engineering handoff | **Passed in this Cursor environment** for hashes, git baseline, smoke, formula guard, and Chromium interaction regression. Still not product acceptance. |
| B — Official 1320 integration | Not passed (Nova schema, totems, license, fixtures) |
| C — Hosted Preview | Not authorized |
| D — Production / public launch | Not authorized |

Founder review of `docs/cursor/PHASE_1_INTAKE_RECEIPT.md` and this closeout can proceed. Cursor will not call Nova, add network, embed official WebP, or apply for Preview unless separately approved.
