
from random import randint
import pygame
import time

pygame.init()


white = (255,255,255)

x = 600
y = 800
z = [x,y]

FPS = 30
GLOB_STEPSIZE = 0.6
clock = pygame.time.Clock()

EASTER_EGG1 = False
win = pygame.display

win.set_caption("My pygame window meme")

surface = win.set_mode(z)
giraffe_1_img = pygame.transform.scale(pygame.image.load('images/giraffe_1.png').convert_alpha(), (100, 100))
background = pygame.image.load('images/background.png')
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

        for i in range(30):
            self.memes.append(Meme())

    def growSome(self):

        for meme in self.memes:

            # random
            if bool(randint(0,1)):
                meme.grow(randint(-5,10))
            
class Meme():
    def __init__(self):
        self.x = 0
        self.y = randint(550, 580)
        self.image = pygame.transform.scale(pygame.image.load('images/giraffe_1.png').convert_alpha(), (100, 100))

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

    def grow(self, amt):
        size = self.image.get_size()
        if size[1] < 780:
            width, length = size[0], size[1]

            
            if not EASTER_EGG1:
                self.image = pygame.transform.scale(pygame.image.load('images/running_giraffe_small_deprecatred.png').convert_alpha(), (width, length+amt))
                self.y -= amt
            else:
                self.image = pygame.transform.rotozoom(self.image, randint(0,360),1)





m = Memes()


while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False


    # draw background first
    surface.blit(background,(0,0))
    #surface.fill([0,0,0])

    # render stuff
    
    m.walkAll()
    m.drawAll()
    m.growSome()


    # update (render) the screen (?)
    win.update()

    # fps
    clock.tick(FPS)


pygame.quit()
