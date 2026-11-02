---
name: red-ass-brand
description: Red Ass brand rules: voice, logo, colours, fonts, themes, art and supporter badges. Use for anything players or the public see (UI, copy, art, posts, pages).
---

# Red Ass brand (owner: Social Claude; only Jonathan saves changes)

Use this for anything players or the public will see: game UI, copy, art, web pages, posts, emails, store text. DECISIONS.md in the team mailbox wins if it ever disagrees with this skill; tell Social about the mismatch. To suggest an addition, leave Social a note in inbox/social/ with a subject starting "brand skill:". Do not edit this skill.

## 1. What Red Ass is
- A family-style card game for adults (18+), played in the browser at https://www.redass.net. Approved line: "Red Ass is a family-style card game for adults (18+). You must be 18 or older to play."
- Tagline: **Draw. Burn. Repeat.**
- News and social hub: https://news.redass.net (repo energized/red-ass-hub).

## 2. Hard rules (never break)
1. **18+ only.** Never aim anything at children. Never imply children may play.
2. **Cosmetics only, never pay-to-win.** Rarity is looks, never power. Coins are earned by playing and can never be bought.
3. **No gambling look:** no casino chips, dice, slot-machine reels, spinning wheels, odds countdowns, flashing JACKPOT, fake scarcity timers. Treasure, trophies and flames are fine.
4. **No (R) symbol and never say "trademarked".** The Red Ass mark is not registered yet.
5. **Nothing is announced before it is live.** Merch, Steam, Play Store, trademark and LLC are on hold: do not mention them.
6. **No secrets or players' personal data** in chat, GitHub or wiki.
7. **Social posting is on hold** until Jonathan gives the live date and a go. Do not post or schedule anything.
8. No other companies' logos, characters or fonts; no real people; no real flags or hate symbols as items. Use original art and Google Fonts only.
9. Ask Jonathan before anything about privacy, collecting data, ads, analytics, payments or legal text. Draft only; he decides.

## 3. Voice
Playful, warm, cheeky, a little spicy: burns and teasing between friends. Never mean, never crude, never about real people. Short plain sentences. No invented claims.
- Good: "Draw. Burn. Repeat." / "Your turn. Try not to embarrass yourself." / "Thanks for keeping the fire going."
- Bad: anything cruel, sexual, kid-friendly cute, corporate ("leverage", "synergy"), or promising what is not live.
- Spell the name "Red Ass". Wordmark: "Red" regular + "Ass" semibold, Oswald, uppercase, letter-spacing .05em.

## 4. Logo
- Final = the "clean ace": a cream playing card tilted 9 degrees counter-clockwise with a big flame in the middle and an A (outlined paths, red) top-left and upside-down bottom-right. Same logo in the hub, the game and the Godot app.
- Master file: red-ass-hub `project/logo-final.svg` (viewBox 120 0 160 210). Card x140 y20, 120x168, radius 12, fill #FBF8F3, stroke #1A1F2B width 5. Flame: red outer #C4211B, gold inner #E8AB35.
- Do not redraw or add small flames. Use the master files; do not trace a new one.

## 5. Colours (hex)
- Table blue (game and hub background) **#17202B**; glow #1E2A38; lamp #22324A; felt line #2C3B4D.
- Cream **#FBF8F3** (also #F1EBE0, #F6F1E8). Ink #1A1F2B; ink-muted #4F5868.
- Light text #E9EDF3; smoke (muted text on dark) #A3AFC0 (game uses #93A0B2).
- Burn red **#C4211B** (hover #A01A15). Ember #FF5A4F. Gold **#E8AB35** (on light backgrounds use #B07A12).
- Good/green #1D7A4A (on dark #4CC790).
- Keep text contrast readable (WCAG AA). Never use colour alone to carry meaning.

## 6. Fonts
Oswald (headings, uppercase, 500/600) and IBM Plex Sans (body 400/500/600), IBM Plex Mono for code. Google Fonts only.

## 7. Game themes and accessibility (live since 1.116.11)
- Themes: Dark (default), Light, Negative (photo-negative, trial). Colourblind modes with a strength slider and a four-colour deck. Prefs are additive: theme 'negative', cbMode, cbStrength, deck4.
- Rarity frames (UI draws them, never baked into icons): Common smoke #93A0B2 (0 pips), Uncommon green #4CC790 (1), Rare blue #5B9BFF (2), Epic purple #A57BFF (3), Legendary gold #E8AB35 (4), Server First burn red #C4211B + gold edge (4). Always show frame colour + pip count + text label.

## 8. Art rules
- Card backs: 5:7 portrait, subject centred, ~8% margin, bold gold ornamental frame, no text/logos/real people, must read at 56 px wide, shipped as 260 x 364 webp (quality ~58, under ~40 KB); the game adds rounded corners.
- 3D (ComfyUI/Browser/Godot): glossy vinyl-toy humans, clearcoat material, colour slots c1/c2/c3 tinted at runtime (no KHR_materials_variants), stage Table blue with warm key light and cool rim #9FC3FF. See red-ass-hub `project/3d/3D-STYLE-GUIDE.md`.
- Do not put the logo or "RED ASS" wordmark on cosmetic items unless Jonathan asks. Flames are fine as a motif.
- AI-made art (placeholders) is fine for now; before launch the tool's current terms are checked. Save prompt, date and original file.

## 9. Supporter badges (cosmetic thank-yous)
- Tiers by lifetime US dollars given: **Spark $15, Blaze $25, Inferno $50** (renamed from Silver/Gold/Diamond on 2026-10-30). Inferno also unlocks the exclusive **Inferno card back**. Players see only another player's tier badge, never the amount.
- Art: one flame that grows. Spark = small amber flame; Blaze = the logo flame; Inferno = a cluster of three flames. Files in red-ass-hub `project/supporters/` (`-small.svg` for 15-34 px).
- Thank-yous: Spark "Thanks for striking the match." Blaze "Thanks for keeping the fire going." Inferno "Thanks for burning the whole place down."
- Page wording must say: optional, cosmetic only, never pay-to-win, 18+, and that Lemon Squeezy is the seller and sends the receipt. Checkout product name: "Red Ass Supporter".

## 10. Accounts and links (all in red-ass-hub docs/config.js)
Play: https://www.redass.net. Discord: https://discord.gg/gH577r59C8 (no expiry). Facebook: https://www.facebook.com/redassgame. YouTube: https://www.youtube.com/@RedAssGame. TikTok: hidden until Jonathan gives the new handle. X, Instagram, Twitch: none yet.

## 11. Before you ship anything public
- 18+ and no kid appeal? Cosmetic only? No gambling look? No (R)/"trademarked"? Nothing unreleased announced?
- Colours and fonts from sections 5-6; logo from the master file; text readable and scalable; alt text on images.
- Test at 360, 390 and 1280 px wide; real phones have never been tested, so say so plainly.
- Any message for another team member goes in one copy-paste box for Jonathan.
