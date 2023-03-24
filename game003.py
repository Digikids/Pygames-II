import pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rectangles in Pygame")

# Set up the background color
screen.fill((200, 120, 255))

# Set up the rectangle
rect_width = 200
rect_height = 100
rect_x = (screen_width / 2)
rect_y = (screen_height / 2)
rect_color = (0, 0, 0)

# Draw the rectangle on the screen
pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

# Update the screen
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
