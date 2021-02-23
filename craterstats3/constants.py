
import numpy as np
import matplotlib.path as mpath

PRESENTATIONS=('cumulative', 'differential', 'relative (R)', 'Hartmann', 'chronology', 'rate')

DEF_XRANGE = ((-3, 2), (-3, 2), (-2, 3), (-3.15, 2.56), (4.5, 0), (4.5, 0))
DEF_YRANGE = ((-4, 1), (-5, 5), (-4, 1), (-8, 5), (-6, 2), (-6, 3))

GREYS = (['#aaaaaa', '#e0e0e0', '#ededed', '#f8f8f8'], #standard/inverted grey values
         ['#787878', '#464646', '#373737', '#282828'])

PALETTE = ( #1st column for white background; 2nd for inverted
            ('#000000', '#ffffff', 'Black'),
            ('#a00000', '#ff0000', 'Red'),
            ('#008200', '#00ff00', 'Green'),
            ('#0050c8', '#5ab4ff', 'Blue'),
            ('#e1af00', '#ffdc00', 'Yellow'),
            ('#8748bd', '#b464ff', 'Violet'),
            ('#aaaaaa', '#787878', 'Grey'),
            ('#19426b', '#19426b', 'blue1'),
            ('#476788', '#476788', 'blue2'),
            ('#7a91a9', '#7a91a9', 'blue3'),
            ('#a0ccd3', '#a0ccd3', 'blue4'),
            ('#533714', '#533714', 'brown1'),
            ('#6b4719', '#6b4719', 'brown2'),
            ('#7b5c33', '#7b5c33', 'brown3'),
            ('#af9c83', '#af9c83', 'brown4'),
            ('#336b19', '#336b19', 'green1'),
            ('#5d8a49', '#5d8a49', 'green2'),
            ('#91af83', '#91af83', 'green3'),
            ('#b58000', '#b58000', 'orange'),
            ('#6b1946', '#6b1946', 'pink1'),
            ('#975e7d', '#975e7d', 'pink2'),
            ('#ba93a8', '#ba93a8', 'pink3'),
            ('#4c265d', '#4c265d', 'purple1'),
            ('#876e93', '#876e93', 'purple2'),
            ('#6b1920', '#6b1920', 'red1'),
            ('#7c393f', '#7c393f', 'red2'),
            ('#8d595e', '#8d595e', 'red3'),
            ('#196b64', '#196b64', 'teal1'),
            ('#6ba09b', '#6ba09b', 'teal2'),
            ('#b5a200', '#b5a200', 'yellow1'),
            ('#ded68e', '#ded68e', 'yellow2'),
            ('#a8b100', '#a8b100', 'yellow-green'),
            )

star4 = mpath.Path(
    np.array(([-1, -.25, 0, .25, 1, .25, 0, -.25, -1], [0, .25, 1, .25, 0, -.25, -1, -.25, 0])).transpose())

MARKERS = ( {'marker': 's', 'fillstyle': 'none', 'markersize': 3.},
            {'marker': '^', 'fillstyle': 'none', 'markersize': 3.5},
            {'marker': star4, 'fillstyle': 'none', 'markersize': 4.3},
            {'marker': 'x', 'markersize': 3.},
            {'marker': '*', 'fillstyle': 'none', 'markersize': 4.5},
            {'marker': '+', 'markersize': 3.5},
            {'marker': '.', 'markersize': 3.},
            {'marker': 'v', 'fillstyle': 'none', 'markersize': 3.5},
            {'marker': 'o', 'fillstyle': 'none', 'markersize': 3.},
            {'marker': 's', 'markersize': 2.5},
            {'marker': '^', 'markersize': 2.5},
            {'marker': 'v', 'markersize': 2.5},
            {'marker': 'o', 'markersize': 2.5},
            {'marker': '*', 'markersize': 3.5},
            {'marker': star4, 'markersize': 3.8},
            )