import pygame
from surfaces.start import Start


def main():
    """Pelin aloittava funktio, joka alustaa pygamen ja aloittaa Start-luokan start-funktion.
    """
    pygame.init()
    display = pygame.display.set_mode((750, 500))
    pygame.display.set_caption("Speed Typing Test")

    gameloop = Start(display)
    gameloop.start()


if __name__ == "__main__":
    main()
