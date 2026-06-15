import pygame
import random
import math
import os

# ==================================================
# USER-TUNABLE SETTINGS
# ==================================================
WIDTH, HEIGHT = 1280, 720

BG_COLOR = (30, 30, 30)       # dark grey background
GEM_COLOR = (255, 255, 255)   # white gems
LINE_COLOR = (40, 40, 40)        # black internal lines

NUM_GEMS = 30
SIDES_OPTIONS = [6, 8]        # hexagons & octagons

SIZE_MIN = 10
SIZE_MAX = 30

SPEED_MIN = 1.0
SPEED_MAX = 4.0

ROT_MIN = -0.03
ROT_MAX = 0.03

DRAW_RADIAL_LINES = True
LINE_WIDTH = 1
LINE_LENGTH_FACTOR = 0.85     # how far lines extend toward vertices

FPS = 60
DURATION_SECONDS = 240
OUTPUT_DIR = "frames"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# ==================================================
# HELPER FUNCTION
# ==================================================
def regular_polygon(x, y, radius, sides, rotation):
    points = []
    for i in range(sides):
        angle = (2 * math.pi / sides) * i + rotation
        px = x + radius * math.cos(angle)
        py = y + radius * math.sin(angle)
        points.append((px, py))
    return points

# ==================================================
# GEM CLASS
# ==================================================
class Gem:
    def __init__(self):
        self.reset()

    def reset(self):
        self.sides = random.choice(SIDES_OPTIONS)
        self.radius = random.uniform(SIZE_MIN, SIZE_MAX)

        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(-HEIGHT, 0)

        # larger gems fall slower
        self.speed = random.uniform(SPEED_MIN, SPEED_MAX) * (SIZE_MAX / self.radius)

        self.rotation = random.uniform(0, math.pi * 2)
        self.rotation_speed = random.uniform(ROT_MIN, ROT_MAX)

        self.has_lines = random.random() < 0.8

    def update(self):
        self.y += self.speed
        self.rotation += self.rotation_speed

        if self.y - self.radius > HEIGHT:
            self.reset()

    def draw(self, surface):
        points = regular_polygon(
            self.x, self.y, self.radius, self.sides, self.rotation
        )

        # draw filled gem
        pygame.draw.polygon(surface, GEM_COLOR, points)

        # draw internal black radial lines
        if DRAW_RADIAL_LINES and self.has_lines:
            cx, cy = self.x, self.y
            for px, py in points:
                lx = cx + (px - cx) * LINE_LENGTH_FACTOR
                ly = cy + (py - cy) * LINE_LENGTH_FACTOR
                pygame.draw.line(
                    surface,
                    LINE_COLOR,
                    (cx, cy),
                    (lx, ly),
                    LINE_WIDTH
                )

# ==================================================
# MAIN LOOP
# ==================================================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

gems = [Gem() for _ in range(NUM_GEMS)]

total_frames = FPS * DURATION_SECONDS
frame_count = 0
running = True

while running and frame_count < total_frames:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    for gem in gems:
        gem.update()
        gem.draw(screen)

    pygame.display.flip()

    # save frame
    filename = f"{OUTPUT_DIR}/frame_{frame_count:04d}.png"
    pygame.image.save(screen, filename)

    frame_count += 1
    clock.tick(FPS)

pygame.quit()
