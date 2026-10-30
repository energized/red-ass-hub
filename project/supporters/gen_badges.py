import math, sys
def grad(id_, stops, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<linearGradient id="{id_}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>'

def coin(cx, y, rx, ry, h, pre):
    # y = top-face centre
    return (f'<path d="M{cx-rx} {y} v{h} a{rx} {ry} 0 0 0 {2*rx} 0 v{-h} z" fill="url(#{pre}side)"/>'
            f'<path d="M{cx-rx+6} {y+h+ry*0.55} q{rx-6} {ry*0.9} {2*rx-12} 0" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2.2" stroke-linecap="round"/>'
            f'<ellipse cx="{cx}" cy="{y}" rx="{rx}" ry="{ry}" fill="url(#{pre}top)" stroke="{{edge}}" stroke-width="2"/>'
            f'<ellipse cx="{cx}" cy="{y}" rx="{rx-9}" ry="{ry-4}" fill="none" stroke="{{rim}}" stroke-width="2" stroke-opacity=".7"/>')

def stack(cx, base, n, rx, ry, h, pre, edge, rim, star=True):
    out = ""
    for i in range(n):
        y = base - i*h
        jx = ((i*7) % 5 - 2) * 1.6
        out += coin(cx+jx, y, rx, ry, h-1, pre).replace("{edge}", edge).replace("{rim}", rim)
    if star:
        y = base-(n-1)*h; jx = ((n-1)*7 % 5 - 2)*1.6
        px, py = cx+jx, y
        pts = []
        for k in range(10):
            r = (13 if k%2==0 else 5.5); a = -math.pi/2 + k*math.pi/5
            pts.append(f"{px+r*math.cos(a):.1f},{py+ (r*math.sin(a))*0.55:.1f}")
        out += f'<polygon points="{" ".join(pts)}" fill="{rim}" fill-opacity=".85"/>'
    return out

def ingot(cx, y, w, h, d, pre):
    # y = top of front face
    t = 7
    front = f"{cx-w/2},{y+h} {cx+w/2},{y+h} {cx+w/2-t},{y} {cx-w/2+t},{y}"
    top = f"{cx-w/2+t},{y} {cx+w/2-t},{y} {cx+w/2-t-11},{y-d} {cx-w/2+t+11},{y-d}"
    return (f'<polygon points="{front}" fill="url(#{pre}front)" stroke="#8a5a06" stroke-width="2" stroke-linejoin="round"/>'
            f'<polygon points="{top}" fill="url(#{pre}top)" stroke="#8a5a06" stroke-width="2" stroke-linejoin="round"/>'
            f'<rect x="{cx-w/2+t+9}" y="{y+5}" width="{w*0.3}" height="4" rx="2" fill="#fff" fill-opacity=".55"/>'
            f'<rect x="{cx-w/2+t+9+w*0.3+5}" y="{y+5}" width="6" height="4" rx="2" fill="#fff" fill-opacity=".4"/>')

def gem(cx, cy, s, fills, edge="#2a7c96"):
    P = {"T1":(-.5,-.55),"T2":(.5,-.55),"G1":(-1,-.1),"G2":(1,-.1),"g2":(-.38,-.1),"g3":(.38,-.1),"B":(0,1)}
    def pt(k): x,y=P[k]; return f"{cx+x*s:.1f},{cy+y*s:.1f}"
    facets = [(["T1","T2","g3","g2"],0),(["T1","G1","g2"],1),(["T2","G2","g3"],2),(["G1","g2","B"],3),(["g2","g3","B"],4),(["g3","G2","B"],5)]
    out = ""
    for ks, i in facets:
        out += f'<polygon points="{" ".join(pt(k) for k in ks)}" fill="{fills[i]}" stroke="{edge}" stroke-width="1.8" stroke-linejoin="round"/>'
    return out

def sparkle(x, y, r, c="#fff"):
    return f'<path d="M{x} {y-r} Q{x+r*.15} {y-r*.15} {x+r} {y} Q{x+r*.15} {y+r*.15} {x} {y+r} Q{x-r*.15} {y+r*.15} {x-r} {y} Q{x-r*.15} {y-r*.15} {x} {y-r}z" fill="{c}"/>'

def svg(body, defs):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240"><defs>{defs}</defs>{body}</svg>'

shadow = '<ellipse cx="120" cy="208" rx="86" ry="11" fill="#000" fill-opacity=".35"/>'

# SILVER: three stacks of coins, cool white-silver with a faint blue cast (distinct from Smoke grey frame)
d = (grad("stop",[(0,"#FFFFFF"),(1,"#D5DEEA")])+grad("stside",[(0,"#C9D3E1"),(.5,"#E9EFF7"),(1,"#9AA8BC")],1,0))
d = d.replace('id="stop"','id="sitop"').replace('id="stside"','id="sisid"')
d = d.replace('id="sisid"','id="siside"')
silver = shadow + stack(70,196,3,34,11,12,"si","#6F7F95","#8D9BB0",False) + stack(172,196,4,34,11,12,"si","#6F7F95","#8D9BB0",False) + stack(120,200,7,40,13,13,"si","#6F7F95","#7A8AA2",True) + sparkle(190,62,12)+sparkle(52,92,8)+sparkle(148,36,6)
open("badge-silver.svg","w").write(svg(silver,d))

# GOLD: pyramid of ingots, deeper orange-gold (distinct from Legendary flat #E8AB35 frame)
d = (grad("gofront",[(0,"#FFD35A"),(1,"#E2931A")])+grad("gotop",[(0,"#FFF0A8"),(1,"#FFD35A")]))
rows = [ (3,[58,120,182],188), (2,[89,151],152), (1,[120],116) ]
gold = shadow
for n, xs, y in rows:
    for x in xs: gold += ingot(x, y, 56, 30, 14, "go")
gold += sparkle(196,70,12)+sparkle(46,110,8)+sparkle(150,52,6)
open("badge-gold.svg","w").write(svg(gold,d))

# DIAMOND: pile of ice-cyan gems with one pink-violet accent (distinct from Rare blue/Epic purple frames)
ice = ["#EFFFFF","#9CEBFF","#6FD6F2","#53BBDC","#7FD8F0","#3FA6CC"]
ice2= ["#FFFFFF","#B8F3FF","#8BE3FA","#6AC9E8","#92E0F5","#52B3D6"]
pink= ["#FFF0FA","#FFC2EA","#FF9AD8","#E26BC0","#FFA9DE","#D257B0"]
dia = shadow
dia += gem(70,170,38,ice2,"#2a7c96")+gem(170,170,38,ice,"#2a7c96")+gem(120,150,54,ice2,"#2a7c96")
dia += gem(92,108,26,pink,"#9a3a85")+gem(152,104,30,ice,"#2a7c96")
dia += sparkle(196,56,13)+sparkle(44,96,9)+sparkle(122,40,8)
open("badge-diamond.svg","w").write(svg(dia,""))
print("ok")
