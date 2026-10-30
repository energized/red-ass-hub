import re
from playwright.sync_api import sync_playwright
OUT="M50 3C58 28 90 46 90 84C90 112 72 127 50 127C28 127 10 112 10 84C10 63 23 53 29 40C33 52 39 57 44 55C39 36 41 18 50 3Z"
IN ="M50 64C56 78 70 84 70 100C70 114 61 122 50 122C39 122 30 114 30 100C30 90 38 84 42 76C45 82 48 83 50 82C47 76 47 70 50 64Z"
def flame(cx,base,s,o,i,stroke,core=None,flip=1):
    # place so that bottom centre (50,127) sits at (cx,base)
    g=f'<g transform="translate({cx-50*s*flip:.1f} {base-127*s:.1f}) scale({s*flip} {s})">'
    g+=f'<path d="{OUT}" fill="{o}" stroke="{stroke}" stroke-width="{3.2/s:.1f}" stroke-linejoin="round"/>'
    g+=f'<path d="{IN}" fill="{i}"/>'
    if core: g+=f'<g transform="translate(50 100) scale(.55) translate(-50 -100)"><path d="{IN}" fill="{core}"/></g>'
    return g+'</g>'
def spark(x,y,r,c): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
def svg(b): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">{b}</svg>'
glow=lambda c:f'<ellipse cx="120" cy="206" rx="70" ry="9" fill="{c}" fill-opacity=".28"/>'
# SPARK: one small amber flame + two sparks
spark_b=glow("#E8AB35")+flame(120,200,0.9,"#E8AB35","#FFF1C9","#7a4b06")+spark(70,150,4,"#E8AB35")+spark(176,120,3,"#FFF1C9")+spark(88,96,2.5,"#E8AB35")
# BLAZE: the logo flame, big (exact brand colours)
blaze_b=glow("#C4211B")+flame(120,202,1.4,"#C4211B","#E8AB35","#7a120e")+spark(48,130,4,"#FF5A4F")+spark(196,92,4,"#E8AB35")+spark(180,150,3,"#FF5A4F")
# INFERNO: big centre flame in ember, two red side flames, white-hot core, sparks
inf_b=glow("#FF5A4F")+flame(52,204,1.0,"#C4211B","#E8AB35","#7a120e")+flame(188,204,1.0,"#C4211B","#E8AB35","#7a120e",flip=-1)+flame(120,206,1.6,"#FF5A4F","#FFC94D","#8a1511","#FFF6DA")+spark(40,110,4,"#FF5A4F")+spark(204,98,4,"#FFC94D")+spark(150,40,3,"#FFF6DA")+spark(88,48,3,"#FF5A4F")
data={"spark":spark_b,"blaze":blaze_b,"inferno":inf_b}
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page()
    for n,body in data.items():
        s=svg(body); open(f"badge-{n}.svg","w").write(s)
        pg2=b.new_page(viewport={"width":512,"height":512}); pg2.set_content(f'<body style="margin:0">{s.replace(chr(34)+"240"+chr(34)+" height="+chr(34)+"240"+chr(34),chr(34)+"512"+chr(34)+" height="+chr(34)+"512"+chr(34))}</body>'); pg2.screenshot(path=f"badge-{n}.png",omit_background=True)
        # small: drop glow + tiny sparks, tight square crop
        sm=re.sub(r'<ellipse[^>]*/>','',s); sm=re.sub(r'<circle[^>]*/>','',sm)
        pg.set_content(sm); x,y,w,h=pg.evaluate("(()=>{const b=document.querySelector('svg').getBBox();return [b.x,b.y,b.width,b.height]})()")
        m=max(w,h)+6; sm=sm.replace('viewBox="0 0 240 240" width="240" height="240"',f'viewBox="{x+w/2-m/2:.1f} {y+h/2-m/2:.1f} {m:.1f} {m:.1f}" width="64" height="64"')
        open(f"badge-{n}-small.svg","w").write(sm)
    rows="".join(f'<div style="margin:8px 16px"><small style="color:#A3AFC0">{n}</small><div style="display:flex;gap:10px;align-items:flex-end;background:#1b2634;padding:8px 10px;border-radius:10px">'+"".join(open(f"badge-{n}-small.svg").read().replace('width="64" height="64"',f'width="{w}" height="{w}"') for w in (15,22,34))+open(f"badge-{n}.svg").read().replace('width="240" height="240"','width="130" height="130"')+'</div></div>' for n in data)
    pg.set_viewport_size({"width":640,"height":210}); pg.set_content(f'<body style="background:#17202B;margin:0;display:flex;font-family:IBM Plex Sans">{rows}</body>'); pg.screenshot(path="flames-sheet.png")
    b.close()
