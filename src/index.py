import pygame
from speedtyping import SpeedTyping

def main():
    pygame.init()
    display = pygame.display.set_mode((750, 500))
    pygame.display.set_caption("Speed Typing Test")
    screen = SpeedTyping()
    sentence = screen.get_sentence()
    font = pygame.font.SysFont("Times New Roman", 24)
    text = font.render(sentence, True, (255,255,255))

    display.fill((0,0,0))
    display.blit(text, (300, 250))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

if __name__ == "__main__":
    main()