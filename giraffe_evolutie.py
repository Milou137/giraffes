
####### reminder notes
# add a class to store statistics ?



# ██╗███╗   ███╗██████╗  ██████╗ ██████╗ ████████╗███████╗
# ██║████╗ ████║██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝
# ██║██╔████╔██║██████╔╝██║   ██║██████╔╝   ██║   ███████╗
# ██║██║╚██╔╝██║██╔═══╝ ██║   ██║██╔══██╗   ██║   ╚════██║
# ██║██║ ╚═╝ ██║██║     ╚██████╔╝██║  ██║   ██║   ███████║
# ╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝

from random import randint
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib import style
import time
import pygame


#  ██████╗ ██╗      ██████╗ ██████╗  █████╗ ██╗     ███████╗
# ██╔════╝ ██║     ██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
# ██║  ███╗██║     ██║   ██║██████╔╝███████║██║     ███████╗
# ██║   ██║██║     ██║   ██║██╔══██╗██╔══██║██║     ╚════██║
# ╚██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║███████╗███████║
#  ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                          

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

x = 800
y = 630
z = [x,y]

FACTOR = 5 #int
FPS = 25
GLOB_STEPSIZE = 5
clock = pygame.time.Clock()
PIXELS_ONDERGROND = 40

EASTER_EGG1 = False
win = pygame.display

win.set_caption("My pygame window meme")

surface = win.set_mode(z)
background = pygame.transform.scale(pygame.image.load('images/background.png'), (z))
window = True


# Trees
DEFAULT_TREE_LENGTH = 1000
tree_length = DEFAULT_TREE_LENGTH
# Population
DEFAULT_GIRAFFE_START_AMOUNT = 10
DEFAULT_MAX_ALLOWED_GIRAFFES = 100
DEFAULT_CHANCE_SPAWN_NEW_GIRAFFE = 50 # 1/33
DEFAULT_MUTATION_AMOUNT = 5

TREEDOWN = - 3
TREEUP = 30

visualise = True
verbose = False

total_spawned = 0
total_died = 0
all_gen_neck_length_counts = dict()
all_lengths = []
all_shortest_lengths =  []
all_tallest_lengths = []
all_treelengths = [1000]
axvlineXes = []
SHORTEST_NECK = DEFAULT_NECK_LENGTH
TALLEST_NECK = DEFAULT_NECK_LENGTH
MAX_DECREASE = DEFAULT_MUTATION_AMOUNT
MAX_INCREASE  = DEFAULT_MUTATION_AMOUNT
CHANCE_SPAWN_NEW_GIRAFFE = DEFAULT_CHANCE_SPAWN_NEW_GIRAFFE
MAX_ALLOWED_GIRAFFES= DEFAULT_MAX_ALLOWED_GIRAFFES


Game = True
generation = 0
population_size_per_generation = []

tree_length = DEFAULT_TREE_LENGTH # DO THIS FOR EVERYTHING



"""
 ██████╗ ██╗██████╗  █████╗ ███████╗███████╗███████╗
██╔════╝ ██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
██║  ███╗██║██████╔╝███████║█████╗  █████╗  █████╗  
██║   ██║██║██╔══██╗██╔══██║██╔══╝  ██╔══╝  ██╔══╝  
╚██████╔╝██║██║  ██║██║  ██║██║     ██║     ███████╗
 ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝"""
                                                    



class Giraffe():

    def __init__(self, neck_length = DEFAULT_NECK_LENGTH, image=4):

        self.x = randint(0+10, x-10)
        imagepath = "images/giraffe_"+str(image)+".png" # > 0 < MAXRANGE
        self.image = pygame.image.load(imagepath).convert_alpha()
        self.neck_length = randint(neck_length-EAT_RANGE,
                                   neck_length+EAT_RANGE)
        size = self.image.get_size()
        width, length = size[0],size[1]
        new_w, new_l = width*FACTOR, length*FACTOR
        self.y = y - new_l - PIXELS_ONDERGROND     
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

        if self.hunger <= 0:
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

           
        distance = randint(0, 100)
        negative = bool(randint(0,1))
        
        for i in range(distance):
            if not negative:
                self.x += 3
            else:
                self.x -= 3
            #self.y = self.y + randint(-5, 5)
            # reset if giraffe out of boundaries 
            if self.x < 0:
                self.x = x/2
            if self.x > x:
                self.x = x/3
            if self.y < 0:
                self.y = 15
            if self.y > y:
                self.y = y/2

