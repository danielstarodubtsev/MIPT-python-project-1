import pygame

pygame.font.init()

class Colors:
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 0, 255)
  YELLOW = (255, 255, 0)
  PINK = (255, 192, 203)
  GREY = (150, 150, 150)
  WHITE = (255, 255, 255)

class Fonts:
  SMALL_FONT = pygame.font.Font(None, 35)
  REGULAR_FONT = pygame.font.Font(None, 40)
  LARGE_FONT = pygame.font.Font(None, 100)

class WindowSettings:
  SCREEN_SIZE = 500
  BOTTOM_PANEL_SIZE = 40
  FIRST_BUTTON_MIN_X = 20
  FIRST_BUTTON_MAX_X = 130
  SECOND_BUTTON_MIN_X = 170
  SECOND_BUTTON_MAX_X = 280
  BUTTON_MIN_Y = 20
  BUTTON_MAX_Y = 80

class Probabilities:
  WALL_SPAWN = 1 / 50
  FOOD_SPAWN = 1 / 30
  BIG_FOOD_SPAWN = 1 / 600
  STOP_FOOD_SPAWN = 1 / 300

class MaxSpawn:
  FOOD = 70
  BIG_FOOD = 6
  STOP_FOOD = 10

class Directions:
  UP = 1
  DOWN = 3
  LEFT = 2
  RIGHT = 4

class Values:
  BIG_FOOD_VALUE = 10
  STOP_FOOD_VALUE = 40
