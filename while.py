import pygame
import random

pygame.init()

# set up the display
dim = (800, 600)
screen = pygame.display.set_mode(dim)
pygame.display.set_caption("Ping Pong")

# Create a function that returns a random color


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)


# set up the rectangle
rect_width = 50
rect_height = 50
rect_color = random_color()
rect_x = dim[0] // 2
rect_y = dim[1] // 2
rect_x_speed = 0.5
rect_y_speed = 0.5
radius = 40

# draw the rectangle on the screen


def draw_rect():
    pygame.draw.rect(screen, rect_color,
                     (rect_x, rect_y, rect_width, rect_height), radius)


# update the screen
r_c = random_color()


def update_screen():
    screen.fill(r_c)
    draw_rect()
    pygame.display.update()


update_screen()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # move the rectangle
    rect_x += rect_x_speed
    rect_y += rect_y_speed

    if rect_x > dim[0]:
        rect_x_speed = rect_x_speed * -1
        rect_color = random_color()

    if rect_x < 0:
        rect_x_speed = rect_x_speed * -1
        rect_color = random_color()

    if rect_y > dim[1]:
        rect_y_speed = rect_y_speed * -1
        rect_color = random_color()

    if rect_y < 0:
        rect_y_speed = rect_y_speed * -1
        rect_color = random_color()

    update_screen()
