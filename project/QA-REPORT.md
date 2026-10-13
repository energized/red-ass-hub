# QA report: Red Ass news & social hub (news.redass.net)

Tester: Joker (QA) - 2026-10-13
What I tested: the 7 pages in `site/` (Home, News, How to Play, Gallery, Windows App, Store, 404), on my test computer with a robot Chrome browser, at phone widths 360 and 390 and desktop width 1280.

Short version: **the site is in good shape.** Every rule on How to Play matches the game's own code. I fixed 4 small things. 2 small things need a decision from you.

---

## Tested and OK

**Fits on phones and desktop**
- All 7 pages at 360, 390 and 1280 wide: no sideways scrolling, nothing cut off, nothing overlapping.
- I looked at screenshots of every page (saved in `qa/joker-<page>-360.png` and `-1280.png`).
- Everything you can tap is at least 44 x 44 pixels on phones (after fix 1 below).

**Menu and keyboard**
- The phone menu opens and closes by tapping, closes when you tap outside it, and its links work.
- With a keyboard: Tab reaches the menu button, Enter opens it, the next Tab goes into the menu links (after fix 2), Escape closes it and puts you back on the button.
- "Skip to content" is the first thing Tab reaches, shows up on screen, and jumps to the main content on every page (after fix 3 for the 404 page).
- Everything you can Tab to shows a clear gold or red outline.

**Links and pictures**
- Every link between pages works. No missing pictures anywhere.
- Play Now, Facebook, TikTok, YouTube, Terms and Privacy all go to the right addresses, the same ones in `config.js`, and open in a new tab.
- Discord shows "coming soon" in the footer of every page and on the Home page card.

**News**
- With the game's news feed out of reach (it is not live yet, and my test computer could not reach redass.net anyway), Home and News both show the friendly "news is shuffling / taking a smoke break" message. No error shows to visitors.
- With the sample news switched on (`?feed=sample`): Home shows exactly 3 items, News shows all of them, newest first.
- News text containing web code (like `<b>` or a sneaky `<img>` / `<script>`) is shown as plain text and never runs. I tried a deliberately nasty feed: nothing ran.
- An empty or broken feed also shows the friendly message.

**Gallery**
- All 40 card backs load, each with its name under it and a description for screen readers (for example "Comet card back").

**Readability (contrast)**
- I measured 27 text/background color pairs from the style sheet. All pass the standard accessibility level (AA). The lowest is red text on the cream cards at 5.5 : 1 (4.5 is needed).
- Headings are in the right order on every page. Every picture has a description (or is marked as decoration). Language is set to English. Every page has its own title.

**Speed**
- Page sizes (not counting the Google fonts): Home 244 KB, Gallery 855 KB (40 card pictures, most load only as you scroll), the other pages 32-38 KB each. All light for phones.
- No errors from the site's own code. The only browser messages were the blocked Google Fonts and news feed on my test computer (see "NOT tested").

**Facts checked against the game's code** (`engine.js`, the wiki, the changelog and the game page)
- Setup: 2 to 8 players, bots can fill seats; 4 decks up to 6 players, 6 decks for 7-8; 7 cards each. CORRECT.
- First card: a Jack, Queen, King or 3 is burned and another is turned up; a first 2 or 4 is live. CORRECT.
- Dealing: whoever presses Start deals first, the deal moves one seat each round, the player after the dealer goes first. CORRECT.
- Drawing ends your turn; you cannot play the card you drew. CORRECT.
- 3: only on its own suit or another 3, then a bonus card or Done; another 3 as the bonus gives another bonus; a 3 used as a 4-chain step gets no bonus. CORRECT.
- 4 chain: 5, 6 ... K, A, 2, 3, 4 in the same suit; first miss costs 4 cards, +1 per step; once someone pays, it is dead. CORRECT.
- King reverses. 2s: draw 2, each stacked 2 adds 2. CORRECT.
- Last card: forget and get called out = draw 1. Going out on a 2 or 4 means the round ends only when someone pays. CORRECT.
- Points: 4 = 40, 2 = 30, Ace = 20, 10/J/Q/K = 10, everything else = 5. CORRECT.
- Game ends when anyone reaches 500 (host can choose 50 to 5000); lowest total wins. CORRECT.
- In-game guided practice game against bots ("How to play" in the menu): EXISTS.
- Voice chat: EXISTS (the host turns it on per table).
- "Dozens of card backs": the game has 58. OK.
- Mystery chests as you level up: EXIST (at level 2, then every 4th level), and they hold card backs, table looks and doll outfits. OK (see fix 4).
- Other players see your card back: true by default. Doll hats, jackets, wings, capes: all exist.
- Windows app: the game's changelog says it is coming. The site says only "coming soon", no dates or promises. OK.
- Store: "coming soon, cosmetics only, nothing for sale yet". No dates, no prices. OK.

