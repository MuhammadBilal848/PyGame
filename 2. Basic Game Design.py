# The goal of the game is to avoid incoming obstacles:
    # The player starts on the left side of the screen.
    # The obstacles enter randomly from the right and move left in a straight line.
# The player can move left, right, up, or down to avoid the obstacles.
# The player cannot move off the screen.
# The game ends either when the player is hit by an obstacle or when the user closes the window.

# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode([500, 500])

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            print('KEYDOWN PRESSED')
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
    
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            print('QUIT PRESSED')
            running = False
    
    screen.fill((255, 255, 255))

    # Create a surface and pass in a tuple containing its length and width
    surf = pygame.Surface((50, 50))

    # Give the surface a color to separate it from the background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()
    
    pygame.display.flip()
            
pygame.quit()