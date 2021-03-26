'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

The driver- will fasilitate the game play and update the status board

known glitch/things to do as of 12.10.20
    - make a quit button
    - add more images to configuration for testing 
    - more informational messages for bad user input
    - make a prettier 'you've won .gif'
    - lots of global variables, will fix if I have time

'''

import turtle
from deck import Deck
from Click import * # only contains get_button
from Board import *
from LeaderBoard import *

# global variables are not good coding. I acknowledge and will fix if I have time
current_card = -1
status = 1
first_card = -1
move_count = 0
match_count = 0
playing = 1
deck = ''
name = ''
playing = True

no_click = 0 # you can't click anything while the cards are flipping

# for displaying text
status_turtle = turtle.Turtle()
status_turtle.pu()
status_turtle.ht()
status_turtle.setposition((-350,-225))
    
def on_click(x,y):
    ''' Function: on_click - takes the x and y cords of an on screen click and responds accordingly
        Parameters:  x & y ints - the cords passed by a screen.onclick()
        Returns - None. Just makes the game respond to the click
    '''
    ''' Okay so like idealy, I would pass all of these as parameters to get rid of the need for globals since
they are bad practice. But I can only pass two parameters to on_click and still have it be the function
recieving the cords from screen.onclick().  
    '''
    global current_card
    global status
    global first_card
    global playing
    global deck
    global name
    global playing

    # checks if the click was over a card
    click = check_button(x,y) 

    # if a card was clicked and the selected card is on the table
    if type(click) == int and click in deck.table and no_click == 0:
        
        current_card = click # index of the clicked card in deck.box
        
        if status == 1: # first card selected for the turn
            first_card = current_card
            first_click()
        elif status == 2 and current_card != first_card: # one card flipped and a new one clicked on
            second_click(first_card)
            status_turtle.clear() # update the status counter display
            status_turtle.write('Turns: ' +  str(move_count) + '           Matches: ' + str(match_count), font=("Arial", 30, "normal"))

    if len(deck.table) == 0: # no cards on the table, game over
        update_leader_board(name,move_count) # update the LeaderBoard.txt file
        # display Congrats message
        screen.addshape('game_over.gif')
        t = turtle.Turtle()
        t.shape('game_over.gif')
        playing = False
        
        

def first_click():
    global status
    global deck
    
    deck.box[first_card].flip() # flip over the selected card
    
    status = 2 # keep track of how many cards are flipped over

    
def play_game(deck,screen):
    # will need to add a check for the quit button eventually    
    global current_card
    
    if len(deck.table)>0: # while there are cards on the table
            screen.onclick(on_click)

        
def second_click(first_card):
    global status
    global move_count 
    global match_count
    global no_click
    global deck

    deck.box[current_card].flip() # flip the selected card
    
    move_count = move_count + 1 # incriment the move 
    status = 1 # update status so first_click() runs on the next click
    
    # if the cards are a match
    if deck.box[first_card].__eq__(deck.box[current_card]):
        match_count = match_count + 1 # increase match count
        deck.box[first_card].matched(deck.box[current_card]) # take cards off table

        # remove the two cards from the deck.table list
        deck.table.pop(deck.table.index(first_card))
        deck.table.pop(deck.table.index(current_card))
        
    else:
        no_click = 1
        screen.ontimer(delay(0,0),1000) # delay a bit
 
        # flip both cards
        deck.box[first_card].flip()
        deck.box[current_card].flip()

        no_click = 0


def main():
    
        global deck
        global name

        #turtle.mainloop()

    # create the screen object to run the game on
        screen = turtle.Screen()
        screen.setup(1000,600)
        screen.screensize(1000,600)
    
        name = get_name() 
        card = get_card_number()

        
        draw_board()
        
        status_turtle.write('Turns: ' +  str(move_count) + ' Matches: ' + str(match_count), font=("Arial", 30, "normal"))
        deck = Deck(card)#deck = Deck(card)

        play_game(deck,screen)
    
main()
turtle.done() #keeps window open when not run through IDLE
