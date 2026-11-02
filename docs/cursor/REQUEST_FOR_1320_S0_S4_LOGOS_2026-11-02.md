# Request for 1320 — S0–S4 Soul Code logos

**From:** SoulSync Kingdom (hollywoodyj-dev/soulsync-kingdom-1320)  
**Date:** 2026-11-02  
**Please reply on this repo or by note. Do not put API keys in git.**

---

## 1. Please pull the Kingdom-only repo

https://github.com/hollywoodyj-dev/soulsync-kingdom-1320

- Latest file to consider: `src/current/soulsync-kingdom-1320-v0.2.5-local-tonight-reflection.html`
- Tonight’s four-choice sentence is composed **in the game**. We do **not** call `POST /api/soulsync-kingdom/reflect` for that line.
- Leave `/reflect` as you shipped it. LLM is already linked. Model failure: no substitute sentence from us.
- This push does **not** change the current Vercel Preview. You pull, then choose which HTML Preview uses.
- We will not push to `hollywoodyj-dev/1320web`, `master` on that repo, or `preview/soulsync-kingdom-bridge`.

---

## 2. What is already working

- `POST /api/soulsync-kingdom/blueprints/resolve` — official S1 / S3 / S2 / S0 **codes** and public **names**, after consent. No birthday in the response. No DEMO blueprint on failure.
- `POST /api/soulsync-kingdom/reflect` — linked. We are not asking you to change it.

---

## 3. Please connect S0–S4 official logos

Kingdom still draws **realm placeholder** symbols. Official Soul Code logos for **S0, S1, S2, S3, S4** are not linked from your resolve response.

You already said only four hashed samples are approved to ship as official art:

| code | fixture we already hold (hash-checked) |
| --- | --- |
| S1-18 | Transformer |
| S3-03 | Explorer |
| S2-27 | The Soul Shock Mirror |
| S0-07 | Self-Worth Illusion |

Example you gave: `2022-02-02` → S1-06 / S3-01 / S2-04 / S0-10 should keep **labeled placeholders** until those codes have an official logo. That is still correct.

### What we need from 1320 (no secrets)

On `POST /api/soulsync-kingdom/blueprints/resolve`, for each of `s0` `s1` `s2` `s3` (and `s4` if you return it), add only when a **real** official mapping exists:

```json
"totemId": "S1-18",
"totemAssetUrl": "https://…same-origin or allowlisted…/….webp"
```

Rules we will follow:

1. `totemId` must equal that segment’s `code`. Mismatch → visible error. We will not swap in a generic symbol and call it official.
2. If there is no official logo for that code, **omit** `totemId` and `totemAssetUrl`. We keep the labeled placeholder.
3. Do not invent files from public path patterns (`/S1-44/S18.webp` etc.). Those are not a roster.
4. Filename regularity in the site folder is not a registry. Please send a manifest: `code`, `totemId`, URL or filename, sha256, content version.
5. S4: include it in the same roster even if Kingdom’s current map only shows S1 / S3 / S2 / S0.
6. CORS if the game loads the URL from Preview: allow the Preview origin, or serve the files same-origin with `/soulsync-kingdom/`.
7. No API keys in the browser. No birthday on the logo URL.

We will not scrape or guess the rest of the library. After you return matching `totemId` + `totemAssetUrl`, we will add a **new** HTML filename to display them. We will not overwrite v0.2.2 / v0.2.3 / v0.2.4 / v0.2.5.

---

## 4. Out of scope

- Do not change Coze, price, Taiwan paid fulfillment, or `/api/v1/blueprints/resolve`.
- Do not put production on `www.1320soulcode.com/soulsync-kingdom` unless you separately open it.
- Retracted formulas stay retracted: no `S2 = month + day`, no `S3 = month × day`.
