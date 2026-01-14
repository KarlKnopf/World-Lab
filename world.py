"""
World generation module.

ASSUMPTIONS:

TEMPORARY:
- Terrain is generated from uniform random noise.
- Cells are independent at generation time.

STRUCTURAL:
- The world is a 2D grid of fixed resolution.
- World generation is deterministic given a seed.
- The world exists independently of visualization.

NOT MODELED:
- Geological processes
- Climate systems
- Temporal evolution
"""

import random
import numpy as np

def generate_world(width=64, hight=64, seed=None):

    """
    Generate a procedural elevation map.

    ASSUMPTIONS:

    TEMPORARY:
    - Elevation values are uniformly random.
    - All terrain features are uncorrelated.

    STRUCTURAL:
    - Output is a 2D NumPy array.
    - World dimensions are fixed at creation.

    NOTES:
    - This function serves as a baseline generator.
    """

    if seed is not None:
        random.seed(seed)
        numpy_seed = random.randint(0,2**32-1)
        np.random.seed(numpy_seed)
    elevation = np.random.rand(hight,width)
    return elevation
    return np.random.rand(width,hight)
