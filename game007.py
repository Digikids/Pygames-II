import pygame
import random

pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Rectangle")

# Create a function that returns a random color
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

# Set up the rectangle
rect_width = 40
rect_height = 40
rect_color = random_color()
rect_x = screen_width // 2 - rect_width // 2
rect_y = screen_height // 2 - rect_height // 2

# Set up the movement
move_step = 50

# Set up the score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Draw the rectangle on the screen
def draw_rect(x, y):
    pygame.draw.rect(screen, rect_color, pygame.Rect(x, y, rect_width, rect_height))
    score_surface = font.render("Score: " + str(score), False, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

r_c = random_color()
# Update the screen
def update_screen():
    screen.fill(r_c)
    draw_rect(rect_x, rect_y)
    pygame.display.update()

update_screen()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # Move the rectangle in response to arrow key presses
            if event.key == pygame.K_LEFT and rect_x > 0:
                rect_x -= move_step
                score += 1
            elif event.key == pygame.K_RIGHT and rect_x < screen_width - rect_width:
                rect_x += move_step
                score += 1
            elif event.key == pygame.K_UP and rect_y > 0:
                rect_y -= move_step
                score += 1
            elif event.key == pygame.K_DOWN and rect_y < screen_height - rect_height:
                rect_y += move_step
                score += 1
            update_screen()
