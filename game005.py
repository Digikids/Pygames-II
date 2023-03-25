import pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Circle")

# Set up the circle
circle_radius = 50
circle_color = (0, 255, 0)
circle_x = screen_width // 2
circle_y = screen_height // 2

# Set up the movement
move_step = 50

# Draw the circle on the screen
def draw_circle(x, y):
    pygame.draw.circle(screen, circle_color, (x, y), circle_radius)

# Update the screen
def update_screen():
    screen.fill((0, 0, 0))
    draw_circle(circle_x, circle_y)
    pygame.display.update()
update_screen()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Move the circle in response to arrow key presses
            if event.key == pygame.K_LEFT:
                circle_x -= move_step
            elif event.key == pygame.K_RIGHT:
                circle_x += move_step
            elif event.key == pygame.K_UP:
                circle_y -= move_step
            elif event.key == pygame.K_DOWN:
                if circle_y < screen_height - circle_radius:
                    circle_y += move_step
            update_screen()
