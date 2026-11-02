#!/usr/bin/env python3
"""Apply official-fixture totem display to the v0.2.6 copy."""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = ROOT / "src" / "current" / "soulsync-kingdom-1320-v0.2.6-official-fixture-totems.html"
URIS = ROOT / "src" / "current" / "_official_totem_uri.inc.js"


def main() -> int:
    text = HTML.read_text(encoding="utf-8")
    uris = URIS.read_text(encoding="ascii")

    reps = [
        (
            "<title>SoulSync Kingdom · 1320 SoulCode 原型 v0.2.5 · 今夜映照</title>",
            "<title>SoulSync Kingdom · 1320 SoulCode 原型 v0.2.6 · 官方图腾样品</title>",
        ),
        (
            "   SoulSync Kingdom × 1320 SoulCode — Phase A v0.2.5 — Local tonight reflection\n"
            "   Copied from v0.2.4 1320web bridge (Preview). Do not overwrite v0.2.2 / v0.2.3 / v0.2.4.\n"
            "   Official codes still go through POST /api/soulsync-kingdom/blueprints/resolve.\n"
            "   Tonight's four-choice sentence is composed in this file. Do not call /reflect for it.\n"
            "   Model failure must not grow a substitute sentence. 1320 API stays as they shipped it.",
            "   SoulSync Kingdom × 1320 SoulCode — Phase A v0.2.6 — Official fixture totems\n"
            "   Copied from v0.2.5. Do not overwrite v0.2.2 / v0.2.3 / v0.2.4 / v0.2.5.\n"
            "   Shows hash-checked official logos only for S1-18, S3-03, S2-27, S0-07.\n"
            "   Other codes keep labeled placeholders. Do not invent the rest of the library.",
        ),
        (
            "'bp.totemNote':'官方图腾目前只核验了 S1-18、S3-03、S2-27、S0-07 四张样品。其他编号继续用标明的占位符号。'",
            "'bp.totemNote':'S1-18、S3-03、S2-27、S0-07 显示已核验的官方样品图腾。其他编号继续用标明的占位符号。'",
        ),
        (
            "'totem.note':'示例占位：原创通用符号，不是 1320 官方图腾，也不会改变你的固定蓝图。'",
            "'totem.note':'已核验的官方编号显示官方样品图腾；其他编号仍是标明的占位符号。'",
        ),
        (
            "'totem.ph':'示例占位'",
            "'totem.ph':'示例占位','totem.official':'官方样品图腾','totem.mismatch':'图腾与编号不匹配，不能用占位符号代替。'",
        ),
        (
            "const VERSION_LABEL='Phase A v0.2.5 — Local tonight reflection';",
            "const VERSION_LABEL='Phase A v0.2.6 — Official fixture totems';\n"
            + uris,
        ),
        (
            ".bp-card{display:grid;grid-template-columns:48px 1fr;gap:12px;padding:12px 0;border-bottom:1px solid var(--line)}\n"
            ".bp-card .d{font-family:var(--serif);font-size:30px;color:var(--gold);line-height:1.1;text-align:center}\n"
            ".bp-card .d small{display:block;font-size:14px;color:var(--mist);font-family:var(--sans)}",
            ".bp-card{display:grid;grid-template-columns:40px 96px 1fr;gap:12px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)}\n"
            ".bp-card .d{font-family:var(--serif);font-size:30px;color:var(--gold);line-height:1.1;text-align:center}\n"
            ".bp-card .d small{display:block;font-size:14px;color:var(--mist);font-family:var(--sans)}",
        ),
        (
            ".bp-card .d .tm{width:32px;height:32px;margin-top:6px}",
            ".bp-card .tm{width:88px;height:88px;margin:0}\n"
            ".tm.offi{border-style:solid;border-color:var(--gold-d);background:#050814}\n"
            ".tm.offi img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}\n"
            ".tm.err{width:auto;height:auto;padding:8px;border-radius:10px;border-color:var(--danger);color:var(--danger);font-size:13px;text-align:left}",
        ),
    ]
    for old, new in reps:
        if old not in text:
            raise SystemExit(f"missing snippet:\n{old[:180]}")
        text = text.replace(old, new, 1)

    old_totem = (
        "const totem=(id,on,extra)=>`<span class=\"tm ${on?'on':''} ${extra||''}\">"
        "<svg class=\"tt ${on?'on':''}\" viewBox=\"0 0 120 120\" aria-hidden=\"true\">${TOTEM_SHAPE[id]}</svg></span>`;"
    )
    new_totem = r"""function officialTotemSrc(id){
  const f=getFoundation(id);
  if(f.totemId&&f.code&&f.totemId!==f.code)return {error:'mismatch'};
  if(f.totemAssetUrl&&f.totemId&&f.totemId===f.code)return {src:f.totemAssetUrl,official:true};
  if(f.code&&OFFICIAL_TOTEM_URI[f.code])return {src:OFFICIAL_TOTEM_URI[f.code],official:true};
  return null;
}
const totem=(id,on,extra)=>{
  const hit=officialTotemSrc(id);
  if(hit&&hit.error)return `<span class="tm err" role="alert">${t('totem.mismatch')}</span>`;
  if(hit&&hit.src){
    const name=esc((getFoundation(id).name||id.toUpperCase())+' '+t('totem.official'));
    return `<span class="tm offi on ${extra||''}"><img src="${hit.src}" alt="${name}" width="88" height="88"></span>`;
  }
  return `<span class="tm ${on?'on':''} ${extra||''}"><svg class="tt ${on?'on':''}" viewBox="0 0 120 120" aria-hidden="true">${TOTEM_SHAPE[id]}</svg></span>`;
};"""
    if old_totem not in text:
        raise SystemExit("missing totem() snippet")
    text = text.replace(old_totem, new_totem, 1)

    old_bp = (
        "${ORDER.map(i=>{const f=getFoundation(i);return `<div class=\"bp-card\"><div class=\"d\">${DIGIT[i]}<small>${i.toUpperCase()}</small>${totem(i,!!S.visited[i])}</div><div>"
    )
    new_bp = (
        "${ORDER.map(i=>{const f=getFoundation(i);return `<div class=\"bp-card\"><div class=\"d\">${DIGIT[i]}<small>${i.toUpperCase()}</small></div>${totem(i,true)}<div>"
    )
    if old_bp not in text:
        raise SystemExit("missing V.bp card snippet")
    text = text.replace(old_bp, new_bp, 1)

    HTML.write_text(text, encoding="utf-8")
    print("patched", HTML, "bytes", HTML.stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
