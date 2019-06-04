
import random

class Giraffe():
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
        


class GiraffeGroup():
    def __init__(self):

        self.giraffes = []

        for i in range(20):
            self.spawnGiraffe()
        

    def reproduce(self):


        for giraffe in self.giraffes:

            giraffe.grow()
            giraffe.birthday()


        for i in range (0, len(self.giraffe)/2, 2):
            try:
                self.spawnGiraffe([self.giraffes[i],self.giraffes[i+1]])
            except
                print("somefuckingerror")
            
        
    def spawnGiraffe(self, parents=False):

        
        giraffe = Giraffe()
        if parents:
            giraffe.neckLength = (parent[0].neckLength + parent[1].neckLength)/2 + random.randin(-10,10)
            
        self.giraffes.append(giraffe)

                

def main():

    bob = GiraffeGroup()

    years = 0

    while years < 250:
        bob.reproduce()
        years += 1




main()





    

    

