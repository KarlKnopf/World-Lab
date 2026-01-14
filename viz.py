"""
Visualization utilities for World Lab.

ASSUMPTIONS:
- Data is 2D and numeric.
- Color represents magnitude, not categorical meaning.

NOT MODELED:
- Geographic projection
- Scale or units
- Visual realism

NOTES:
- Visualization is intended for comparison and inspection,
  not presentation-quality rendering.
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
