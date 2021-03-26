'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

Card Class
'''
import turtle

class Card:
        ''' Class: Card - creates the playing card objects as turtle objects 
           Attributes:
                   turtle - each card contains a turtle obect and can therefore use turtle methods
                   front - the gif set as the front image
                   back - the gif set as the back image
                   ID - the identifier of the image (used for matching)
                   visible - the state of the card. when the card is 'image up', the visible = True
           Methods:
                   flip(self) - turns the card over
                   eq(self, otherCard) - returns true if both card have the same ID
                   matched(self, otherCard) - to be used when two cards are equal and to take both card
                                                                  off the table                  
        '''
        
        def __init__(self, front, back, x, y):
                ''' Parameters : front - the front gif of the card
                                           back - the back gif of the card
                                           x - the starting x coord of the card
                                           y - the starting y coord of the card
                '''

                screen = turtle.Screen()        
                self.turtle = turtle.Turtle()
                
                self.turtle.pu()
                
                screen.addshape(front)
                screen.addshape(back)
        
                self.turtle.shape(back)

                 # my attempt to resize but it will still display as the size of the .gif
                self.turtle.shapesize(4.5,7.5)
                self.turtle.turtlesize(4.5,7.5)

                self.turtle.setposition((x,y))

                self.ID = front[:-5] # the name of the image file without .txt
                
                self.front = front
                self.back = back
                
                self.visible = False # bicycle side up to start with

        def flip(self):
                ''' Function - 'flips' the card by displaying whichever image it is not currently displaying and
                        updates visibility to match
                   Parameters - none
                   Return - none
                '''
                if self.visible == False:
                        self.turtle.shape(self.front)
                        self.visible = True
                else:
                       self.turtle.shape(self.back)
                       self.visible = False


        def __eq__(self, otherCard):
                ''' Funtion - checks if two cards are equal ie if the match
                    Parameters - a card instance
                    Return - true if the two cards match, false if not
                '''
                return self.ID == otherCard.ID

        def matched(self, otherCard):
                ''' Function : matched - clears two card objects 'off the table'
                    Parameters - a card object
                    Return - none. 
                '''
                self.turtle.clear()
                otherCard.turtle.clear()
                self.turtle.ht()
                otherCard.turtle.ht()
