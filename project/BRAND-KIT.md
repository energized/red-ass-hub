# Red Ass brand kit + news feed (from Red Dealer, 2026-10-12)

## NEWS FEED
- Version 1.114.0, on staging, NOT live until Jonathan publishes.
- Final URL once live: https://www.redass.net/news.json
- Shape (newest first, up to 20): [{ "version": "1.113.0", "date": "2026-10-12", "title": "Captions for voice chat", "items": ["plain sentence", "plain sentence"] }]
- Hand-written, player-facing wording only. `date` = day the version was built, not necessarily went live.
- CORS: Access-Control-Allow-Origin: *. Cache-Control: public, max-age=300. GET/HEAD only.
- 13 entries today (1.100.0 to 1.113.0).
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
- Big flame center (outer red #c4211b, inner gold #e8ab35); small flames top-left under the A and upside down bottom-right.
- Weak spots: "A" is live text (should be outlined to shapes); flames use <use> (some tools skip); no standalone logo.svg exists yet - make one. Ask Jonathan which logo issues he means.
- Existing icons in game repo public/: favicon-48.png, icon-192.png, icon-512.png, icon-maskable-512.png, apple-touch-icon.png.
- Later sizes: Play Store icon 512x512; Play feature graphic 1024x500; phone screenshots 1080x1920; App Store icon 1024x1024 (no transparency, no rounded corners).

## COLORS
- Light: bg #eef0f3, surface #ffffff, text #161a22, muted #566070, accent red #c4211b, gold #e8ab35, good #1d7a4a.
- Dark: bg #0f1217, surface #1a1f28, text #eceef2, accent #ff5a4f.
- Table felt (default): #17202b, lighter #1e2a38, text #e9edf3.
- Other table looks: green #0f3d2a / #17533a (gold #f0cf6a), purple #1b0f26 (gold #ff9d2e), pink #4a1030, navy #0e1d4a, orange-brown #633a17.

## FONTS (Google Fonts)
- Display: Oswald 500/600 (headings, uppercase). Body: IBM Plex Sans 400/500/600. Mono: IBM Plex Mono.

## CARDS AND ART
- Cards 5:7. 58 card backs (43 gilded illustrated, 14 SVG holiday/theme, Classic red stripes). Illustrated: gold frame, 260x364 webp q58, 8% safe margin, game adds rounded corners.
- 18 of the backs exist only as inline CSS in the game's index.html (not as /backs/<id>.webp) - per Godot team notes.
- Paper dolls: flat vector, 4 body shapes, 8 skin tones, 8 hair styles, 8 hair colors, 126 wardrobe pieces. Drawn in code as SVG. Looks only, never helps you win.

## RULES FOR ALL BRAND WORK
- Cosmetics only, never pay-to-win. 18+. No other companies' logos/characters/fonts. No real people.
- Merch, Steam, Play Store, trademark/LLC are ON HOLD: do not announce them.
- Secrets never in chat, GitHub or wiki. Ask Jonathan before privacy, payments, analytics or legal text.

## PART 3 (for a future ComfyUI Claude - pass along, not ours)
Card back spec: 5:7 portrait, generate large (1040x1456 or 1200x1680), shrunk to 260x364. Subject centered, ~8% margin, gold ornamental frame like the gilded set, no text/logos/real people/other companies' characters. Must read at 56 px wide: bold simple shapes.
Already covered (don't duplicate): landscapes/water, space, foods, nature - full list in tools/cardbacks.json.
Standing procedure per batch (Jonathan's rule):
1) Name each back by what the picture SHOWS.
2) Fill in type, color and search words in tools/cardbacks.json (fields: id, name, src, type, color, words).
3) Run tools/addbacks.py: trims pale edges, resizes to 260x364, saves webp q58 in public/backs/, updates Backpack names and search tags.
4) Tell Jonathan about duplicates or look-alikes. They are marked "held" and NOT added. NEVER delete or skip anything until Jonathan decides.
Who does what: ComfyUI Claude delivers image files (named by id, e.g. comet.png) plus filled-in cardbacks.json lines. Red Dealer does the import, tests and release.

Style guide for backs:
- Warm, bold, slightly cheeky. Gold ornamental frame like the gilded set. Limited palette per back (navy, teal, blue, green, red, brown, purple, plus gold).
- Must read at 56 px wide: bold simple shapes.
- No text, logos, real people, other companies' characters, nothing that needs rotating.
- Under ~40 KB as webp after shrinking.

Frames and portraits (later): no real art yet. Ask Jonathan for sizes from the in-game wiki pages "Avatar frames and portraits" and "Table looks and frames" first.

Housekeeping:
- Save model, prompt and seed next to each image so any back can be remade.
- No prompts naming living artists, brands or copyrighted characters.
- Never put secrets or keys in chat, GitHub or the wiki.
