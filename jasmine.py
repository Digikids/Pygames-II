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


# Set up the rectangle
rect_radius = 50
rect_color = random_color()
rect_x = screen_width // 2
rect_y = screen_height // 2

# Set up the movement
move_step = 50

# Set up the score
score = 0
font = pygame.font.SysFont("Arial", 30)

# Draw the rect on the screen


def draw_rect(x, y):
    pygame.draw.rect(screen, rect_color, (x, y), rect_radius)
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
            # Move the rect in response to arrow key presses
            if event.key == pygame.K_LEFT:
                if rect_x > 0 + rect_radius:
                    rect_x -= move_step
                    score += 1
            elif event.key == pygame.K_RIGHT:
                if rect_x < screen_width - rect_radius:
                    rect_x += move_step
                    score += 1
            elif event.key == pygame.K_UP:
                if rect_y > 0 + rect_radius:
                    rect_y -= move_step
                    score += 1
            elif event.key == pygame.K_DOWN:
                if rect_y < screen_height - rect_radius:
                    rect_y += move_step
                    score += 1

             # Check if the rect has touched the left edge of the screen
            if rect_x <= 0 + rect_radius:
                score = 0
            # Check if the rect has touched the right edge of the screen
            if rect_x >= screen_width - rect_radius:
                score = 0
            # Check if the rect has touched the top edge of the screen
            if rect_y <= 0 + rect_radius:
                score = 0
            # Check if the rect has touched the bottom edge of the screen
            if rect_y >= screen_height - rect_radius:
                score = 0

            update_screen()
