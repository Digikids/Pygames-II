import pygame
import random

pygame.init()

# Set up the display
dim = (800, 600)
screen = pygame.display.set_mode(dim)
pygame.display.set_caption("Moving Rectangle")

# Create a function that returns a random color
def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

# set up the rectangle
rect_width = 40
rect_height = 40
rect_color = random_color()
rect_x = dim[0] // 2
rect_y = dim[1] // 2

# set up the movement
move_step = 50
# set up the score
score = 0
font = pygame.font.SysFont("Arial", 30)

# draw the rectangle on the screen
def draw_rectangle(x, y):
    pygame.draw.rect(screen, rect_color, (x, y, rect_width, rect_height))
    score_surface = font.render("Score: " + str(score), False, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

r_c = random_color()

# update the screen
def update_screen():
    screen.fill(r_c)
    draw_rectangle(rect_x, rect_y)
    pygame.display.update()
    
update_screen()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # move the rectangle in response to arrow key presses
            if event.key == pygame.K_LEFT:
                if rect_x > 0 + rect_width:
                    rect_x -= move_step
                    score += 1
            elif event.key == pygame.K_RIGHT:
                if rect_x < dim[0] - rect_width:
                    rect_x += move_step
                    score += 1
            elif event.key == pygame.K_UP:
                if rect_y > 0 + rect_height:
                    rect_y -= move_step
                    score += 1
            elif event.key == pygame.K_DOWN:
                if rect_y < dim[1] - rect_height:
                    rect_y += move_step
                    score += 1
    update_screen()
