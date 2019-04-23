import pygame
import math
import random
import time

pygame.init()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# Set up the screen [width, height]
length = 700
width = 400
size = (length, width)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

 
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()








    

# --- game loop ---
while not done:
    # --- Events loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- scene logic ---

    # --- repaints screen ---
    screen.fill(WHITE)
 
    # --- new drawings ---


    # Updates screen with new drawings
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

