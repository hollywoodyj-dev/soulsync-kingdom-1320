# 1320 team bridge status — 2026-11-02

Source: Founder-forwarded note from the 1320 site team. This file is a receipt, not a license to change their API.

## Their runtime (do not treat as our deploy)

- Preview only, Vercel login required: `1320web-hevlm6h1r-jing-yangs-projects-db5d1ce8.vercel.app` + `/soulsync-kingdom`
- Production is closed. `www.1320soulcode.com/soulsync-kingdom` does **not** have this bridge.
- Reports, Coze, price, and Taiwan paid fulfillment were not changed.

## Already on their side

- `POST /api/soulsync-kingdom/blueprints/resolve` — official S1 / S3 / S2 / S0 codes and public names. Consent required. Birthday is not in the response or ordinary logs. Failure does not return a DEMO blueprint.
- `POST /api/soulsync-kingdom/reflect` — live. Browser may send `locale`, `purpose`, and tonight’s choice summary (`module`, `choice`, S2 may include `relation`). Not birthday, not blueprint codes, not gate answers, not private free text, not the whole game state. Model key stays on the server.
- One real click returned 200:「你刚才选择了不认同这个描述、只观察不改变、在亲密关系中先听见自己的需要，并带着它离开。」

## Not on their side

- Official totems: only hashed samples **S1-18, S3-03, S2-27, S0-07**. Other codes keep labeled placeholders. `2022-02-02` → S1-06 / S3-01 / S2-04 / S0-10 showing placeholders is expected.
- Remaining images in the site folder are not an official roster. Do not ingest the whole folder.

## What they asked Kingdom to do

- Compose that four-choice sentence **in the game**. This range does not need a language model.
- Copy Preview’s `soulsync-kingdom-1320-v0.2.4-1320web-bridge.html` to a **new filename**. Do not overwrite v0.2.2, v0.2.3, or v0.2.4.
- Leave their API as shipped. If the model fails, do **not** insert a substitute sentence.

## New file

`src/current/soulsync-kingdom-1320-v0.2.5-local-tonight-reflection.html`

- Official resolve path unchanged (still no DEMO fallback).
- Tonight’s sentence is built from the four fixed option keys only. `/reflect` is not called.
- No invented totems.

## Git (binding)

- Later updates go to a **separate GitHub project that contains only `soulsync-kingdom-1320`**. They will send the URL. We push there. They pull into 1320web and choose which new file Preview uses.
- Our push will **not** change the current Preview URL.
- **Do not** push to `hollywoodyj-dev/1320web`.
- **Do not** push `master` or `preview/soulsync-kingdom-bridge` on that repo.
- Do not put the 1320 site or API keys in the Kingdom repo.
