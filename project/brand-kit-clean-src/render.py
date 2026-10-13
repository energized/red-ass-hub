from playwright.sync_api import sync_playwright
import os, pathlib
_p=None;_b=None
def browser():
    global _p,_b
    if _b is None:
        _p=sync_playwright().start(); _b=_p.chromium.launch()
    return _b
def svg_png(svg_path, png_path, w, h, transparent=True):
    pg=browser().new_page(viewport={'width':w,'height':h})
    tmp='/tmp/claude-0/kitclean/_wrap.html'
    open(tmp,'w').write(f'<html><body style="margin:0;background:transparent"><img src="file://{os.path.abspath(svg_path)}" style="display:block;width:{w}px;height:{h}px"></body></html>')
    pg.goto('file://'+tmp)
    pg.wait_for_timeout(100)
    pg.screenshot(path=png_path, omit_background=transparent); pg.close()
def html_png(html_path, png_path, w, h, transparent=False, scale=1):
    pg=browser().new_page(viewport={'width':w,'height':h}, device_scale_factor=scale)
    pg.goto('file://'+os.path.abspath(html_path)); pg.wait_for_timeout(250)
    pg.screenshot(path=png_path, omit_background=transparent); pg.close()
def html_pdf(html_path, pdf_path, width, height):
    pg=browser().new_page(); pg.goto('file://'+os.path.abspath(html_path)); pg.wait_for_timeout(250)
    pg.pdf(path=pdf_path, width=width, height=height, print_background=True, margin={'top':'0','bottom':'0','left':'0','right':'0'}); pg.close()
