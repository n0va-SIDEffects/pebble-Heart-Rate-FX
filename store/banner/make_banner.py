#!/usr/bin/env python3
"""Draws the 720x320 store banner.

    python3 store/banner/make_banner.py

Dark ground, the heartbeat running across it, the app icon and title top left, and the
SIDE effect's logo along the bottom. The wave is drawn oversized and reduced so it stays smooth,
and its quiet stretch is put where the logo sits so the two never touch.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
W, H, SS = 720, 320, 3
GROUND = (18, 22, 30)
RED = (232, 62, 74)
WAVE = (196, 44, 58)
WHITE = (245, 248, 252)
GREY = (158, 168, 180)
LOGO_GREY = (225, 232, 240)
LOGO_WIDTH = 185

FONT_BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

BEAT = [(0.00, 0.0), (0.16, 0.0), (0.22, -0.16), (0.28, 0.0), (0.36, 0.0),
        (0.40, 0.14), (0.48, -1.0), (0.55, 0.40), (0.61, 0.0),
        (0.70, 0.0), (0.78, -0.30), (0.86, 0.0), (1.00, 0.0)]


def prepare_logo():
    """White background out, and the lettering lightened so it reads on a dark ground.

    The Pac-Man and its black X are left exactly as they are: they are the mark itself.
    """
    logo = Image.open(os.path.join(ROOT, 'store', 'icon', 'side_effects_logo.png')).convert('RGBA')
    px = logo.load()
    for y in range(logo.height):
        for x in range(logo.width):
            r, g, b, a = px[x, y]
            if r > 235 and g > 235 and b > 235:
                px[x, y] = (r, g, b, 0)
    logo = logo.crop(logo.getbbox())

    px = logo.load()
    start = int(logo.width * 0.42)
    for y in range(logo.height):
        for x in range(start, logo.width):
            r, g, b, a = px[x, y]
            if a > 0 and r < 90 and g < 90 and b < 90:
                px[x, y] = LOGO_GREY + (a,)
    height = max(1, int(logo.height * LOGO_WIDTH / logo.width))
    return logo.resize((LOGO_WIDTH, height), Image.LANCZOS)


def main():
    im = Image.new('RGB', (W * SS, H * SS), GROUND)
    d = ImageDraw.Draw(im)

    # Two beats across the picture, their flat stretch over the corner the logo will occupy.
    baseline = int(H * 0.60) * SS
    amp = 86 * SS
    for beat in range(2):
        x0 = (260 + beat * 250) * SS
        x1 = x0 + 250 * SS
        pts = [(x0 + (x1 - x0) * f, baseline + amp * v) for f, v in BEAT]
        d.line(pts, fill=WAVE, width=9 * SS, joint='curve')
    d.line([(0, baseline), (260 * SS, baseline)], fill=WAVE, width=9 * SS)
    d.line([(760 * SS, baseline), (W * SS, baseline)], fill=WAVE, width=9 * SS)

    im = im.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)

    icon = Image.open(os.path.join(ROOT, 'store', 'icon', 'icon_master.png')).convert('RGBA')
    icon = icon.resize((120, 120), Image.LANCZOS)
    im.paste(icon, (36, 30), icon)

    d.text((184, 40), 'Heart Rate FX', font=ImageFont.truetype(FONT_BOLD, 52), fill=WHITE)
    d.text((186, 104), 'Your pulse as a trace, a sound and a light',
           font=ImageFont.truetype(FONT, 20), fill=GREY)

    logo = prepare_logo()
    im.paste(logo, (30, H - logo.height - 8), logo)

    out = os.path.join(HERE, 'banner_720x320.png')
    im.save(out)
    print(out)


if __name__ == '__main__':
    main()
