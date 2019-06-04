
import random

class Giroffe():
    def __init__(self):


        self.age = 0
        self.neckLength = 100


    def grow(self):
        self.neckLength += 10

    def birthday(self):

        self.age += 1

    def eat(self):

        chance_for_eat = neckLength * random.randint(1,10)

        if chance_for_eat > 
        


class GiroffeGroup():
    def __init__(self):

        self.giroffes = []

        for i in range(20):
            self.spawnGiroffe()
        

    def reproduce(self):


        for giroffe in self.giroffes:

            giroffe.grow()
            giroffe.birthday()


        for i in range (0, len(self.giroffe)/2, 2):
            try:
                self.spawnGiroffe([self.giroffes[i],self.giroffes[i+1]])
            except
                print("somefuckingerror")
            
        
    def spawnGiroffe(self, parents=False):

        
        giroffe = Giroffe()
        if parents:
            giroffe.neckLength = (parent[0].neckLength + parent[1].neckLength)/2 + random.randin(-10,10)
            
        self.giroffes.append(giroffe)

                

def main():

    bob = GiroffeGroup()

    years = 0

    while years < 250:
        bob.reproduce()
        years += 1




main()





    

    

