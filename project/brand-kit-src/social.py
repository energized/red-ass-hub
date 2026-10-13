import os, sys, html; sys.path.insert(0,os.path.dirname(__file__))
from brand import *; import render
W='/tmp/claude-0/kitwork'; K=f'{W}/kit/02-social-media'; T=f'{W}/_html'; os.makedirs(T,exist_ok=True)
FONTS='/tmp/claude-0/kitwork/fonts'
LOGO_F='file:///home/claude/red-ass-hub/docs/img/logo.svg'
BACKS='file:///home/claude/red-ass-hub/docs/img/backs/'
pat=f'<svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120"><g opacity=".06" fill="#fff"><g transform="translate(14 10) scale(.32)"><path d="{FL}"/></g><g transform="translate(74 66) rotate(180 16 20) scale(.32)"><path d="{FL}"/></g></g></svg>'
open(f'{W}/pattern.svg','w').write(pat)
CSS=f'''
@font-face{{font-family:Oswald;src:url(file://{FONTS}/Oswald-VariableFont.ttf);font-weight:200 700}}
@font-face{{font-family:Plex;src:url(file://{FONTS}/IBMPlexSans-Regular.ttf);font-weight:400}}
@font-face{{font-family:Plex;src:url(file://{FONTS}/IBMPlexSans-SemiBold.ttf);font-weight:600}}
*{{box-sizing:border-box;margin:0}}
html,body{{width:100%;height:100%}}
body{{font-family:Plex,sans-serif;color:{FELT_FG};overflow:hidden;position:relative;
 background:url(file://{W}/pattern.svg),radial-gradient(120% 90% at 50% 35%,#24344a 0,{FELT} 55%,#0d1219 100%)}}
body.red{{background:url(file://{W}/pattern.svg),radial-gradient(120% 90% at 50% 35%,#d62a22 0,{RED} 50%,#7d120e 100%)}}
body.cream{{color:{INK};background:radial-gradient(120% 90% at 50% 35%,#fffdf9 0,{CREAM} 60%,#efe6d6 100%)}}
.d{{font-family:Oswald,sans-serif;text-transform:uppercase;letter-spacing:.03em;line-height:.95}}
.wm{{font-family:Oswald;text-transform:uppercase;letter-spacing:.05em;font-weight:400;white-space:nowrap}}
.wm b{{font-weight:600;color:{EMBER}}} .cream .wm b,.cream .ember{{color:{RED}}} .cream .muted{{color:#566070}} .cream .foot{{color:#566070}}
.gold{{color:{GOLD}}} .ember{{color:{EMBER}}} .muted{{color:{MUTED}}}
.ace{{display:block}}
.tag{{font-family:Oswald;font-weight:500;letter-spacing:.06em;text-transform:uppercase}}
.tag b{{color:{GOLD};font-weight:500}}
.pill{{display:inline-block;border:3px solid {GOLD};color:{GOLD};border-radius:999px;font-family:Oswald;font-weight:600;letter-spacing:.08em;text-transform:uppercase}}
.age{{display:inline-flex;align-items:center;justify-content:center;background:{RED};color:#fff;font-family:Oswald;font-weight:600;border-radius:8px}}
.fan{{position:absolute}} .fan img{{position:absolute;border-radius:6%;box-shadow:0 18px 40px rgba(0,0,0,.55);border:3px solid #f3e7c9}}
.foot{{position:absolute;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:.6em;font-family:Oswald;letter-spacing:.12em;text-transform:uppercase;color:{MUTED}}}
.stamp{{display:inline-block;border:6px solid {EMBER};color:{EMBER};font-family:Oswald;font-weight:600;text-transform:uppercase;letter-spacing:.08em;padding:.15em .45em;transform:rotate(-8deg);border-radius:10px}}
.card{{background:{CREAM};color:{INK};border-radius:28px;box-shadow:0 30px 60px rgba(0,0,0,.5);position:relative}}
.pip{{position:absolute;font-family:Oswald;font-weight:600;color:{RED};line-height:1;text-align:center}}
'''
def page(name,w,h,body,cls='',sub='',transparent=False):
    os.makedirs(f'{K}/{sub}' if sub else K,exist_ok=True)
    f=f'{T}/{name}.html'
    open(f,'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}">{body}</body></html>')
    out=f'{K}/{sub}/{name}.png' if sub else f'{K}/{name}.png'
    render.html_png(f,out,w,h,transparent)
