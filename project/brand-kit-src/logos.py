import os, sys; sys.path.insert(0,os.path.dirname(__file__))
from brand import *; import render
K='/tmp/claude-0/kitwork/kit/01-logos'; os.makedirs(K,exist_ok=True)
def save(name,w,h,body,bg=None,pngs=(1,),transparent=True):
    p=f'{K}/{name}.svg'; open(p,'w').write(svgdoc(w,h,body,bg))
    for s in pngs:
        sfx='' if s==1 else f'@{s}x'
        render.svg_png(p,f'{K}/{name}{sfx}.png',int(w*s),int(h*s),transparent and bg is None)

# 1 ace mark
open(f'{K}/ace-mark.svg','w').write(LOGO)
for px in (512,1024,2048):
    render.svg_png(f'{K}/ace-mark.svg',f'{K}/ace-mark-{px}.png',int(px*160/210),px)

# 2 horizontal lockup (mark + wordmark + tagline)
def horizontal(fg,ass,burn,tagcol):
    H=240; body=ace(10,15,210)
    wm,ww=wordmark(195,128,112,fg,ass)
    tg,tw=tagline(199,192,38,tagcol,burn)
    return 195+max(ww,tw)+30,H,body+wm+tg
w,h,b=horizontal(FELT_FG,EMBER,GOLD,MUTED); save('lockup-horizontal-for-dark-backgrounds',w,h,b,pngs=(2,))
w,h,b=horizontal(INK,RED,'#b07a12','#566070'); save('lockup-horizontal-for-light-backgrounds',w,h,b,pngs=(2,))

# 3 stacked lockup
def stacked(fg,ass,burn,tagcol):
    W=560; body=ace(W/2-110,20,290)
    _,ww=wordmark(0,0,120,fg,ass); wm,_=wordmark((W-ww)/2,440,120,fg,ass)
    _,tw=tagline(0,0,44,tagcol,burn); tg,_=tagline((W-tw)/2,510,44,tagcol,burn)
    return W,545,body+wm+tg
w,h,b=stacked(FELT_FG,EMBER,GOLD,MUTED); save('lockup-stacked-for-dark-backgrounds',w,h,b,pngs=(2,))
w,h,b=stacked(INK,RED,'#b07a12','#566070'); save('lockup-stacked-for-light-backgrounds',w,h,b,pngs=(2,))

# 4 wordmark only
for nm,fg,ass in (('wordmark-white',FELT_FG,EMBER),('wordmark-ink',INK,RED),('wordmark-all-white','#ffffff','#ffffff'),('wordmark-all-black','#000000','#000000')):
    _,ww=wordmark(0,0,200,fg,ass); wm,_=wordmark(10,215,200,fg,ass); save(nm,int(ww+20),240,wm,pngs=(1,))

# 5 one-colour marks (for stamps, embroidery-free single ink uses)
mono=LOGO_INNER.replace(GOLD,'#ffffff')
for nm,c,card in (('ace-mark-one-color-red',RED,'#ffffff'),('ace-mark-one-color-white','#ffffff','none')):
    inner=LOGO_INNER.replace('fill="#fbf8f3"',f'fill="{card}"').replace('stroke="#1a1f2b"',f'stroke="{c}"').replace(f'fill="{RED}"',f'fill="{c}"').replace(f'fill="{GOLD}"',f'fill="{card if card!="none" else FELT}"' if nm.endswith('red') else 'fill="none"')
    body=f'<g transform="translate(-120 0)">{inner}</g>'
    p=f'{K}/{nm}.svg'; open(p,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 210" width="160" height="210">{body}</svg>\n')
    render.svg_png(p,f'{K}/{nm}-1024.png',780,1024)

# 6 app icon (square, no transparency, no rounded corners)
glow=f'<defs><radialGradient id="g" cx="50%" cy="45%" r="65%"><stop offset="0" stop-color="#2a3a4e"/><stop offset="1" stop-color="{FELT}"/></radialGradient></defs><rect width="1024" height="1024" fill="url(#g)"/>'
icon=glow+ace(512-330,512-410,820)
p=f'{K}/app-icon-1024.svg'; open(p,'w').write(svgdoc(1024,1024,icon))
for px in (1024,512,192,180):
    nm='app-icon' if px!=180 else 'apple-touch-icon'
    render.svg_png(p,f'{K}/{nm}-{px}.png',px,px,False)
render.svg_png('/home/claude/red-ass-hub/docs/img/logo-small.svg',f'{K}/favicon-48.png',48,48)
render.svg_png('/home/claude/red-ass-hub/docs/img/logo-small.svg',f'{K}/favicon-32.png',32,32)
print(sorted(os.listdir(K)))
