import pygame
import random
import time

from cell import Cell
from consts import Colors, WindowSettings, Fonts, Directions, Values
from map import Map
from snake import Snake

from utils import move_cell, render

def has_lost(snake_to_check: Snake, other_snake: Snake, map: Map) -> bool:
  return not 0 <= snake_to_check.body[-1][0] < map.SIZE or \
         not 0 <= snake_to_check.body[-1][1] < map.SIZE or \
         snake_to_check.body[-1] in other_snake.body or \
         snake_to_check.body.count(snake_to_check.body[-1]) > 1 or \
         map.get_cell(*snake_to_check.body[-1]).value() == Cell.HAS_WALL

def check_snake_head(snake: Snake, map: Map) -> None:
  if map.get_cell(*snake.body[-1]).value() == Cell.HAS_FOOD:
    snake.increase_grow(1)
  elif map.get_cell(*snake.body[-1]).value() == Cell.HAS_BIG_FOOD:
    snake.increase_grow(Values.BIG_FOOD_VALUE)
  elif map.get_cell(*snake.body[-1]).value() == Cell.HAS_STOP_FOOD:
    snake.increase_stop(Values.STOP_FOOD_VALUE)
    snake.increase_grow(1)

  map.get_cell(*snake.body[-1]).set_value(Cell.EMPTY)

def handle_key_event(key: pygame.key, snake1: Snake, snake2: Snake) -> bool:
    directions1 = {pygame.K_w: Directions.UP, pygame.K_s: Directions.DOWN,
                   pygame.K_a: Directions.LEFT, pygame.K_d: Directions.RIGHT}
    directions2 = {pygame.K_UP: Directions.UP, pygame.K_DOWN: Directions.DOWN,
                   pygame.K_LEFT: Directions.LEFT, pygame.K_RIGHT: Directions.RIGHT}

    if key in directions1:
        snake1.change_direction(directions1[key])
    elif key in directions2:
        snake2.change_direction(directions2[key])

class Game:
  def run(number_of_players: int) -> None:
    pygame.init()
    sc = pygame.display.set_mode((WindowSettings.SCREEN_SIZE, 
                                  WindowSettings.SCREEN_SIZE + WindowSettings.BOTTOM_PANEL_SIZE))

    pygame.display.set_caption("Two player snake game")

    first_wins = 0
    second_wins = 0
    game_paused = False

    while True:
      if number_of_players == 2:
        x = random.randint(0, Map.SIZE - 1)
        player_one_snake = Snake([(x, 0), (x, 1), (x, 2), (x, 3), (x, 4)])
      else:
        player_one_snake = Snake([(-1, -1)], stop_factor=1e9)
      
      x = random.randint(0, Map.SIZE - 1)
      player_two_snake = Snake([(x, Map.SIZE - 1), (x, Map.SIZE - 2), (x, Map.SIZE - 3), 
                                (x, Map.SIZE - 4), (x, Map.SIZE - 5)],
                                Directions.UP)
      
      lost_players = []
      map = Map()

      while True:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()

          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              game_paused = not game_paused
            elif not game_paused:
              handle_key_event(event.key, player_one_snake, player_two_snake)

        if game_paused:
          continue

        map.perform_spawns(player_one_snake, player_two_snake)

        if not player_one_snake.is_stopped():
          player_one_snake.body.append(move_cell(player_one_snake.body[-1], 
                                                player_one_snake.direction()))
        else:
          player_one_snake.reduce_stop()

        if not player_two_snake.is_stopped():
          player_two_snake.body.append(move_cell(player_two_snake.body[-1], 
                                                player_two_snake.direction()))
        else:
          player_two_snake.reduce_stop()

        if not player_one_snake.is_stopped():
          if player_one_snake.is_growing():
            player_one_snake.reduce_grow()
          else:
            player_one_snake.pop_tail()

        if not player_two_snake.is_stopped():
          if player_two_snake.is_growing():
            player_two_snake.reduce_grow()
          else:
            player_two_snake.pop_tail()

        if has_lost(player_one_snake, player_two_snake, map):
          lost_players.append(1)

        if has_lost(player_two_snake, player_one_snake, map):
          lost_players.append(2)

        if lost_players and not (number_of_players == 1 and 2 not in lost_players):
          if number_of_players == 1:
            text = Fonts.LARGE_FONT.render("TOTAL: " + str(len(player_two_snake.body)), 1, Colors.YELLOW)
            sc.blit(text, (100, 220))
            pygame.display.update()

          time.sleep(1.5)
          pygame.event.clear()
          break

        check_snake_head(player_one_snake, map)
        check_snake_head(player_two_snake, map)

        if not render(sc, player_one_snake, player_two_snake, map, number_of_players, 
                      first_wins, second_wins, Map.SIZE):
          break

        if len(lost_players) and not (number_of_players == 1 and 2 not in lost_players):
          if number_of_players == 1:
            text = Fonts.LARGE_FONT.render("TOTAL: " + str(len(player_two_snake.body)), 1, Colors.YELLOW)
            sc.blit(text, (100, 220))
            pygame.display.update()

          time.sleep(1.5)
          pygame.event.clear()
          break

        pygame.display.update()
        pygame.time.delay(50)

      if len(lost_players) == 2:
        continue
      elif 1 in lost_players:
        first_wins += 1
      else:
        second_wins += 1
