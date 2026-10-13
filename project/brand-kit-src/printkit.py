import os, sys, qrcode, qrcode.image.svg; sys.path.insert(0,os.path.dirname(__file__))
from brand import *; import render
from social import CSS, wm, tag, ace_img, fan, foot, LOGO_F, W, T
P=f'{W}/kit/03-print-and-documents'; X=f'{W}/kit/04-extras'; os.makedirs(P,exist_ok=True); os.makedirs(X,exist_ok=True)
L1=f'file://{W}/kit/01-logos/lockup-horizontal-for-light-backgrounds.svg'
L2=f'file://{W}/kit/01-logos/lockup-horizontal-for-dark-backgrounds.svg'
# QR code to the game
q=qrcode.QRCode(border=1,box_size=10,image_factory=qrcode.image.svg.SvgPathImage); q.add_data('https://www.redass.net'); q.make()
q.make_image().save(f'{W}/qr.svg')
open(f'{X}/qr-code-redass-net.svg','wb').write(open(f'{W}/qr.svg','rb').read())
qrcode.make('https://www.redass.net',border=2,box_size=20).save(f'{X}/qr-code-redass-net.png')
QR=f'file://{W}/qr.svg'
PCSS=CSS+'@page{margin:0}'
def doc(name,html,cls='',size=None):
    if size: html=f'<div style="position:relative;width:{size[0]};height:{size[1]};overflow:hidden">{html}</div>'
    f=f'{T}/{name}.html'; open(f,'w').write(f'<html><head><meta charset="utf-8"><style>{PCSS}</style></head><body class="{cls}">{html}</body></html>'); return f

# ---- letterhead (US Letter) ----
lh=f'''<div style="position:absolute;inset:0;background:#fff;color:{INK}"></div>
<div style="position:absolute;left:0;right:0;top:0;height:14px;background:{RED}"></div><div style="position:absolute;left:0;right:0;top:14px;height:5px;background:{GOLD}"></div>
<div style="position:absolute;left:64px;top:52px"><img src="{L1}" style="height:92px"></div>
<div style="position:absolute;right:64px;top:70px;text-align:right;font-size:13px;line-height:1.7;color:#566070;font-family:Plex">www.redass.net<br>news.redass.net<br>discord.gg/gH577r59C8</div>
<div style="position:absolute;left:64px;right:64px;top:170px;height:1.5px;background:#e3dccf"></div>
<div style="position:absolute;right:-60px;bottom:-40px;opacity:.06;transform:rotate(-14deg)"><img src="{LOGO_F}" style="height:520px"></div>
<div style="position:absolute;left:64px;right:64px;bottom:44px;display:flex;justify-content:space-between;font-family:Oswald;letter-spacing:.12em;font-size:12px;color:#566070;text-transform:uppercase"><span>Draw. <b style="color:{RED};font-weight:500">Burn.</b> Repeat.</span><span>Adults 18+</span></div>'''
render.html_pdf(doc('lh',lh,size=('8.5in','11in')),f'{P}/letterhead.pdf','8.5in','11in')
render.html_png(doc('lh',lh),f'{P}/letterhead-preview.png',816,1056)

# ---- business card 3.5x2 + 0.125in bleed each side = 3.75x2.25in (360x216 css px) ----
front=f'''<div style="position:absolute;inset:0;display:flex;align-items:center;gap:22px;padding-left:40px">{ace_img(120,"transform:rotate(-2deg)")}<div>{wm(48)}{tag(13.5,"margin-top:6px")}</div></div>'''
back=f'''<div style="position:absolute;inset:0;padding:30px 34px;display:flex;flex-direction:column;justify-content:space-between">
<div><div class="d" style="font-size:22px;font-weight:600;color:{INK};white-space:nowrap">The card game where<br>your friends are<br><span style="color:{RED}">the enemy.</span></div></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div style="font-size:10.5px;line-height:1.6;color:#566070">www.redass.net<br>discord.gg/gH577r59C8<br><b style="font-family:Oswald;letter-spacing:.12em;color:{RED};font-weight:600">ADULTS 18+</b></div>
<img src="{QR}" style="width:64px;height:64px;background:#fff;padding:3px"></div></div>'''
for nm,h,c in (('business-card-front',front,''),('business-card-back',back,'cream')):
    f=doc(nm,h,c,size=('3.75in','2.25in')); render.html_pdf(f,f'{P}/{nm}-with-bleed.pdf','3.75in','2.25in'); render.html_png(f,f'{P}/{nm}-preview.png',360,216,scale=3)

# ---- game night flyer (Letter) ----
fly=f'''<div style="position:absolute;top:60px;left:0;right:0;text-align:center"><img src="{L2}" style="height:110px"></div>
<div style="position:absolute;top:230px;left:0;right:0;text-align:center"><div class="stamp" style="font-size:28px">Adults only. Grudges welcome.</div>
<div class="d" style="font-size:124px;font-weight:600;margin-top:30px">Game <span class="ember">night</span></div></div>
<div style="position:absolute;left:96px;right:96px;top:520px;display:grid;grid-template-columns:110px 1fr;row-gap:22px;font-family:Oswald;font-size:34px;letter-spacing:.04em;text-transform:uppercase">
<span class="gold">When</span><span style="border-bottom:2px solid rgba(233,237,243,.35)"></span>
<span class="gold">Where</span><span style="border-bottom:2px solid rgba(233,237,243,.35)"></span>
<span class="gold">Table</span><span style="border-bottom:2px solid rgba(233,237,243,.35)"></span></div>
<div style="position:absolute;left:96px;right:96px;bottom:100px;display:flex;align-items:center;justify-content:space-between">
<div><div class="d" style="font-size:44px;font-weight:600">Scan. Sit. <span class="ember">Burn.</span></div><div class="muted" style="font-size:20px;margin-top:10px">Free in your browser at www.redass.net</div></div>
<img src="{QR}" style="width:170px;height:170px;background:#fff;padding:8px;border-radius:10px"></div>'''
f=doc('flyer',fly,size=('8.5in','11in')); render.html_pdf(f,f'{P}/game-night-flyer.pdf','8.5in','11in'); render.html_png(f,f'{P}/game-night-flyer-preview.png',816,1056)

# ---- extras: wallpapers + video call background ----
def shot(name,w,h,body,cls=''):
    render.html_png(doc(name,body,cls),f'{X}/{name}.png',w,h)
shot('phone-wallpaper-1179x2556',1179,2556,f'{fan(590,900,560,("galaxy","volcano"),spread=15)}<div style="position:absolute;top:1780px;left:0;right:0;text-align:center">{wm(120)}{tag(48,"margin-top:20px")}</div>')
shot('desktop-wallpaper-2560x1440',2560,1440,f'<div style="position:absolute;left:300px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">{wm(230)}{tag(80,"margin-top:30px")}</div>{fan(1850,420,560,("galaxy","volcano"),spread=15)}')
shot('video-call-background-1920x1080',1920,1080,f'<div style="position:absolute;right:70px;top:60px;display:flex;align-items:center;gap:22px">{ace_img(130)}<div>{wm(64)}{tag(22,"margin-top:6px")}</div></div>')
print('ok')
