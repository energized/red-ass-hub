from playwright.sync_api import sync_playwright
def inl(n,w=64): return open(f"badge-{n}-small.svg").read().replace('width="64" height="64"',f'width="{w}" height="{w}"')
css='''
*{box-sizing:border-box}body{margin:0;font-family:'IBM Plex Sans';color:#E9EDF3;background:#0b1118}
.stage{display:flex;gap:40px;padding:36px;justify-content:center;background:#0b1118}
.phone{width:390px;background:radial-gradient(circle at 50% 0,#1E2A38,#17202B 60%);border:1px solid #2C3B4D;border-radius:26px;padding:22px 18px 26px}
h1,h2,h3{font-family:Oswald;text-transform:uppercase;letter-spacing:.05em;margin:0}
h1{font-size:30px;font-weight:600}h2{font-size:16px;font-weight:500;color:#A3AFC0;margin:22px 0 10px}
.sub{color:#A3AFC0;font-size:14px;line-height:1.5;margin:8px 0 0}
.btns{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px}
.b{border-radius:12px;padding:13px 10px;text-align:center;font-weight:600;font-size:15px;border:1px solid #2C3B4D;background:#1b2634;color:#E9EDF3}
.b.p{background:#C4211B;border-color:#C4211B;color:#fff}.b.w{grid-column:1/3}
.tier{display:flex;gap:12px;align-items:center;background:#1b2634;border:1px solid #2C3B4D;border-radius:14px;padding:10px 12px;margin-bottom:10px}
.tier h3{font-size:17px;font-weight:600}.tier small{color:#A3AFC0;font-size:12.5px}
.bar{height:8px;border-radius:6px;background:#0f1620;margin:7px 0 4px;overflow:hidden}.bar i{display:block;height:100%;background:#E8AB35;border-radius:6px}
.bk{display:flex;gap:14px;align-items:center;background:#1b2634;border:1px solid #2C3B4D;border-radius:14px;padding:12px}
.card{width:70px;height:98px;border-radius:9px;border:2px solid #E8AB35;background:repeating-linear-gradient(45deg,#3a1512 0 8px,#4a1a15 8px 16px);display:grid;place-items:center;font-size:10px;color:#E8AB35;text-align:center;font-family:Oswald;letter-spacing:.06em}
.fine{font-size:12px;color:#A3AFC0;line-height:1.55;margin-top:18px;border-top:1px solid #2C3B4D;padding-top:12px}
.co{width:460px;background:#fff;color:#1A1F2B;border-radius:18px;overflow:hidden;border:1px solid #d7dce4}
.co .hd{background:#17202B;padding:16px 22px;display:flex;align-items:center;gap:10px;color:#E9EDF3}
.co .hd span{font-family:Oswald;font-size:22px;letter-spacing:.05em;text-transform:uppercase}.co .hd b{font-weight:600}
.co .bd{padding:22px}.co .row{display:flex;gap:16px;align-items:center}
.co .im{width:96px;height:96px;background:#17202B;border-radius:14px;display:grid;place-items:center}
.co h3{font-size:22px}.co .pr{font-size:20px;font-weight:600;margin-top:4px}
.co .in{border:1px solid #cfd5de;border-radius:10px;padding:12px;margin-top:10px;color:#4F5868;font-size:14px}
.co .pay{background:#C4211B;color:#fff;text-align:center;border-radius:12px;padding:15px;font-weight:600;margin-top:16px;font-size:16px}
.co .ft{font-size:12px;color:#4F5868;margin-top:12px;line-height:1.5}
.rc{margin-top:18px;background:#F1EBE0;border-radius:12px;padding:14px;font-size:13px;line-height:1.5}
.cap{color:#A3AFC0;font-size:13px;text-align:center;margin-top:12px}
'''
tiers=[("spark","Spark Supporter","$10 of $15",67,"Thanks for striking the match."),("blaze","Blaze Supporter","$10 of $25",40,"Thanks for keeping the fire going."),("inferno","Inferno Supporter","$10 of $50",20,"Thanks for burning the whole place down.")]
t="".join(f'<div class="tier">{inl(n,64)}<div style="flex:1"><h3>{a}</h3><small>{b}</small><div class="bar"><i style="width:{pc}%"></i></div><small>{c}</small></div></div>' for n,a,b,pc,c in tiers)
page=f'''<div><div class="phone"><h1>Supporters</h1>
<p class="sub">Red Ass is free to play. Supporting is optional, 100% cosmetic, and never gives you an edge. Coins are earned by playing and can never be bought.</p>
<div class="btns"><div class="b p">Support $5</div><div class="b p">Support $10</div><div class="b w">Enter your own amount</div></div>
<h2>Badges · example: $10 given so far</h2>{t}
<h2>Inferno exclusive</h2>
<div class="bk"><div class="card">INFERNO<br>BACK</div><div><h3 style="font-size:17px;font-weight:600">Inferno card back</h3><p class="sub" style="margin:4px 0 0;font-size:13px">Unlocked at Inferno. Art coming soon.</p></div></div>
<div class="fine">Optional. 18+. Payments are handled by Lemon Squeezy, who is the seller and sends your receipt. Nothing here changes how you win.</div></div>
<div class="cap">Supporters page, inside Profile (dark first)</div></div>'''
co=f'''<div><div class="co"><div class="hd"><span>Red <b>Ass</b></span></div><div class="bd">
<div class="row"><div class="im">{inl("blaze",92)}</div><div><h3>Red Ass Supporter</h3><div style="font-size:14px;color:#4F5868">Thank you for keeping the fire going.</div><div class="pr">$10.00</div></div></div>
<div class="in">Email for your receipt</div><div class="in">Card details</div>
<div class="pay">Pay $10.00</div>
<div class="ft">Optional support. Cosmetic only: a badge on your profile, nothing that helps you win. 18+ only. Sold and billed by Lemon Squeezy.</div>
<div class="rc"><b>Receipt text</b><br>Thanks for backing Red Ass! Your support counts toward your supporter badges, which appear on your profile within a few minutes. Questions? Reply to this email. Optional support, cosmetic only. 18+.</div></div></div>
<div class="cap">Checkout look: dark header, burn-red button, badge as the product picture (final layout depends on what Lemon Squeezy lets us style)</div></div>'''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1000,"height":1000},device_scale_factor=2)
    pg.set_content(f'<html><head><style>{css}</style></head><body><div class="stage">{page}{co}</div></body></html>'); pg.screenshot(path="supporters-mock.png",full_page=True); b.close()
