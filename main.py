import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Objects")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 255)
MAGENTA = (255, 0, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
CYAN= (0, 255, 255)
ORANGE = (255, 128, 0)


display_surface.fill(WHITE)

CENTER = (300, 300)
RADIUS = 100
pygame.draw.circle(display_surface, RED, CENTER, RADIUS)

START = (100, 100)
END = (500, 500)
pygame.draw.line(display_surface, BLACK, START, END, 23)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()