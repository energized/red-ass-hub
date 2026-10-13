import os,sys; sys.path.insert(0,os.path.dirname(__file__))
from cleanlib import *
G=f'{K}/00-START-HERE'; os.makedirs(G,exist_ok=True)
PG='position:relative;width:11in;height:8.5in;overflow:hidden;page-break-after:always'
M=72
def page(cls,title,inner,num):
    return f'''<div class="{cls}" style="{PG}"><div style="position:absolute;inset:0" class="pbg {cls}"></div>
<div style="position:absolute;left:{M}px;right:{M}px;top:{M}px;display:flex;justify-content:space-between" class="lbl mute"><span style="font-size:12px">Red Ass &middot; Brand kit 2026</span><span style="font-size:12px">{num:02d}</span></div>
<div style="position:absolute;left:{M}px;right:{M}px;top:130px"><div class="d" style="font-size:64px">{title}</div><div style="margin-top:36px">{inner}</div></div></div>'''
def sw(name,hexv,txt,note):
    return f'<div><div style="height:130px;border-radius:18px;background:{hexv};box-shadow:inset 0 0 0 1px rgba(128,128,128,.25)"></div><div style="font-family:Oswald;font-weight:600;font-size:20px;text-transform:uppercase;margin-top:12px">{name}</div><div class="lbl mute" style="font-size:11px;margin-top:4px">{hexv.upper()}</div><div class="mute" style="font-size:13px;margin-top:4px">{note}</div></div>'
pages=[f'''<div style="{PG}" class="night"><div style="position:absolute;inset:0;background:{NIGHT}"></div>
<div style="position:absolute;left:{M}px;top:{M}px" class="lbl mute"><span style="font-size:12px">Brand kit &middot; October 2026</span></div>
<div style="position:absolute;left:{M}px;bottom:{M+10}px">{wm(150)}{tag(46,"margin-top:24px")}</div>
<div style="position:absolute;right:110px;top:50%;transform:translateY(-50%)">{ace(420)}</div></div>''']
pages.append(page('white','The burning ace',f'''<div style="display:grid;grid-template-columns:1fr 1.3fr;gap:56px;align-items:start">
<div><div style="background:{CREAM};border-radius:22px;height:300px;display:flex;align-items:center;justify-content:center">{ace(230)}</div></div>
<div style="font-size:16px;line-height:1.6"><p>One ace. One flame. An <b>A</b> top-left and again <b>upside down bottom-right</b>, like a real card. Always tilted the same way. Letters are shapes, so it looks identical everywhere.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-top:28px"><div><div class="lbl" style="font-size:12px;color:{RED}">Do</div><p style="margin-top:8px">Give it room: at least the width of the A on every side.<br>Light version on dark, dark version on light.<br>Keep it 24 px tall or bigger on screens.</p></div>
<div><div class="lbl" style="font-size:12px;color:{RED}">Don't</div><p style="margin-top:8px">Stretch, recolour, straighten or add effects.<br>Add ® or "TM" (the name isn't registered).<br>Put it on busy photos.</p></div></div></div></div>''',2))
pages.append(page('night','Colour',f'''<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:22px">{sw("Night",NIGHT,'',"Main background")}{sw("Cream",CREAM,'',"Light background")}{sw("Burn red",RED,'',"Logo, red pages, red on light")}{sw("Ember",EMBER,'',"Red words on dark")}{sw("Gold",GOLD,'',"Only the word Burn.")}{sw("Ink",INK,'',"Text on light")}{sw("Bone",BONE,'',"Text on dark")}{sw("Smoke",SMOKE,'',"Small print on dark")}</div>
<p class="mute" style="font-size:15px;margin-top:30px">One background per piece: Night, Cream or Burn red. One accent colour. Flat colour only: no patterns, no gradients.</p>''',3))
pages.append(page('cream','Type and voice',f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:56px">
<div><div class="d" style="font-size:96px">Oswald</div><p style="font-size:15px;margin-top:10px" class="mute">Headlines. Uppercase. Big. Tight. Let it carry the design.</p>
<div style="font-size:46px;margin-top:34px">IBM Plex Sans</div><p style="font-size:15px;margin-top:10px" class="mute">Sentences and small labels (labels in spaced-out capitals).</p></div>
<div><div class="lbl" style="font-size:12px;color:{RED}">How we talk</div><p style="font-size:16px;line-height:1.6;margin-top:10px">Cheeky trash talk between friends. Short. Punchline last.</p>
<div class="d" style="font-size:30px;margin-top:22px;line-height:1.15">It's not personal. <span class="hl">It's a 4.</span><br>Kings reverse. <span class="hl">Grudges don't.</span><br>Burn your friends. <span class="hl">Legally.</span></div>
<p style="font-size:15px;line-height:1.6;margin-top:24px"><b>Never</b> mean, crude, about real people or aimed at kids. Always <b>Adults 18+</b>. Looks only, never pay-to-win. No merch, Steam or Play Store announcements.</p></div></div>''',4))
rows=[('Profile picture, every account','profile-picture-*-1080.png'),('Facebook cover','facebook-cover-1640x624.png'),('YouTube banner','youtube-banner-2560x1440.png'),('Discord banner / invite','discord-*.png'),('X header (if you make one)','x-twitter-header-1500x500.png'),('Shared-link image','link-preview-1200x630.png'),('Feed posts','spicy-posts, fill-in-templates'),('Stories, Reels, TikTok','stories-and-tiktok-covers'),('Letters','letterhead-editable.docx / letterhead.pdf'),('Printing','business cards + flyer PDFs (bleed included)')]
tr=''.join(f'<tr><td style="padding:10px 0;border-bottom:1px solid rgba(139,149,165,.25);font-size:15px">{a}</td><td style="padding:10px 0;border-bottom:1px solid rgba(139,149,165,.25);font-size:15px;text-align:right" class="mute">{b}</td></tr>' for a,b in rows)
pages.append(page('night','Where it goes',f'<table style="width:100%;border-collapse:collapse">{tr}</table>',5))
css_extra='.pbg.night{background:'+NIGHT+'}.pbg.white{background:#fff}.pbg.cream{background:'+CREAM+'} .night{color:'+BONE+'} .white,.cream{color:'+INK+'}'
f=f'{T}/guide.html'; open(f,'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}{css_extra} @page{{margin:0;size:11in 8.5in}} html,body{{height:auto;overflow:visible;background:none}}</style></head><body>{"".join(pages)}</body></html>')
render.html_pdf(f,f'{G}/Red-Ass-Brand-Guide-Clean.pdf','11in','8.5in'); print('ok')
