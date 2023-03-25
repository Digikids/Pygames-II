import pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shapes in Pygame")

# Set up the background color
screen.fill((20, 120, 255))

# Draw a circle
circle_color = (255, 0, 0)
circle_center = (screen_width // 2, screen_height // 2)
circle_radius = 50
pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

# Draw an ellipse
# ellipse_color = (0, 0, 255)
# ellipse_rect = (screen_width // 2 - 100, screen_height // 2 - 50, 200, 100)
# pygame.draw.ellipse(screen, ellipse_color, ellipse_rect)

# # Draw a polygon
polygon_color = (255, 0, 0)
polygon_points = [(100, 100), (150, 200), (250, 180), (200, 120)]
pygame.draw.polygon(screen, polygon_color, polygon_points)

# # Draw a line
line_color = (255, 255, 0)
line_start = (50, 50)
line_end = (200, 200)
line_width = 5
pygame.draw.line(screen, line_color, line_start, line_end, line_width)

# Update the screen
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
