"""
Visualization utilities for World Lab.

ASSUMPTIONS:
- Input data is 2D and numeric.

KNOWN LIMITATIONS:
- Color scales may exaggerate small differences.
- Visual similarity does not imply model similarity.
- Plots are not geographically meaningful.

NOT MODELED:
- Projection
- Physical units
- Perceptual color calibration
"""

import matplotlib.pyplot as plt

def show_world(grid, title='World Map', intropolation='nearest'):
    plt.imshow(grid, cmap='Set3', interpolation=intropolation)
    plt.title(title)
    plt.colorbar()
    plt.show()

def show_worlds_side_by_side(worlds, titles=None, cmap='Set3', interpolation='nearest'):
    count = len(worlds)

    fig, axes = plt.subplots(1, count, figsize=(4 * count, 4))

    if count == 1:
        axes = [axes]

    img = None

    for i, ax in enumerate(axes):
        img = ax.imshow(worlds[i], cmap=cmap, interpolation=interpolation)
        if titles:
            ax.set_title(titles[i])

        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')

        ax.set_xticks([])
        ax.set_yticks([])

    cbar = fig.colorbar(img, ax=axes, shrink=0.75, location='right')
    cbar.set_label('Colorbar Label')

    plt.show()

