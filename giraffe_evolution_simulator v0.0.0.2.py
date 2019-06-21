
####### reminder notes
# add a class to store statistics ?



# imports
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# set style
style.use("fivethirtyeight")

GIRAFFE_START_AMOUNT = 10
MAX_ALLOWED_GIRAFFES = 500
CHANCE_SPAWN_NEW_GIRAFFE = 25 # 1/33
EAT_RANGE = 10
MAX_HUNGER = 5
HUNGER_DRAIN_TICKS = 5
DEFAULT_NECK_LENGTH = 100
DEFAULT_TREE_LENGTH = 100
MAX_DECREASE = 3
MAX_INCREASE = 3

class Giraffe():

    def __init__(self, neck_length = DEFAULT_NECK_LENGTH):

        self.neck_length = randint(neck_length-EAT_RANGE,
                                   neck_length+EAT_RANGE)
        self.hunger = MAX_HUNGER
        self.dead = False
        
        self.x = 0


    def eat(self, tree_length):
        
        if self.can_eat(tree_length):
            if self.hunger < MAX_HUNGER+1:
                self.hunger += 1
                return True
        else:
            return False

    def drain_hunger(self):
        self.hunger -= 1

        if self.hunger == 0:
            self.dead = True
            #redundancy

    def can_eat(self, tree_length):
        difference = self.neck_length - tree_length
        within_max = difference < EAT_RANGE
        within_min = difference > -EAT_RANGE
        can_eat = within_max and within_min
        return can_eat
        
    def isDead(self):
        return self.dead

def add_to_dict(original_dict, dict_to_add):
    """assumes values of both dicts are integers and
       can be added together, then adds them to the first
       one and returns it"""

    for key, value in dict_to_add.items():
        if not key in original_dict.keys():
            original_dict[key] = value
        else:
            original_dict[key] += value
            
def print_dict(d):
    for k, v in d.items():
        print ( k, "\t:", v )

def print_neck_lengths(counts):
    print("necklengths:\n-----------")
    print("length \t: amount")
    print_dict(counts)

def highest_frequency(l):

    highest = 0
    counts = {}
    
    for i in set(l):
        frequency = l.count(i)
        counts[i] = frequency
        if frequency > highest:
            highest = frequency
            item = i
    # sorted_x = sorted(x.items(), key=lambda kv: kv[1]) <- for later
    # if we want to return like a top-3 or something. h.
    return "Most occuring item was %s with a frequency of %s " %(item,highest)
        
    
    
                
def main(verbose=False):

    total_spawned = 0
    all_gen_neck_length_counts = dict()
    
    giraffes = []
    for i in range(GIRAFFE_START_AMOUNT):
        giraffes.append(Giraffe())
        total_spawned += 1

    
    Game = True
    generation = 0
    population_size_per_generation = []

    tree_length = DEFAULT_TREE_LENGTH # DO THIS FOR EVERYTHING
    
    
    print("GAME STARTS!","there are", len(giraffes))
    while len(giraffes) > 0:
        
        for hunger_drain in range(HUNGER_DRAIN_TICKS):
            for g_index in range(len(giraffes)):

                giraffe = giraffes[g_index]
                giraffe.drain_hunger()
                giraffe.eat(tree_length)         
 
            dead_giraffes = [giraffe for giraffe in giraffes if giraffe.isDead()]
            for corpse in dead_giraffes:
                giraffes.remove(corpse)

        # some logging for now
        neck_lengths = [giraffe.neck_length for giraffe in giraffes]
        current_gen_neck_length_counts = {neck_length:neck_lengths.count(neck_length) for
                  neck_length in set(neck_lengths)}
        add_to_dict(all_gen_neck_length_counts,
                    current_gen_neck_length_counts)

        # verbosity (logging prints)
        
        if verbose:
            print_neck_lengths(counts)

        # to do :
        # - add live graph
        # - update livegraph here
        #
        # - graphs to update
        #    - population_size_per_generation (population)
        #

        
        #input("press enter to go to the next generation")
        print("there are",len(giraffes),"in generation",generation)
        population_size_per_generation.append(len(giraffes))
        generation += 1


        # NEW GENERATION SPAWNING
        new_gen = []
        for giraffe in giraffes:
            new_giraffe = Giraffe( giraffe.neck_length + randint(MAX_DECREASE,MAX_INCREASE))
            new_gen.append(new_giraffe)

            # randoms
            if len(giraffes) < MAX_ALLOWED_GIRAFFES:
                if not bool(randint(0,CHANCE_SPAWN_NEW_GIRAFFE)):
                    new_gen.append(Giraffe( giraffe.neck_length + randint(MAX_DECREASE,MAX_INCREASE)))
                    total_spawned += 1
            else:
                break

            total_spawned += 1

        giraffes = new_gen




    # end whileloop
    print("In generation",generation,"all giraffes are dead")
    print_neck_lengths(all_gen_neck_length_counts)
    print(highest_frequency(population_size_per_generation))

    

main()
