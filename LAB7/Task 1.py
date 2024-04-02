import pygame
import sys
import math
from datetime import datetime

pygame.init()

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 1300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mickey = pygame.image.load('mainclock.png')
mickey_rect = mickey.get_rect()
mickey_center = (mickey_rect.centerx, mickey_rect.centery)

minute_hand = pygame.image.load('rightarm.png')
minute_hand_rect = minute_hand.get_rect()

second_hand = pygame.image.load('leftarm.png')
second_hand_rect = second_hand.get_rect()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mickey Clock')

def rotate(image, angle, pivot):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    return rotated_image, rotated_rect

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    current_time = datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    minute_angle = (minute / 60) * 360 + 90
    second_angle = (second / 60) * 360 + 90

    rotated_minute_hand, minute_hand_rect = rotate(minute_hand, minute_angle, mickey_center)
    rotated_second_hand, second_hand_rect = rotate(second_hand, second_angle, mickey_center)

    screen.blit(mickey, mickey_rect)
    screen.blit(rotated_minute_hand, minute_hand_rect)
    screen.blit(rotated_second_hand, second_hand_rect)
 
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()