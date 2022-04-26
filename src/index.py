import pygame
from speedtyping import SpeedTyping
from start import Start


def main():
    pygame.init()
    display = pygame.display.set_mode((750, 500))
    pygame.display.set_caption("Speed Typing Test")
    screen = SpeedTyping()

    gameloop = Start(screen, display)
    gameloop.start()


if __name__ == "__main__":
    main()
