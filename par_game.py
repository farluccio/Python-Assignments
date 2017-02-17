# Scratch game developed for an exercise displaying various techniques such as for loops, while loops, if/then statements
#
# Written by Eric Farley 02/16/207 using Python 2.7.13

def start_golf(holeNumber = 0):
    introTuple = ('Number Golf is a game where you try to guess the winning number in the fewest guesses possible.',
                  '\nEach guess is a stroke.  You want to get to the number in the fewest strokes possible.',
                  '\nYou will get hints for how close you are to the number.',
                  '\nThe further away you are the more general the hint will be.')
    for item in introTuple:     # iterating through tuple to print assigned lines
        print item
    holeNumber = round_selection(holeNumber)     # Getting user input for the number of times they want to play
    totalStrokes = winning_number(holeNumber)      # Calling the guessing part of the game, cycles through par 3, 4, & 5
    finish_game(holeNumber, totalStrokes)
                

def round_selection(holeNumber):        # User input for number of times they would like to play
    holeNumber = input('\nHow many holes would you like to play? 3, 6, or 9? ')
    check = True
    while check:
        if holeNumber == 3 or holeNumber == 6 or holeNumber == 9:   # Use of if then statements
            check = False
        else:
            print('Please select 3, 6, or 9.')      # Validating user input
            holeNumber = input('How many holes would you like to play? 3, 6, or 9? ')
    return holeNumber
    
def winning_number(holeNumber):
    totalStrokes = []       # Assigning a string to a variable
    from random import randint
    counter = 0     # Assigning an integer to a variable
    while counter < (holeNumber / 3):        # This while loop cycles through the number of rounds selected by user
        counter += 1
        for par in range(1,4):                  # This for loop will cycle through a round of 3 holes
            stroke = 0
            rangeDistance = 30
            winningNumber = randint(0,(rangeDistance * par))
            print '\nA number between 0 and {} has been selected.'.format((rangeDistance * par))
            guess = input('Which number would you like to guess? ')
            stroke += 1
            print 'Stroke: {}'.format(stroke)  # add .format here
            print 'You guessed: {}'.format(guess)
            '''while type(guess) != int:   # validating user input
                guess = input('Please try a different guess.  Choose a number between 0 and ' + str(rangeDistance * par) + ': ')
                print('You guessed: ' + str(guess))'''  # I was going to validate user input.  The input command already accepts a int value.
            if guess == winningNumber:       # This if/else statement is used to differentiate between a hole in one or move to a function to generate hints and cycle till user gets the answer
                print('Hole in 1.  Great job!')
            else:
                stroke = hint_generator(winningNumber, guess, stroke)
            totalStrokes.append((str(stroke)))
    return totalStrokes

def hint_generator(winningNumber, guess, stroke):       # function to give hints to help user get to correct answer and track strokes (number of guesses)
    while winningNumber != guess:
        distance = abs(winningNumber - guess)
        if distance <= 10:
            print 'You are within plus or minus {} paces of the hidden value.'.format(distance)
        if distance > 10 and distance <= 60:    # Use of logical operators
            addedHint = even_odd(winningNumber)
            print 'You are within plus or minus {} paces of the hidden value.'.format((distance + 3)) # adding some variance (could use random number for added difficulty)
            print 'It is an {} number.'.format(addedHint)
        if distance > 60:
            print 'You are within plus or minus {} paces of the hidden value.'.format((distance + 9)) # adding some variance (could use random number for added difficulty)
        guess = input('Which number would you like to guess? ')
        stroke += 1
        print stroke
        print 'You guessed: {}'.format(guess)
    print 'You got the hidden value: {}'.format(winningNumber)
    return stroke

def even_odd(winningNumber):
    x = winningNumber % 2       # Using % operator
    if x == 0:
        hint = 'even'
    else:
        hint = 'odd'
    return hint

def finish_game(holeNumber, totalStrokes):
    print '\nSCOREBOARD'
    averageStroke = 0.0     # assigning a float variable
    print type(averageStroke)
    for i in range(1, holeNumber + 1):      # for loop to cycle through string of hole values
        print 'Hole {}: {}'.format(i, totalStrokes[i - 1])
        averageStroke = averageStroke + int(totalStrokes[i-1])
    averageStroke = averageStroke / holeNumber
    print 'Average strokes per hole: {}'.format(averageStroke)
    print '\nThanks for playing!'
    exit()
    
if __name__ == "__main__":
    start_golf()
