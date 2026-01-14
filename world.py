import random
import numpy as np

def generate_world(width=64, hight=64, seed=None):
    if seed is not None:
        random.seed(seed)
        numpy_seed = random.randint(0,2**32-1)
        np.random.seed(numpy_seed)
    elevation = np.random.rand(hight,width)
    return elevation
    return np.random.rand(width,hight)