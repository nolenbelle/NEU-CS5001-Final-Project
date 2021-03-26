'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

Function check_button - Will take the x and y coordinates
of the click and will return an integer if the click was 'on a card'. The returned int serves as the index #
of where the clicked on card is stored in the deck.box

area  - a list containing tuples of tuples which correspond to the x min and max & the y min and max
coordinates of each card displayed on the table. 

'''

area = [((160, 250), (75, 225)), ((160, 250), (-100, 50)), ((45, 135), (75, 225)), ((45, 135), (-100, 50)), ((-70, 20), (75, 225)), ((-70, 20), (-100, 50)), ((-185, -95), (75, 225)), ((-185, -95), (-100, 50)), ((-300, -210), (75, 225)), ((-300, -210), (-100, 50)), ((-415, -325), (75, 225)), ((-415, -325), (-100, 50))]

            
def delay(x,y):
    x = 0
    y = 0


def check_button(x,y):
    ''' Function: check_button - checks if an on screen click was on a card
        Parameters: x (int), y (int) - coordinates of click
        Return- int - the index of the card stored in deck.box if a click on a card or string if not
    '''
    for i in range(12): 
        if area[i][0][0] <= x and area[i][0][1] >= x: # check valid x
            if area[i][1][0] <= y and area[i][1][1] >= y: # check valid y
                return(i)
    return ('invalid')

