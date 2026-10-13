import os,sys; sys.path.insert(0,os.path.dirname(__file__))
from brand import *; import render
from social import CSS, wm, tag, ace_img, fan, LOGO_F, W, T
G=f'{W}/kit/00-START-HERE'; os.makedirs(G,exist_ok=True)
L1=f'file://{W}/kit/01-logos/lockup-horizontal-for-light-backgrounds.svg'
L2=f'file://{W}/kit/01-logos/lockup-horizontal-for-dark-backgrounds.svg'
S1=f'file://{W}/kit/01-logos/lockup-stacked-for-dark-backgrounds.svg'
PG='position:relative;width:11in;height:8.5in;overflow:hidden;page-break-after:always;padding:56px 64px'
def h(t,c=''): return f'<div class="d" style="font-size:54px;font-weight:600;margin-bottom:26px;{c}">{t}</div>'
def sw(name,hexv,txt='#fff',note=''):
    return f'<div style="flex:1"><div style="height:150px;border-radius:16px;background:{hexv};border:1px solid rgba(0,0,0,.15);display:flex;align-items:flex-end;padding:14px;color:{txt};font-family:Oswald;letter-spacing:.06em;font-size:22px">{hexv.upper()}</div><div style="font-family:Oswald;font-size:22px;margin-top:10px;text-transform:uppercase;letter-spacing:.04em">{name}</div><div style="font-size:15px;opacity:.75;margin-top:4px">{note}</div></div>'
