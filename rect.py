import pygame
import random

pygame.init()

# setup the display
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
rectangle_width = 80
rectangle_height = 60
rectangle_color = random_color()
rectangle_x = dim[0] // 2 - rectangle_width // 2
rectangle_y = dim[1] // 2 - rectangle_height // 2
rectangle_x_speed = 0.5
rectangle_y_speed = 0.5
radius = 300

# draw the rectangle on the screen


def draw_rectangle():
    pygame.draw.rect(screen, rectangle_color, pygame.Rect(
        rectangle_x, rectangle_y, rectangle_width, rectangle_height), radius)


# update the screen
r_c = random_color()


def update_screen():
    screen.fill(r_c)
    draw_rectangle()
    pygame.display.update()
update_screen()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # move the rectangle
    rectangle_x += rectangle_x_speed
    rectangle_y += rectangle_y_speed

    if rectangle_x > dim[0] - rectangle_width or rectangle_x < 0:
        rectangle_x_speed = rectangle_x_speed * -1
        rectangle_color = random_color()

    if rectangle_y > dim[1] - rectangle_height or rectangle_y < 0:
        rectangle_y_speed = rectangle_y_speed * -1
        rectangle_color = random_color()

    update_screen()
