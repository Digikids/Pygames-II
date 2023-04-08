import pygame

# Initialize Pygame
pygame.init()

# Set up game window
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")

# Set up game objects
BALL_RADIUS = 50
BALL_COLOR = (255, 255, 255)
ball = pygame.draw.circle(WIN, BALL_COLOR, (WIDTH//2, HEIGHT//2), BALL_RADIUS)
ball_speed_x = 5
ball_speed_y = 5

# Set up game loop
FPS = 60
clock = pygame.time.Clock()
running = True
while running:
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game state
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collision with left or right wall
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1

    # Check for collision with top or bottom wall
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Draw ball on screen
    WIN.fill((0, 0, 0))
    ball = pygame.draw.circle(WIN, BALL_COLOR, (ball.x, ball.y), BALL_RADIUS)
    pygame.display.update()

    # Set the frame rate
    clock.tick(FPS)

# Quit Pygame when the game loop exits
pygame.quit()
