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




class Ball:
    x=0; y=0; vx=0; vy=0; radius=0; x2=0; y2=0;
    def __init__(self, xP, yP, vxx, vyy, r):
        self.x = xP
        self.y = yP
        self.vx=vxx
        self.vy=vyy
        self.x2 = xP
        self.y2 = yP
        self.radius = r
    
    
    #getfunctions
    def getRect(s):
        x = s.x-s.radius
        y = s.y-s.radius
        s1 = s.radius*2
        x2 = s.x2-s.radius
        y2 = s.y2-s.radius
        r1 = pygame.Rect(x,y,s1,s1)
        r2= pygame.Rect(x2,y2,s1,s1)
        return pygame.Rect.union(r1,r2)
    #movement
    def move(s):
        s.x2 = s.x
        s.y2 = s.y
        s.x += s.vx
        s.y += s.vy
    def bounceV(s):
        s.vy = -s.vy
    def bounceH(s,p):
        s.vx = -s.vx +2*p.vx
        s.vy = s.vy +2*p.vy
    def bounceH2(s):
        s.vx = -s.vx
    #endgame
    def lose(s):
        global scene, score2, score1, lose, p1Score, p2Score
        scene = 1
        if(lose == 1):
            score2+=1
        else:
            score1+=1
        p1Score = font.render(str(score1), True, BLACK)
        p2Score = font.render(str(score2), True, BLACK)

class Panel:
    len = 0; vy = 0; vx=0; x = 0; y = 0;
    def __init__(self,len,vxx,vyy,xP,yP):
        self.len = len
        self.vx = vxx
        self.vy = vyy
        self.y = yP
        self.x = xP
    def getRect2(s):
        x = s.x-2; y = s.y - s.len; w = 4; h = s.len*2;
        return pygame.Rect(x,y,w,h)
    #movement
    def checkCollision(s,a):
        br = a.getRect()
        lr = s.getRect2()
        return pygame.Rect.colliderect(br,lr)
    
    def move(s):
        s.x += s.vx
        s.y += s.vy


# main program

# --- global variables ---
speed = 4;
scene = 1;
lose = 0;  # 0: none, 1: p1, 2: p2
tick1 = 6
tick2 = 6
vBall = 10
edge = 10
vx = 4
vy = 4
b = Ball(length/2,width/2,vBall,0,15)
p1 = Panel(30,vx,vy,edge,width/2)
p2 = Panel(30,vx,vy,length-edge,width/2)
p3 = Panel(0,0,0,0,0) # dummy

font = pygame.font.SysFont('helvetica', 20)
score1 = 0
score2 = 0
p1Score = font.render(str(score1), True, BLACK)
p2Score = font.render(str(score2), True, BLACK)
goalT = width/4
goalB = 3*width/4

# --- game scenes ---
def doScene1():
    global scene
    #game over someone wins, space to start
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        scene =2
        b.x = length/2
        b.y = width/2
        p1.x = edge
        p2.x = length - edge
        b.vx = 3
        b.vy = 0

def doScene2():
    global scene, tick1, tick2, lose, vBall
    
    l= b.x-b.radius
    r= b.x+b.radius
    if(l < 0-8):
        if(b.y > goalT and b.y < goalB):
            lose =1
            b.lose()
            lose=0
        else:
            b.bounceH2()
            b.move()
    elif(r > length+8):
        if(b.y > goalT and b.y < goalB):
            lose =2
            b.lose()
            lose=0
        else:
            b.bounceH2()
            b.move()
    else:
        #print(b.vx)
        # checks collision once every 3 frames
        if(tick1 < 6):
            tick1 += 2
        if(tick2 < 6):
            tick2 += 2
        if((b.y-b.radius < 0+.1 and b.vy <= 0 )or (b.y+b.radius > width-.1 and b.vy >= 0)):
            b.bounceV()
        if(p1.checkCollision(b) and tick1 == 6):
            b.bounceH(p1)
            tick1 = 0
        if(p2.checkCollision(b) and tick2 == 6):
            b.bounceH(p2)
            tick2 = 0

        #slows down ball
        vt = math.sqrt(b.vx*b.vx+b.vy*b.vy)
        vtd = math.atan(b.vy/b.vx)
        if(vt > vBall +.5):
            sd = .05 + vt/100
            sdx = abs(sd*math.cos(vtd))
            sdy = abs(sd*math.sin(vtd))

            if(b.vx < 0):
                b.vx += sdx
            else:
                b.vx -= sdx
            if(b.vy < 0):
                b.vy += sdy
            else:
                b.vy -= sdy

        # move panels
        p2.vx = 0; p2.vy = 0; p1.vx=0; p1.vy=0;
        keys=pygame.key.get_pressed()
        # add boundries?
        if keys[pygame.K_DOWN]:
            p2.vy = vy
        if keys[pygame.K_UP]:
            p2.vy = -vy
        if keys[pygame.K_LEFT]:
            p2.vx = -vx
        if keys[pygame.K_RIGHT]:
            p2.vx = vx
        if keys[pygame.K_s]:
            p1.vy = vy
        if keys[pygame.K_w]:
            p1.vy = -vy
        if keys[pygame.K_a]:
            p1.vx = -vx
        if keys[pygame.K_d]:
            p1.vx = vx

        # move ball
        b.move()
        p1.move()
        p2.move()



    

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
    # --- repaints screen ---
    screen.fill(WHITE)
 
    # --- new drawings ---
    #ball
    pygame.draw.circle(screen, GREEN,(int(b.x),int(b.y)),int(b.radius),0)
    # panels
    pygame.draw.line(screen,RED,(p1.x, p1.y+p1.len), (p1.x, p1.y-p1.len), 4) #place color ps pe width
    pygame.draw.line(screen,BLUE,(p2.x, p2.y+p1.len), (p2.x, p2.y-p1.len), 4)
    #lines
    pygame.draw.line(screen,BLACK,(0, 0), (0, goalT), 2)
    pygame.draw.line(screen,BLACK,(0, width), (0, goalB), 2)
    pygame.draw.line(screen,BLACK,(length, 0), (length, goalT), 6)
    pygame.draw.line(screen,BLACK,(length, width), (length, goalB), 6)
    pygame.draw.line(screen,BLACK,(0, 0), (length, 0), 2)
    pygame.draw.line(screen,BLACK,(0, width), (length, width), 6)

    screen.blit(p1Score,(5,5))
    screen.blit(p2Score,(length-15,5))

    # Updates screen with new drawings
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

