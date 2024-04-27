class Cell:
  EMPTY = 0
  HAS_WALL = 1
  HAS_FOOD = 2
  HAS_BIG_FOOD = 3
  HAS_STOP_FOOD = 4

  def __init__(self, value: int = EMPTY) -> None:
    self._value = value

  def value(self) -> int:
    return self._value

  def set_value(self, value: int) -> None:
    self._value = value
