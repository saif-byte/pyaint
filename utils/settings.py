import pygame

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
GRAY = (128, 128, 128)
SILVER = (192, 192, 192)
DARKGRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
AQUA = (0, 255, 255)
PURPLE = (128, 0, 128)
OLIVE = (128, 128, 0)
TEAL = (0, 128, 128)
GREEN = (0, 128, 0)
FUCHSIA = (255, 0, 255)

COLORS = []
COLORS.append(WHITE)
COLORS.append(BLACK)
COLORS.append(DARKGRAY)
COLORS.append(GRAY)
COLORS.append(SILVER)
COLORS.append(RED)
COLORS.append(MAROON)
COLORS.append(ORANGE)
COLORS.append(YELLOW)
COLORS.append(BLUE)
COLORS.append(NAVY)
COLORS.append(AQUA)
COLORS.append(OLIVE)
COLORS.append(TEAL)
COLORS.append(GREEN)
COLORS.append(LIME)
COLORS.append(FUCHSIA)
COLORS.append(PURPLE)


def get_font(size):
    return pygame.font.SysFont("arial", size)


FPS = 80

WIDTH, HEIGHT = 600, 760

ROWS = COLS = 40  # increase to have smaller pixels

TOOLBAR_HEIGHT = HEIGHT - WIDTH

RIGHT_TOOLBAR_WIDTH = 75

PIXEL_SIZE = WIDTH // COLS

DRAW_GRID_LINES = True

MOUSE_POSITION_TEXT_SIZE = 12

BRUSH_SIZE = 1  # can be 2, 3, 4 or any other value

STATE = "COLOR"

pygame_icon = pygame.image.load("assets/pyaint.png")
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("Pyaint")

WIN = pygame.display.set_mode((WIDTH + RIGHT_TOOLBAR_WIDTH, HEIGHT))


def get_font(size):
    return pygame.font.SysFont("arial", size)