cream='background:'+CREAM+';color:'+INK
pages=[]
pages.append(f'''<div style="{PG}"><div style="position:absolute;left:90px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
<div class="stamp" style="font-size:24px;align-self:flex-start">Brand kit &middot; October 2026</div>
<div style="margin-top:36px">{wm(130)}</div>{tag(48,"margin-top:18px")}
<div style="font-size:22px;margin-top:40px;max-width:520px;line-height:1.5" class="muted">How to make anything look and sound like Red Ass: the logo, colours, fonts, voice and where every file goes.</div></div>
{fan(870,190,330,("galaxy","volcano"),spread=15)}</div>''')
pages.append(f'''<div style="{PG};{cream}" class="cream">{h("The logo: the burning ace")}
<div style="display:grid;grid-template-columns:1fr 1.25fr;gap:44px">
<div><div style="background:#fff;border-radius:18px;padding:30px;display:flex;justify-content:center">{ace_img(250)}</div>
<div style="font-size:17px;line-height:1.55;margin-top:20px">An ace with a flame on it. The <b>A and small flame</b> sit top-left and again <b>upside down bottom-right</b>, like a real playing card. The card is always tilted the same way. All letters are shapes, so it looks the same everywhere.</div></div>
<div><div style="background:{FELT};border-radius:18px;padding:26px 30px"><img src="{L2}" style="height:110px"></div>
<div style="background:#fff;border-radius:18px;padding:26px 30px;margin-top:14px"><img src="{L1}" style="height:110px"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:22px;font-size:16px;line-height:1.5">
<div><b style="font-family:Oswald;font-size:20px;letter-spacing:.05em;text-transform:uppercase;color:{RED}">Do</b><br>Leave space around it (at least the width of the A).<br>Use the dark-background version on dark, the light one on light.<br>Keep the ace at least 24 px tall on screens.</div>
<div><b style="font-family:Oswald;font-size:20px;letter-spacing:.05em;text-transform:uppercase;color:{RED}">Don't</b><br>Stretch, recolour, or untilt it.<br>Add a ® or "TM": the name isn't registered.<br>Put it on busy photos without a dark or light box.</div></div></div></div></div>''')
pages.append(f'''<div style="{PG}">{h("Colours")}
<div style="display:flex;gap:20px">{sw("Table felt",FELT,'#e9edf3',"Main background")}{sw("Felt light",FELT2,'#e9edf3',"Panels on felt")}{sw("Card cream",CREAM,INK,"Cards, light pages")}{sw("Ink",INK,'#fff',"Text on light")}</div>
<div style="display:flex;gap:20px;margin-top:30px">{sw("Burn red",RED,'#fff',"Logo, buttons, text on cream")}{sw("Ember",EMBER,INK,"Red text on dark only")}{sw("Gold",GOLD,INK,"Highlights, 'Burn.'")}{sw("Smoke",MUTED,INK,"Small print on dark")}</div>
<div class="muted" style="font-size:17px;margin-top:30px;line-height:1.5">Rule of thumb: mostly felt, a hit of red, a pinch of gold. Use Ember (not Burn red) for red words on dark backgrounds so they stay readable.</div></div>''')
pages.append(f'''<div style="{PG};{cream}" class="cream">{h("Fonts and voice")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:50px">
<div><div class="d" style="font-size:88px;font-weight:600">Oswald</div><div style="font-size:16px;margin-top:6px">Headlines, always UPPERCASE. 600 for punch, 400 for "Red" in the wordmark.</div>
<div style="font-size:48px;margin-top:28px">IBM Plex Sans</div><div style="font-size:16px;margin-top:6px">Everything you read in sentences.</div>
<div style="font-size:15px;margin-top:22px;opacity:.75">Both are free Google Fonts. Install files are in the "fonts" folder.</div></div>
<div><div class="d" style="font-size:30px;font-weight:600;color:{RED}">How we talk</div>
<div style="font-size:17px;line-height:1.55;margin-top:10px">Playful, cheeky, a little spicy: teasing between friends at the card table. Short lines. Punchline last.</div>
<div class="d" style="font-size:24px;margin-top:20px;line-height:1.25">"It's not personal. It's a 4."<br>"Kings reverse. Grudges don't."<br>"Burn your friends. Legally."</div>
<div style="font-size:16px;line-height:1.55;margin-top:20px"><b>Never:</b> mean, crude, aimed at kids, or about real people. Always say <b>Adults 18+</b>. Looks are cosmetic only, never pay-to-win. Don't announce merch, Steam, the Play Store or anything not yet decided.</div></div></div></div>''')
rows=[('Profile picture (Facebook, TikTok, YouTube, Discord, Instagram)','profile-picture-*-1080.png'),('Facebook cover','facebook-cover-1640x624.png'),('YouTube banner','youtube-banner-2560x1440.png'),('Discord server banner / invite background','discord-*.png'),('X (Twitter) header, if you make an account','x-twitter-header-1500x500.png'),('Link preview (when a link is shared)','link-preview-1200x630.png'),('Feed posts (Facebook, Instagram)','spicy-posts/*.png, fill-in-templates/*.png'),('Stories, Reels, TikTok covers','stories-and-tiktok-covers/*.png'),('Letters','letterhead-editable.docx (Word) or letterhead.pdf'),('Printing','business cards and flyer PDFs (include bleed)')]
tr=''.join(f'<tr><td style="padding:9px 0;border-bottom:1px solid rgba(233,237,243,.15)">{a}</td><td style="padding:9px 0 9px 20px;border-bottom:1px solid rgba(233,237,243,.15);font-family:Oswald;letter-spacing:.03em;color:{GOLD}">{b}</td></tr>' for a,b in rows)
pages.append(f'''<div style="{PG}">{h("Which file goes where")}<table style="width:100%;border-collapse:collapse;font-size:17px">{tr}</table>
<div class="muted" style="font-size:15px;margin-top:20px">Covers are designed with the important bits in the middle, because phones crop the edges.</div></div>''')
f=f'{T}/guide.html'; open(f,'w').write(f'<html><head><meta charset="utf-8"><style>{CSS} @page{{margin:0;size:11in 8.5in}} html,body{{height:auto;overflow:visible}}</style></head><body>{"".join(pages)}</body></html>')
render.html_pdf(f,f'{G}/Red-Ass-Brand-Guide.pdf','11in','8.5in'); print('ok')
