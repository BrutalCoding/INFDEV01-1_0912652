import math
amount = raw_input("How many characters would you like to use?\n")
x = ""
def showFullSquare(amount, x): #done
    for h in range(amount):
        for w in range(amount):
            x += "*"
        x += "\n"
    return x

def showHollowSquare(amount, x):
    for h in range(amount):
        for w in range(amount):
            if h == 0 or h == amount -1:
                x += "*"
            else:
                if w == 0 or w == amount -1:
                    x += "*"
                else:
                    x += " "
        x += "\n"
    return x

def showRectangleTriangle(amount, x):
    for h in range(amount):
        for w in range(h +1):
            x += "*"
        x += "\n"
    return x

def showIsoscelesTriangle(amount, x):
    for h in range(amount):
        maxWidth = amount * 2 - 1
        for w in range(maxWidth):
            test = maxWidth - (w * 2)
            leftover = maxWidth - test
            for a in range(leftover):
                x += "."
            for b in range(test - 1):
                x += "*"
            x += "\n"
            
        x += "\n"
    return x

def showIsoscelesTriangle2(amount, x):
    asterisks = 1
    for h in range(amount):
        spaces = (amount * 2 - 1) - asterisks
        helft = spaces / 2
        for s in range(helft):
            x += " "
        for a in range(asterisks):
            x += "*"
        x += "\n"
        asterisks += 2                   
    return x


def printCircle(d, x):
    straal = d / 2 #Helft van diameter is de straal
    for h in range(d): #Hoogte
        for w in range(d): #Breedte
            test0 = h - straal
            test1 = w - straal
            afstand = math.sqrt(test0**2 + test1**2)
            if afstand < straal:
                x += "x"
            else:
                x += "."
        x += "\n"
    return x

def printSmiley(d, x):
    straal = d / 2 #Helft van diameter is de straal
    for h in range(d): #Hoogte
        for w in range(d): #Breedte
            test0 = h - straal
            test1 = w - straal
            afstand = math.sqrt(test0**2 + test1**2)
            if afstand < straal:
                x += "x"
            else:
                x += "."
        x += "\n"
    return x


if amount.isdigit():
    amount = int(amount)
    print printCircle(amount, x)