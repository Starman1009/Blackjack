import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake
snake_block = 20
snake_speed = 15
snake_list = []
snake_length = 1

# Initial position of the snake
snake_x = width // 2
snake_y = height // 2
snake_dx = 0
snake_dy = 0

# Set up the food
food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], snake_block, snake_block])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx == 0:
                snake_dx = -snake_block
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx == 0:
                snake_dx = snake_block
                snake_dy = 0
            elif event.key == pygame.K_UP and snake_dy == 0:
                snake_dx = 0
                snake_dy = -snake_block
            elif event.key == pygame.K_DOWN and snake_dy == 0:
                snake_dx = 0
                snake_dy = snake_block

    # Update the position of the snake
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with boundaries
    if snake_x >= width or snake_x < 0 or snake_y >= height or snake_y < 0:
        pygame.quit()
        sys.exit()

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
        snake_length += 1

    # Update the snake's body
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for collision with itself
    for x in snake_list[:-1]:
        if x == snake_head:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(BLACK)

    # Draw the food
    pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

    # Draw the snake
    draw_snake(snake_block, snake_list)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(snake_speed)