"""
████████╗██████╗ ███████╗███████╗
╚══██╔══╝██╔══██╗██╔════╝██╔════╝
   ██║   ██████╔╝█████╗  █████╗  
   ██║   ██╔══██╗██╔══╝  ██╔══╝  
   ██║   ██║  ██║███████╗███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝"""                              
class Boom():
    def __init__(self, offset=0, minBOOM=tree_length/2,maxBOOM=tree_length*2):

        if offset == 0:
            offset = randint (0+10, x-10)
        boom_image_num = normalise([500, tree_length, 2000],10)[1]
        imagepath = "images/boom_"+str(boom_image_num)+".png" # > 0 < MAXRANGE
        self.image = pygame.image.load(imagepath).convert_alpha()
        size = self.image.get_size()
        width, length = size[0],size[1]
        new_w, new_l = width*FACTOR, length*FACTOR
        self.x = (x/2) - (new_w/2) + offset
        self.y = y - new_l - PIXELS_ONDERGROND
        self.image = pygame.transform.scale(self.image, (new_w, new_l))

    def draw(self):
        surface.blit(self.image,(self.x,self.y))

    def update(self, tree_items):
        """ tree min, max, length"""
        image_num = normalise([500,tree_items[1],2000],10)[1]
        imagepath = "images/boom_"+str(image_num)+".png" # > 0 < MAXRANGE
        self.image = pygame.image.load(imagepath).convert_alpha()
        size = self.image.get_size()
        width, length = size[0],size[1]
        new_w, new_l = width*FACTOR, length*FACTOR
        self.x = (x/2) - (new_w/2)
        self.y = y - new_l - PIXELS_ONDERGROND
        self.image = pygame.transform.scale(self.image, (new_w, new_l))
        
"""
██████╗ ██╗   ██╗████████╗████████╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║╚══██╔══╝╚══██╔══╝██╔═══██╗████╗  ██║
██████╔╝██║   ██║   ██║      ██║   ██║   ██║██╔██╗ ██║
██╔══██╗██║   ██║   ██║      ██║   ██║   ██║██║╚██╗██║
██████╔╝╚██████╔╝   ██║      ██║   ╚██████╔╝██║ ╚████║
╚═════╝  ╚═════╝    ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
                                                      """
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False       
    
def normalise(l, r):
    # how many times does the smallest thing fit all the other things?
    minim, maxim = min(l), max(l)
    result = []

    if minim == maxim:
        minim -= 1
        maxim += 1
        
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


#
# instanciating some objects
# --------------------------


# demo trees
bob = Boom(420)
job = Boom(-350)

# background trees
back_trees = []
for i in range(6):
    tree = Boom()
    tree.draw()
    back_trees.append(tree)

# herd of giraffes
giraffes = []
for i in range(DEFAULT_GIRAFFE_START_AMOUNT):
    giraffeboy = Giraffe()
    giraffeboy.draw()
    giraffes.append(giraffeboy)
    
    total_spawned += 1

# foreground trees
fore_trees = []
for i in range(6):
    tree = Boom()
    tree.draw()
    fore_trees.append(tree)

# buttons
upButton = button((0,255,0), 70, 20,50, 50,  '+')
downButton = button((255,0,0), 150, 20,50, 50,  '-')


#  ██████╗  █████╗ ███╗   ███╗███████╗    ██╗      ██████╗  ██████╗ ██████╗ 
# ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
# ██║  ███╗███████║██╔████╔██║█████╗      ██║     ██║   ██║██║   ██║██████╔╝
# ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝ 
# ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗╚██████╔╝╚██████╔╝██║     
#  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  (start)    

                                                                           
print("GAME STARTS!","there are", len(giraffes))
while len(giraffes) > 0:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            window = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            if upButton.isOver(pos):
                tree_length += 50


            if downButton.isOver(pos):
                tree_length -= 50
            
    

