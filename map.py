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
    self._wall_count = 0

  def get_cell(self, x: int, y: int) -> Cell:
    return self._map[y][x]
  
  def _place_object(self, snake1: Snake, snake2: Snake, object_name: str, object_type: 
                    int, max_count: int, probability: float) -> None:
    if chance(probability):
      for _ in range(10): # Limit the number of attempts
        x, y = random_coords(Map.SIZE - 1)
        if self._map[y][x].value() == Cell.EMPTY and (x, y) not in snake1.body \
           and (x, y) not in snake2.body:
          self._map[y][x].set_value(object_type)
          count_attribute = getattr(self, f'_{object_name}_count')
          setattr(self, f'_{object_name}_count', count_attribute + 1)
          break

  def perform_spawns(self, first_snake: Snake, second_snake: Snake) -> None:
    spawns = [
      ("food", Cell.HAS_FOOD, MaxSpawn.FOOD, Probabilities.FOOD_SPAWN),
      ("big_food", Cell.HAS_BIG_FOOD, MaxSpawn.BIG_FOOD, Probabilities.BIG_FOOD_SPAWN),
      ("stop_food", Cell.HAS_STOP_FOOD, MaxSpawn.STOP_FOOD, Probabilities.STOP_FOOD_SPAWN),
      ("wall", Cell.HAS_WALL, 1, Probabilities.WALL_SPAWN)
    ]

    for spawn in spawns:
      self._place_object(first_snake, second_snake, *spawn)
