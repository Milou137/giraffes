# imports
from random import randint
EAT_RANGE = 10
MAX_HUNGER = 5
DEFAULT_NECK_LENGTH = 100

class Giraffe():

    def __init__(self, neck_length = DEFAULT_NECK_LENGTH):

        self.neck_length = neck_length
        self.hunger = MAX_HUNGER
        self.dead = False
    def eat(self, tree_length):
        if ((self.neck_length - tree_length) > -EAT_RANGE) and (
            (self.neck_length - tree_length) < EAT_RANGE):

            if self.hunger < MAX_HUNGER+1:
                self.hunger += 1
                return True
        else:
            return False
    def drain_hunger(self):
        self.hunger -= 1
        if self.hunger == 0:
            print("a giraffe died with necklength",self.neck_length)
            self.dead = True
    def isDead(self):
        return self.dead
def main():
    giraffes = []
    for i in range(3):
        giraffes.append(Giraffe())
    Game = True
    generation = 0
    tree_length = 100
    print("GAME STARTS!","there are", len(giraffes))
    while Game:
        for hunger_drain in range(5):
            for g_index in range(len(giraffes)):
                giraffe = giraffes[g_index]
                giraffe.drain_hunger()
                giraffe.eat(tree_length)
            dead_giraffes = [giraffe for giraffe in giraffes if giraffe.isDead()]
            for corpse in dead_giraffes:
                giraffes.remove(corpse)
        input("press enter to go to the next generation")
        print("there are",len(giraffes),"in generation",generation)
        generation += 1
        new_gen = []
        for giraffe in giraffes:
            new_giraffe = Giraffe( giraffe.neck_length + randint(-3,3))
            new_gen.append(new_giraffe)

        giraffes = new_gen
main()
