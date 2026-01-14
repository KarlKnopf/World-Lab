from world import generate_world
from viz import show_worlds_side_by_side

"""
Main experiment runner for World Lab.

Edit this file to generate and compare worlds.
Add or remove seeds below to explore variations.
"""

worlds = [
    generate_world(seed="example-a"),
    generate_world(seed="example-b"),
]

titles = [
    "Seed: example-a",
    "Seed: example-b",
]

show_worlds_side_by_side(worlds, titles)
