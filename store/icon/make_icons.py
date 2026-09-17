#!/usr/bin/env python3
"""Draws the Heart Rate FX icon and writes every size the store and the watch need.

    python3 store/icon/make_icons.py

The motif is the QRS spike of a heartbeat leaving the mouth of the SIDE effect's Pac-Man, which
sits at the left edge. Everything is drawn four times oversized and then reduced, so the curves
stay smooth. Change a number here rather than editing a PNG.
"""
import math
import os

from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SS = 4                       # supersampling
M = 1024                     # master edge length
DARK = (18, 22, 30)
RED = (232, 62, 74)
ORANGE = (255, 132, 0)

# The Pac-Man lies almost entirely outside the picture. Only the two tips of its open mouth reach
# in from the left, as an accent; MOUTH_TIP_X says how far.
PAC_Y, PAC_R = 512, 360
PAC_MOUTH_DEG = 34                       # half angle of the open mouth
MOUTH_TIP_X = 110
PAC_X = MOUTH_TIP_X - PAC_R * math.cos(math.radians(PAC_MOUTH_DEG))
LINE_W = 74                              # thickness of the heartbeat line

# One P-QRS-T complex as fractions of the run, and of the amplitude.
BEAT = [(0.00, 0.0), (0.16, 0.0), (0.22, -0.16), (0.28, 0.0), (0.36, 0.0),
        (0.40, 0.14), (0.48, -1.0), (0.55, 0.40), (0.61, 0.0),
        (0.70, 0.0), (0.78, -0.30), (0.86, 0.0), (1.00, 0.0)]


def draw(size=M, background=DARK, pac=True, line=RED, transparent=False, weight=1.0):
    im = Image.new('RGBA', (size * SS, size * SS),
                   (0, 0, 0, 0) if transparent else background + (255,))
    d = ImageDraw.Draw(im)
    k = size / float(M) * SS          # master units to device units

    if pac:
        box = [(PAC_X - PAC_R) * k, (PAC_Y - PAC_R) * k,
               (PAC_X + PAC_R) * k, (PAC_Y + PAC_R) * k]
        d.pieslice(box, start=PAC_MOUTH_DEG, end=360 - PAC_MOUTH_DEG,
                   fill=(line if transparent else ORANGE))

    x0 = ((MOUTH_TIP_X - 14) if pac else 60) * k
    x1 = (M - 40) * k
    amp = 300 * k
    pts = [(x0 + (x1 - x0) * f, PAC_Y * k + amp * v) for f, v in BEAT]
    d.line(pts, fill=line, width=int(LINE_W * weight * k), joint='curve')

    return im.resize((size, size), Image.LANCZOS)


def main():
    master = draw()
    master.convert('RGB').save(os.path.join(HERE, 'icon_master.png'))

    for size in (144, 80, 48):
        icon = draw(size)
        icon.convert('RGB').save(os.path.join(HERE, 'icon_%d.png' % size))
        icon.save(os.path.join(HERE, 'icon_%d_transparent.png' % size))

    # The watch draws its launcher icon from the shape alone, so it is white on nothing.
    # At 25 px the Pac-Man is a white blob that runs into the line, so the launcher icon keeps
    # the beat alone, drawn heavier because a hairline disappears at that size.
    launcher = draw(25, pac=False, line=(255, 255, 255), transparent=True, weight=1.5)
    os.makedirs(os.path.join(HERE, '..', '..', 'resources', 'images'), exist_ok=True)
    launcher.save(os.path.join(HERE, '..', '..', 'resources', 'images', 'launcher_icon.png'))
    print('icon_master.png, icon_144/80/48(.png/_transparent.png), resources/images/launcher_icon.png')


if __name__ == '__main__':
    main()
