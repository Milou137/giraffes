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
    def isDead(self):
        return self.dead
def main():
    giraffes = []
    for i in range(3):
        giraffes.append(Giraffe())
main()
