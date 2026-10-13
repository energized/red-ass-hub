import os, sys, qrcode, qrcode.image.svg; sys.path.insert(0,os.path.dirname(__file__))
from brand import RED,GOLD,EMBER,INK; import render
W='/tmp/claude-0/kitclean'; K=f'{W}/kit'; T=f'{W}/_html'; os.makedirs(T,exist_ok=True)
FONTS='/tmp/claude-0/kitwork/fonts'
NIGHT='#0f1319'; NIGHT2='#171d26'; CREAM='#f6f1e8'; SMOKE='#8b95a5'; BONE='#eef0f3'
LOGO=f'file://{W}/logo-clean.svg'
L1=f'file://{K}/01-logos/lockup-horizontal-for-light-backgrounds.svg'; L2=f'file://{K}/01-logos/lockup-horizontal-for-dark-backgrounds.svg'
CSS=f'''
@font-face{{font-family:Oswald;src:url(file://{FONTS}/Oswald-VariableFont.ttf);font-weight:200 700}}
@font-face{{font-family:Plex;src:url(file://{FONTS}/IBMPlexSans-Regular.ttf);font-weight:400}}
@font-face{{font-family:Plex;src:url(file://{FONTS}/IBMPlexSans-Medium.ttf);font-weight:500}}
@font-face{{font-family:Plex;src:url(file://{FONTS}/IBMPlexSans-SemiBold.ttf);font-weight:600}}
@page{{margin:0}}
*{{box-sizing:border-box;margin:0}} html,body{{width:100%;height:100%}}
body{{font-family:Plex,sans-serif;background:{NIGHT};color:{BONE};overflow:hidden;position:relative;-webkit-font-smoothing:antialiased}}
body.cream{{background:{CREAM};color:{INK}}} body.red{{background:{RED};color:#fff}} body.white{{background:#fff;color:{INK}}}
.d{{font-family:Oswald;font-weight:600;text-transform:uppercase;line-height:.9;letter-spacing:-.005em}}
.hl{{color:{EMBER}}} .cream .hl,.white .hl{{color:{RED}}} .red .hl{{color:{INK}}}
.lbl{{font-family:Plex;font-weight:500;text-transform:uppercase;letter-spacing:.16em}}
.mute{{color:{SMOKE}}} .cream .mute,.white .mute{{color:#5d6675}} .red .mute{{color:rgba(255,255,255,.75)}}
.wm{{font-family:Oswald;text-transform:uppercase;letter-spacing:.05em;font-weight:400;white-space:nowrap;line-height:1}}
.wm b{{font-weight:600;color:{EMBER}}} .cream .wm b,.white .wm b{{color:{RED}}} .red .wm b{{color:#fff}}
.tag{{font-family:Oswald;font-weight:500;letter-spacing:.06em;text-transform:uppercase}} .tag b{{font-weight:500;color:{GOLD}}} .cream .tag b,.white .tag b{{color:#b07a12}} .red .tag b{{color:{INK}}}
.pill{{display:inline-flex;align-items:center;gap:.5em;border-radius:999px;font-family:Plex;font-weight:600;letter-spacing:.02em;background:{BONE};color:{NIGHT}}}
.cream .pill,.white .pill{{background:{INK};color:#fff}} .red .pill{{background:#fff;color:{RED}}}
.chip{{display:inline-block;border:1.5px solid currentColor;border-radius:999px;font-family:Plex;font-weight:500;text-transform:uppercase;letter-spacing:.14em}}
.rule{{height:1.5px;background:currentColor;opacity:.18}}
.box{{border:1.5px solid currentColor;border-radius:28px;opacity:.28}}
'''
def doc(name,body,cls='',size=None):
    if size: body=f'<div style="position:relative;width:{size[0]};height:{size[1]};overflow:hidden">{body}</div>'
    f=f'{T}/{name}.html'; open(f,'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}">{body}</body></html>'); return f
def png(sub,name,w,h,body,cls=''):
    os.makedirs(f'{K}/{sub}',exist_ok=True); render.html_png(doc(name,body,cls),f'{K}/{sub}/{name}.png',w,h)
def wm(px): return f'<div class="wm" style="font-size:{px}px">Red <b>Ass</b></div>'
def tag(px,x=''): return f'<div class="tag" style="font-size:{px}px;{x}">Draw. <b>Burn.</b> Repeat.</div>'
def ace(h,x=''): return f'<img src="{LOGO}" style="height:{h}px;display:block;{x}">'
def frame(w,h,inner,m=None,top=True,bottom=True,brand_size=None):
    """Clean grid: header (ace+wordmark | 18+ chip) and footer (url | tagline)."""
    m=m or round(w*0.075); s=brand_size or round(w*0.036)
    hd=f'<div style="position:absolute;left:{m}px;right:{m}px;top:{m}px;display:flex;justify-content:space-between;align-items:center"><div style="display:flex;align-items:center;gap:{s*.45}px">{ace(s*1.5)}{wm(s)}</div><span class="chip" style="font-size:{s*.42}px;padding:{s*.18}px {s*.5}px">Adults 18+</span></div>' if top else ''
    ft=f'<div style="position:absolute;left:{m}px;right:{m}px;bottom:{m}px"><div class="rule" style="margin-bottom:{s*.6}px"></div><div style="display:flex;justify-content:space-between;font-size:{s*.5}px" class="lbl mute"><span>redass.net</span><span>Draw. Burn. Repeat.</span></div></div>' if bottom else ''
    return hd+inner+ft

