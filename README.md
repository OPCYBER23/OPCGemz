# Procedural Falling Gem System (Pygame)

## Overview

This project is a generative animation system built using Python and Pygame that simulates a field of abstract geometric “gems” falling through space.

Each gem is procedurally generated with randomised shape, size, rotation, and motion behaviour. The system continuously animates these forms and exports each frame as an image sequence, allowing the output to be used for video or further creative processing.

The result is a synthetic “digital weather system” of rotating geometric objects.

---

## Features

* Procedural generation of polygonal geometric forms
* Multiple shape types (hexagons, octagons)
* Physics-inspired downward motion with variation per object
* Rotation dynamics per individual gem
* Optional internal radial line structures
* Frame-by-frame rendering system (image sequence export)
* Configurable animation duration and frame rate

---

## Visual Behaviour

Each gem behaves as an independent animated object:

### 1. Generation

* Random shape type selected (6 or 8 sides)
* Random size and starting position
* Randomised rotation and motion speed

### 2. Motion

* Gems fall vertically down the screen
* Larger gems fall more slowly than smaller ones
* Rotation is continuously applied during descent

### 3. Rendering

* Each gem is drawn as a filled polygon
* Optional internal radial lines extend toward vertices
* Creates a crystalline, “etched” visual effect

### 4. Recycling

* When a gem leaves the screen, it is reset to the top with new parameters
* Ensures continuous non-repeating motion field

---

## Output System

This project exports each animation frame as a `.png` image:

```
frames/frame_0000.png
frames/frame_0001.png
frames/frame_0002.png
...
```

These frames can be assembled into video using tools such as:

* ffmpeg
* Adobe Premiere / After Effects
* DaVinci Resolve

---

## Configuration Options

Key parameters controlling behaviour:

* `NUM_GEMS` – number of active objects
* `SIDES_OPTIONS` – allowed polygon types (e.g. hexagon, octagon)
* `SIZE_MIN / SIZE_MAX` – gem size range
* `SPEED_MIN / SPEED_MAX` – falling speed range
* `ROT_MIN / ROT_MAX` – rotation speed range
* `DRAW_RADIAL_LINES` – enables internal line structure
* `FPS` – animation frame rate
* `DURATION_SECONDS` – total runtime
* `OUTPUT_DIR` – folder for exported frames

---

## Requirements

* Python 3.x
* Pygame

Install dependency:

```bash id="pygame_install"
pip install pygame
```

---

## Running the Project

```bash id="run_gems"
python gem_simulation.py
```

Output frames will be saved to:

```
/frames
```

---

## Conceptual Framing

This system explores:

* procedural geometry as synthetic natural forms
* motion as emergent structure rather than scripted animation
* repetition with controlled randomness
* visual entropy through continuous regeneration
* simulation of “material behaviour” in abstract space

The “gems” function less as objects and more as a dynamic field of evolving geometry.

---

## Performance Notes

* Higher `NUM_GEMS` increases visual density but reduces performance
* Frame export is disk-intensive due to continuous PNG writing
* Designed for offline rendering rather than real-time playback

---

## Potential Extensions

* audio-reactive motion (FFT-driven geometry changes)
* shader-based rendering (OpenGL / GLSL version)
* interactive control of parameters in real time
* colour evolution over time (palette drift system)

---

## Output Use Cases

* generative video art
* ambient visual backgrounds
* audiovisual performance assets
* procedural motion studies
* experimental animation sequences

---

## Author

Cyber Security / Creative Systems Student (Certificate IV – TAFE)

---

## Disclaimer

This project is a generative visual simulation intended for educational and creative exploration. It does not interact with external systems or data sources.
