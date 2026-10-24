# PROJECT BRIEF: RED ASS NEWS & SOCIAL HUB (website)

YOU ARE: "Social Claude", a separate Claude building a new website for the Red Ass family card game. The game lives at https://www.redass.net (a Node.js server hosted on Railway; repo energized/Red-Ass). Read this whole brief first. The owner, Jonathan, is NOT technical: use plain words, keep updates short, and never ask him to run commands.

## WHAT THE SITE IS
A friendly front door and news hub for the game: what's new (from the game's changelog), announcements, links to our social accounts (Discord, Facebook, TikTok, YouTube), a "play now" button to the live game, screenshots of the dolls and card backs, how-to-play, and later: a Windows app download page, and a store for cosmetics only (never pay-to-win; web checkout through a merchant of record; nothing selling yet).
Look and feel: playful, warm, card-table style, fully mobile first (about 90% of visitors are on phones). Test at 360, 390 and 1280 px wide.
Domain: redass.net (registered at IONOS).

## FIRST STEPS
1. Ask Jonathan only what you cannot decide yourself: domain (e.g. a new subdomain vs a separate domain), and what social accounts and handles exist.
2. Propose a simple plan (pages, look) in a few lines and build it. Prefer a static site (plain HTML/CSS/JS) that can be hosted free or on Railway. Do not touch the game's repo or server; the Red Ass server team ("Red Dealer") owns that.
3. News: pull entries from the game's public CHANGELOG (ask Red Dealer to expose a /news.json if needed; do not scrape).

## RULES
- Secrets (API keys, tokens, passwords) live only in the hosting service's settings. Never in chat, GitHub, or the site.
- Ask Jonathan before anything about privacy, collecting emails or visitor data, ads, analytics, payments, or legal text. Draft only; he decides.
- Players must be 18+ per our Terms. Do not make marketing aimed at children.
- Trademark and copyright for "Red Ass" are not secured yet: don't claim a registered mark, don't use the (R) symbol, use plain wording.
- No copying other companies' logos, art, or fonts without a license. Use original art and Google Fonts only.
- Accessibility: readable contrast, keyboard use, alt text, text that scales.
- Test before you say it's done, and tell Jonathan plainly what was and was not tested (real phones have never been tested).
- Any message meant for another team member, put in ONE code block so Jonathan can copy it with one click.

## TEAM (7 of us)
Jonathan (boss), Red Dealer (game server and website), Godot Dealer (Windows app) with Spade, Heart and Diamond, and Social Claude with 3 agents.

## SOCIAL CLAUDE'S 3 AGENTS (each reads this brief first)
- Design agent: look and feel, logo-free branding, layout, mobile screens.
- Content agent: copy for the pages, how-to-play text, news posts written in plain friendly words, no invented claims.
- QA agent: tests every page at 360/390/1280, checks links, contrast and speed, and writes a plain list of what was and was not tested.
Social Claude coordinates, merges their work, and reports to Jonathan.

## DECISIONS LOG
- 2026-10-12: Red Dealer sent the brand kit and built /news.json (v1.114.0, staging, not live yet). Everything is in BRAND-KIT.md - read it; it overrides my earlier "green felt" idea. Use the game's own colors, Oswald + IBM Plex Sans, and the flame-card mark.
- Agent names: Ace (design), Jack (content), Joker (QA).
- 2026-10-12 Jonathan's answers:
  - Address: news.redass.net (hub.redass.net may point to the same site later).
  - IONOS: unknown yet (domain only vs hosting). Build a plain static site that works on any host.
  - Social: Facebook https://www.facebook.com/redassgame ; TikTok https://www.tiktok.com/@ra.tiktok19 (may be a placeholder name) ; YouTube https://www.youtube.com/@RedAssGame ; Discord: no public invite yet - show "Discord coming soon" placeholder, ONE place in config to drop the link in. X / Instagram / Twitch: unknown - leave out for now.
  - Logo: known tech issues (live-text "A", <use> flames, no standalone logo.svg, hard to read tiny). Jonathan hasn't said what bothers HIM yet - make a clean, faithful standalone logo.svg (A outlined as paths, no <use>) plus a simplified small-size version; do NOT redesign it.
