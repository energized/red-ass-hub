# Red Ass 3D Style Guide: "Glossy Vinyl Toy"

_Owner: Social Claude (brand). Version 1, 2026-10-16. Follows Jonathan's decisions of 2026-10-16 (DECISIONS.md, 3D decisions 1-5)._
_Applies to: the 3D character, every cosmetic item, item icons and 2D portraits. Readers: ComfyUI (art), Browser and Godot (viewers), Backend (catalog names)._

**Decided by Jonathan:** human avatars, glossy vinyl toy style, a free CC0 base for the P0 proof, items earned through chests, events, server firsts and sets, earned in-game currency (no real money until a lawyer has reviewed it), P0 proof now and the full system after votes and accolades.
**Approved for now (Jonathan, 2026-10-16 19:43; may change):** rarity tiers and colours (section 7) and the seven set names (section 9).

---

## 1. The look in one line

**A collectible vinyl figure on a card table:** chunky, smooth, glossy, saturated, with a cheeky adult attitude. Think of a designer toy on a collector's shelf, not a kids' cartoon and not a realistic game character.

## 2. The character (humans)

**Proportions** (chunky designer toy):
- About 3 to 3.5 heads tall. The head is big, the hands and feet are slightly oversized, and the legs are short and sturdy.
- Simple, big shapes that read as one silhouette. No thin, fiddly parts: the minimum thickness of anything is about 2% of body height, so nothing snaps visually on a phone.
- Every edge is rounded, like moulded plastic. There are no razor-sharp corners anywhere.

**Faces: adult, not cute.** This is an 18+ game.
- Eyes are small to medium (never big "kawaii" eyes), with defined brows and a visible jaw or chin.
- The default expression is a confident half-smirk. Emotes can go bigger (a smug grin on a win, a dramatic sulk on a loss).
- No baby faces, no blush stickers, no chibi proportions that read as a child. If someone could mistake the figure for a kids' toy ad, it's wrong.

**Body types: the 4 existing shapes become morphs (blend shapes) on one body:**
Broad (a), Curved (b), Straight (c), Round (d). Every worn item must fit all 4 morphs. Test every item on all 4.

**Skin tones: carry over 1:1** (doll.json `skins`, light to deep):
`#FDE0C8  #F5C9A0  #E3A878  #C88A5A  #A8693C  #8A4E2A  #6A3A1F  #4A2814`

**Hair: 8 styles carry over** (short, long, bun, curly, afro, buzz, mohawk, bald), modelled as chunky sculpted shapes (vinyl hair, not strands). **8 hair colours 1:1** (doll.json `hairc`):
`#1B1410  #4A2A14  #8A5A2A  #D9A441  #C4211B  #7B3FA0  #3AA0FF  #E8E8EE`

## 3. Material: "glossy vinyl" without killing phones

One shared material recipe for everything (glTF PBR, works in three.js and Godot 4):

| | Value | Notes |
|---|---|---|
| Base colour | flat, saturated colour blocks | Colour comes from the material, not from painted texture detail |
| Roughness | 0.30 (skin 0.40, hair 0.25) | Smooth plastic |
| Metallic | 0 (real metal parts only: 0.9, roughness 0.25) | Chains, buckles, trophies |
| Clearcoat | 1.0, clearcoat roughness 0.08 | This gives the "vinyl" shine. Use `KHR_materials_clearcoat`; three.js `MeshPhysicalMaterial` and Godot `StandardMaterial3D.clearcoat` both support it |
| Normal map | only for small sculpted detail (seams, stitches) | Keep shapes in the geometry, not in the texture |
| Texture | at most one 512 px texture per item, KTX2 | Most items need none, just material colours |

**Phone fallback:** if the device is weak, drop the clearcoat and use one small baked environment map (the same "studio" map for everyone). The look should still read as glossy because of the highlight shape, not real reflections.

**Gloss rules (so glossy stays clean):**
- One crisp highlight per form, from the key light. No mirror reflections of a room.
- No glitter, noise, grunge, scratches or "realistic wear" textures.
- No neon glow or bloom on items, except a single "Legendary" sparkle effect if Jonathan approves it later.

## 4. Colour on items

- Each item has **up to 3 colours**, like today (`c:[main, accent, detail]`). **Colourways** are material variants of the same mesh.
- Colours are free to be any colour, but must be **saturated and clean**: no muddy browns-greys unless it's the point of the item.
- The **stage, UI and frames** always use the brand colours (section 6). The item never has to match the brand; the frame does.
- Don't make items that copy the brand mark: **no ace-with-flame logo, no "RED ASS" wordmark on items** unless Jonathan asks. The logo stays out of the item system.

## 5. Content rules for items (all teams)

