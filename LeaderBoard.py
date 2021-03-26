'''
Proj - Memory Game
CS5001 Fall 2020
Nolen Belle Bryant

Contains just one function which given the name and score of the most
recent game, it updates LeaderBoard.txt accordingly

- idealy this function would have been a bit more modular, broken up into smaller chunks, I
will come back and do so if I have time.

'''

    
def update_leader_board(name, score):
    ''' Function: update_leader_board - updates the LeaderBoard.txt file if appropriot
        Parameters: name (str) - the user name of the last game
                               score (int) - how many turns it took to complete the last game
        Returns - none - the LeaderBoard.txt file is rewritten
    '''
    
    leaders = []
    scores = []
    no_go = 0 # used to help me track when if blocks are being done

    text = '' # if nothing in the LeaderBoard.txt, this remains empty
      
    with open('LeaderBoard.txt', mode='r') as infile:
        text = infile.read()
        text= text.split("\n")


    if len(text) == 1 and len(text[0]) == 0: # if leader board empty
        with open('LeaderBoard.txt', mode='w') as infile:
            line = name + ': ' + str(score)
            char = infile.write(line)
        no_go = 1      # don't want to enter any other code blocks,  job done 
                   
    if no_go == 0 and len(text[0]) > 0 : # at least on score on the board
        for i in range(len(text)): # populate the two list types
            info = text[i].split(': ')
            leaders.append(info[0])
            scores.append(int(info[1]))

    # the board not full and the new score is the new worst score
    if no_go == 0 and len(text)<8 and score >= scores[-1]: 
        leaders.append(name)
        scores.append(score)
        with open('LeaderBoard.txt', mode='w') as infile:
            for i in range(len(scores)-1):
                infile.write(leaders[i] + ": " + str(scores[i]) + '\n')
            infile.write(leaders[-1] + ': ' + str(scores[-1])) # don't want extra new lines at the end
        
    # the new score goes somewhere other than last on the board
    elif no_go == 0: 
        for i in range(len(scores)): # check against all scores currently on the board
            if score < scores[i]: # if the new score is lower than a score on the board
                if i == len(scores)-1 and len(scores) == 8: # if it is only smaller than last place on a full board
                    print('New score is new last place')
                    leaders[i] = name
                    scores[i] = score          
                    break # done w/ the loop because this updated the last one

                # this holds the value of the score which is being replaced by the new score
                temp_leader = leaders[i]
                temp_score = scores[i]

                # add new score to the lists
                leaders[i] = name
                scores[i] = score
                j = 0

                # move each subsiquent score to one place lower on the list
                for j in range(i+1,len(scores)):
                    next_leader = leaders[j]
                    next_score = scores[j]
                    leaders[j] = temp_leader
                    scores[j] = temp_score
                    temp_leader= next_leader
                    temp_score = next_score

                # add te last score outside of the loop to avoid indexing errors    
                leaders.append('')
                scores.append('')
                leaders[-1] = temp_leader
                scores[-1] = temp_score
                break

        if len(leaders) > 8: # if a score needs to be pushed off the display
            leaders = leaders[:8]
            scores = scores[:8]
            
        with open('LeaderBoard.txt', mode='w') as infile:
            print()
            for i in range(len(scores)-1):
                infile.write(leaders[i] + ": " + str(scores[i]) + '\n')
            infile.write(leaders[-1] + ': ' + str(scores[-1])) # don't want extra new lines at the end

