#Created a number guess game using random library in python for fun purpose.

from random import shuffle

#User Guess
def userInput():
    guess=' '
    while guess not in ['0','1','2']:
        guess=input('Guess a number between 0,1 or 2:\n')
    return int(guess)

def checkGuess(mylist,x):
    if mylist[x]=='0':
        print("Congrats! You won.")
        new = int(input("Press 1 to play again and 0 to exit.\n"))
    else:
        print("Oops! You lost.")
        new=int(input("Press 1 to play again and 0 to exit.\n"))
    return new

new=1
while new==1:
    # Created a list
    mylist = ['', '0', '']
    # Random shuffling of list
    shuffle(mylist)
    #Take user input
    x=userInput()
    #Check the user's guess
    new=checkGuess(mylist,x)
