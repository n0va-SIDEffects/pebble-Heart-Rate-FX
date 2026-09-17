#!/usr/bin/env python3
"""Draws the 720x320 store banner.

    python3 store/banner/make_banner.py

One idea carries the picture: the heartbeat leaves the mouth of the SIDE effect's Pac-Man, which
lies off the left edge so that only the two tips of its mouth reach in, and runs the full width as
the main wave. No separate icon tile. The logo sits along the bottom, and the wave's quiet stretch
is placed above it so the two never touch.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
W, H, SS = 720, 320, 3
GROUND = (18, 22, 30)
RED = (232, 62, 74)
ORANGE = (255, 132, 0)
WHITE = (245, 248, 252)
GREY = (168, 178, 190)
LOGO_GREY = (225, 232, 240)
LOGO_WIDTH = 185

BASELINE = 168          # the mouth axis, and the line the wave rests on
MOUTH_DEG = 34          # half angle of the open mouth
MOUTH_TIP_X = 30        # how far the tips reach in: an accent, no more
MOUTH_R = 52            # small enough that the tips do not compete with the logo's own Pac-Man
WAVE_W = 10
AMP = 78

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

    # The mouth the wave comes out of. Its centre lies off the picture; only the tips reach in.
    cx = MOUTH_TIP_X - MOUTH_R * math.cos(math.radians(MOUTH_DEG))
    box = [(cx - MOUTH_R) * SS, (BASELINE - MOUTH_R) * SS,
           (cx + MOUTH_R) * SS, (BASELINE + MOUTH_R) * SS]
    d.pieslice(box, start=MOUTH_DEG, end=360 - MOUTH_DEG, fill=ORANGE)

    # One long wave out of the mouth: quiet, two beats, quiet again over the logo's corner.
    start_x = MOUTH_TIP_X - 10
    d.line([(start_x * SS, BASELINE * SS), (300 * SS, BASELINE * SS)], fill=RED, width=WAVE_W * SS)
    for beat in range(2):
        x0 = (300 + beat * 200) * SS
        x1 = x0 + 200 * SS
        pts = [(x0 + (x1 - x0) * f, BASELINE * SS + AMP * SS * v) for f, v in BEAT]
        d.line(pts, fill=RED, width=WAVE_W * SS, joint='curve')
    d.line([(700 * SS, BASELINE * SS), (W * SS, BASELINE * SS)], fill=RED, width=WAVE_W * SS)

    im = im.resize((W, H), Image.LANCZOS)
    d = ImageDraw.Draw(im)

    d.text((92, 30), 'Heart Rate FX', font=ImageFont.truetype(FONT_BOLD, 54), fill=WHITE)
    d.text((96, 96), 'Your pulse as a trace, a sound and a light',
           font=ImageFont.truetype(FONT, 21), fill=GREY)

    logo = prepare_logo()
    im.paste(logo, (30, H - logo.height - 8), logo)

    out = os.path.join(HERE, 'banner_720x320.png')
    im.save(out)
    print(out)


if __name__ == '__main__':
    main()
