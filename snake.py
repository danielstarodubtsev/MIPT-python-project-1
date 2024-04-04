from consts import Directions

class Snake:
  def __init__(self, body: list[(int, int)] = [], direction: int = Directions.DOWN, stop_factor = 0) -> None:
    self.body = body
    self._direction = direction
    self._stop_factor = stop_factor
    self._grow_factor = 0

  def change_direction(self, new_direction: int) -> None:
    if new_direction % 2 != self._direction % 2:
      self._direction = new_direction

  def is_stopped(self) -> bool:
    return self._stop_factor > 0
  
  def is_growing(self) -> bool:
    return self._grow_factor > 0

  def direction(self) -> int:
    return self._direction
  
  def pop_tail(self) -> None:
    self.body.pop(0)

  def reduce_stop(self) -> None:
    self._stop_factor -= 1
  
  def reduce_grow(self) -> None:
    self._grow_factor -= 1

  def increase_stop(self, delta: int) -> None:
    self._stop_factor += delta

  def increase_grow(self, delta: int) -> None:
    self._grow_factor += delta