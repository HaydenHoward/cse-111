"""
Tic tac toe game. User places x's while the computer places the o's.
"""

import turtle
import math
import random
import time

# Global variables for the functions to access

# Create the turtle
drawer = turtle.Turtle()
announcer = turtle.Turtle()
turtle.title("Tic Tac Toe")

drawer.pensize(10)
drawer.ht()

announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("maroon")

# Create a screen
screen = turtle.Screen()
screen.tracer(0)
screen.bgcolor("gainsboro")

# Create the board
board = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(" ")
    board.append(row)

def main():

    drawBoard()

    # activates the listeners
    activate(functions)
    screen.listen()

    # Keeps screen open
    turtle.done()

def drawBoard():
    drawer.pencolor("dim grey")
    # Draw the horizontal lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-315, 100 -200 *i)
        drawer.pendown()
        drawer.forward(620)
    
    drawer.right(90)

    # Draw the vertical lines
    for i in range(2):
        drawer.penup()
        drawer.goto(-100 + 200 * i, 300)
        drawer.pendown()
        drawer.forward(600)
    
    addNumber()

    # Update screen with changes
    screen.update()
    return True

def addNumber():
    # Adding numbers in the square
    drawer.color("black")
    num = 1
    for i in range(3):
        for j in range(3):
            drawer.penup()
            drawer.goto(-290 + j * 200, 280 - i * 200)
            drawer.pendown()
            drawer.write(num, font = ("Arial", 12, "bold"))
            num += 1
    return True

# Draws an x
def drawX(x, y):
    # Moving to the correct spot
    drawer.pencolor("cornflower blue")
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    
    # sets the direction at an angle
    drawer.setheading(60)

    # Draw the lines of the x
    for i in range(2):
        num = random.randint(65,85)
        drawer.forward(num)
        drawer.backward(150)
        drawer.forward(num)
        drawer.left(60)
    
    # Update screen
    screen.update()
    return True

# Draws an o
def drawO(x, y):
    # Moving to the correct spot
    drawer.pencolor("sea green")
    drawer.penup()
    drawer.goto(x,y + 75)
    drawer.pendown()

    drawer.setheading(0)

    # Draw a circle with the correct size
    for i in range(180):
        drawer.forward((150 * math.pi)/180)
        drawer.right(2)
    
    screen.update()
    return True

# Checks if the player has won
def checkWon(letter):
    # Check if there are three in a row horizontally
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
            return True
        
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
            return True
    
    # Check if there are three in a row vertically
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
        return True
    
    # Check if there are three in a row diagonally
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
        return True

    # If no one won yet
    return False

# Checks if the game is a tie
def checkTie():
    # Count the number of x's on the board
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "x":
                count += 1
    # Check what the value of count was
    if count > 4:
        return True
    else:
        return False

# Will add an o to the board
def addO():
    # Check if any places would result in a win for o
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                if checkWon("o"):
                    drawO(-200 + 200 * j, 200 -200 * i)
                    return
                board[i][j] = " "

    # Check if there is any place that o should block x
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "x"
                if checkWon("x"):
                    board[i][j] = "o"
                    drawO(-200 + 200 * j, 200 -200 * i)
                    return
                board[i][j] = " "
    # Try to place an o in one of the corners
    for i in range(0, 3, 2):
        for j in range(0, 3, 2):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "o"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return

# Activates the event listeners
def activate(functions):
    for i in range(9):
        screen.onkey(functions[i], str(i + 1))
        # turtle.onclick(functions[2])
        
    return True

# Deactivates the event listeners
def deactivate():
    for i in range(9):
        screen.onkey(None, str(i + 1))
    return True

# This function will add a x to the inputted location
def addX(row, column):
    # Clear any announcements on screen
    announcer.clear()
    # Check if the space is taken
    if board[row][column] == "x" or board[row][column] == "o":
        # Tell the spot is take
        announcer.write("That spot is taken!", font=("Arial", 36))
        screen.update()
    else:
        # Draw an x in the correct spot
        drawX(-200 + 200 * column, 200 - 200 * row)

        # Add an x to the computer's board
        board[row][column] = "x"

        # Check if x wins
        if checkWon("x"):
            # tell the use they won
            announcer.goto(-97, 0)
            announcer.write("You Won", font = ("Arial", 36))

            # Update the screen and deactivate the event listeners
            screen.update()
            deactivate()
        else:
            # If they didn't win, then an o get added to the board
            time.sleep(.5)
            addO()

            # Check if O won
            if checkWon("o"):
                # Tell player they lost
                announcer.goto(-90, 0)
                announcer.write("You lost", font=("Arial", 36))

                # Update the screen and deactivate the event listeneres
                screen.update()
                deactivate()
            # Check if there is a tie
            elif checkTie():
                # Tell the play they tied with the computer
                announcer.goto(-90,0)
                announcer.write("Tied Game", font = ("Arial", 36))

                # Update screen and event listeners
                screen.update()
                deactivate()
    return True

# Define functions for event listneners
def squareOne():
    addX(0, 0)
def squareTwo():
    addX(0, 1)
def squareThree():
    addX(0, 2)
def squareFour():
    addX(1, 0)
def squareFive():
    addX(1, 1)
def squareSix():
    addX(1, 2)
def squareSeven():
    addX(2, 0)
def squareEight():
    addX(2, 1)
def squareNine():
    addX(2, 2)

# list of event listener functions
functions = [squareOne, squareTwo, squareThree, 
squareFour, squareFive, squareSix, squareSeven, 
squareEight, squareNine]

if __name__ == "__main__":
    main()