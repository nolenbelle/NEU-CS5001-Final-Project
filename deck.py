'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

The deck class will contain instances of the card class, go figure

'''

from card import Card
from Shuffle import shuffle
from Bonus import bonus_points


class Deck:
    ''' Class: Deck - a collection of Card objects
       Attibutes:
           box - a list containing all of the card objects. not meant to be mutated
           table - a list containing the indexs of the card objects in deck.box which are considered 'in play'
       Methods:
           get_card() - returns the deck.box
    '''
    
    def __init__(self, card_number):
        '''
        will take parameter 8, 10, or 12
        '''
        self.box = [] # holds all the card objects
        self.table = [] # holds the cards on the table
        
        with open('positions.txt', mode='r') as infile: # where the cards get placed on the screen
            text = infile.read()
            position = text.split("\n")

        with open('card_front.txt', mode='r') as infile: # card front .gif file
            text = infile.read()
            card_front = text.split("\n")

        card_front = card_front[:card_number] # select only the deck size
        card_front = shuffle(card_front) # shuffle the cards each game

        pass_config, image_list = bonus_points() # test for configuration.txt file

        if pass_config: # there is a congiguration file
            image_list = image_list[:card_number] # select only the deck size
            card_front = shuffle(image_list) # shuffle the cards each game
        
        with open('card_back.txt', mode='r') as infile:
            text = infile.read()
            card_back = text.split("\n")
        card_back = card_back[:card_number]  # select only the deck size
                
        for i in range(card_number):
            # get the x and y positioning for each card
            position_info = position[i]
            position_info = position_info.split(", ")
            x = int(position_info[0])
            y = int(position_info[1])

            # get the front and back image of each card                           
            front = card_front[i]
            back = card_back[i]

            self.table.append(i) # add cards look up index to the 'on the table' list                 
            self.box.append(Card(front, back, x, y)) # add card object to 'box' of cards which are dealt
