"""Shared brand pieces for the Red Ass kit (Social Claude)."""
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import functools

RED='#c4211b'; GOLD='#e8ab35'; CREAM='#fbf8f3'; INK='#1a1f2b'
FELT='#17202b'; FELT2='#1e2a38'; FELT_FG='#e9edf3'; MUTED='#a3afc0'; EMBER='#ff5a4f'

FL="M50 3C58 28 90 46 90 84C90 112 72 127 50 127C28 127 10 112 10 84C10 63 23 53 29 40C33 52 39 57 44 55C39 36 41 18 50 3Z"
IN="M50 64C56 78 70 84 70 100C70 114 61 122 50 122C39 122 30 114 30 100C30 90 38 84 42 76C45 82 48 83 50 82C47 76 47 70 50 64Z"
import os as _o
LOGO=open(_o.environ.get('RA_LOGO','/tmp/claude-0/kitclean/logo-clean.svg')).read()
# inner of logo (everything between <title>..</svg>) for embedding
LOGO_INNER=LOGO.split('</title>')[1].split('</svg>')[0]

@functools.lru_cache(None)
def font(w):
    f=TTFont('/root/.fonts/Oswald.ttf')
    return instantiateVariableFont(f,{'wght':w})

def text_path(text,w=600,size=100,x=0,y=0,track=0.05):
    """Return (svg path d, advance width) of text in Oswald at weight w; y = baseline."""
    f=font(w); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm; s=size/upm
    hmtx=f['hmtx']; out=[]; cx=x
    for ch in text:
        gn=cmap.get(ord(ch))
        if gn is None: continue
        p=SVGPathPen(gs, ntos=lambda v:('%.2f'%v).rstrip('0').rstrip('.'))
        gs[gn].draw(TransformPen(p,(s,0,0,-s,cx,y)))
        out.append(p.getCommands())
        cx+=hmtx[gn][0]*s+track*size
    return ' '.join(out), cx-x-track*size

def flame(x,y,scale,outer=RED,inner=GOLD,rot=0):
    t=f'translate({x} {y})'+(f' rotate({rot})' if rot else '')+f' scale({scale})'
    s=f'<g transform="{t}"><path fill="{outer}" d="{FL}"/>'
    if inner: s+=f'<path fill="{inner}" d="{IN}"/>'
    return s+'</g>'

def ace(x,y,h):
    """Ace card logo placed with top-left of its 160x210 box at x,y, height h."""
    s=h/210
    return f'<g transform="translate({x} {y}) scale({s}) translate(-120 0)">{LOGO_INNER}</g>'

def wordmark(x,y,size,red_col,ass_col):
    """'RED ASS' wordmark, baseline y. returns (svg, width)."""
    d1,w1=text_path('RED',400,size,x,y)
    gap=size*0.28
    d2,w2=text_path('ASS',600,size,x+w1+gap,y)
    return f'<path fill="{red_col}" d="{d1}"/><path fill="{ass_col}" d="{d2}"/>', w1+gap+w2

def tagline(x,y,size,col,burn=GOLD,w=500):
    out=[];cx=x
    for word,c in (('DRAW.',col),('BURN.',burn),('REPEAT.',col)):
        d,wd=text_path(word,w,size,cx,y,0.04); out.append(f'<path fill="{c}" d="{d}"/>'); cx+=wd+size*0.3
    return ''.join(out), cx-x-size*0.3

def svgdoc(w,h,body,bg=None,title='Red Ass'):
    b=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}"><title>{title}</title>{b}{body}</svg>\n'
