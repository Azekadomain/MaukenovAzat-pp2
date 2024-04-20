import pygame
from base import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 500))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = white
    last_pos = None

    screen.fill(white)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                # buttons for various modes:
                if event.key == pygame.K_r:
                    mode = red
                elif event.key == pygame.K_g:
                    mode = green
                elif event.key == pygame.K_b:
                    mode = blue
                elif event.key == pygame.K_y:
                    mode = yellow
                elif event.key == pygame.K_BACKSPACE:
                    mode = white
                elif event.key == pygame.K_x:
                    drawRectangle(screen, pygame.mouse.get_pos(), 200, 100, mode)
                elif event.key == pygame.K_w:
                    draw_square(screen, pygame.mouse.get_pos(), 100, mode)
                elif event.key == pygame.K_c:
                    draw_circle(screen, pygame.mouse.get_pos(), 100, mode)
                elif event.key == pygame.K_s:
                    draw_right_triangle(screen, pygame.mouse.get_pos(), 100, 150, mode)
                elif event.key == pygame.K_t:
                    draw_equilateral_triangle(screen, pygame.mouse.get_pos(), 100, mode)
                elif event.key == pygame.K_p:
                    draw_rhombus(screen, pygame.mouse.get_pos(), 100, 150, mode)
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                last_pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION and event.buttons[0]:
                if last_pos is not None:
                    start_pos = last_pos
                    end_pos = pygame.mouse.get_pos()
                    draw_line_between(screen, start_pos, end_pos, radius, mode)
                    last_pos = end_pos
        
        pygame.display.flip()
        clock.tick(60)

def draw_line_between(screen, start, end, width, color_mode):
    color = color_mode
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

def draw_square(screen, mouse_pos, side_length, color):
    x = mouse_pos[0] - side_length / 2
    y = mouse_pos[1] - side_length / 2
    rect = pygame.Rect(x, y, side_length, side_length)
    pygame.draw.rect(screen, color, rect, 3)

def draw_circle(screen, mouse_pos, radius, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), radius, 3)

def draw_right_triangle(screen, mouse_pos, base, height, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    points = [(x, y), (x + base, y), (x, y - height), (x, y)]
    pygame.draw.polygon(screen, color, points, 3)

def draw_equilateral_triangle(screen, mouse_pos, side_length, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    height = side_length * (3 ** 0.5) / 2
    points = [(x, y), (x + side_length / 2, y - height), (x - side_length / 2, y - height), (x, y)]
    pygame.draw.polygon(screen, color, points, 3)

def draw_rhombus(screen, mouse_pos, width, height, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    points = [(x, y), (x + width / 2, y - height / 2), (x + width, y), (x + width / 2, y + height / 2), (x, y)]
    pygame.draw.polygon(screen, color, points, 3)

main()
