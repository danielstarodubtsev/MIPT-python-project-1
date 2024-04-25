import pygame
from consts import Colors, Fonts, WindowSettings
from game import Game

def main():
  menu_screen = pygame.display.set_mode((300, 100))
  pygame.init()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if WindowSettings.BUTTON_MIN_Y <= event.pos[1] <= WindowSettings.BUTTON_MAX_Y:
          if WindowSettings.FIRST_BUTTON_MIN_X <= event.pos[0] <= WindowSettings.FIRST_BUTTON_MAX_X:
            Game.run(1)
          elif WindowSettings.SECOND_BUTTON_MIN_X <= event.pos[0] <= WindowSettings.SECOND_BUTTON_MAX_X:
            Game.run(2)
    
    try:
      menu_screen.fill(Colors.WHITE)
    except:
      break

    pygame.draw.rect(menu_screen, Colors.BLACK, 
                     (WindowSettings.FIRST_BUTTON_MIN_X, WindowSettings.BUTTON_MIN_Y,
                      WindowSettings.FIRST_BUTTON_MAX_X - WindowSettings.FIRST_BUTTON_MIN_X,
                      WindowSettings.BUTTON_MAX_Y - WindowSettings.BUTTON_MIN_Y), 4)
    pygame.draw.rect(menu_screen, Colors.BLACK, 
                     (WindowSettings.SECOND_BUTTON_MIN_X, WindowSettings.BUTTON_MIN_Y,
                      WindowSettings.SECOND_BUTTON_MAX_X - WindowSettings.SECOND_BUTTON_MIN_X,
                      WindowSettings.BUTTON_MAX_Y - WindowSettings.BUTTON_MIN_Y), 4)
    text = Fonts.SMALL_FONT.render("1 Player        2 Player", 1, Colors.RED)
    menu_screen.blit(text, (30, 40))

    pygame.display.update()
    pygame.time.delay(50)

if __name__ == "__main__":
  main()
