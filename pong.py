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

# --- global variables ---
speed = 3;
scene = 1;
lose = 0;  # 0: none, 1: p1, 2: p2


class Ball:
    x=0; y=0; vx=0; vy=0; radius=0;
    def __init__(self, xP, yP, vxx,vyy, r):
        self.x = xP
        self.y = yP
        self.vx=vxx
        self.vy=vyy
        self.radius = r
    #movement
    def move(s):
        s.x += s.vx
        s.y += s.vy
    def bounceV(s):
        s.vy = -s.vy
    def bounceH(s):
        s.vx = -s.vx
    #endgame
    def lose1(s):
        g.scene = 3
        g.lose = 1
    def lose2(s):
        g.scene = 3
        g.lose = 2

class Panel:
    len = 0; vy = 0; x = 0; y = 0;
    def __init__(self,len,vyy,xP,yP):
        self.len = len
        self.vy = vyy
        self.y = yP
        self.x = xP
    #movement
    def up(s):
        s.y -= s.vy
    def down(s):
        s.y += s.vy





# main program

# --- objects ---
edge = 10
b = Ball(length/2,width/2,speed,speed,15)
p1 = Panel(30,3,edge,width/2)
p2 = Panel(30,3,length-edge,width/2)


# --- game scenes ---
def doScene1():
    global scene
    # space to start
    scene = 2

def doScene2():
    global scene
    # move ball
    b.move()
    l= b.x-b.radius
    r= b.x+b.radius
    if(b.y-b.radius < 0+.1 or b.y+b.radius > width-.1):
        b.bounceV()
    if(l < 0+.1 or r > length-.1):
        b.bounceH()
    if(b.y >= p1.y-p1.len and b.y <= p1.y+p1.len and l<=edge+.1):
        b.bounceH()
    if(b.y >= p2.y-p2.len and b.y <= p2.y+p2.len and r>=length-edge-.1):
        b.bounceH()
    # move panels
    move_ticker = 0
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        p2.down()
    if keys[pygame.K_UP]:
        p2.up()
    if keys[pygame.K_s]:
        p1.down()
    if keys[pygame.K_w]:
        p1.up()

def doScene3():
    global scene
    #game over someone wins, space to start
    print(3)
    scene = 2
    print(2)

# --- game loop ---
while not done:
    # --- Events loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- scene logic ---
    if(scene == 1):
        doScene1()
    elif(scene == 2):
        doScene2()
    elif(scene == 3):
        doScene3()

    # --- repaints screen ---
    screen.fill(WHITE)
 
    # --- new drawings ---
    pygame.draw.circle(screen, GREEN,(int(b.x),int(b.y)),int(b.radius),0)
    pygame.draw.line(screen,RED,(p1.x, p1.y+p1.len), (p1.x, p1.y-p1.len), 4) #place color ps pe width
    pygame.draw.line(screen,RED,(p2.x, p2.y+p1.len), (p2.x, p2.y-p1.len), 4)

    # Updates screen with new drawings
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

