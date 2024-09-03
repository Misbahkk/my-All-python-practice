import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SIZE = 30
BALL_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Run Game")

# Create the ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT -
                   BALL_SIZE, BALL_SIZE, BALL_SIZE)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball.x -= BALL_SPEED
    if keys[pygame.K_RIGHT]:
        ball.x += BALL_SPEED

    # Keep the ball within the screen bounds
    ball.x = max(0, min(ball.x, WIDTH - BALL_SIZE))

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball
    pygame.draw.ellipse(screen, BLUE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
