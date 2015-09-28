from random import randint

#===Definitions===
#Status of the battle
def displayBattleStatus(userObject, AIObject, result):
    #Assign default values
    x = 1
    y = 1

    if userObject == 1:
        x = "ROCK"
    elif userObject == 2:
        x = "PAPER"
    elif userObject == 3:
        x = "SCISSORS"
    elif userObject == 4:
        x = "LIZARD"
    elif userObject == 5:
        x = "SPOCK"

    if AIObject == 1:
        y = "ROCK"
    elif AIObject == 2:
        y = "PAPER"
    elif AIObject == 3:
        y = "SCISSORS"
    elif AIObject == 4:
        y = "LIZARD"
    elif AIObject == 5:
        y = "SPOCK"

    if result == "win":
        print x, "(you) is stronger than", y
    elif result == "lose":
        print x, "(you) is weaker than", y
    elif result == "draw":
        print x, "(you) is just as strong as", y

#Let the user make a choice:
def selectTactic():
    print('Hello, choose a number to select your tactic\n')
    userInput = raw_input('1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock\n')
    if userInput.isdigit():
        return int(userInput)
    userSelection = randint(1,5)
    print "No valid input detected, we're giving you number #",userSelection
    return userSelection

def runGame():
    #Program
    userSelection = selectTactic()
    AISelection = randint(1,5)
    if(userSelection <= 5 and userSelection >= 1):
        print '\nYou have chosen for #',userSelection
        print 'AI has chosen for #',AISelection

        #Match results:
        def playAgainQuestion():
            playAgain = raw_input("Would you like to play again? Y or N\n")
            if playAgain == "Y":
                runGame()
            else:
                print "Game finished.."
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
            displayBattleStatus(userObject, AIObject, "draw")
            print "\n===It is a draw, better luck next time!==="
            playAgainQuestion()

        #Choices: 1 = Rock | 2 = Paper | 3 = Scissors | 4 = Lizard | 5 = Spock
        if(userSelection == 1 and AISelection == 1):
            resultDraw(userSelection,AISelection)
        elif(userSelection == 1 and AISelection == 2):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 1 and AISelection == 3):
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 1 and AISelection == 4):
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 1 and AISelection == 5):
            resultPlayerLose(userSelection,AISelection)

        elif(userSelection == 2 and AISelection == 1):
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 2 and AISelection == 2):
            resultDraw(userSelection,AISelection)
        elif(userSelection == 2 and AISelection == 3):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 2 and AISelection == 4):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 2 and AISelection == 5):
            resultPlayerWin(userSelection,AISelection)

        elif(userSelection == 3 and AISelection == 1):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 3 and AISelection == 2):
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 3 and AISelection == 3):
            resultDraw(userSelection,AISelection)
        elif(userSelection == 3 and AISelection == 4):
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 3 and AISelection == 5):
            resultPlayerLose(userSelection,AISelection)

        elif(userSelection == 4 and AISelection == 1):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 4 and AISelection == 2):
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 4 and AISelection == 3):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 4 and AISelection == 4):
            resultDraw(userSelection,AISelection)
        elif(userSelection == 4 and AISelection == 5):
            resultPlayerWin(userSelection,AISelection)

        elif(userSelection == 5 and AISelection == 1):
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 5 and AISelection == 2):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 5 and AISelection == 3): 
            resultPlayerWin(userSelection,AISelection)
        elif(userSelection == 5 and AISelection == 4):
            resultPlayerLose(userSelection,AISelection)
        elif(userSelection == 5 and AISelection == 5): 
            resultDraw(userSelection,AISelection)  

#Start the application
runGame()