from cell import Cell
from consts import Probabilities, MaxSpawn
from snake import Snake
from utils import chance, random_coords

class Map:
  SIZE = 50

  def __init__(self, size: int = SIZE) -> None:
    self._size = size
    self._map = [[Cell() for _ in range(size)] for _ in range(size)]

    self._food_count = 0
    self._big_food_count = 0
    self._stop_food_count = 0

  def get_cell(self, x: int, y: int) -> Cell:
    return self._map[y][x]
  
  def perform_spawns(self, first_snake: Snake, second_snake: Snake) -> None:
    if chance(Probabilities.FOOD_SPAWN) and self._food_count < MaxSpawn.FOOD:
      while True:
        x, y = random_coords(Map.SIZE - 1)
        if self._map[y][x].value() == Cell.EMPTY and (x, y) not in first_snake.body and (x, y) not in second_snake.body:
          self._map[y][x].set_value(Cell.HAS_FOOD)
          self._food_count += 1
          break

    if chance(Probabilities.BIG_FOOD_SPAWN) and self._big_food_count < MaxSpawn.BIG_FOOD:
      while True:
        x, y = random_coords(Map.SIZE - 1)
        if self._map[y][x].value() == Cell.EMPTY and (x, y) not in first_snake.body and (x, y) not in second_snake.body:
          self._map[y][x].set_value(Cell.HAS_BIG_FOOD)
          self._big_food_count += 1
          break

    if chance(Probabilities.STOP_FOOD_SPAWN) and self._stop_food_count < MaxSpawn.STOP_FOOD:
      while True:
        x, y = random_coords(Map.SIZE - 1)
        if self._map[y][x].value() == Cell.EMPTY and (x, y) not in first_snake.body and (x, y) not in second_snake.body:
          self._map[y][x].set_value(Cell.HAS_STOP_FOOD)
          self._stop_food_count += 1
          break

    if chance(Probabilities.WALL_SPAWN):
      while True:
        x, y = random_coords(Map.SIZE - 1)
        if self._map[y][x].value() == Cell.EMPTY and (x, y) not in first_snake.body and (x, y) not in second_snake.body:
          self._map[y][x].set_value(Cell.HAS_WALL)
          break