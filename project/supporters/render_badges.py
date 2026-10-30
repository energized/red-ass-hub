from playwright.sync_api import sync_playwright
names=[("silver","Silver Supporter","Thanks for pulling up a chair.","#A3AFC0"),("gold","Gold Supporter","Thanks for keeping the table lit.","#E8AB35"),("diamond","Diamond Supporter","Thanks for being the reason the lights stay on.","#8EEBFF")]
cards="".join(f'<div class="c"><div class="t">{open(f"badge-{n}.svg").read()}</div><h3>{t}</h3><p>{l}</p></div>' for n,t,l,_ in names)
html=f'''<html><body style="margin:0;background:#17202B;font-family:'IBM Plex Sans';color:#E9EDF3">
<style>.w{{display:flex;gap:24px;padding:32px;background:radial-gradient(circle at 50% 30%,#1E2A38,#17202B 70%)}}
.c{{width:300px;text-align:center}}.t{{background:#1b2634;border:1px solid #2C3B4D;border-radius:18px;padding:12px}}.t svg{{width:100%;height:auto}}
h3{{font-family:Oswald;font-weight:600;letter-spacing:.05em;text-transform:uppercase;margin:14px 0 4px;font-size:22px}}p{{margin:0;color:#A3AFC0;font-size:14px}}</style>
<div class="w">{cards}</div></body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1032,"height":420},device_scale_factor=2)
    pg.set_content(html); pg.screenshot(path="badges-sheet.png")
    for n,*_ in names:
        pg2=b.new_page(viewport={"width":512,"height":512}); pg2.set_content(f'<body style="margin:0;background:transparent">{open(f"badge-{n}.svg").read().replace("width=\"240\" height=\"240\"","width=\"512\" height=\"512\"")}</body>')
        pg2.screenshot(path=f"badge-{n}.png",omit_background=True)
    b.close()
