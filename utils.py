import pygame
from random import random, randint
from typing import Tuple

from cell import Cell
from snake import Snake
from consts import Directions, Colors, WindowSettings, Fonts

def chance(ch: float) -> bool:
  return random() <= ch

def random_coords(bound: int) -> Tuple[int, int]:
  return randint(0, bound), randint(0, bound)

def move_cell(cell: Tuple[int, int], direction: int) -> Tuple[int, int]:
  if direction == Directions.DOWN:
    return (cell[0], cell[1] + 1)
  elif direction == Directions.UP:
    return (cell[0], cell[1] - 1)
  elif direction == Directions.LEFT:
    return (cell[0] - 1, cell[1])
  elif direction == Directions.RIGHT:
    return (cell[0] + 1, cell[1])
  
def render(sc: pygame.Surface, first_player_snake: Snake, second_player_snake: Snake, map,
           number_of_players: int, first_wins: int, second_wins: int, map_size: int) -> bool:
  try:
    sc.fill(Colors.BLACK)

    cell_size = WindowSettings.SCREEN_SIZE / map_size

    for x in range(map_size):
      for y in range(map_size):
        if map.get_cell(x, y).value() == Cell.HAS_FOOD:
          pygame.draw.circle(sc, Colors.BLUE, (x * cell_size + cell_size / 2, y * cell_size + cell_size / 2), 4)
        elif map.get_cell(x, y).value() == Cell.HAS_BIG_FOOD:
          pygame.draw.circle(sc, Colors.YELLOW, (x * cell_size + cell_size / 2, y * cell_size + cell_size / 2), 5)
        elif map.get_cell(x, y).value() == Cell.HAS_STOP_FOOD:
          pygame.draw.circle(sc, Colors.PINK, (x * cell_size + cell_size / 2, y * cell_size + cell_size / 2), 5)
        elif map.get_cell(x, y).value() == Cell.HAS_WALL:
          pygame.draw.rect(sc, Colors.GREY, (x * cell_size, y * cell_size, cell_size, cell_size))

    for x, y in first_player_snake.body:
      pygame.draw.rect(sc, Colors.RED, (x * cell_size, y * cell_size, cell_size, cell_size))
    for x, y in second_player_snake.body:
      pygame.draw.rect(sc, Colors.GREEN, (x * cell_size, y * cell_size, cell_size, cell_size))

    pygame.draw.rect(sc, Colors.WHITE, (0, WindowSettings.SCREEN_SIZE, WindowSettings.SCREEN_SIZE, WindowSettings.BOTTOM_PANEL_SIZE))

    if number_of_players == 2:
      text1 = Fonts.REGULAR_FONT.render(str(second_wins), 1, Colors.RED)
      text2 = Fonts.REGULAR_FONT.render(":", 1, Colors.BLACK)
      text3 = Fonts.REGULAR_FONT.render(str(first_wins), 1, Colors.GREEN)
      text4 = Fonts.REGULAR_FONT.render(str(len(first_player_snake.body)), 1, Colors.RED)
      text5 = Fonts.REGULAR_FONT.render(str(len(second_player_snake.body)), 1, Colors.GREEN)

      sc.blit(text2, (250, 506))
      sc.blit(text3, (265, 508))
      sc.blit(text1, (245 - 16 * len(str(second_wins)), 508))
      sc.blit(text4, (20, 508))
      sc.blit(text5, (475 - 16 * len(str(len(first_player_snake.body))), 508))
    else:
      text = Fonts.REGULAR_FONT.render("SCORE: " + str(len(second_player_snake.body)), 1, Colors.GREEN)
      sc.blit(text, (220, 508))

    return True
  except pygame.error:
    return False