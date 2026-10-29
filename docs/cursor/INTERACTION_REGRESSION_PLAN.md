# Interaction regression plan — v0.2.3

Script: `tools/interaction_regression.py` (Playwright, selftest copy, 390×844, reduced motion).

This replaces the lost full-flow script at smoke+happy-path depth. Device Safari / Android Chrome remain open.

## Covered now

| Flow | Assertion |
|---|---|
| Intro skip → dream already complete → gate skip ×3 → door `1320` → sample birth | Map reached |
| Leave unfinished S1 | Node not marked visited |
| Complete S1 / S3 / S2 / S0 (minimal choices) | All four nodes `done` |
| Redo S1 then leave | Completed result restored; gather available |
| Gather lamps → blueprint | Four blueprint cards |
| Empty bottle → preview | Error shown |
| Fill experience → preview | Publish disabled until consent |
| Regen alias | Consent revoked, publish disabled |
| Consent + publish → skip meteor → wall | Wall reached |
| Public payload | Exactly 6 keys; birth not included |
| Touch targets on map | `min(width,height) ≥ 44` |
| Walker vs node labels | No overlap > 2px |

## Still to add

- Full dream catch of 4 lights (not skipPro).
- Invalid door code, then correct `1320`.
- Manual birth date including leap day (needs Nova fixture before official asserts).
- Focus trap / Tab order / `#shell.inert` while modal open.
- Horizontal overflow at 360 / 390 / 430 / 1280 (smoke already covers load; need mid-flow).
- Contact/URL in bottle fields blocked.
- Snippet-only bottle still blocked.
- Star-wall gestures on a non-mine sample star.
- Restart confirm.
- Official-adapter error states once Nova schema exists: `unconnected` / `validation_failed` / `temporarily_unavailable`, no DEMO fallback.

## How to run

```
py -3.13 -I tools/interaction_regression.py
```

Do not point this script at the clean (non-selftest) file; the state hook lives only on the selftest copy.
