import os, sys; sys.path.insert(0,'/tmp/claude-0/kitblue/src')
import cleanlib as C; import render
from cleanlib import wm, tag, ace, frame, RED, GOLD, EMBER, INK, NIGHT, CREAM, BONE, SMOKE, FELT2
D='/tmp/claude-0/devices'; OUT=f'{D}/kit'; os.makedirs(OUT,exist_ok=True)
QR=f'file:///tmp/claude-0/kitblue/qr.svg'
SITE_P=f'file://{D}/site-phone.png'; SITE_T=f'file://{D}/site-tablet.png'; SITE_D=f'file://{D}/site-desktop.png'
EXTRA=f'''
.dev{{position:absolute;background:#0a0d12;box-shadow:0 0 0 2px #2c3b4d,0 40px 80px -20px rgba(0,0,0,.65)}}
.scr{{position:absolute;overflow:hidden;background:{NIGHT} radial-gradient(ellipse at 50% 45%,{FELT2} 0,{NIGHT} 70%);display:flex;align-items:center;justify-content:center;flex-direction:column}}
.scr img.shot{{width:100%;height:100%;object-fit:cover;object-position:top}}
.island{{position:absolute;left:50%;transform:translateX(-50%);background:#000;border-radius:999px}}
.qrcard{{background:#fff;border-radius:22px;display:inline-block}}
.qrcard img{{display:block}}
.handles{{display:grid;row-gap:14px}}
.handles div{{display:flex;justify-content:space-between;gap:24px;border-bottom:1.5px solid rgba(147,160,178,.22);padding-bottom:12px}}
.handles b{{font-family:Oswald;font-weight:500;letter-spacing:.06em;text-transform:uppercase;color:{SMOKE}}}
.handles span{{font-weight:500}}
'''
C.CSS=C.CSS+EXTRA
def phone(x,y,h,content):
    w=h*0.486; r=h*0.095; b=h*0.022
    return f'<div class="dev" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{r}px"><div class="scr" style="left:{b}px;top:{b}px;right:{b}px;bottom:{b}px;border-radius:{r-b}px;justify-content:flex-start;padding-top:{h*0.058}px;background:#121922">{content}</div><div class="island" style="top:{b+h*0.014}px;width:{w*0.3}px;height:{h*0.032}px"></div></div>'
def tablet(x,y,h,content):
    w=h*0.74; r=h*0.05; b=h*0.03
    return f'<div class="dev" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:{r}px"><div class="scr" style="left:{b}px;top:{b}px;right:{b}px;bottom:{b}px;border-radius:{r*0.45}px">{content}</div></div>'
def laptop(x,y,w,content):
    h=w*0.64; b=w*0.022
    return f'''<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px">
<div class="dev" style="position:relative;width:{w}px;height:{h}px;border-radius:{w*0.025}px {w*0.025}px 0 0"><div class="scr" style="left:{b}px;top:{b}px;right:{b}px;bottom:{b*1.6}px;border-radius:4px">{content}</div></div>
<div style="position:relative;margin-left:-{w*0.07}px;width:{w*1.14}px;height:{w*0.032}px;background:linear-gradient(#3a4556,#202833);border-radius:0 0 {w*0.03}px {w*0.03}px;box-shadow:0 30px 60px -18px rgba(0,0,0,.7)"><div style="position:absolute;left:50%;top:0;transform:translateX(-50%);width:{w*0.16}px;height:{w*0.011}px;background:#151b23;border-radius:0 0 8px 8px"></div></div></div>'''
def ace_screen(h,with_wm=False):
    s=ace(h,"transform:translateX(-4%)")
    if with_wm: s+=f'<div style="margin-top:{h*0.18}px">{wm(h*0.17)}</div>'
    return s
shot=lambda src: f'<img class="shot" src="{src}">'
def qr(px,pad=None):
    pad=pad or px*0.09
    return f'<div class="qrcard" style="padding:{pad}px"><img src="{QR}" style="width:{px}px;height:{px}px"></div>'
HANDLES=[('Discord','discord.gg/gH577r59C8'),('Facebook','facebook.com/redassgame'),('YouTube','@RedAssGame'),('Play','redass.net')]
def handles(px):
    return '<div class="handles" style="font-size:%dpx">'%px+''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in HANDLES)+'</div>'
def out(name,w,h,body,cls=''):
    f=C.doc(name,body,cls); render.html_png(f,f'{OUT}/{name}.png',w,h)

# 1. Play anywhere: all three devices (feed post 1080x1350)
out('01-play-anywhere-all-devices-1080x1350',1080,1350,frame(1080,1350,f'''
<div style="position:absolute;left:81px;right:81px;top:210px"><div class="d" style="font-size:118px">Phone. Tablet. PC.<br><span class="hl">Same burn.</span></div></div>
{laptop(170,560,740,shot(SITE_D))}{tablet(700,600,440,shot(SITE_T))}{phone(81,640,400,shot(SITE_P))}
<div class="lbl mute" style="position:absolute;left:81px;top:1100px;font-size:24px">Free in your browser. Nothing to install.</div>'''))

