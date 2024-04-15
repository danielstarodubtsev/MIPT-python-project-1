import pygame
from consts import Colors, Fonts
from game import Game

def main():
  menu_screen = pygame.display.set_mode((300, 100))
  pygame.init()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if 20 <= event.pos[1] <= 80:
          if 20 <= event.pos[0] <= 130:
            Game.run(1)
          elif 170 <= event.pos[0] <= 280:
            Game.run(2)
    
    try:
      menu_screen.fill(Colors.WHITE)
    except:
      break

    pygame.draw.rect(menu_screen, Colors.BLACK, (20, 20, 110, 60), 4)
    pygame.draw.rect(menu_screen, Colors.BLACK, (170, 20, 110, 60), 4)
    text = Fonts.SMALL_FONT.render("1 Player        2 Player", 1, Colors.RED)
    menu_screen.blit(text, (30, 40))

    pygame.display.update()
    pygame.time.delay(50)

if __name__ == "__main__":
  main()