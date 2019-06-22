from random import randint
import pygame
import time

pygame.init()


white = (255,255,255)

x = 1280
y = 1024
z = [x,y]

FPS = 30
GLOB_STEPSIZE = 0.6
clock = pygame.time.Clock()

EASTER_EGG1 = True
win = pygame.display

win.set_caption("My pygame window meme")

surface = win.set_mode(z)
giraffe_1_img = pygame.transform.scale(pygame.image.load('images/giraffe_1.png'), (2000,2000))
background = pygame.transform.scale(pygame.image.load('images/background.png'), (1280, 1024))
boom = pygame.image.load('images/boom_0.png')
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
        self.y = randint(550, 580)
        self.image = pygame.transform.scale(pygame.image.load('images/giraffe_1.png'), (200,200))

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



m = Memes()


while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False


    # draw background first
    surface.blit(background,(0,0))

    # render stuff
    
    m.walkAll()
    m.drawAll()


    # update (render) the screen (?)
    win.update()

    # fps
    clock.tick(FPS)


pygame.quit()
