# Red Ass brand kit + news feed (owned by Social; first written 2026-10-12)

## NEWS FEED
- Status as of 2026-10-12 (dated, old): version 1.114.0 was on staging. Current live game version is 1.124.4.
- Feed URL: to be confirmed. The old address (https://www.redass.net/news.json) is unknown after the move. The game now lives at play.redass.net; redass.net is the new landing page.
- Shape (newest first, up to 20): [{ "version": "1.113.0", "date": "2026-10-12", "title": "Captions for voice chat", "items": ["plain sentence", "plain sentence"] }]
- Hand-written, player-facing wording only. `date` = day the version was built, not necessarily went live.
- CORS: Access-Control-Allow-Origin: *. Cache-Control: public, max-age=300. GET/HEAD only.
- 13 entries as of 2026-10-12 (1.100.0 to 1.113.0); dated, not rechecked.
- The hub must handle the feed being unavailable (show a friendly fallback).

## NAME AND VOICE
- Name: Red Ass. Tagline: "Draw. Burn. Repeat."
- Adults 18+: playful, cheeky, a little spicy, burns and teasing between friends. Never mean, never about real people.
- No registered-mark symbol, never say "trademarked".
- Wordmark: "Red" plain + "Ass" bold, Oswald 600, uppercase, letter-spacing .05em.

## LOGO (the mark)
- Cream playing card tilted 9 degrees counter-clockwise, flame on it. viewBox 120 0 160 210.
- Card: x140 y20, 120x168, radius 12, fill #fbf8f3, stroke #1a1f2b width 5.
- Top-left "A", Oswald 600, size 30, #c4211b.
- Big flame center (outer red #c4211b, inner gold #e8ab35). An A top-left and the same A upside down bottom-right. No small flames.
- Logo file (checked 2026-11-04 on branch social/brand-kit-refresh): the master is project/logo-final.svg. Identical copies (same blob) are project/logo-clean.svg and docs/img/logo.svg. In that file the "A" is already outlined paths and the flame is plain paths (no live text, no <use>). Ask energizedGG which logo issues he means.
- Existing icons in game repo public/: favicon-48.png, icon-192.png, icon-512.png, icon-maskable-512.png, apple-touch-icon.png.
- Later sizes: Play Store icon 512x512; Play feature graphic 1024x500; phone screenshots 1080x1920; App Store icon 1024x1024 (no transparency, no rounded corners).

## COLORS
- Brand ink and muted text (art, posts, pages, logo): ink #1A1F2B, muted text #4F5868.
- Light: bg #eef0f3, surface #ffffff, accent red #c4211b, gold #e8ab35, good #1d7a4a.
- Game light theme (UI), unverified: text #161a22, muted #566070.
- Dark: bg #0f1217, surface #1a1f28, text #eceef2, accent #ff5a4f.
- Table felt (default): #17202b, lighter #1e2a38, text #e9edf3.
- Other table looks: green #0f3d2a / #17533a (gold #f0cf6a), purple #1b0f26 (gold #ff9d2e), pink #4a1030, navy #0e1d4a, orange-brown #633a17.

## FONTS (Google Fonts)
- Display: Oswald 500/600 (headings, uppercase). Body: IBM Plex Sans 400/500/600. Mono: IBM Plex Mono.

## CARDS AND ART
- Cards 5:7. 58 card backs (43 gilded illustrated, 14 SVG holiday/theme, Classic red stripes). Illustrated: gold frame, 260x364 webp q58, 8% safe margin, game adds rounded corners.
- 18 of the backs exist only as inline CSS in the game's index.html (not as /backs/<id>.webp) - per Godot team notes (Godot is on hold).
- Paper dolls: flat vector, 4 body shapes, 8 skin tones, 8 hair styles, 8 hair colors, 126 wardrobe pieces. Drawn in code as SVG. Looks only, never helps you win.

## RULES FOR ALL BRAND WORK
- Cosmetics only, never pay-to-win. 18+. No other companies' logos/characters/fonts. No real people.
- Merch, Steam, Play Store, trademark/LLC are ON HOLD: do not announce them.
- Secrets never in chat, GitHub or wiki. Ask energizedGG before privacy, payments, analytics or legal text.

## PART 3 (ComfyUI, a current crew member: makes the art and the 3D wardrobe)
Card back spec: 5:7 portrait, generate large (1040x1456 or 1200x1680), shrunk to 260x364. Subject centered, ~8% margin, gold ornamental frame like the gilded set, no text/logos/real people/other companies' characters. Must read at 56 px wide: bold simple shapes.
Already covered (don't duplicate): landscapes/water, space, foods, nature - full list in tools/cardbacks.json.
Standing procedure per batch (energizedGG's rule):
1) Name each back by what the picture SHOWS.
2) Fill in type, color and search words in tools/cardbacks.json (fields: id, name, src, type, color, words).
3) Run tools/addbacks.py: trims pale edges, resizes to 260x364, saves webp q58 in public/backs/, updates Backpack names and search tags.
4) Tell energizedGG about duplicates or look-alikes. They are marked "held" and NOT added. NEVER delete or skip anything until energizedGG decides.
Who does what: ComfyUI delivers image files (named by id, e.g. comet.png) plus filled-in cardbacks.json lines. Browser builds, Backend checks, Helix approves, energizedGG presses Publish. Social owns the kit.

Style guide for backs:
- Warm, bold, slightly cheeky. Gold ornamental frame like the gilded set. Limited palette per back (navy, teal, blue, green, red, brown, purple, plus gold).
- Must read at 56 px wide: bold simple shapes.
- No text, logos, real people, other companies' characters, nothing that needs rotating.
- Under ~40 KB as webp after shrinking.

Frames and portraits (later): no real art yet. Ask energizedGG for sizes from the in-game wiki pages "Avatar frames and portraits" and "Table looks and frames" first.

Housekeeping:
- Save model, prompt and seed next to each image so any back can be remade.
- No prompts naming living artists, brands or copyrighted characters.
- Never put secrets or keys in chat, GitHub or the wiki.
