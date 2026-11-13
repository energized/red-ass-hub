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
- Game light theme (UI), checked 2026-11-06 against the live game CSS (energized/Red-Ass main, game 1.127.13, source/game/template.html): page bg #e8e0d0, surface #f8f4ec, surface2 #ddd3c0, line #a99d86, text #1a1f2b, muted #4f5868, accent text #a81a14, gold text #7f5504, good #1d7a4a. The older figures text #161a22 and muted #566070 were wrong for the light theme: #161a22 is the playing-card ink (--ink, used in every theme) and #566070 was not found anywhere in the game page CSS.
- Game dark theme (the default), same check: page bg #17202b, cream panel surface #fbf8f3 (text on it #1a1f2b), light text #e9edf3, muted #a3afc0, accent text #ff5a4f, gold #e8ab35, good #4cc790.
- Dark (hub or older notes, not the game; not rechecked): bg #0f1217, surface #1a1f28, text #eceef2, accent #ff5a4f.
- Table felt (default): #17202b, lighter #1e2a38, text #e9edf3.
- Header colors (named, added 2026-11-13, approved by energizedGG for Social to decide): header navy #121922 (the bar background is this at 94%, rgba(18,25,34,.94), and the phone menu panel is solid #121922); header line #2c3b4d (1px lines under the bar, under menu rows and in the kit's felt border). Used for the Standard header only. Reason: both are what the live hub already uses, and the header is copied, not redrawn, so naming them keeps every site identical; mapping them to the nearest kit colors (#17202b, #1e2a38) would change the live look.
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

