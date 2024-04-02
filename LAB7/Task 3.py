import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

x, y = WIDTH // 2, HEIGHT // 2
speed = 20

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y = max(y - speed, 0)
    if keys[pygame.K_DOWN]:
        y = min(y + speed, HEIGHT - 50)
    if keys[pygame.K_LEFT]:
        x = max(x - speed, 0)
    if keys[pygame.K_RIGHT]:
        x = min(x + speed, WIDTH - 50)

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (x, y), 25)

    pygame.display.flip()
pygame.quit()
sys.exit()
