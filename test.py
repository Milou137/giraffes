from random import randint
import pygame
import time

pygame.init()


white = (255,255,255)

x = 1500
y = 1024
z = [x,y]
FACTOR = 7 #int
FPS = 30
GLOB_STEPSIZE = 0.6
clock = pygame.time.Clock()

EASTER_EGG1 = True
win = pygame.display

win.set_caption("My pygame window meme")
surface = win.set_mode(z)
background = pygame.transform.scale(pygame.image.load('images/background.png'), (z))
window = True


# testing sprites

class Memes():
    def __init__(self):
        self.memes = []
        self.makeMemes()

    def walkAll(self):

        for meme in self.memes:
            meme.walk()

            
    def drawAll(self):

        for meme in self.memes:
            meme.draw()

    def makeMemes(self):

        for i in range(12):
            self.memes.append(Meme())

            
class Meme():
    def __init__(self):
        self.x = 0
        self.image = pygame.image.load('images/giraffe_10.png')
        size = self.image.get_size()
        width, length = size[0],size[1]
        new_w, new_l = width*FACTOR, length*FACTOR
        self.y = 1020 - new_l       
        self.image = pygame.transform.scale(self.image, (new_w, new_l))
        
                                            

    def getpos(self):
        return self.x, self.y

    def walk(self):

           
        distance = randint(0, 20)
        negative = bool(randint(0,1))
        
        for i in range(distance):
            if not negative:
                self.x += GLOB_STEPSIZE
            else:
                self.x -= GLOB_STEPSIZE
            #self.y = self.y + randint(-5, 5)
            # reset if giraffe out of boundaries 
            if self.x < 0:
                self.x = 1
            if self.x > x:
                self.x = (x/3)
            if self.y < 0:
                self.y = 15
            if self.y > y:
                self.y = (y/2)


    def draw(self):
        surface.blit(self.image,(self.x,self.y))

class Boom():
    def __init__(self, offset=0):
        self.image = pygame.image.load('images/boom_0.png')
        size = self.image.get_size()
        width, length = size[0],size[1]
        new_w, new_l = width*FACTOR, length*FACTOR
        self.x = (x/2) - (new_w/2) + offset
              
        
        self.y = 1020 - new_l
        self.image = pygame.transform.scale(self.image, (new_w, new_l))

    def draw(self):
        surface.blit(self.image,(self.x,self.y))
        

m = Memes()

bob = Boom(420)
job = Boom(-350)

while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False


    # draw background first
    surface.blit(background,(0,0))

    # render stuff
    
    m.walkAll()
    m.drawAll()
    bob.draw()
    job.draw()

    # update (render) the screen (?)
    win.update()

    # fps
    clock.tick(FPS)


pygame.quit()