## STANDARD HEADER (added 2026-11-13 by Social, branch social/standard-header)
STATUS: APPROVED by energizedGG 2026-11-13 for these points: (1) PLAY NOW always points to https://play.redass.net; (2) the Home / News / How to Play / Gallery links on sites outside the hub, as in the table below; (3) the two header shades are named header colors in the COLORS list (Social's decision, as energizedGG asked). The phone layout is read from the CSS, not yet tested on a real phone.
The header on https://news.redass.net/ is the Red Ass standard header for the marketing site, policy pages, wiki and admin pages.
- NOT in scope: the in-game table screen. A slim in-game variant is NOT part of this job and has no spec here.
- Source (checked 2026-11-13): the live page, plus energized/red-ass-hub main (39bfc3e) docs/index.html, docs/css/style.css, docs/js/main.js, docs/config.js. The header rules in the repo CSS and the live CSS read the same. One difference on purpose: the hub's PLAY_URL in config.js still says https://www.redass.net, which is old; this spec uses https://play.redass.net.
- Copy the header, do not redraw it. If the hub header changes, this section changes first (energizedGG's yes needed).

### The look, in numbers
- Bar: sticky at the top, full width, content centered in a 1120px column with 16px side padding. Height at least 64px, plus a 1px bottom line in header line #2c3b4d.
- Background: header navy #121922 at 94% (rgba(18,25,34,.94)), with an 8px background blur. Both shades are named header colors in the COLORS list.
- Logo: img/logo-small.svg (copy of the mark, same blob family as logo-final.svg), 40x40 px (34x34 under 375px wide), with the wordmark "RED ASS" beside it: "Red" regular + "Ass" bold, Oswald, uppercase, letter-spacing .05em, 1.35rem (1.15rem under 375px), color #e9edf3. Gap between logo and wordmark 8px. The whole logo + wordmark is one link to the site's home, tap height at least 44px. Keep at least 8px clear on all sides inside the bar (the bar's own 16px side padding covers the left edge); no other element goes inside that space. Draft rule: the 8px clearance is what the hub does today, not a number written down before.
- Nav items, in this order: Home, News, How to Play, Gallery. Do not add, drop or reorder on one site only. Oswald 500, 1rem, uppercase, letter-spacing .06em, color #e9edf3, 14px side padding, 44px tall, 4px between items, hover background #1e2a38 with white text.
- Current page: the item gets aria-current="page", gold text #e8ab35 and a 3px gold underline (#e8ab35) along the bottom of the item. Only one item at a time.
- PLAY NOW button, far right on desktop: glossy red, background #c4211b, white text, 2px border #e0443d, radius 10px, shadow 0 4px 0 #a01a15 plus a soft red glow 0 10px 24px -8px rgba(196,33,27,.7). Oswald 600, 1rem, uppercase, letter-spacing .06em, small white play-triangle icon before the words. 44px tall, padding 8px 16px (8px 12px under 375px). Hover: background #d42a23, lifts 1px. Pressed: sinks 2px, shadow 0 2px 0 #a01a15. Always links to https://play.redass.net on every site and page, and opens in a new tab (target="_blank" rel="noopener"). Same button on every site; never recolored, never renamed, never pointed anywhere else.
- Focus ring: 3px gold outline (#e8ab35), 3px offset. Skip link ("Skip to content") sits above the header.

### Phone behavior (under 860px wide)
- Nav links are hidden. A Menu button (48x48, hamburger icon, 2px border #a3afc0, radius 10px) sits at the far right, after the PLAY NOW button. Left to right on a phone: logo + wordmark, PLAY NOW, Menu.
- PLAY NOW always stays visible in the bar, never inside the menu.
- Open menu: a full-width panel drops from the bottom of the bar (background header navy #121922, 1px line header line #2c3b4d), one link per row, 52px tall, 1.15rem, thin divider lines. The current page gets a 4px gold bar on its left edge instead of the underline. The Menu button turns gold while open and says "Close" to screen readers. Escape or a tap outside closes it.
- 860px and wider: Menu button hidden, links shown in the bar.
- Under 375px: smaller logo (34px), smaller wordmark (1.15rem), tighter button padding, 8px gaps.
- Motion: the lift and sink effects switch off for visitors who ask for reduced motion.

### Which links change per site
Everything else is fixed. Only the four nav links (and the logo link) and the current-page mark change. PLAY NOW does not change: it is https://play.redass.net everywhere.
| Item | On news.redass.net (the hub) | On every other Red Ass site (main site, game policy pages, wiki, admin) |
|---|---|---|
| Logo + wordmark, Home | index.html (stays on the hub) | https://www.redass.net/ |
| News | news.html | https://news.redass.net/news.html |
| How to Play | how-to-play.html | https://news.redass.net/how-to-play.html |
| Gallery | gallery.html | https://news.redass.net/gallery.html |
| PLAY NOW | https://play.redass.net | https://play.redass.net |
| Current page mark (aria-current="page") | set on the page you are on | none of the four are on these sites, so leave it off, unless the page really is one of them (the hub pages) |
On the hub itself, Home stays on the hub (index.html).

### Ready-to-copy snippet (taken from the hub, 2026-11-13; PLAY NOW address and header colors updated 2026-11-13)
Needs: the Google Fonts line, img/logo-small.svg copied from the hub (docs/img/logo-small.svg), the HTML, the CSS and the small menu script. Change only the hrefs in the table above and move aria-current to the right link. The hrefs below are the HUB version; on other sites swap in the right-hand column of the table. Do not change the PLAY NOW href.

HTML (put right after the opening body tag):
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=Oswald:wght@400;500;600&display=swap">

<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="Red Ass home"><img src="img/logo-small.svg" alt="" width="40" height="40"><span class="wordmark">Red <b>Ass</b></span></a>
    <button class="menu-btn" type="button" aria-controls="site-nav" aria-expanded="false" data-open-label="Menu" data-close-label="Close"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" d="M4 7h16M4 12h16M4 17h16"/></svg><span class="sr-only">Menu</span></button>
    <nav class="nav" id="site-nav" aria-label="Main">
      <ul>
        <li><a href="index.html" aria-current="page">Home</a></li>
        <li><a href="news.html">News</a></li>
        <li><a href="how-to-play.html">How to Play</a></li>
        <li><a href="gallery.html">Gallery</a></li>
      </ul>
    </nav>
    <a class="btn btn-play" href="https://play.redass.net" target="_blank" rel="noopener"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path fill="currentColor" d="M4 2.5v11l9.5-5.5z"/></svg><span>Play Now</span></a>
  </div>
</header>
```

CSS (the pieces the header needs; same values as the hub stylesheet, with the two header shades now named):
```css
:root{
  --header-navy:#121922; --header-line:#2c3b4d;
  --felt2:#1e2a38; --felt-fg:#e9edf3; --felt-muted:#a3afc0;
  --ink:#1a1f2b; --red:#c4211b; --red-dark:#a01a15; --gold:#e8ab35;
  --display:'Oswald','Arial Narrow',Impact,sans-serif;
  --body:'IBM Plex Sans',system-ui,-apple-system,'Segoe UI',sans-serif;
  --gutter:16px; --max:1120px;
}
*,*::before,*::after{box-sizing:border-box}
body{margin:0;font:400 1rem/1.6 var(--body);color:var(--felt-fg);background-color:#17202b}
img{max-width:100%;height:auto;display:block}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:4px}
.skip{position:absolute;left:8px;top:-60px;z-index:100;background:var(--gold);color:var(--ink);padding:10px 16px;border-radius:8px;font-weight:600;text-decoration:none}
.skip:focus{top:8px}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.wrap{width:100%;max-width:var(--max);margin:0 auto;padding:0 var(--gutter)}
.wordmark{font-family:var(--display);text-transform:uppercase;letter-spacing:.05em;font-weight:400;white-space:nowrap}
.wordmark b{font-weight:600}
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:.5em;
  min-height:48px;padding:10px 22px;border-radius:10px;border:2px solid transparent;
  font:600 1.05rem/1.1 var(--display);text-transform:uppercase;letter-spacing:.06em;
  text-decoration:none;cursor:pointer;transition:transform .15s ease, background-color .15s ease;
}
.btn-play{background:var(--red);color:#fff;border-color:#e0443d;box-shadow:0 4px 0 var(--red-dark),0 10px 24px -8px rgba(196,33,27,.7)}
.btn-play:hover{background:#d42a23;color:#fff;transform:translateY(-1px)}
.btn-play:active{transform:translateY(2px);box-shadow:0 2px 0 var(--red-dark)}
.btn-play svg{width:1em;height:1em}

/* header */
.site-header{position:sticky;top:env(safe-area-inset-top,0px);z-index:50;background:rgba(18,25,34,.94);border-bottom:1px solid var(--header-line);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.bar{display:flex;align-items:center;gap:10px;min-height:64px}
.brand{display:flex;align-items:center;gap:8px;color:var(--felt-fg);text-decoration:none;font-size:1.35rem;min-height:44px;margin-right:auto}
.brand img{width:40px;height:40px}
.brand:hover{color:#fff}
.nav{display:none}
.nav ul{list-style:none;margin:0;padding:0;display:flex;gap:4px}
.nav a{display:flex;align-items:center;min-height:44px;padding:0 14px;border-radius:8px;color:var(--felt-fg);text-decoration:none;font:500 1rem var(--display);text-transform:uppercase;letter-spacing:.06em}
.nav a:hover{background:var(--felt2);color:#fff}
.nav a[aria-current="page"]{color:var(--gold);box-shadow:inset 0 -3px 0 var(--gold)}
.site-header .btn-play{min-height:44px;padding:8px 16px;font-size:1rem}
.menu-btn{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;border-radius:10px;border:2px solid var(--felt-muted);background:transparent;color:var(--felt-fg);cursor:pointer;padding:0}
.menu-btn svg{width:24px;height:24px}
/* the button sits before the menu in the page (so Tab goes from it into the links) but shows at the far right */
.menu-btn{order:3}
.menu-btn[aria-expanded="true"]{border-color:var(--gold);color:var(--gold)}
/* phone menu: drops down like a dealt row */
.nav.open{display:block;position:absolute;left:0;right:0;top:100%;background:var(--header-navy);border-bottom:1px solid var(--header-line);padding:8px var(--gutter) 16px;box-shadow:0 20px 30px -10px rgba(0,0,0,.6)}
.nav.open ul{flex-direction:column}
.nav.open a{min-height:52px;font-size:1.15rem;border-bottom:1px solid var(--header-line);border-radius:0}
.nav.open a[aria-current="page"]{box-shadow:inset 4px 0 0 var(--gold);padding-left:18px}
@media (min-width:860px){
  .menu-btn{display:none}
  .nav,.nav.open{display:block;position:static;background:none;border:0;padding:0;box-shadow:none}
  .nav.open ul{flex-direction:row}
  .nav.open a{min-height:44px;font-size:1rem;border:0;border-radius:8px}
  .brand{margin-right:12px}
  .nav{margin-right:auto}
}
@media (max-width:374px){
  .brand .wordmark{font-size:1.15rem}
  .brand img{width:34px;height:34px}
  .site-header .btn-play{padding:8px 12px}
  .bar{gap:8px}
}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation:none!important;transition:none!important}
  .btn-play:hover{transform:none}
}
```

JS (menu on phones; put before the closing body tag):
```html
<script>
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    var label = btn.querySelector('.sr-only');
    var setOpen = function (open) {
      nav.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (label) label.textContent = open ? btn.getAttribute('data-close-label') : btn.getAttribute('data-open-label');
    };
    btn.addEventListener('click', function () { setOpen(!nav.classList.contains('open')); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { setOpen(false); btn.focus(); }
    });
    document.addEventListener('click', function (e) {
      if (nav.classList.contains('open') && !nav.contains(e.target) && !btn.contains(e.target)) setOpen(false);
    });
  }
})();
</script>
```
Notes: the hub also sets the PLAY NOW address from config.js (PLAY_URL, applied to every link marked data-play by docs/js/main.js lines 29-30). The hub fix is to set PLAY_URL to https://play.redass.net and change the hard-coded hrefs; other sites can write the address straight into the href as above. The page behind the header needs a dark background such as #17202b so the white wordmark can be read. Last checked against the live hub 2026-11-13; the phone layout is read from the CSS, not yet tested on a real phone.