- Cosmetics only. **Rarity is looks, never power.**
- Adult and cheeky, never crude, never nudity, never aimed at kids.
- No real people, no real brands or logos, no other companies' characters, no sports team colours as a named item, no flags of real countries as rare items (avoids fights), no hate symbols, no realistic weapons or drugs.
- Card-table, firehouse, casino-lounge, food and party themes all fit. Flames are fine as a motif on items, separate from the logo.
- Every item gets a plain name (2 to 3 words): what it is plus a twist, e.g. "Dealer Visor", "Burnt Toast Tee", "Last Card Gloves".

## 6. Stage, camera and light: one setup for everything

**Wardrobe turntable (web and Godot):**
- Background: Table blue `#17202B` with a soft centre glow `#1E2A38` behind the character (same as the game table).
- Floor: an invisible floor with a soft round **contact shadow** (black, 35% opacity). No visible pedestal.
- Lights:
  - **Key:** warm white `#FFF3E3`, upper-left front, about 45 degrees.
  - **Fill:** soft, from the front-right at about 30% of the key.
  - **Rim:** cool `#9FC3FF`, from behind and above, to separate the figure from the dark blue.
- Default camera: 3/4 front (yaw 25 degrees to the character's left, pitch 8 degrees down), the whole body in frame with 8% headroom. Spin by drag; idle sway when untouched.

**Item icons (inventory grid):** 512 x 512 PNG, transparent background (the UI adds the Table blue tile and the rarity frame). The item alone, centred, filling about 78% of the tile. Same key/fill/rim and the same 3/4 angle for every item in a slot, so the grid looks tidy. Worn items are shown on an invisible mannequin, so they hold their shape.

**Portraits (2D at the table):** 512 x 512, head and shoulders, the same 3/4 angle, Table blue background with the glow (also export a transparent version). Rendered from the 3D model, never drawn separately, so it always matches.

## 7. Rarity (approved for now, may change)

See `rarity-frames.png` next to this file.

| Tier | Colour | Corner pips | Label |
|---|---|---|---|
| Common | Smoke `#93A0B2` | 0 | COMMON |
| Uncommon | Green `#4CC790` | 1 | UNCOMMON |
| Rare | Blue `#5B9BFF` | 2 | RARE |
| Epic | Purple `#A57BFF` | 3 | EPIC |
| Legendary | Gold `#E8AB35` | 4 | LEGENDARY |
| Server First (special) | Burn red `#C4211B` + gold edge | 4 | SERVER FIRST |

- **Never colour alone:** every tile shows the frame colour, the pip count and the text label, for colour-blind players.
- All tier colours are readable on Table blue.
- The frame is drawn by the UI, never baked into the icon.

## 8. Getting an item: no gambling look

- Chests are **earned in play** (and currency is earned in play). The reveal is **a card dealt face-up**: the card flips, the item rises out of it with the rarity frame. It uses the game's existing "deal" overshoot motion `cubic-bezier(.2,.8,.2,1.15)`.
- **Never:** slot-machine reels, spinning wheels, "odds" countdowns, flashing JACKPOT, near-miss teases, fake scarcity timers.
- New items get a small "New" tag until seen.

## 9. Sets (names approved for now, may change)

A set is 3 to 6 items that share a theme and colourway. Naming rules: 1 to 3 plain words, a card-table or burn twist, no real brands or people.
Starter list: **High Roller**, **Last Card**, **Dealer's Choice**, **Burn Unit**, **Firehouse** (a nod to where the game came from), **Wild Three**, **Reverse King**.

## 10. File and naming conventions

- One `.glb` per item: `<slot>_<name>.glb`, lowercase with hyphens, e.g. `hat_dealer-visor.glb`. Colourways live as material variants inside the file (`KHR_materials_variants`), named `<name>_<colourway>`, e.g. `dealer-visor_red`.
- Ids in the catalog match today's style (`top-tee-basic`) so existing ownership carries over.
- Icons: `icons/<id>__<colourway>.png`; portraits are rendered on demand, not stored per player.
- Phone budget (from the proposal): base body ≤ 8k triangles, each item ≤ 2k, a full outfit about 1.5 MB or less, 60 fps on a mid-range phone.

## 11. P0 proof checklist (what Jonathan will judge)

1. The base human in all 4 body shapes, 3 skin tones (light, mid, deep), on the turntable with the stage above.
2. Three items: a rigid hat, a worn top, shoes, each in 2 colourways.
3. One icon per item, plus one portrait, made with the section 6 setup.
4. It looks like a glossy vinyl figure, adult and cheeky, and reads clearly at portrait size (about 64 px) on a phone.
5. Same files open in the web viewer and in Godot and look the same.

Changes to this guide go through Social (brand) and Commander.