**Brand rules**
- No (R) symbol, no "trademark", no LLC, Steam, Play Store or merch anywhere.
- 18+ note on every page (footer), plus the big 18+ section on Home.
- Footer says only "© 2026 Red Ass".

---

## Fixed (small, clear bugs I fixed myself)

1. **"Store" link in the footer was too small to tap easily** (38 px wide, needs 44). Footer links now have a minimum width. (`css/style.css`)
2. **Phone menu with a keyboard:** after opening the menu, Tab jumped *past* the menu links to the Play Now button. I moved the menu button before the links in the page code (it still shows in the same spot on screen), so Tab now goes straight into the menu. (all 7 pages + one line in `css/style.css`)
3. **404 page "Skip to content" sent people to the Home page** instead of skipping down the 404 page. Cause: a `<base href="/">` line. I removed it and gave every link and file on the 404 page a full path (`/css/style.css`, `/index.html`...), so the page still looks right at any wrong address (tested at `/deep/missing/page`). (`404.html`)
4. **Home page wording:** "Dozens of card backs, table looks and a dress-up paper doll. Found in mystery chests..." made it sound like the doll itself is in chests. Every player has a doll; the *outfits* come from chests. Now reads: "Dozens of card backs, table looks and outfits for your paper doll. Win them from mystery chests as you level up." (`site/index.html`. Jack: please copy this into `content/home.md` line 31 so the two match.)

A backup of the site from before my fixes is at `/tmp/claude-0/joker/site-backup/`.

---

## Still wrong / needs a decision

1. **Wordmark "RED ASS":** the brand rule is "RED" plain + "ASS" bold. The site uses Oswald 500 for RED and 600 for ASS. On screen they look almost the same weight (see the header in any screenshot). If you want a visible difference, Ace could make RED lighter (Oswald 400, one more font weight to load) or make only ASS 600 and RED 400. That's a design call, so I did not change it.
2. **Store page line "One day you'll find card backs, table looks and outfits here."** It has no date, but it is a soft promise of what the store will sell. Fine by the brief as I read it; flagging only so you can say yes or no.

Minor notes, no action needed:
- The game's own wiki says "Every time you level up you win a mystery chest", but the code gives one at level 2 and then every 4th level. The site says "as you level up", which is true either way. (That's a game wiki note for Red Dealer, not a site bug.)
- Players can switch on "Use my back for all" in the game, so "Everyone sees your back" (Gallery) is true by default, not always.

---

## NOT tested

- **Real phones.** Everything was tested in a robot Chrome browser set to phone sizes, not on an actual phone.
- **iPhone Safari** (and Android Chrome / Samsung Internet on a real device). Safari can behave differently, especially the sticky header and blurred header background.
- **The live news feed** (`https://www.redass.net/news.json`). It is not published yet, and my test computer could not reach redass.net at all. Only the sample feed and the "feed unavailable" message were tested. Once it's live, open the News page and check the real entries show up.
- **Real Google Fonts.** Google Fonts was blocked on my test computer. Oswald happened to be installed locally so headings looked right; IBM Plex Sans was replaced by a system font. Page sizes above do not include the fonts (about 50-100 KB more).
- **The site on its real address** (news.redass.net), the hosting, HTTPS, and whether the host actually shows `404.html` for wrong addresses.
- **That the outside links really open** (Facebook, TikTok, YouTube, Terms, Privacy, the game). I checked the addresses are correct; I could not visit them. The TikTok handle `@ra.tiktok19` may be a placeholder, per Jonathan.
- **Screen readers** (VoiceOver, TalkBack) and very large text settings on a phone.
- **Slow mobile connections** and the share preview picture (og.png) on Facebook and other apps.