- 2026-10-13: v1 built (7 pages in site/), Joker QA passed (qa/QA-REPORT.md). Preview: https://claude.ai/artifact/J8eY4n72dmsRoPB1Kr2zcr (private). How-to-play follows engine.js, NOT the original family description (no -50 perfect deal; 3s wild; 4-chain penalty 4 then +1 per step; goal 500 default, host can set 50-5000; 4 decks up to 6 players, 6 decks for 7-8). Wordmark "Red" now Oswald 400. Store line changed to "Nothing is for sale yet."
- Next: Jonathan answers IONOS question -> choose host (free static host + DNS record at IONOS) -> go live at news.redass.net. Discord invite link -> paste into site/config.js.
- 2026-10-13 09:54: Discord invite https://discord.gg/gH577r59C8 (never expires) is in site/config.js. IONOS = domain only; Jonathan can make subdomains. Plan: host free on GitHub Pages (new repo energized/red-ass-hub, public) + a CNAME record "news" -> energized.github.io at IONOS.
- Logo: Jonathan says it's lopsided (3 flames, 1 A). Options in qa/logo-options.png: Option 1 A+A (real card), Option 2 R top + A bottom. Waiting for his pick; then update hub logo and send Red Dealer the new logo.svg for the game icons.
- 2026-10-13 09:56: Jonathan picked logo OPTION 1 (A + small flame in top-left, same group turned 180 degrees in bottom-right, big flame center). Final file: site/img/logo.svg (also qa/logo-final.svg). All letters outlined, no <text>, no <use>. Must be rolled out everywhere: game table + redass.net homepage + icons (Red Dealer), Godot table (Godot Dealer). Messages sent via Jonathan.
- 2026-10-13 10:05: Repo energized/red-ass-hub (public) created by Jonathan; site pushed (commit e293720). Layout: docs/ = published site (with CNAME news.redass.net, .nojekyll), project/ = notes (not published). This proxy blocks the GitHub Pages API, so Jonathan turns Pages on by hand (Settings > Pages > main, /docs). Then IONOS CNAME news -> energized.github.io, then tick Enforce HTTPS. red-ass-voice exists (private).
- From now on, the repo is the source of truth: edit /home/claude/red-ass-hub (clone it fresh in a new session), not /home/claude/hub.
- 2026-10-13 16:05: LIVE at http://news.redass.net (Pages on, branch main /docs; IONOS CNAME news -> energized.github.io, after fixing a "gethub" typo). HTTPS certificate still pending; Jonathan to tick Enforce HTTPS in Settings > Pages when it unlocks. This sandbox can't load the live site directly (only via web fetch), so live-address testing is limited.
- 2026-10-13 16:16: Brand kit v1 made (Red-Ass-Brand-Kit-2026-10.zip on Jonathan's Desktop): logos, social covers/profile pics, 8 spicy posts, 4 fill-in templates, 3 stories, letterhead (docx+pdf), business cards, game night flyer, email signature, wallpapers, fonts, 5-page brand guide. Generator scripts in project/brand-kit-src/ (paths point at the old sandbox; adjust before reusing). Email signature logo hosted at docs/img/brand/email-signature-logo.png. Forgetting "last card" = draw 1 (not 4).
- 2026-10-13 16:57: Godot Dealer confirmed the even ace logo is in the Godot app (assets/logo.svg at 4x; home screen, update notice, app + window icon). Still waiting on Red Dealer for the game table, redass.net homepage and icons.
- 2026-10-13 17:10: Jonathan asked for a CLEAN kit (no small flames, '2026 crisp'). Made project/logo-clean.svg (A top-left + upside-down A bottom-right, one centered bigger flame, no small flames) and Red-Ass-Brand-Kit-Clean-2026-10.zip on his Desktop: flat Night #0f1319 / Cream #f6f1e8 / Burn red backgrounds, no patterns or card fans, type-led posts. NOT yet rolled out to hub/game/Godot - waiting for Jonathan to choose.
- 2026-10-13 17:33: Table-blue version of the clean kit made (Red-Ass-Brand-Kit-Clean-Table-Blue-17202B-2026-10.zip on Desktop). Game table blue = #17202B with centre glow #1E2A38 (from public/index.html --felt/--felt2).
- 2026-10-13 18:36: FINAL LOGO DECISION: Jonathan picked the CLEAN ace (big centered flame, A top-left + upside-down A bottom-right, NO small flames). Hub switched (logo.svg, logo-small.svg, favicons, apple-touch, og.png, email-signature logo). Messages sent to Red Dealer and Godot Dealer to switch. This replaces the 09:56 'Option 1' logo.
- 2026-10-16: Play Anywhere device graphics (9 images, table blue, clean ace; some with QR, some with handles; TikTok left off until confirmed) -> Red-Ass-Play-Anywhere-Graphics-Table-Blue-2026-10.zip on Desktop. Joined team mailbox energized/redass-team (inbox/social); sent status note to Commander.
- 2026-10-16 15:00: Jonathan asked: hero fan on home page now deals 4 random card backs each visit; middle card is the ace logo ~1 in 3, otherwise a featured card back with a gold edge (.fan .c.star). Inline script in docs/index.html right after the fan; tested 30 loads (10 logo / 20 back), 390 + 1280 px, no errors.
- 2026-10-16: News box VERIFIED by Jonathan 14:58 (shows game versions from news.json). Random card fan approved and live.
- 2026-10-16 15:32: Hub now reads card backs live from the game: config BACKS_URL=https://www.redass.net/backs.json (list) + BACKS_IMG=https://www.redass.net/backs/<id>.webp. Gallery uses live list (5 s timeout), falls back to data/backs.json / local 40. Home refreshes a saved copy (localStorage ra_backs_v1) so the next visit's fan can deal new backs; missing images fall back to local. Waiting on Browser to publish /backs.json (asked via mailbox). Until then nothing changes for visitors.
- 2026-10-16 19:32: 3D style guide v1 (glossy vinyl toy, Jonathan's pick) at project/3d/3D-STYLE-GUIDE.md + rarity-frames.png. /backs.json built by Browser, on staging as 1.115.1 (shape [{id,name}], 40 entries, CORS *, 5 min cache) - hub code already matches; goes live when Jonathan publishes.
- 2026-10-16 19:47: Enforce HTTPS is ON (Jonathan). TikTok @ra.tiktok19 was a mistake; hidden from the hub (config TIKTOK ""), social cards re-flow to fill the row. New handle expected 2026-10-17: paste full link into docs/config.js TIKTOK.
- 2026-10-16 19:50: 'Play anywhere' strip added to home (between How it works and Looks): devices picture (site on phone/laptop/tablet), QR to www.redass.net on desktop, Play Now button on phones. Tested 390/1280, no sideways scroll.
- 2026-10-17 10:45: RULE (Jonathan): do NOT post or schedule anything through Metricool (or any social account) until Jonathan gives the go and the live/launch date. The posting-plan doc's dates (19 Oct start) were my assumption, not approved. Nothing has been posted or scheduled.
- 2026-10-23 20:24: Jonathan: news.redass.net colours are THE Red Ass colours; game (redass.net 1.116.8) should match. Spec + draft CSS sent to Browser via mailbox: project/game-theme/table-theme.css, before-after.png.