def wm(size,extra=''): return f'<div class="wm" style="font-size:{size}px;{extra}">Red <b>Ass</b></div>'
def tag(size,extra=''): return f'<div class="tag" style="font-size:{size}px;{extra}">Draw. <b>Burn.</b> Repeat.</div>'
def ace_img(h,extra=''): return f'<img class="ace" src="{LOGO_F}" style="height:{h}px;{extra}">'
def fan(x,y,h,ids=('galaxy','volcano','pizza'),spread=14,gap=None,center_ace=True):
    w=h*5/7; gap=gap or w*0.42; n=len(ids)+(1 if center_ace else 0); out=[]
    items=list(ids); 
    if center_ace: items.insert(len(items)//2+0,'ACE')
    n=len(items); mid=(n-1)/2
    for i,it in enumerate(items):
        a=(i-mid)*spread; dx=(i-mid)*gap; dy=abs(i-mid)**1.6*h*0.04
        if it=='ACE':
            out.append(f'<img src="{LOGO_F}" style="left:{dx-w*0.16}px;top:{dy-h*0.06}px;height:{h*1.12}px;width:auto;border:none;box-shadow:none;filter:drop-shadow(0 20px 30px rgba(0,0,0,.6));transform:rotate({a+9}deg);z-index:9">')
        else:
            out.append(f'<img src="{BACKS}{it}.webp" style="left:{dx}px;top:{dy}px;height:{h}px;width:{w}px;transform:rotate({a}deg);z-index:{i}">')
    return f'<div class="fan" style="left:{x-w/2}px;top:{y}px">{"".join(out)}</div>'
def foot(bottom,size,extra=''):
    return f'<div class="foot" style="bottom:{bottom}px;font-size:{size}px;{extra}"><span>redass.net</span><span class="ember">&#9679;</span><span>Adults 18+</span></div>'

def _main():
    C='display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;text-align:center'

    # ---- profile pictures (circle-safe) ----
    page('profile-picture-felt-1080',1080,1080,f'<div style="{C}">{ace_img(720,"transform:translateX(-14px)")}</div>',sub='profile-pictures')
    page('profile-picture-red-1080',1080,1080,f'<div style="{C}">{ace_img(720,"transform:translateX(-14px)")}</div>',cls='red',sub='profile-pictures')
    page('profile-picture-cream-1080',1080,1080,f'<div style="{C}">{ace_img(720,"transform:translateX(-14px)")}</div>',cls='cream',sub='profile-pictures')

    # ---- covers / banners ----
    def banner(name,w,h,safe_w,safe_h,sub='covers-and-banners',cls=''):
        s=safe_h  # scale by safe area height
        body=f'''<div style="position:absolute;left:50%;top:50%;width:{safe_w}px;height:{safe_h}px;transform:translate(-50%,-50%);display:flex;align-items:center;justify-content:space-between;gap:{s*0.08}px">
          <div style="display:flex;align-items:center;gap:{s*0.08}px">{ace_img(s*0.86)}
          <div>{wm(s*0.36)}{tag(s*0.115,f"margin-top:{s*0.04}px")}</div></div>
          <div style="text-align:right">
            <div class="d" style="font-size:{s*0.13}px;font-weight:600;white-space:nowrap">The card game where<br>your friends are <span class="ember">the enemy.</span></div>
            <div class="pill" style="font-size:{s*0.075}px;padding:{s*0.02}px {s*0.06}px;margin-top:{s*0.07}px">Play free at redass.net &nbsp;&#9654;</div>
            <div class="muted" style="font-size:{s*0.06}px;margin-top:{s*0.05}px;font-family:Oswald;letter-spacing:.12em">ADULTS 18+</div>
          </div></div>'''
        page(name,w,h,body,cls=cls,sub=sub)
    banner('facebook-cover-1640x624',1640,624,1180,330)
    banner('youtube-banner-2560x1440',2560,1440,1500,410)
    banner('x-twitter-header-1500x500',1500,500,1180,300)
    banner('discord-server-banner-960x540',960,540,860,250)
    banner('discord-invite-background-1920x1080',1920,1080,1500,420)

    # ---- link preview ----
    page('link-preview-1200x630',1200,630,f'''<div style="position:absolute;left:80px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;width:560px">
     {wm(110)}{tag(40,"margin-top:18px")}
     <div style="font-size:30px;margin-top:34px;line-height:1.3">The card game where your friends are the enemy. Play free in your browser.</div>
     <div class="muted" style="font-size:22px;margin-top:22px;font-family:Oswald;letter-spacing:.12em">REDASS.NET &nbsp;&middot;&nbsp; ADULTS 18+</div></div>
     {fan(905,150,300,('galaxy','pizza'),spread=16)}''',sub='covers-and-banners')

    # ---- spicy quote posts (1080x1350) ----
    lines=[('forgot-last-card','Forgot to say<br><span class="ember">“Last card”?</span>','Draw one. Shame included.'),
     ('not-personal',"It's not personal.<br><span class='ember'>It's a 4.</span>",'Chain it or eat it.'),
     ('kings-reverse','Kings reverse.<br><span class="ember">Grudges don’t.</span>','See you next round.'),
     ('nice-hand','Nice hand.<br><span class="ember">Shame about the score.</span>','Lowest score wins.'),
     ('ego','Lowest score wins.<br><span class="ember">Your ego doesn’t.</span>','Play anyway.'),
     ('burn-friends','Burn your friends.<br><span class="ember">Legally.</span>','Draw. Burn. Repeat.'),
     ('red-assed','You just got<br><span class="ember">Red-Assed.</span>','Sit down. Shuffle up.'),
     ('hold-my-4','Hold<br><span class="ember">my 4.</span>','Then hold these 5.')]
    for i,(slug,big,small) in enumerate(lines,1):
        cls=['','red','cream'][i%3] if False else ('red' if i%4==3 else ('cream' if i%4==1 else ''))
        em = '' 
        body=f'''<div style="position:absolute;left:90px;right:90px;top:90px;display:flex;justify-content:space-between;align-items:center">{wm(46)}{ace_img(120,"transform:rotate(4deg)")}</div>
        <div style="position:absolute;left:90px;right:90px;top:240px;bottom:180px;display:flex;flex-direction:column;justify-content:center">
          <div class="d" style="font-size:{150 if len(big)<60 else 128}px;font-weight:600">{big}</div>
          <div style="font-size:44px;margin-top:48px;font-family:Oswald;letter-spacing:.06em;text-transform:uppercase" class="{'muted' if cls!='red' else ''}">{small}</div></div>
        {foot(80,30)}'''
        if cls=='red': body=body.replace('class="ember"','style="color:#ffd27a"').replace("class='ember'","style='color:#ffd27a'")
        page(f'post-{i:02d}-{slug}-1080x1350',1080,1350,body,cls=cls,sub='spicy-posts')

    # ---- fill-in templates (blank space to add text in Canva / phone) ----
    def tpl(name,title,sub_line,w=1080,h=1350,cls=''):
        body=f'''<div style="position:absolute;left:90px;right:90px;top:90px;display:flex;justify-content:space-between;align-items:center">{wm(46)}{ace_img(120,"transform:rotate(4deg)")}</div>
        <div style="position:absolute;left:90px;right:90px;top:280px"><div class="stamp" style="font-size:40px">{sub_line}</div>
        <div class="d" style="font-size:140px;font-weight:600;margin-top:40px">{title}</div></div>
        <div style="position:absolute;left:90px;right:90px;top:700px;bottom:200px;border:3px dashed rgba(233,237,243,.25);border-radius:24px;display:flex;align-items:center;justify-content:center;color:rgba(233,237,243,.35);font-family:Oswald;letter-spacing:.12em;font-size:30px">YOUR TEXT HERE</div>
        {foot(80,30)}'''
        page(name,w,h,body,cls=cls,sub='fill-in-templates')
    tpl('template-whats-new-1080x1350',"What's<br><span class='gold'>new</span>",'Fresh from the dealer')
    tpl('template-game-night-1080x1350',"Game<br><span class='ember'>night</span>",'Tonight. Bring a grudge.')
    tpl('template-burn-of-the-week-1080x1350',"Burn of<br>the <span class='ember'>week</span>",'Hall of shame')
    tpl('template-announcement-1080x1350',"Listen<br><span class='gold'>up</span>",'From the table')

    # ---- stories / TikTok covers (1080x1920) ----
    page('story-play-now-1080x1920',1080,1920,f'''<div style="position:absolute;top:220px;left:0;right:0;text-align:center">{wm(150)}{tag(56,"margin-top:24px")}</div>
     {fan(540,640,520,('volcano','galaxy'),spread=15)}
     <div style="position:absolute;top:1330px;left:0;right:0;text-align:center"><div class="d" style="font-size:96px;font-weight:600">Your friends are<br><span class="ember">the enemy.</span></div>
     <div class="pill" style="font-size:44px;padding:14px 46px;margin-top:50px">Play free &#9654; redass.net</div></div>{foot(120,32)}''',sub='stories-and-tiktok-covers')
    page('story-last-card-1080x1920',1080,1920,f'''<div style="position:absolute;top:200px;left:0;right:0;text-align:center">{wm(80)}</div>
     <div style="position:absolute;left:50%;top:420px;transform:translateX(-50%) rotate(-6deg)" class="card"><div style="width:600px;height:840px"></div>
     <div class="pip" style="left:40px;top:34px;font-size:110px">A</div><div class="pip" style="right:40px;bottom:34px;font-size:110px;transform:rotate(180deg)">A</div>
     <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center"><div class="d" style="font-size:150px;font-weight:600;color:{RED};text-align:center">Last<br>card!</div></div></div>
     <div style="position:absolute;top:1390px;left:80px;right:80px;text-align:center"><div class="d" style="font-size:80px;font-weight:600">Say it first.<br><span class="ember">Or draw one.</span></div></div>{foot(120,32)}''',cls='red',sub='stories-and-tiktok-covers')
    page('story-game-night-1080x1920',1080,1920,f'''<div style="position:absolute;top:200px;left:0;right:0;text-align:center">{wm(80)}</div>
     <div style="position:absolute;top:380px;left:80px;right:80px;text-align:center"><div class="stamp" style="font-size:52px">Tonight</div>
     <div class="d" style="font-size:220px;font-weight:600;margin-top:40px">Game<br><span class="ember">night</span></div>
     <div class="d" style="font-size:64px;margin-top:40px" >Bring snacks.<br>Bring a grudge.</div></div>
     <div style="position:absolute;left:120px;right:120px;top:1300px;height:300px;border:3px dashed rgba(233,237,243,.3);border-radius:24px;display:flex;align-items:center;justify-content:center;color:rgba(233,237,243,.4);font-family:Oswald;letter-spacing:.12em;font-size:36px">TIME &amp; TABLE CODE HERE</div>{foot(120,32)}''',sub='stories-and-tiktok-covers')
    print('done')
if __name__=="__main__": _main()
