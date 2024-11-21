import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (200, 100, 0)
# Set up the clock
clock = pygame.time.Clock()

# Initial position of the rectangle
rect_x, rect_y = 100, 100
rect_width, rect_height = 50, 50
rect_speed = 5
green = (0, 200, 10)
# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    # Update the position of the rectangle based on arrow key inputs
    if keys[pygame.K_LEFT] and rect_x - rect_speed >= 0:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT] and rect_x + rect_width + rect_speed <= width:
        rect_x += rect_speed
    if keys[pygame.K_UP] and rect_y - rect_speed >= 0:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_y + rect_height + rect_speed <= height:
        rect_y += rect_speed

    # Clear the screen
    screen.fill(BLACK)

    # Draw the white rectangle
    pygame.draw.rect(screen, ORANGE, (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect()
    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)