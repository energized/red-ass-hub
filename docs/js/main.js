/* Red Ass hub - the only script. No trackers, no cookies, no storage.
   Links come from config.js (window.RA_CONFIG). Feed text is always set with textContent. */
(function () {
  'use strict';
  var C = window.RA_CONFIG || {};
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };
  var safeUrl = function (u) { return typeof u === 'string' && /^https:\/\//i.test(u.trim()) ? u.trim() : ''; };

  /* ---------- phone menu ---------- */
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

  /* ---------- links from config ---------- */
  var play = safeUrl(C.PLAY_URL);
  if (play) $$('[data-play]').forEach(function (a) { a.href = play; });

  $$('[data-social]').forEach(function (el) {
    var key = el.getAttribute('data-social');
    var url = safeUrl(C[key]);
    if (url) {
      if (el.tagName === 'A') { el.href = url; return; }
      // a "coming soon" placeholder that now has a link: turn it into a real link
      var a = document.createElement('a');
      a.href = url; a.target = '_blank'; a.rel = 'noopener';
      if (el.hasAttribute('data-card')) {
        a.className = 'social-card';
        while (el.firstChild) a.appendChild(el.firstChild);
        var go = a.querySelector('.go');
        if (go) go.textContent = el.getAttribute('data-go') || 'Open';
        var what = a.querySelector('.what');
        if (what) what.textContent = what.textContent.replace(/^Coming soon\.\s*/, '');
      } else {
        a.textContent = el.getAttribute('data-label') || key;
      }
      el.parentNode.replaceChild(a, el);
    } else if (el.tagName === 'A' && key !== 'DISCORD' && C.hasOwnProperty(key)) {
      // link removed from config: hide it rather than send people somewhere old
      var li = el.closest('li'); (li || el).hidden = true;
    }
  });

  /* ---------- news ---------- */
  var lists = $$('[data-news]');
  if (lists.length) loadNews();

  function loadNews() {
    var sample = /[?&]feed=sample\b/.test(location.search);
    var url = sample ? 'data/news-sample.json' : safeUrl(C.NEWS_URL);
    if (!url) return showFallback();
    var ctrl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctrl) ctrl.abort(); showFallback(); }, 6000);
    var done = false;
    fetch(url, { signal: ctrl ? ctrl.signal : undefined, credentials: 'omit', cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (data) {
        clearTimeout(timer);
        var entries = clean(data);
        if (!entries.length) throw new Error('empty');
        done = true;
        render(entries);
      })
      .catch(function () { clearTimeout(timer); if (!done) showFallback(); });
  }

  function clean(data) {
    if (!Array.isArray(data)) return [];
    return data.filter(function (e) {
      return e && typeof e === 'object' && typeof e.title === 'string' && e.title.trim();
    }).map(function (e) {
      return {
        version: typeof e.version === 'string' ? e.version : '',
        date: typeof e.date === 'string' ? e.date : '',
        title: e.title,
        items: Array.isArray(e.items) ? e.items.filter(function (i) { return typeof i === 'string' && i.trim(); }) : []
      };
    }).sort(function (a, b) { return cmpVer(b.version, a.version) || (b.date > a.date ? 1 : b.date < a.date ? -1 : 0); });
  }

  function cmpVer(a, b) {
    var x = a.split('.'), y = b.split('.');
    for (var i = 0; i < 3; i++) {
      var d = (parseInt(x[i], 10) || 0) - (parseInt(y[i], 10) || 0);
      if (d) return d;
    }
    return 0;
  }

  function niceDate(s) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(s);
    if (!m) return s;
    var d = new Date(Date.UTC(+m[1], +m[2] - 1, +m[3]));
    try { return d.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' }); }
    catch (e) { return s; }
  }

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function render(entries) {
    lists.forEach(function (list) {
      var limit = parseInt(list.getAttribute('data-limit'), 10) || entries.length;
      var heading = list.closest('#whats-new') ? 'h3' : 'h2';
      list.textContent = '';
      entries.slice(0, limit).forEach(function (e) {
        var li = el('li');
        var art = el('article', 'panel news-item');
        art.appendChild(el(heading, null, e.title));
        var meta = el('p', 'news-meta');
        if (e.version) meta.appendChild(el('span', 'ver', 'Version ' + e.version));
        if (e.date) {
          var t = el('time', null, 'Built on ' + niceDate(e.date));
          t.setAttribute('datetime', e.date);
          meta.appendChild(t);
        }
        if (meta.childNodes.length) art.appendChild(meta);
        if (e.items.length) {
          var ul = el('ul');
          e.items.forEach(function (i) { ul.appendChild(el('li', null, i)); });
          art.appendChild(ul);
        }
        li.appendChild(art);
        list.appendChild(li);
      });
      list.hidden = false;
    });
    $$('[data-news-loading]').forEach(function (n) { n.hidden = true; });
    $$('[data-news-fallback]').forEach(function (n) { n.hidden = true; });
    $$('[data-news-more]').forEach(function (n) { n.hidden = false; });
  }

  function showFallback() {
    if (lists.some(function (l) { return !l.hidden; })) return;
    $$('[data-news-loading]').forEach(function (n) { n.hidden = true; });
    $$('[data-news-fallback]').forEach(function (n) { n.hidden = false; });
  }

  /* ---------- card backs: live list from the game, saved copies as backup ---------- */
  var CFG = window.RA_CONFIG || {};
  var LOCAL = 'astronaut aurora autumn burger canyon coffee comet croissant cupcake dunes earth friedchicken fries galaxy glacier hotdog icecream icecrystal junglefalls lighthouse moon mtnfalls oceancliff pancakes pines pizza pretzel ramen redplanet ringplanet rocket snowpeaks stepfalls sun sunsetbeach sushi taco telescope volcano watermelon'.split(' ');
  var CACHE_KEY = 'ra_backs_v1';
  var okId = function (id) { return typeof id === 'string' && /^[a-z0-9]{2,24}$/.test(id); };
  var cleanList = function (d) {
    var arr = Array.isArray(d) ? d : (d && Array.isArray(d.backs) ? d.backs : []);
    return arr.filter(function (b) { return b && okId(b.id) && typeof b.name === 'string' && b.name.length < 60; })
              .map(function (b) { return { id: b.id, name: b.name }; });
  };
  function loadLiveBacks() {
    if (!CFG.BACKS_URL || !window.fetch) return Promise.reject(0);
    var ctl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctl) ctl.abort(); }, 5000);
    return fetch(CFG.BACKS_URL, { credentials: 'omit', signal: ctl ? ctl.signal : undefined })
      .then(function (r) { clearTimeout(timer); if (!r.ok) throw 0; return r.json(); })
      .then(function (d) {
        var list = cleanList(d);
        if (list.length < 5) throw 0;
        try { localStorage.setItem(CACHE_KEY, JSON.stringify({ ids: list.map(function (b) { return b.id; }), base: CFG.BACKS_IMG, at: Date.now() })); } catch (e) {}
        return list;
      });
  }
  var grid = document.querySelector('[data-backs]');
  if (grid) {
    var fromLocal = function () {
      return fetch('data/backs.json', { credentials: 'omit' })
        .then(function (r) { if (!r.ok) throw 0; return r.json(); })
        .then(function (d) { var l = cleanList(d); if (!l.length) throw 0; return l; })
        .catch(function () { return LOCAL.map(function (id) { return { id: id, name: id.charAt(0).toUpperCase() + id.slice(1) }; }); });
    };
    loadLiveBacks()
      .then(function (list) { buildGrid(list, true); })
      .catch(function () { fromLocal().then(function (l) { buildGrid(l, false); }); });
  } else if (document.querySelector('#hero .fan')) {
    // home page: refresh the saved list quietly so the next visit can deal brand-new backs
    loadLiveBacks().catch(function () {});
  }

  function buildGrid(backs, live) {
    var frag = document.createDocumentFragment();
    backs.forEach(function (b, i) {
      var li = el('li');
      var fig = el('figure');
      var frame = el('div', 'frame');
      var img = new Image(260, 364);
      img.src = (live ? CFG.BACKS_IMG : 'img/backs/') + b.id + '.webp';
      if (live) img.onerror = function () {
        img.onerror = null;
        if (LOCAL.indexOf(b.id) >= 0) img.src = 'img/backs/' + b.id + '.webp'; else li.remove();
      };
      img.alt = b.name + ' card back';
      img.decoding = 'async';
      if (i > 3) img.loading = 'lazy';
      frame.appendChild(img);
      fig.appendChild(frame);
      fig.appendChild(el('figcaption', null, b.name));
      li.appendChild(fig);
      frag.appendChild(li);
    });
    grid.textContent = '';
    grid.appendChild(frag);
  }
})();
