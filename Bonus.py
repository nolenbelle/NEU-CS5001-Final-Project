'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

Bonus points

Alright listen, I'm aware that this approach is pretty inefficient at least as
far as creating 2 new .gifs per gif in the config file goes. Ideally I'd just use
stamp and not need individual gifs for each card object. BUT, it's just gotta run
to get the bonus points, so se la vie.

Also... It really only works ~perfectly~ if the .gifs are correctly sized which for my fame is 90 x 150. You
can play it with whatever size they come as. It does work! The UI is just messed up, and I couldn't figure
out a way to program the .gif to resize without downloading the PIL module to used Pillow which just...
seemed like too much work for .05 pts on the final grade. But it does work!
'''

from shutil import copyfile # to make copies of the povided .gifs
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape

from Shuffle import shuffle

def bonus_points():
    ''' Function: bonus_points - will run the game with user provided images if there exists a configuration.txt
                                                    file which contains at least 6 .gif file names
        Parameters - none
        Returns - boolean for if there exists a configuration file,
                          list empty in the case of no config or containing 6 random .gif files names if config present
    '''
    try:
        with open('memory.txt', mode='r') as infile: # config file named memory in the demo video
            text = infile.read()
            images = text.split("\n") # list of gif names 
    except FileNotFoundError: # in the event that there is no file
        return False, []

    images = shuffle(images) # shuffle them incase more than 6 provided
    images = images[:6] # only need max of 6 for the 12 cards 

    new_images = []

    for gif in range(len(images)):
        # create duplicates and formate the name as needed to run in the Card class
        new_gifA = images[gif][:-4] + 'A' + '.gif'
        new_gifB = images[gif][:-4] + 'B' + '.gif'
        
        copyfile(images[gif], new_gifA)
        copyfile(images[gif], new_gifB)

        new_images.append(new_gifA)
        new_images.append(new_gifB)


    return True, new_images #list of 12 .gifs

'''
def resize(gif): # doesn't work bc zoom() must have ints
    screen = Screen()
    new = PhotoImage(file=gif)
    old_height = new.height()
    old_width =  new.width()
    height_ratio = 150/old_height
    width_ratio = 90/old_width

    return PhotoImage(file=gif).zoom(height_ratio, width_ratio)

resize('config_prebble.gif')
'''
