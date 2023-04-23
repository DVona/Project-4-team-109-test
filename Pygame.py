import pygame, sys
import sudoku_generator

#  pygame template

pygame.init()
pygame.display.set_caption("Sudoku")


def draw_lines():
    # draw horizontal lines
    for i in range(1, 9):
        if i == 3 or i == 6:
            length = 5
        else:
            length = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * 70), (630, i * 70), length)

    # draw vertical lines
    for i in range(1, 9):
        if i == 3 or i == 6:
            length = 5
        else:
            length = 1
        pygame.draw.line(screen, (0, 0, 0), (i * 70, 0), (i * 70, 630), length)


screen = pygame.display.set_mode((630, 630))
# change background color if we want
screen.fill((255, 255, 245))
draw_lines()
while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()