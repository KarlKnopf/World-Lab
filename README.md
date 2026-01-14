## Learning-Oriented Project

World Lab is a learning-first project.

The systems modeled here are **simplifications**, not authoritative simulations.
They are designed to explore ideas, ask questions, and gradually increase in
fidelity over time.

Domain knowledge (biology, ecology, anthropology, climate science, etc.)
is being learned alongside implementation.

Accuracy may improve, assumptions may change, and earlier models may be replaced.
That is an expected and intentional part of the process.

Thoughtful feedback and corrections are welcome, especially when they help clarify
assumptions or suggest more interesting directions to explore.

This project treats simulation as a learning process rather than a finished model.

## How to Run

World Lab is designed to be run locally.

### Requirements
- Python 3.10+
- NumPy
- matplotlib

Install dependencies if needed:
```bash
pip install numpy matplotlib

## Running the Project

The main entry point is main.py.

python main.py


By default, main.py generates and visualizes a small set of example worlds.

## Experimenting with Seeds

Edit main.py to add, remove, or modify worlds.

Seeds can be numbers or arbitrary strings:

worlds = [
    generate_world(seed=42),
    generate_world(seed="ice-age"),
    generate_world(seed="oops all deserts"),
]

titles = [
    "Seed: 42",
    "Seed: ice-age",
    "Seed: oops all deserts",
]


The same seed will always generate the same world.
Different seeds produce different worlds.

Experiment freely — this file is intended to be modified.

There is no “correct” configuration — `main.py` is an experiment runner, not a fixed interface.
