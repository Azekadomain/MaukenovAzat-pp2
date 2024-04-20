import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
GRID_SIZE = 16
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
GRID_COLOR = (0, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
SCORE_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
WALL_COLOR = (0, 0, 255)

font = pygame.font.SysFont(None, 30)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = SNAKE_COLOR

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WIDTH), (cur[1] + (y * GRID_SIZE)) % HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((WIDTH // 2), (HEIGHT // 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for i in self.positions:
            i = pygame.Rect((i[0], i[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, i)
            pygame.draw.rect(surface, GRID_COLOR, i, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

    def check_collision_with_wall(self, wall_positions):
        return self.get_head_position() in wall_positions


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = FOOD_COLOR
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, GRID_COLOR, r, 1)


class Wall:
    def __init__(self):
        self.positions = [
            (0, 0), (GRID_SIZE, 0), (2 * GRID_SIZE, 0), (3 * GRID_SIZE, 0), (4 * GRID_SIZE, 0), (5 * GRID_SIZE, 0), (6 * GRID_SIZE, 0),
            (WIDTH - GRID_SIZE, 0), (WIDTH - 2 * GRID_SIZE, 0), (WIDTH - 3 * GRID_SIZE, 0), (WIDTH - 4 * GRID_SIZE, 0), (WIDTH - 5 * GRID_SIZE, 0), (WIDTH - 6 * GRID_SIZE, 0),
            (0, HEIGHT - GRID_SIZE), (GRID_SIZE, HEIGHT - GRID_SIZE), (2 * GRID_SIZE, HEIGHT - GRID_SIZE), 
            (3 * GRID_SIZE, HEIGHT - GRID_SIZE), (4 * GRID_SIZE, HEIGHT - GRID_SIZE), (5 * GRID_SIZE, HEIGHT - GRID_SIZE), (6 * GRID_SIZE, HEIGHT - GRID_SIZE),
            (WIDTH - GRID_SIZE, HEIGHT - GRID_SIZE), 
            (WIDTH - 2 * GRID_SIZE, HEIGHT - GRID_SIZE), (WIDTH - 3 * GRID_SIZE, HEIGHT - GRID_SIZE), (WIDTH - 4 * GRID_SIZE, HEIGHT - GRID_SIZE), (WIDTH - 5 * GRID_SIZE, HEIGHT - GRID_SIZE), (WIDTH - 6 * GRID_SIZE, HEIGHT - GRID_SIZE)
        ]
        self.color = WALL_COLOR

    def draw(self, surface):
        for position in self.positions:
            r = pygame.Rect((position[0], position[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, GRID_COLOR, r, 1)


def draw_grid(surface):
    for y in range(0, HEIGHT, GRID_SIZE):
        for x in range(0, WIDTH, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, GRID_COLOR, rect, 1)


def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    wall = Wall()

    while True:
        screen.fill(BACKGROUND_COLOR)
        draw_grid(screen)
        snake.handle_keys()
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        snake.draw(screen)
        food.draw(screen)
        wall.draw(screen)

        if snake.check_collision_with_wall(wall.positions):
            snake.reset()

        score_text = font.render(f"Score: {snake.length - 1}", True, SCORE_COLOR)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
