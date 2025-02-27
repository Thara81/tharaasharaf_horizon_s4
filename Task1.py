import pygame
import random
import time
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circles")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

circles = []
path_length = 0

font = pygame.font.Font(None, 30)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def save_drawing():
    pygame.image.save(win, "Circles.png")

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Task A
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_time = time.time()

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                end_time = time.time()
                duration = min(end_time - start_time, 2)
                radius = max(5, int(duration * 50))
                x, y = pygame.mouse.get_pos()
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                circles.append((x, y, radius, color))

    win.fill(WHITE)

    # Task B
    for x, y, r, color in circles:
        pygame.draw.circle(win, color, (x, y), r)

    path_length = 0
    if len(circles) > 1:
        for i in range(len(circles) - 1):
            pygame.draw.line(win, BLACK, (circles[i][0], circles[i][1]), (circles[i + 1][0], circles[i + 1][1]), 2)
            path_length += distance((circles[i][0], circles[i][1]), (circles[i + 1][0], circles[i + 1][1]))

    text_surface = font.render(f"Path Length: {float(path_length)} px", True, BLACK)
    win.blit(text_surface, (10, 10))

    # Task C
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and circles:
                circles.pop()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                circles.clear()
            elif event.key == pygame.K_s:
                save_drawing()

    pygame.display.update()

pygame.quit()

