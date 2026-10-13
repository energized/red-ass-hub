import sys,os,glob; sys.path.insert(0,os.path.dirname(__file__)); import render
d=sys.argv[1]; out=sys.argv[2]; pat=sys.argv[3] if len(sys.argv)>3 else '*.png'
files=sorted(glob.glob(os.path.abspath(d)+'/'+pat))
cells=''.join(f'<figure><div class="bg"><img src="file://{f}"></div><figcaption>{os.path.basename(f)}</figcaption></figure>' for f in files)
h=f'''<html><style>body{{margin:0;padding:16px;background:#888;font:12px sans-serif;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}
figure{{margin:0}}.bg{{background:repeating-conic-gradient(#ccc 0 25%,#999 0 50%) 0 0/20px 20px;height:220px;display:flex;align-items:center;justify-content:center}}
img{{max-width:100%;max-height:220px}}figcaption{{color:#000;word-break:break-all}}</style><body>{cells}</body></html>'''
open('/tmp/claude-0/kitclean/_sheet.html','w').write(h)
rows=(len(files)+3)//4
render.html_png('/tmp/claude-0/kitclean/_sheet.html',out,1400,rows*260+40)
