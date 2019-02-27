import pygame
import math
import random
import time
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
 
# Set the width and height of the screen [width, height]
length = 700
width = 400
size = (length, width)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pong")
 
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()




class Ball:
    x=0
    y=0
    vx=0
    vy=0
    radius=0
    def __init__(self, xP, yP, vxx,vyy, r):
        self.x = xP
        self.y = yP
        self.vx=vxx
        self.vy=vyy
        self.radius = r
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    def bounceV(self):
        self.vy = self.vy *-1
    def lose1(self):
        global scene, p1lose
        scene = 3
        p1lose = True
    def lose2(self):
        global scene
        scene = 3
        p2lose =True





#global variables (cause im too lazy to make a game class but thatd be more optimal)
speed = 1;
scene = 1;
p1lose = False p2lose = False
# main program
b = Ball(length/2,width/2,speed,speed,15)

# --- game scenes ---
#scene 1 (game start)
def doScene1():
    # space to start
    global scene
    print(-42)
    scene = 2


def doScene2():
    b.move()
    if(b.y-b.radius < 0+.1 or b.y+b.radius > width-.1):
        b.bounceV()
    if(b.x-b.radius < 0+.1) or b.x+b.radius > height-.1):
        b.bounceH()


def doScene3():
    global scene
#game over someone wins, space to start
    scene = 2


# main loop
while not done:
    # --- Main event loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic ---
    if(scene == 1):
        doScene1()
    elif(scene == 2):
        doScene2()

    # --- Screen-clearing code goes here ---
 
    # --- repaints screen ---
    screen.fill(WHITE)
 
    # --- new drawings ---
    pygame.draw.circle(screen, GREEN,(int(b.x),int(b.y)),int(b.radius),0)

    # Updates screen with new drawings
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

