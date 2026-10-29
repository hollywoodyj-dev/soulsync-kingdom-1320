#!/usr/bin/env python3
"""Interaction regression for the v0.2.3 selftest copy.

Covers the happy path plus bottle-empty, alias-regen consent revoke,
replay/leave restore, touch targets, and walker-vs-label overlap.
Not a substitute for iPhone Safari / Android Chrome device tests.
"""
from __future__ import annotations

import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parents[1]
HTML = ROOT / "src" / "current" / "soulsync-kingdom-1320-v0.2.3-visual-dev-selftest.html"
fails: list[str] = []


def chk(cond: bool, msg: str) -> None:
    print(("PASS " if cond else "FAIL ") + msg)
    if not cond:
        fails.append(msg)


def click_act(page, act: str, **data) -> None:
    sel = f'[data-act="{act}"]'
    if "v" in data:
        sel += f'[data-v="{data["v"]}"]'
    if "id" in data:
        sel += f'[data-id="{data["id"]}"]'
    if "i" in data:
        sel += f'[data-i="{data["i"]}"]'
    page.locator(sel).first.click()


def wait_act(page, act: str, timeout: int = 8000) -> None:
    page.locator(f'[data-act="{act}"]').first.wait_for(state="visible", timeout=timeout)


def heading(page) -> str:
    return page.locator("h1, h2").first.inner_text()


def min_touch(page) -> float:
    return page.evaluate(
        """() => {
          const nodes = [...document.querySelectorAll('button.btn, button.opt, button.node, .pad button')];
          if (!nodes.length) return 999;
          return Math.min(...nodes.map(el => {
            const r = el.getBoundingClientRect();
            return Math.min(r.width, r.height);
          }));
        }"""
    )


def walker_overlap(page) -> bool:
    return page.evaluate(
        """() => {
          const wk = document.querySelector('#wk');
          if (!wk) return false;
          const wr = wk.getBoundingClientRect();
          return [...document.querySelectorAll('button.node span, button.node em')].some(el => {
            const r = el.getBoundingClientRect();
            const x = Math.max(0, Math.min(wr.right, r.right) - Math.max(wr.left, r.left));
            const y = Math.max(0, Math.min(wr.bottom, r.bottom) - Math.max(wr.top, r.top));
            return x > 2 && y > 2;
          });
        }"""
    )


def finish_s1(page) -> None:
    click_act(page, "pickSym", v="lamp")
    click_act(page, "s1act", v="part")
    click_act(page, "finish")
    wait_act(page, "scene")


def finish_s3(page) -> None:
    click_act(page, "s3act", v="stay")
    click_act(page, "finish")
    wait_act(page, "scene")


def finish_s2(page) -> None:
    click_act(page, "pickRel", v="none")
    click_act(page, "finish")
    wait_act(page, "scene")


def finish_s0(page) -> None:
    click_act(page, "breatheSkip")
    click_act(page, "s0act", v="blank")
    click_act(page, "finish")
    wait_act(page, "scene")


def main() -> int:
    if not HTML.exists():
        print("missing selftest html")
        return 1
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(
            viewport={"width": 390, "height": 844},
            reduced_motion="reduce",
        )
        page = ctx.new_page()
        errors: list[str] = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(HTML.as_uri() + "#selftest")
        page.wait_for_timeout(300)

        click_act(page, "skipPro")
        wait_act(page, "dreamNext")
        click_act(page, "dreamNext")

        for _ in range(3):
            wait_act(page, "gateAns")
            page.locator('[data-act="gateAns"][data-v="-1"]').click()

        wait_act(page, "pwKey")
        for digit in "1320":
            click_act(page, "pwKey", v=digit)
        wait_act(page, "birthSample", timeout=4000)

        click_act(page, "birthSample")
        wait_act(page, "scene")
        chk("四境" in heading(page) or page.locator("#map").count() == 1, "reached four-realm map")
        chk(min_touch(page) >= 44, f"map controls >= 44px (min={min_touch(page):.1f})")
        chk(not walker_overlap(page), "walker does not overlap node labels")

        # Replay/leave: start S1, leave mid-flow, map should not mark visited.
        click_act(page, "scene", id="s1")
        wait_act(page, "pickSym")
        click_act(page, "toMap")
        wait_act(page, "scene")
        done = page.locator("#node-s1.done").count()
        chk(done == 0, "leaving unfinished S1 does not mark visited")

        finishers = {"s1": finish_s1, "s3": finish_s3, "s2": finish_s2, "s0": finish_s0}
        for sid, fn in finishers.items():
            click_act(page, "scene", id=sid)
            fn(page)
            chk(page.locator(f"#node-{sid}.done").count() == 1, f"{sid} marked visited")

        # Redo then leave should restore completed result.
        click_act(page, "scene", id="s1")
        wait_act(page, "redo")
        click_act(page, "redo")
        wait_act(page, "pickSym")
        click_act(page, "toMap")
        wait_act(page, "gather")
        chk(page.locator("#node-s1.done").count() == 1, "redo+leave restores completed S1")

        click_act(page, "gather")
        wait_act(page, "toBottle", timeout=4000)
        chk("蓝图" in heading(page) or page.locator(".bp-card").count() == 4, "blueprint screen")

        click_act(page, "toBottle")
        wait_act(page, "toPreview")
        click_act(page, "toPreview")
        err = page.locator("#berr").inner_text()
        chk(bool(err.strip()), "empty bottle blocked preview")

        page.fill("#exp", "今夜先把灯放稳。")
        click_act(page, "toPreview")
        wait_act(page, "publish")
        chk(page.locator("#pubBtn").is_disabled(), "publish disabled before consent")

        page.locator("#consent").check()
        chk(page.locator("#pubBtn").is_enabled(), "publish enabled after consent")
        click_act(page, "regen")
        chk(page.locator("#pubBtn").is_disabled(), "regen alias revokes consent")

        page.locator("#consent").check()
        click_act(page, "publish")
        page.wait_for_timeout(400)
        skip = page.locator('[data-act="skipMeteor"]')
        if skip.count() and skip.first.is_visible():
            click_act(page, "skipMeteor")
        wait_act(page, "toWall0", timeout=4000)
        click_act(page, "toWall0")
        wait_act(page, "toMap")
        chk("星" in heading(page) or page.locator("#wallbox").count() == 1, "star wall")

        st = page.evaluate("() => window.__ssk && window.__ssk.getState()")
        chk(bool(st), "selftest hook present")
        if st:
            payload = page.evaluate("() => window.__ssk.buildPublicStarPayload(window.__ssk.getState())")
            chk(
                sorted(payload.keys())
                == sorted(["alias", "experience", "insight", "wish", "blueprintSnippet", "contentWarning"]),
                f"public payload 6 keys {sorted(payload.keys())}",
            )
            chk(st.get("birth") is not None, "birth stays in memory only")
            chk("birth" not in payload, "birth not in public payload")

        chk(not errors, f"no page errors {errors[:2]}")
        browser.close()

    print("\nRESULT:", "ALL PASS" if not fails else f"{len(fails)} FAIL")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
