# Site map and hand-off contract (Social Claude, 2026-10-12)

Read PROJECT-BRIEF.md and BRAND-KIT.md first. The game's code is a READ-ONLY copy at /home/claude/red-ass (never edit it).

## Folders
- /home/claude/hub/site/     the website (Ace owns it)
- /home/claude/hub/content/  page words (Jack owns it)
- /home/claude/hub/qa/       test notes and screenshots (Joker owns it)

## Pages (plain static HTML, one shared style.css + one small main.js)
- index.html     Home
- news.html      News
- how-to-play.html
- gallery.html   Card backs (40 real ones in site/img/backs/*.webp, from the game) + "dolls coming soon"
- app.html       Windows app - coming soon (no dates, no promises)
- store.html     Cosmetics store - coming soon (cosmetics only, never pay-to-win, nothing for sale yet)
- 404.html

## Section ids (Ace builds these with placeholder text; Jack writes the words for each id)
Every page: header nav (Home, News, How to Play, Gallery, Play Now button), footer (18+ note, social links, "Red Ass is a card game by Jonathan's family and friends"-style line ONLY if Jack can support it; otherwise plain "© 2026 Red Ass" - no (R), no "trademark").

index.html: #hero (headline, sub-line, Play Now button -> https://www.redass.net), #whats-new (latest 3 news items from feed), #how-it-works (3 short steps teaser -> how-to-play), #looks (strip of card backs -> gallery, "looks only, never pay-to-win"), #social (cards for Facebook, TikTok, YouTube, Discord-coming-soon), #age (18+ note)
news.html: #news-intro, #news-list (all feed items), #news-fallback (shown when feed unavailable)
how-to-play.html: #htp-intro, #setup, #turn, #special-cards, #last-card, #scoring, #winning, #faq
gallery.html: #gallery-intro, #backs (grid of all 40 with names), #dolls (coming soon)
app.html: #app-intro ; store.html: #store-intro ; 404.html: #lost

## Data
- site/config.js holds ALL links in one place: PLAY_URL, NEWS_URL (https://www.redass.net/news.json), FACEBOOK, TIKTOK, YOUTUBE, DISCORD (empty string = show "coming soon").
- News is read in the browser from NEWS_URL. If it fails or is empty: show #news-fallback text. It is NOT live yet, so the fallback is what people will see first.
- Card back names: Jack writes content/backs.json  [{ "id": "comet", "name": "Comet" }, ...] using tools/cardbacks.json names from the game repo.

## Jack's output format
content/<page>.md with one "## #section-id" heading per section, then the exact words. Keep it short; phones.
