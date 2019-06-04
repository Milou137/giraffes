
from random import randint
import pygame
import time

pygame.init()


white = (255,255,255)

x = 600
y = 800
z = [x,y]




win = pygame.display

win.set_caption("My pygame window meme")

surface = win.set_mode(z)
giraffe_1_img = pygame.image.load('images/giraffe_1.png')
window = True


class Memes():
    def __init__(self):
        self.memes = []
        self.makeMemes()

    def walkAll(self):

        for meme in self.memes:
            meme.walk()

    def makeMemes(self):

        for i in range(2):
            self.memes.append(Meme())
            
class Meme():
    def __init__(self):
        self.x = 200
        self.y = 400
        self.draw()

    def getpos(self):
        return self.x, self.y

    def walk(self):

           
        distance = randint(0, 20)
        for i in range(distance):
            self.x += 1
            #self.y = self.y + randint(-5, 5)
            if self.x < 0:
                self.x = 1
            if self.x > x:
                self.x = (x/3)
            if self.y < 0:
                self.y = 1
            if self.y > y:
                self.y = (y/2)
            surface.fill(white)
            self.draw()
            win.update()

    def draw(self):
        surface.blit(giraffe_1_img,(self.x,self.y))

m = Memes()

while window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False


    surface.fill(white)
    m.walkAll()
    win.update()


pygame.quit()
