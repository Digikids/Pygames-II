import pygame
import random

pygame.init

# set up the display
dim = (800, 600)
screen = pygame.display.set_mode(dim)
pygame.display.set_caption("Ping Pong")

# Create a function that returns a random color


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return(red, green, blue)


# set up the circle
radius = 40
circle_color = random_color()
circle_x = dim[0] // 2
circle_y = dim[1] // 2
circle_x_speed = 0.5
circle_y_speed = 0.5

# draw the circle on the screen


def draw_circle():
   pygame.draw.circle(screen, circle_color, (circle_x, circle_y), radius)


# update the screen
r_c = random_color


def update_screen():
   screen.fill(r_c)
   draw_circle()
   pygame.display.update()


update_screen()

# main game loop
while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()

        # move the circle
   circle_x += circle_x_speed
   circle_y += circle_y_speed

   if circle_x > dim[0] - radius:
      circle_x_speed = circle_x_speed * -1
      circle_color = random_color()

   if circle_x < 0:
      circle_x_speed = circle_x_speed * -1
      circle_color = random_color()

   if circle_y > dim[1] - radius:
      circle_y_speed = circle_y_speed * -1
      circle_color = random_color()

   if circle_y < 0:
      rectangle_y_speed = circle_y_speed * -1
      rectangle_color = random_color()

      update_screen()
