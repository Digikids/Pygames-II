import pygame  # imports the pygame library into the program. Is a must have line of code

pygame.init()  # initializes the pygame library. Is a must have line of code

# Set up the display
screen_width = 400  # sets the width of the screen in pixels
screen_height = 400  # sets the height of the screen in pixels
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Joy Ortega")

# Set up the background color
screen.fill((200, 120, 255))

# Set up the font
font = pygame.font.SysFont("Arial", 30)

# Create the text
text = font.render("Hello, There!", True, (255, 0, 0))

# Get the text dimensions
text_width, text_height = font.size("Hello, There!")

# Set the text position
text_x = screen_width / 2
text_y = screen_height / 2

# Draw the text on the screen
screen.blit(text, (text_x, text_y))

# Update the screen
pygame.display.update()

# Wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
