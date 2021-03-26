'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

When creating a deck object, shuffle will be called to randomize the placement of the card objects
'''
import random
                            
##
##def shuffle(file,cards):
##    ''' Function: shuffle- shuffles the images displayed on the cards
##       Parameters: file (str) - a file containing the names of .gif files to be used as card images
##                             card (int) - the amount of cards to be shuffled
##       Return: none - the file is re-written in a randomized order
##
##    '''
##    with open(file, mode='r') as infile:
##        text = infile.read()
##        cards = text.split("\n")
##
##    temp = []
##
##    for i in range(len(cards)):
##        index_max = len(cards) - 1
##        rand = random.randint(0,index_max)
##        temp.append(cards.pop(rand))
##
##    cards = temp
##                    
##    with open(file, mode='w') as infile:
##        for i in range(len(cards)):
##            if i < len(cards)-1:
##                infile.write(cards[i])
##                infile.write('\n')
##            else:
##                infile.write(cards[i])

def shuffle(image_list):
    ''' Function: shuffle- shuffles the images displayed on the cards
       Parameters: image_list(list) - a list containg the .gif names of the images for the card
       Return: list - the list in a randomized order

    '''
    temp = []

    for i in range(len(image_list)):
        index_max = len(image_list) - 1
        rand = random.randint(0,index_max)
        temp.append(image_list.pop(rand))

    return temp

