"""
World generation module.

ASSUMPTIONS:
- The world is represented as a 2D grid.
- Each cell is independent at generation time.
- Random noise is a sufficient stand-in for terrain at this stage.

NOT MODELED:
- Plate tectonics
- Erosion
- Climate
- Any temporal evolution

NOTES:
- This module prioritizes simplicity and reproducibility.
- More structured terrain generation may replace this entirely later.
"""
import random
import numpy as np

def generate_world(width=64, hight=64, seed=None):
     """
    Generate a procedural world elevation map.

    ASSUMPTIONS:
    - Elevation is uniformly random at generation time.
    - All regions are equally likely to be high or low.
    - World size is fixed and rectangular.

    NOT MODELED:
    - Correlated terrain (mountain ranges, continents)
    - Water level or sea masking
    - Any physical realism

    NOTES:
    - This function exists as a baseline generator.
    - It is expected to be replaced or layered with more complex models.
    """
    if seed is not None:
        random.seed(seed)
        numpy_seed = random.randint(0,2**32-1)
        np.random.seed(numpy_seed)
    elevation = np.random.rand(hight,width)
    return elevation

    return np.random.rand(width,hight)

