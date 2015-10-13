import math

amount = int(raw_input("Fill in the size:\n")) #User input
x = ""                                         #The string to print
figureChar = "*"                               #The character used to draw

def fullsquare(amount, x, figureChar):
    for h in range(amount):
        for w in range(amount):
            x += figureChar
        x += "\n"
    return x

def hollowsquare(amount, x, figurechar):
    for h in range(amount):
        for w in range(amount):
            if h == 0 or h == amount - 1 or w == 0 or w == amount - 1:
                x += figurechar
            else:
                x += " "
        x += "\n"
    return x

def triangle(amount, x, figurechar):
    for h in range(amount):
        for w in range(h + 1):
            x += figurechar
        x += "\n"
    return x

def hollowpyramid(amount, x, figurechar):
    figures = 1
    maxWidth = amount * 2 - 1
    for h in range(amount):
        for a in range(maxWidth):
            if a == maxWidth / 2 - h or a == maxWidth / 2 + h or h == amount - 1:
                x += "*"
            else:
                x += " "

        figures += 2
        x += "\n"
    return x

def pyramid(amount, x, figurechar):
    figures = 1
    maxWidth = amount * 2 - 1
    for h in range(amount):
        for a in range(maxWidth):
            if a == maxWidth / 2 - h or a == maxWidth / 2 + h or h == amount - 1:
                x += " "
            elif a < maxWidth / 2 - h or a > maxWidth / 2 + h or h == amount - 1:
                x += " "
            else:
                x += figurechar

        figures += 2
        x += "\n"
    return x

def circle(amount, x, figurechar):
    straal = amount / 2
    for h in range(amount):
        for w in range(amount):
            hx = h - straal
            wx = w - straal
            afstand = math.sqrt((wx**2) + (hx**2))
            if afstand < straal:
                x += " "
            else:
                x += "*"
        x += "\n"
    return x

print circle(amount, x, figureChar)