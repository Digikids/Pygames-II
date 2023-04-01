import pygame
import random
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Circle")

# Create a function that returns a random color
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


# Set up the circle
circle_radius = 50
circle_color = random_color()
circle_x = screen_width // 2
circle_y = screen_height // 2

# Set up the movement
move_step = 50

# Set up the score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Draw the circle on the screen
def draw_circle(x, y):
    pygame.draw.circle(screen, random_color(), (x, y), circle_radius)
    score_surface = font.render("Score: " + str(score), False, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

r_c = random_color()
# Update the screen

def update_screen():
    screen.fill(r_c)
    draw_circle(circle_x, circle_y)
    pygame.display.update()

update_screen()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # Move the circle in response to arrow key presses
            if event.key == pygame.K_LEFT:
                if circle_x > 0 + circle_radius:
                    circle_x -= move_step
                    score += 1
            elif event.key == pygame.K_RIGHT:
                if circle_x < screen_width - circle_radius:
                    circle_x += move_step
                    score += 1
            elif event.key == pygame.K_UP:
                if circle_y > 0 + circle_radius:
                    circle_y -= move_step
                    score += 1
            elif event.key == pygame.K_DOWN:
                if circle_y < screen_height - circle_radius:
                    circle_y += move_step
                    score += 1

             # Check if the circle has touched the left edge of the screen
            if circle_x <= 0 + circle_radius:
                score = 0
            # Check if the circle has touched the right edge of the screen
            if circle_x >= screen_width - circle_radius:
                score = 0
            # Check if the circle has touched the top edge of the screen
            if circle_y <= 0 + circle_radius:
                score = 0
            # Check if the circle has touched the bottom edge of the screen
            if circle_y >= screen_height - circle_radius:
                score = 0

            update_screen()