# 2. Phone hero + QR (feed post)
out('02-phone-with-qr-1080x1350',1080,1350,frame(1080,1350,f'''
{phone(560,240,860,shot(SITE_P))}
<div style="position:absolute;left:81px;top:300px;width:440px"><div class="d" style="font-size:112px">Game night<br>fits in your<br><span class="hl">pocket.</span></div>
<div style="margin-top:56px">{qr(200)}</div><div class="lbl mute" style="font-size:20px;margin-top:22px">Scan to play</div></div>'''))

# 3. Phone + social handles (feed post)
out('03-phone-with-socials-1080x1350',1080,1350,frame(1080,1350,f'''
{phone(81,240,760,shot(SITE_P))}
<div style="position:absolute;left:520px;right:81px;top:300px"><div class="d" style="font-size:96px">Play<br>anywhere.<br><span class="hl">Talk trash<br>everywhere.</span></div>
<div style="margin-top:56px">{handles(24)}</div></div>'''))

# 4. Square: phone showing the website + QR
out('04-website-on-phone-qr-1080x1080',1080,1080,frame(1080,1080,f'''
{phone(600,190,700,shot(SITE_P))}
<div style="position:absolute;left:81px;top:250px;width:470px"><div class="d" style="font-size:96px">No app.<br>No download.<br><span class="hl">Just play.</span></div>
<div style="margin-top:44px;display:flex;align-items:center;gap:22px">{qr(150)}<div class="lbl mute" style="font-size:18px;line-height:1.6">Scan or visit<br><span style="color:{BONE}">redass.net</span></div></div></div>'''))

# 5. Square: devices, clean, no QR/links (pure brand)
out('05-every-screen-1080x1080',1080,1080,frame(1080,1080,f'''
<div style="position:absolute;left:0;right:0;top:220px;text-align:center"><div class="d" style="font-size:104px">Every screen is<br>a <span class="hl">card table.</span></div></div>
{tablet(170,560,330,shot(SITE_T))}{phone(450,520,380,shot(SITE_P))}{tablet(670,560,330,shot(SITE_T))}'''))

# 6. Story: phone + QR
out('06-story-phone-qr-1080x1920',1080,1920,frame(1080,1920,f'''
<div style="position:absolute;left:81px;right:81px;top:230px"><div class="d" style="font-size:130px">Play on<br>your <span class="hl">phone.</span></div></div>
{phone(320,560,900,shot(SITE_P))}
<div style="position:absolute;left:0;right:0;top:1540px;display:flex;justify-content:center;align-items:center;gap:30px">{qr(180)}<div class="lbl mute" style="font-size:24px;line-height:1.6">Scan to play<br><span style="color:{BONE}">redass.net</span></div></div>''',brand_size=40))

# 7. Story: devices + socials
out('07-story-all-devices-socials-1080x1920',1080,1920,frame(1080,1920,f'''
<div style="position:absolute;left:81px;right:81px;top:230px"><div class="d" style="font-size:112px;white-space:nowrap">Phone. Tablet. PC.<br><span class="hl">Same burn.</span></div></div>
{laptop(150,620,780,shot(SITE_D))}{phone(70,760,440,shot(SITE_P))}{tablet(690,700,440,shot(SITE_T))}
<div style="position:absolute;left:81px;right:81px;top:1330px">{handles(30)}</div>''',brand_size=40))

# 8. Wide banner 1920x1080 (Discord invite / YouTube end screen / desktop)
out('08-wide-play-anywhere-1920x1080',1920,1080,frame(1920,1080,f'''
<div style="position:absolute;left:144px;top:250px;width:680px"><div class="d" style="font-size:112px">Play<br>anywhere.<br><span class="hl">Burn<br>everyone.</span></div></div>
{laptop(860,310,760,shot(SITE_D))}{phone(780,470,420,shot(SITE_P))}
<div style="position:absolute;left:144px;top:820px;display:flex;align-items:center;gap:22px">{qr(110)}<div class="lbl mute" style="font-size:20px;line-height:1.6">Scan to play<br><span style="color:#eef0f3">redass.net</span></div></div>''',brand_size=56))

# 9. Facebook cover version with devices (1640x624), safe centre
out('09-facebook-cover-devices-1640x624',1640,624,f'''
<div style="position:absolute;left:230px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div>{wm(64)}</div><div class="d" style="font-size:78px;margin-top:26px">Play anywhere.<br><span class="hl">Burn everyone.</span></div>
<div class="lbl mute" style="font-size:18px;margin-top:24px">Free in your browser &middot; redass.net &middot; Adults 18+</div></div>
{laptop(960,150,420,shot(SITE_D))}{phone(890,230,300,shot(SITE_P))}''')
print('ok')
