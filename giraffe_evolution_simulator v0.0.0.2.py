
####### reminder notes
# add a class to store statistics ?



# imports
from random import randint
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style
import time
import pygame

# set style
style.use("fivethirtyeight")


# Giraffes
EAT_RANGE = 75
MAX_HUNGER = 5
HUNGER_DRAIN_TICKS = 5
DEFAULT_NECK_LENGTH = 1000

#Pygame
pygame.init()


white = (255,255,255)

x = 1500
y = 1024
z = [x,y]

FACTOR = 5 #int
FPS = 30
GLOB_STEPSIZE = 5
clock = pygame.time.Clock()

EASTER_EGG1 = False
win = pygame.display

win.set_caption("My pygame window meme")

surface = win.set_mode(z)
background = pygame.transform.scale(pygame.image.load('images/background.png'), (z))
window = True


# Trees
DEFAULT_TREE_LENGTH = 1000

# Population
DEFAULT_GIRAFFE_START_AMOUNT = 100
DEFAULT_MAX_ALLOWED_GIRAFFES = 500
DEFAULT_CHANCE_SPAWN_NEW_GIRAFFE = 25 # 1/33
DEFAULT_MUTATION_AMOUNT = 5


class Giraffe():

    def __init__(self, neck_length = DEFAULT_NECK_LENGTH, image=0):

        self.x = 0
        imagepath = "images/giraffe_"+str(image)+".png" # > 0 < MAXRANGE
        self.image = pygame.image.load(imagepath).convert_alpha()
        self.neck_length = randint(neck_length-EAT_RANGE,
                                   neck_length+EAT_RANGE)
        size = self.image.get_size()
        width, length = size[0],size[1]
        new_w, new_l = width*FACTOR, length*FACTOR
        self.y = 1020 - new_l       
        self.image = pygame.transform.scale(self.image, (new_w, new_l))
             
        self.hunger = MAX_HUNGER
        self.dead = False
        

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

    def draw(self):
        surface.blit(self.image,(self.x,self.y))

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
        

    
def normalise(l, r):
    # how many times does the smallest thing fit all the other things?
    minim, maxim = min(l), max(l)
    result = []

    devider = maxim-minim

    for i in l:
        result.append( round(((i - minim)/(devider))*r))

    return result
    
def add_to_dict(original_dict, dict_to_add):
    """assumes values of both dicts are integers and
       can be added together, then adds them to the first
       one and returns it"""

    for key, value in dict_to_add.items():
        if not key in original_dict.keys():
            original_dict[key] = value
        else:
            original_dict[key] += value
            
def spawnGeneration(giraffes, SHORTEST_NECK, TALLEST_NECK):
    new_gen = []
    spawned = 0
    for giraffe in giraffes:
        old_length = giraffe.neck_length
        mutation = randint(MAX_DECREASE,MAX_INCREASE)
        new_length = old_length + mutation
        giraffe_image = normalise([SHORTEST_NECK, new_length, TALLEST_NECK],10)[1]
        
        new_giraffe = Giraffe(new_length, giraffe_image)
        new_gen.append(new_giraffe)
        spawned += 1

        # twin
        if len(giraffes) < MAX_ALLOWED_GIRAFFES:
            if not bool(randint(0,CHANCE_SPAWN_NEW_GIRAFFE)):
                new_giraffe = Giraffe(new_length, giraffe_image)
                new_gen.append(new_giraffe)
                spawned += 1
        else:
            break

    return new_gen, spawned
        
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
        



verbose = False

total_spawned = 0
total_died = 0
all_gen_neck_length_counts = dict()
all_lengths = []
all_shortest_lengths=  []
all_tallest_lengths = []
axvlineXes = []
SHORTEST_NECK = DEFAULT_NECK_LENGTH
TALLEST_NECK = DEFAULT_NECK_LENGTH
MAX_DECREASE = DEFAULT_MUTATION_AMOUNT
MAX_INCREASE  = DEFAULT_MUTATION_AMOUNT
CHANCE_SPAWN_NEW_GIRAFFE = DEFAULT_CHANCE_SPAWN_NEW_GIRAFFE
MAX_ALLOWED_GIRAFFES= DEFAULT_MAX_ALLOWED_GIRAFFES

giraffes = []
for i in range(DEFAULT_GIRAFFE_START_AMOUNT):
    giraffes.append(Giraffe())
    total_spawned += 1


Game = True
generation = 0
population_size_per_generation = []

tree_length = DEFAULT_TREE_LENGTH # DO THIS FOR EVERYTHING

bob = Boom(420)
job = Boom(-350)

print("GAME STARTS!","there are", len(giraffes))
while len(giraffes) > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window = False

    

    # game loop
    for hunger_drain in range(HUNGER_DRAIN_TICKS):
        # draw background
        surface.blit(background,(0,0))
        for g_index in range(len(giraffes)):

            giraffe = giraffes[g_index]
            giraffe.drain_hunger()
            
            
            giraffe.eat(tree_length)
            giraffe.walk()
            giraffe.draw() 
            win.update()
            
         
        dead_giraffes = [giraffe for giraffe in giraffes if giraffe.isDead()]
        for corpse in dead_giraffes:
            total_died += 1
            giraffes.remove(corpse)

        
        clock.tick(FPS)


    # some logging for now
    neck_lengths = [giraffe.neck_length for giraffe in giraffes]
    

    if neck_lengths != []:
        short_one = min(neck_lengths)
        tall_one = max(neck_lengths)
        if short_one < SHORTEST_NECK:
            SHORTEST_NECK = short_one
        if tall_one > TALLEST_NECK:
            TALLEST_NECK = tall_one

    all_lengths = all_lengths + neck_lengths
    for l in neck_lengths:
        all_shortest_lengths.append(short_one)
        all_tallest_lengths.append(tall_one)

    axvlineXes.append(total_spawned-total_died)
    
    print("SHORT:",SHORTEST_NECK,"TALL:",TALLEST_NECK)
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
    giraffes, spawned = spawnGeneration(giraffes, SHORTEST_NECK, TALLEST_NECK)
    total_spawned += spawned


# end state ( diagrams, popuptext, idfk)
surface.blit(background,(0,0))

# end whileloop
print("In generation",generation,"all giraffes are dead")
print_neck_lengths(all_gen_neck_length_counts)
print("tallest:",max(all_gen_neck_length_counts))
print("shortest:",min(all_gen_neck_length_counts))
print("most occuring population:")
print(highest_frequency(population_size_per_generation))
pygame.quit()


print(all_lengths[:10],all_shortest_lengths[:10],
      all_tallest_lengths[:10])

average = np.average(all_lengths)
mean =  np.mean(all_lengths)


plt.plot(all_lengths, 'r--')
plt.plot(all_shortest_lengths, 'bs')
plt.plot(all_tallest_lengths, 'g^')
for tup in zip([average, mean], ['black','grey']):
    print(tup[0], tup[1])
    plt.hlines(tup[0],0,len(all_lengths), tup[1])

for axvline in  axvlineXes:
    plt.axvline(axvline, color='pink')
    
plt.show()
