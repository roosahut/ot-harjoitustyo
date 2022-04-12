import pygame
import time
from speedtyping import SpeedTyping

def main():
    pygame.init()
    display = pygame.display.set_mode((750, 500))
    pygame.display.set_caption("Speed Typing Test")
    screen = SpeedTyping()
    blue = (0, 0, 255)

    end = False
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if end == True:
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if x >= 325 and x <= 425 and y >= 385 and y <= 485:
                        screen.reset()
                        end = False
            elif event.type == pygame.KEYDOWN:
                if not end:
                    if event.key == pygame.K_RETURN:
                        screen.end_time = time.time()
                        if len(screen.input) == 0:
                            screen.words = 1
                        else:
                            for i in screen.input:
                                if i == ' ':
                                    screen.words += 1
                        end = True
                    elif event.key == pygame.K_BACKSPACE:
                        screen.input = screen.input[:-1]
                    else:
                        if screen.input == '':
                            screen.start_time = time.time()
                        screen.input += event.unicode
            display.fill(0)
            sentence_input, xy_sentence = screen.center_text(screen.sentence, 200)
            display.blit(sentence_input, xy_sentence)
            text_input, xy_text = screen.center_text(screen.input, 300)
            display.blit(text_input, xy_text)
            if end == False:
                start_text, xy_start = screen.center_text("Start typing!", 250)
                display.blit(start_text, xy_start)
            if end == True:
                pygame.draw.rect(display, blue, pygame.Rect(325, 385, 100, 100))
                playagain_text, xy_playagain = screen.center_text("Click reset to play again", 250)
                display.blit(playagain_text, xy_playagain)
                reset, xy_reset = screen.center_text("Reset", 435)
                display.blit(reset, xy_reset)
                result = screen.results()
                text_result, xy_result = screen.center_text(result, 350)
                display.blit(text_result, xy_result)
            pygame.display.flip()

if __name__ == "__main__":
    main()