#  ██████╗  █████╗ ███╗   ███╗ ███████╗    ██╗      ██████╗  ██████╗  ██████╗ 
# ██╔════╝ ██╔══██╗████╗ ████║ ██╔════╝    ██║     ██╔═══██╗██╔═══██╗ ██╔══██╗
# ██║  ███╗███████║██╔████╔██║ █████╗      ██║     ██║   ██║██║   ██║ ██████╔╝
# ██║   ██║██╔══██║██║╚██╔╝██║ ██╔══╝      ██║     ██║   ██║██║   ██║ ██╔═══╝ 
# ╚██████╔╝██║  ██║██║ ╚═╝ ██║ ███████╗    ███████╗╚██████╔╝╚██████╔╝ ██║     
#  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝ ╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝  ╚═╝     
# ----------------------------------------------------------------------------
# one full 'loop' equals one 'generation'
# every generation, an inner loop represents time (hunger drains every so often)
#
#
#
    
    for time_unit in range(HUNGER_DRAIN_TICKS*10):
        tree_items = [min(all_treelengths), max(all_treelengths), tree_length]
 
        # background first
        if visualise:
            surface.blit(background,(0,0))
            for tree in back_trees:
                tree.update(tree_items)
                tree.draw()

        # eat every 10 ticks
        if time_unit % 10 == 0:

            for g_index in range(len(giraffes)):
                giraffe = giraffes[g_index]
                giraffe.drain_hunger()
                giraffe.eat(tree_length)
            dead_giraffes = [giraffe for giraffe in giraffes if giraffe.isDead()]
            for corpse in dead_giraffes:
                total_died += 1
                giraffes.remove(corpse)
        else:
            for g_index in range(len(giraffes)):
                giraffe = giraffes[g_index]
                giraffe.walk()
                giraffe.draw()

        # draw background (if visualise is on)
        if visualise:
            
                      
            # foreground (trees)
            bob.draw()
            job.draw()
            for tree in fore_trees:
                tree.update(tree_items)
                tree.draw()


            # draw GUI elements (buttons)
            upButton.draw(surface)
            downButton.draw(surface)
            # actually update the window
            # and show the new frame
            win.update()  

                
            # tick the clock keep frames <= FPS
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
        all_treelengths.append(tree_length)

    # random treelength   
    #tree_length += randint(TREEDOWN, TREEUP)
    axvlineXes.append(total_spawned-total_died)
    
    print("SHORT:",SHORTEST_NECK,"TALL:",TALLEST_NECK,"TREE:",tree_length)
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
    giraffes, spawned = spawnGeneration(giraffes, 600, 1900)
    total_spawned += spawned


# end state ( diagrams, popuptext, idfk)
surface.blit(background,(0,0))

'███████╗███╗   ██╗██████╗  ' #  ███████╗ ██████╗██████╗ ███████╗███████╗███╗   ██╗
'██╔════╝████╗  ██║██╔══██╗ ' #  ██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝████╗  ██║
'█████╗  ██╔██╗ ██║██║  ██║ ' #  ███████╗██║     ██████╔╝█████╗  █████╗  ██╔██╗ ██║
'██╔══╝  ██║╚██╗██║██║  ██║ ' #  ╚════██║██║     ██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║
'███████╗██║ ╚████║██████╔╝ ' #  ███████║╚██████╗██║  ██║███████╗███████╗██║ ╚████║
'╚══════╝╚═╝  ╚═══╝╚═════╝  ' #  ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
                                                                                

# end state ( diagrams, popuptext, idfk)
# from https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.font.init()
myfont =  pygame.font.SysFont('Comic Sans MS', 30)
game_end_text_1 = myfont.render('Endu Of Gamu', False, (0, 0, 0))
game_end_text_2 = myfont.render('generation: '+str(generation), False, (0, 0, 0))

surface.blit(background,(0,0))
surface.blit(game_end_text_1,((x/2)-60,y/2))
surface.blit(game_end_text_2,((x/2)-60,y/2+30))
win.update()


#  -----------------------------------------------------------------------------


# end whileloop
# some log prints
print("In generation",generation,"all giraffes are dead")
print_neck_lengths(all_gen_neck_length_counts)
print("tallest:",max(all_gen_neck_length_counts))
print("shortest:",min(all_gen_neck_length_counts))
print("most occuring population:")
print(highest_frequency(population_size_per_generation))
pygame.quit()

# some log prints

print(all_lengths[:10],all_shortest_lengths[:10],
      all_tallest_lengths[:10])


# pre graph calculations
average = np.average(all_lengths)
mean =  np.mean(all_lengths)

# graphs
plt.plot(all_lengths, 'r--',label='length per generation')
plt.plot(all_shortest_lengths, 'bs', label='shortest giraffe in generation')
plt.plot(all_tallest_lengths, 'g^', label='tallest giraffe in generation')
plt.plot(all_treelengths, 'brown', label='tree length')
for tup in zip([average, mean], ['black','grey'], ['average', 'mean']):
    print(tup[0], tup[1])
    plt.hlines(tup[0],0,len(all_lengths), tup[1], label=tup[2])

for axvline in  axvlineXes:
    plt.axvline(axvline, color='pink')
plt.axvline(axvline, color='pink', label='generation')
    
plt.style.use('fivethirtyeight')
plt.legend(loc='upper left')
plt.show()
