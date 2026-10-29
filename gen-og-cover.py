#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tao lai og-cover.png voi logo 'Cyber B'.Bien nen bang mau that tai vi tri de
khong lo vet den, giu nguyen gradient nen cu."""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, 'img', 'og-cover.png.bak')
DST = os.path.join(BASE, 'img', 'og-cover.png')

W, H = 1080, 566
ORANGE = (244, 123, 32)
WHITE = (255, 255, 255)
MUTED = (150, 168, 196)

# Vi tri can lam sach (logo cu + link cu)
LOGO_BOX = (40, 40, 400, 150)
LINK_BOX = (40, 478, 640, 522)


def font(size, bold=False):
    for n in (['arialbd.ttf'] if bold else []) + ['arial.ttf', 'segoeui.ttf', 'DejaVuSans.ttf']:
        try:
            return ImageFont.truetype(n, size)
        except Exception:
            pass
    for root in ['C:/Windows/Fonts', '/usr/share/fonts/truetype/dejavu']:
        if os.path.isdir(root):
            for f in sorted(os.listdir(root)):
                if f.lower().endswith('.ttf') and (('bold' in f.lower() or 'bd' in f.lower()) == bold):
                    try:
                        return ImageFont.truetype(os.path.join(root, f), size)
                    except Exception:
                        pass
    return ImageFont.load_default()


def inpaint_gradient(img, box, samples=None):
    """Tao patch vien gradient theo mau ke can ben (tren + duoi) roi dan phang."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    patch = Image.new('RGB', (w, h))
    pd = ImageDraw.Draw(patch)
    # lay mau tai 2 hang ke tren va ke duoi -> noi suy theo chieu doc
    top = [img.getpixel((x, max(0, y0 - 3))) for x in range(x0, x1)]
    bot = [img.getpixel((x, min(img.height - 1, y1 + 3))) for x in range(x0, x1)]
    for y in range(h):
        t = y / max(1, h - 1)
        for x in range(w):
            c = tuple(int(top[x][i] + (bot[x][i] - top[x][i]) * t) for i in range(3))
            pd.point((x, y), fill=c)
    img.paste(patch, (x0, y0))


def main():
    img = Image.open(SRC).convert('RGB')
    if img.size != (W, H):
        img = img.resize((W, H), Image.LANCZOS)

    # Lam sach 2 vung bang noi suy gradient
    inpaint_gradient(img, LOGO_BOX)
    inpaint_gradient(img, LINK_BOX)

    d = ImageDraw.Draw(img)

    # Logo moi: 'Cyber' trang + 'B' cam
    f = font(42, True)
    x, y = 66, 66
    d.text((x, y), 'Cyber', font=f, fill=WHITE)
    d.text((x + f.getlength('Cyber'), y), 'B', font=f, fill=ORANGE)
    d.text((x + 3, y + 52), 'P H O N E   S T O R E', font=font(13, True), fill=MUTED)

    # Link moi
    d.text((66, 488), 'emtenlamua.github.io/cyberb-facebook', font=font(15, True), fill=ORANGE)

    img.save(DST, 'PNG', optimize=True)
    print('OK ->', DST)


if __name__ == '__main__':
    main()
