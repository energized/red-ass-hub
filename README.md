# Red Ass news & social hub

The website at **news.redass.net**: news, how to play, card back gallery, and links to the game at www.redass.net.

- `docs/` is the website itself. Everything in it is published by GitHub Pages.
- `docs/config.js` holds every outside link (Play, news feed, Facebook, TikTok, YouTube, Discord). Change a link there and the whole site follows.
- `project/` holds the team's notes (brief, brand kit, page words, test report). It is not published.

No secrets belong in this repository. It is public.

## Public feed for the landing page

`docs/feed.json` is published at `https://news.redass.net/feed.json`. It is read-only, public, and holds no player data. The landing page strip fetches it.

```json
{
  "schema": 1,
  "site": "Red Ass",
  "site_url": "https://news.redass.net/",
  "launch_date": null,
  "updated": "2026-11-05",
  "news": [
    { "title": "...", "date": "YYYY-MM-DD", "summary": "...", "link": "https://..." }
  ]
}
```

- `launch_date`: `null` until energizedGG sets it, then `"YYYY-MM-DD"`. Change it here and the front door follows.
- `news`: newest first, at most 20. Plain text only (no HTML). `link` must start with `https://`. An empty list means no news yet; the strip should hide itself.
- `updated`: the day this file was last edited.
- `docs/feed-sample.json` has made-up SAMPLE entries so the strip can be laid out. Never link to it from a live page.
- If the feed cannot load, the landing page should hide the strip, not show an error.
- Hosting: GitHub Pages serves files with open cross-origin access, so no extra CORS setup is needed. Check once after deploy with a browser request from the landing page.
