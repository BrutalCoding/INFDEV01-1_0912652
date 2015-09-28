from random import randint

#Assign default values
x = 1
y = 1

#===Definitions===
#Status of the battle
def displayBattleStatus(userObject, AIObject, result):
    if userObject == 1:
        x = "ROCK"
    elif userObject == 2:
        x = "PAPER"
    elif userObject == 3:
        x = "SCISSORS"

    if AIObject == 1:
        y = "ROCK"
    elif AIObject == 2:
        y = "PAPER"
    elif AIObject == 3:
        y = "SCISSORS"

    if result == "win":
        print x, "(you) is stronger than", y
    elif result == "lose":
        print x, "(you) is weaker than", y
    elif result == "draw":
        print x, "(you) is just as strong as", y

#Let the user make a choice:
def selectTactic():
    print('Hello, choose a number to select your tactic\n')
    userInput = raw_input('1. Rock\n2. Paper\n3. Scissors\n')
    if userInput.isdigit():
        return int(userInput)
    print "No valid input detected, default selection has been chosen for you: #1 (ROCK)"
    return 1

def runGame():
    #Program
    userSelection = selectTactic()
    AISelection = randint(1,3)
    if(userSelection <= 3 & userSelection >= 1):
        print '\nYou have chosen for #',userSelection
        print 'AI has chosen for #',AISelection

        #Match results:
        def playAgainQuestion():
            playAgain = raw_input("Would you like to play again? Y or N\n")
            if playAgain == "Y":
                runGame()
        def resultPlayerWin(userObject, AIObject):
            displayBattleStatus(userObject, AIObject, "win")
            print "\n===You have won. The AI has lost.==="
            playAgainQuestion()
        def resultPlayerLose(userObject, AIObject):
            displayBattleStatus(userObject, AIObject, "lose")
            print "\n===You have lost. The AI has won.==="
            playAgainQuestion()
        def resultDraw(userObject, AIObject):
            displayBattleStatus(userObject, AIObject, "draw")
            playBattleStatus(userObject, AIObject, "draw")
            print "\n===It is a draw, better luck next time!==="
            playAgainQuestion()
        #Choices: 1 = Rock | 2 = Paper | 3 = Scissors
        if(userSelection == 1 and AISelection == 1):
            resultDraw(1,1)
        elif(userSelection == 1 and AISelection == 2):
            resultPlayerLose(1,2)
        elif(userSelection == 1 and AISelection == 3):
            resultPlayerWin(1,3)
        elif(userSelection == 2 and AISelection == 1):
            resultPlayerWin(2,1)
        elif(userSelection == 2 and AISelection == 2):
            resultDraw(2,2)
        elif(userSelection == 2 and AISelection == 3):
            resultPlayerLose(2,3)
        elif(userSelection == 3 and AISelection == 1):
            resultPlayerLose(3,1)
        elif(userSelection == 3 and AISelection == 2):
            resultPlayerWin(3,2)
        elif(userSelection == 3 and AISelection == 3):
            resultDraw(3,3)

#Start the application
runGame()