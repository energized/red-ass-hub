from cleanlib import *
# ---------- profile pictures ----------
for cls,nm in (('','night'),('cream','cream'),('red','red')):
    png('02-social-media/profile-pictures',f'profile-picture-{nm}-1080',1080,1080,f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{ace(700,"transform:translateX(-12px)")}</div>',cls)

# ---------- covers ----------
def cover(name,w,h,sw,sh,cls=''):
    s=sh
    body=f'''<div style="position:absolute;left:50%;top:50%;width:{sw}px;height:{sh}px;transform:translate(-50%,-50%);display:flex;align-items:center;justify-content:space-between">
     <div style="display:flex;align-items:center;gap:{s*.1}px">{ace(s*.82)}<div>{wm(s*.34)}{tag(s*.1,f"margin-top:{s*.05}px")}</div></div>
     <div style="display:flex;flex-direction:column;align-items:flex-end;gap:{s*.07}px"><div class="d" style="font-size:{s*.155}px;text-align:right;white-space:nowrap">Your friends are<br><span class="hl">the enemy.</span></div>
     <span class="pill" style="font-size:{s*.072}px;padding:{s*.04}px {s*.09}px">Play free at redass.net &#8599;</span></div></div>'''
    png('02-social-media/covers-and-banners',name,w,h,body,cls)
cover('facebook-cover-1640x624',1640,624,1200,320)
cover('youtube-banner-2560x1440',2560,1440,1520,400)
cover('x-twitter-header-1500x500',1500,500,1200,290)
cover('discord-server-banner-960x540',960,540,860,240)
cover('discord-invite-background-1920x1080',1920,1080,1500,400)
png('02-social-media/covers-and-banners','link-preview-1200x630',1200,630,f'''
 <div style="position:absolute;left:84px;top:84px">{wm(40)}</div>
 <div style="position:absolute;left:84px;top:190px;width:640px"><div class="d" style="font-size:84px">The card game where your friends are <span class="hl">the enemy.</span></div></div>
 <div style="position:absolute;left:84px;bottom:76px" class="lbl mute"><span style="font-size:18px">Play free &middot; redass.net &middot; Adults 18+</span></div>
 <div style="position:absolute;right:70px;top:50%;transform:translateY(-50%)">{ace(430)}</div>''')

# ---------- spicy posts: pure type ----------
lines=[('forgot-last-card','Forgot to say<br><span class="hl">“last card”?</span>','Draw one. Shame included.','cream'),
 ('not-personal',"It's not<br>personal.<br><span class='hl'>It's a 4.</span>",'Chain it or eat it.',''),
 ('kings-reverse','Kings<br>reverse.<br><span class="hl">Grudges<br>don’t.</span>','See you next round.','red'),
 ('nice-hand','Nice hand.<br><span class="hl">Shame about<br>the score.</span>','Lowest score wins.',''),
 ('ego','Lowest score<br>wins. <span class="hl">Your<br>ego doesn’t.</span>','Play anyway.','cream'),
 ('burn-friends','Burn your<br>friends.<br><span class="hl">Legally.</span>','Draw. Burn. Repeat.',''),
 ('red-assed','You just<br>got<br><span class="hl">Red-Assed.</span>','Sit down. Shuffle up.','red'),
 ('hold-my-4','Hold<br><span class="hl">my 4.</span>','Then hold these five.','')]
for i,(slug,big,small,cls) in enumerate(lines,1):
    body=frame(1080,1350,f'''<div style="position:absolute;left:81px;right:81px;top:250px;bottom:230px;display:flex;flex-direction:column;justify-content:flex-end">
      <div class="d" style="font-size:168px">{big}</div><div class="lbl mute" style="font-size:24px;margin-top:44px">{small}</div></div>''')
    png('02-social-media/spicy-posts',f'post-{i:02d}-{slug}-1080x1350',1080,1350,body,cls)

# ---------- fill-in templates ----------
for slug,label,title,cls in (('whats-new','Fresh from the dealer',"What's<br><span class='hl'>new</span>",''),('game-night','Tonight',"Game<br><span class='hl'>night</span>",''),('burn-of-the-week','Hall of shame',"Burn of<br>the <span class='hl'>week</span>",'cream'),('announcement','From the table',"Listen<br><span class='hl'>up</span>",'')):
    body=frame(1080,1350,f'''<div style="position:absolute;left:81px;right:81px;top:230px"><span class="chip" style="font-size:20px;padding:8px 20px">{label}</span>
      <div class="d" style="font-size:150px;margin-top:34px">{title}</div></div>
      <div class="box" style="position:absolute;left:81px;right:81px;top:700px;bottom:200px"></div>
      <div class="lbl mute" style="position:absolute;left:0;right:0;top:940px;text-align:center;font-size:20px;opacity:.6">Your text here</div>''')
    png('02-social-media/fill-in-templates',f'template-{slug}-1080x1350',1080,1350,body,cls)

# ---------- stories ----------
png('02-social-media/stories-and-tiktok-covers','story-play-now-1080x1920',1080,1920,frame(1080,1920,f'''
 <div style="position:absolute;left:0;right:0;top:330px;display:flex;justify-content:center">{ace(720,"transform:translateX(-14px)")}</div>
 <div style="position:absolute;left:81px;right:81px;top:1180px"><div class="d" style="font-size:116px;white-space:nowrap">Your friends are<br><span class="hl">the enemy.</span></div>
 <span class="pill" style="font-size:38px;padding:20px 44px;margin-top:56px">Play free &middot; redass.net &#8599;</span></div>''',brand_size=40))
png('02-social-media/stories-and-tiktok-covers','story-last-card-1080x1920',1080,1920,frame(1080,1920,f'''
 <div style="position:absolute;left:81px;right:81px;top:380px"><span class="chip" style="font-size:24px;padding:10px 24px">House rule</span>
 <div class="d" style="font-size:250px;margin-top:40px">Last<br>card.</div>
 <div class="d" style="font-size:110px;margin-top:60px">Say it first.<br><span class="hl">Or draw one.</span></div></div>''',brand_size=40),'red')
png('02-social-media/stories-and-tiktok-covers','story-game-night-1080x1920',1080,1920,frame(1080,1920,f'''
 <div style="position:absolute;left:81px;right:81px;top:330px"><span class="chip" style="font-size:24px;padding:10px 24px">Tonight</span>
 <div class="d" style="font-size:250px;margin-top:40px">Game<br><span class="hl">night.</span></div>
 <div class="lbl mute" style="font-size:30px;margin-top:50px">Bring snacks. Bring a grudge.</div></div>
 <div class="box" style="position:absolute;left:81px;right:81px;top:1250px;height:330px"></div>
 <div class="lbl mute" style="position:absolute;left:0;right:0;top:1400px;text-align:center;font-size:24px;opacity:.6">Time &amp; table code</div>''',brand_size=40))

# ---------- print ----------
P='03-print-and-documents'; os.makedirs(f'{K}/{P}',exist_ok=True)
q=qrcode.QRCode(border=0,box_size=10,image_factory=qrcode.image.svg.SvgPathImage); q.add_data('https://www.redass.net'); q.make(); q.make_image().save(f'{W}/qr.svg')
QR=f'file://{W}/qr.svg'
lh=f'''<div style="position:absolute;inset:0;background:#fff"></div>
<div style="position:absolute;left:72px;top:60px"><img src="{L1}" style="height:64px"></div>
<div style="position:absolute;right:72px;top:66px;text-align:right;font-size:11.5px;line-height:1.75;color:#5d6675">redass.net<br>news.redass.net<br>discord.gg/gH577r59C8</div>
<div style="position:absolute;left:72px;right:72px;bottom:54px;display:flex;justify-content:space-between;font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:#5d6675;font-weight:500"><span>Draw. Burn. Repeat.</span><span>Adults 18+</span></div>'''
f=doc('lh',lh,'white',('8.5in','11in')); render.html_pdf(f,f'{K}/{P}/letterhead.pdf','8.5in','11in'); render.html_png(f,f'{K}/{P}/letterhead-preview.png',816,1056)
front=f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:20px">{ace(104)}<div>{wm(44)}{tag(12.5,"margin-top:7px")}</div></div>'
back=f'''<div style="position:absolute;inset:0;padding:34px 36px;display:flex;flex-direction:column;justify-content:space-between">
<div class="d" style="font-size:25px">Your friends are<br><span class="hl">the enemy.</span></div>
<div style="display:flex;justify-content:space-between;align-items:flex-end"><div style="font-size:10px;line-height:1.75" class="mute">redass.net<br>discord.gg/gH577r59C8<br><b style="letter-spacing:.14em;color:{INK}">ADULTS 18+</b></div><img src="{QR}" style="width:58px;height:58px"></div></div>'''
for nm,b,c in (('business-card-front',front,''),('business-card-back',back,'cream')):
    f=doc(nm,b,c,('3.75in','2.25in')); render.html_pdf(f,f'{K}/{P}/{nm}-with-bleed.pdf','3.75in','2.25in'); render.html_png(f,f'{K}/{P}/{nm}-preview.png',360,216)
fly=frame(816,1056,f'''<div style="position:absolute;left:61px;right:61px;top:170px"><span class="chip" style="font-size:13px;padding:6px 14px">Adults only &middot; grudges welcome</span>
<div class="d" style="font-size:150px;margin-top:26px">Game<br><span class="hl">night.</span></div></div>
<div style="position:absolute;left:61px;right:61px;top:610px;display:grid;grid-template-columns:120px 1fr;row-gap:26px;align-items:end">
<span class="lbl mute" style="font-size:14px">When</span><span class="rule" style="opacity:.35"></span>
<span class="lbl mute" style="font-size:14px">Where</span><span class="rule" style="opacity:.35"></span>
<span class="lbl mute" style="font-size:14px">Table code</span><span class="rule" style="opacity:.35"></span></div>
<div style="position:absolute;left:61px;right:61px;top:800px;display:flex;justify-content:space-between;align-items:center">
<div><div class="d" style="font-size:40px">Scan. Sit. <span class="hl">Burn.</span></div><div class="mute" style="font-size:15px;margin-top:8px">Free in your browser at redass.net</div></div>
<div style="background:#fff;padding:10px;border-radius:12px"><img src="{QR}" style="width:110px;height:110px;display:block"></div></div>''',m=61,brand_size=28)
f=doc('fly',fly,'',('8.5in','11in')); render.html_pdf(f,f'{K}/{P}/game-night-flyer.pdf','8.5in','11in'); render.html_png(f,f'{K}/{P}/game-night-flyer-preview.png',816,1056)

# ---------- extras ----------
X='04-extras'
png(X,'phone-wallpaper-1179x2556',1179,2556,f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:80px;padding-top:300px">{ace(560)}{wm(80)}</div>')
png(X,'desktop-wallpaper-2560x1440',2560,1440,f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:90px">{ace(520)}<div>{wm(190)}{tag(64,"margin-top:28px")}</div></div>')
png(X,'video-call-background-1920x1080',1920,1080,f'<div style="position:absolute;right:80px;top:70px;display:flex;align-items:center;gap:18px">{ace(96)}{wm(52)}</div>')
qrcode.make('https://www.redass.net',border=2,box_size=20).save(f'{K}/{X}/qr-code-redass-net.png')
open(f'{K}/{X}/qr-code-redass-net.svg','wb').write(open(f'{W}/qr.svg','rb').read())
print('ok')
