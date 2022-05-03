import pygame
from start import Start


def main():
    pygame.init()
    display = pygame.display.set_mode((750, 500))
    pygame.display.set_caption("Speed Typing Test")

    gameloop = Start(display)
    gameloop.start()


if __name__ == "__main__":
    main()
