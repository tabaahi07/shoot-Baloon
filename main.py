import pygame, sys
import random
from file1 import fun
from file3 import Score_board
r = 220
g = 250 
b = 240

class Ball:
    def __init__(self , size, balloon_imgs ):
        self.img = balloon_imgs[random.randint(0,2)]
        self.x = random.randint(0, ( width-self.img.get_width() ) )
        self.y = ( size[1] + ( random.randint(1,size[1]) )*3 )
        self.velX = 0
        self.velY = 2
        
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        
    
    def move(self):
        self.x += self.velX
        self.y -= self.velY
        self.velX = random.randint(-2,2)
    
    def play_sound(self):
        self.sound.play()

    def check_boundary(self, screen_size):
        global r,g,b
        scr_width, scr_height = screen_size
        if (self.x < 0 or self.x > scr_width - self.width):
            self.velX = -self.velX
            # self.play_sound()
            # r = random.randint(0,255)
            # g = random.randint(0,255)
            # b = random.randint(0,255)

        if (self.y < 0 or self.y > scr_height - self.height):
            self.velY = -self.velY
            self.play_sound()
            # r = random.randint(0,255)
            # g = random.randint(0,255)
            # b = random.randint(0,255)


pygame.init()
pygame.font.init()
path = r"C:\Users\akrat\OneDrive\Desktop\Python Programs\Program\Pygame\shoot Baloon\\"
balloon_imgs = [pygame.image.load(path + str(i) + ".png") for i in range(1,4)]

sound = pygame.mixer.Sound(r"C:\Users\akrat\OneDrive\Desktop\Python Programs\Program\Pygame\shoot Baloon\sound.wav")

size = width,height = 1000,700
score = 0 
clock = pygame.time.Clock()
mouse = pygame.mouse 

screen = pygame.display.set_mode(size)
balls = []


for j in range(100):
      temp = Ball(size, balloon_imgs )
      balls += [temp]

def Score_card( ) :
   my_font = pygame.font.SysFont('Comic Sans MS', 30)
   text_surface = my_font.render(f' SCORE : {score}', False, (0, 0, 0))
   screen.blit(text_surface, ( 10 , 10 , text_surface.get_width(), text_surface.get_height() ) )

def update():
    for ball in balls:
        ball.move()
        # ball.check_boundary(size)

def draw():
    screen.fill((r,g,b))
    for ball in balls:
        screen.blit(ball.img, (ball.x, ball.y, ball.width, ball.height))
    missed_balls()    
    Score_card()
    Score_board(score) 
    pygame.display.flip()

def shoot(posn) :
    global score
    for ball in balls[::-1] :
        if(posn[0] > ball.x and posn[0] < ball.x + ball.width and posn[1] > ball.y and posn[1] < ball.y + ball.height) :
            balls.remove(ball)
            sound.play()
            score += 1 
            break 
        

def missed_balls () :
    global score
    for ball in balls :
        if( ball.y < 0 ) :
            score -= 1
            balls.remove(ball)


        
pressed = False
fun()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT : sys.exit()
    
 
    update()
    draw()

    if (mouse.get_pressed()[0] and not pressed ):
        pressed = True
        posn = mouse.get_pos()
        shoot(posn)
         
    if (pressed and not mouse.get_pressed()[0]):
        pressed = False
    
    update()
    draw()

    clock.tick(30)   