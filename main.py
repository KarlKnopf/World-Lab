from world import generate_world
from viz import show_worlds_side_by_side

worlds = [
    generate_world(seed=42),
    generate_world(seed='test')
]

titles=['Seed 42', 'Seed test']

show_worlds_side_by_side(worlds, titles)