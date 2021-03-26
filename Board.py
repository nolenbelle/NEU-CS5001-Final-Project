'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

Sets up the playing board and the user inputs
'''
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
    

def draw_board():
    
    
   # status board
    t.pu()
    t.setpos((-450,-150))
    t.pd()
    t.goto(250,-150)
    t.goto(250,-250)
    t.goto(-450,-250)
    t.goto(-450,-150)

    # leader board
    t.pu()
    t.setpos((300,250))
    t.pd()
    t.goto(450,250)
    t.goto(450,-150)
    t.goto(300,-150)
    t.goto(300,250)
    t.pu()

    t.setposition((310,195))
    t.write('Leader Board:\n',font=("Arial", 15, "normal"))

    with open('LeaderBoard.txt', mode='r') as infile:
        leader_scores = infile.read()
        
    t.setposition((310,-25))
    t.write(leader_scores, font =("Arial", 15, "normal"))

def get_name():
    ''' Function: get_name - gets the desired user name from the player
        Parameters: none
        Returns - (str) the desired name or 'QUITCODE' if the user tried to exit the input box
    '''

    name = screen.textinput("Memory Game",
                            "Hello and welcome to Memory! Please entery your name to begin the game.")

    if name == None: # the user closed the box ie is quiting the game
        turtle.bye()

    return name

def get_card_number():
    ''' Function: get_card_number - gets the desired deck size from the player
        Parameters: none
        Returns - 'QUITCODE' if the user tried to exit the input box or the int of the desired deck 
    '''
    card = screen.textinput("Amount of card",
                            "Please input the amount of cards you want to play with:\nType: 8, 10, or 12")

    # this block checks that the box hasn't been closed and a number has been inputted
    if card == None: # the user closed the box ie is quiting the game
        turtle.bye()

    while type(card) == str:
        card = check_number(card)

    while card != 8 and card!= 10 and card != 12:
        try:
            card = screen.textinput("Amount of card",
                                    "Invalid input.\nPlease input the amount of cards you want to play with:\nType: 8, 10, or 12")
        # after every input, must recheck that the input is a number
            if card == None: # the user closed the box ie is quiting the game
                turtle.bye()

            while type(card) == str: # can't restart the outside while with a string
                card = check_number(card)

            if card == None: # the user closed the box ie is quiting the game
                turtle.bye()
   
            if card == 8 or card == 10 or card ==12:
                break
        except AttributeError:           
            turtle.bye()

    return card

def check_number(card):
    ''' Function: check_number - verifies that the uder input is an int
        Parameter: card (str) - the resutl of the user input
        Return - the user input as an int if valid or 'QUITCODE' if the user tried to exit the box

    '''
    try: # check that the input was a number
        if type(card) == None: # the user closed the box ie is quiting the game
            return 'QUITCODE'
        card = int(card)
        return card
    except ValueError: # user input a string
        card = screen.textinput("Amount of card",
                                "check_card failed.\nPlease input the amount of cards you want to play with:\nType: 8, 10, or 12")

        if type(card) == None: # the user closed the box ie is quiting the game
            turtle.bye()

        return card
