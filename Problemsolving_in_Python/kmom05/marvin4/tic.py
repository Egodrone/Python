#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tic Tac Toe game.
Press 's' to save the state to the file and press 'l' to load the
state from the file.
"""
from random import randint


filename = 'tictactoe.txt'
megaTic = []
checkArr = []

def createMatrix(y, x, filler):
    """
    Create a two-dimensional array and return it.
    """
    return [[filler for _ in range(x)] for _ in range(y)]



def printMatrix(matrix):
    """
    Print the content of the matrix.
    """
    for row in matrix:
        print("".join(row))



def saveMatrix(matrix):
    """
    Save the content of the matrix to a file. Do this by joining all items in the
    list and create a string-representing the row and write that string to the file.
    Add a newline to each row.
    """
    with open(filename, 'w') as f:
        for row in matrix:
            f.write("".join(row) + '\n')

    print("Saved the state to the file {}".format(filename))



def loadMatrix(matrix):
    """
    Load the content of the matrix from a file. Do this by reading the lines from the file
    and splitting them into a list by characters.
    Ignore the newline at each row.
    """
    with open(filename, 'r') as f:

        # with \n
        #content = f.readlines()

        # without \n
        content = f.read().splitlines()

        # Update each row of the matrix and fill it by using the file content
        # (may need som care when file and matrix size does not match)
        for y in range(0, len(matrix)):
            matrix[y] = list(content[y])

    print("Loaded the state from the file {}".format(filename))

def checkIfbusy(number, fhit=1):
    '''function '''
    if(fhit > 1):
        lenarr = len(checkArr)
        for x in range(0, lenarr):
            if(checkArr[x] == number):
                return print("Upptagen")

def convertRowCol(row, col):
    '''function'''
    number = 0
    if(row == 0 and col == 0):
        number = 1
    elif(row == 0 and col == 1):
        number = 2
    elif(row == 0 and col == 2):
        number = 3
    elif(row == 1 and col == 0):
        number = 4
    elif(row == 1 and col == 1):
        number = 5
    elif(row == 1 and col == 2):
        number = 6
    elif(row == 2 and col == 0):
        number = 7
    elif(row == 2 and col == 1):
        number = 8
    elif(row == 2 and col == 2):
        number = 9
    else:
        print("Incorrect input")
    return number

def main():
    """
    Main function to carry out the work.
    """

    #print("Enter the size of the matrix.")
    y = 3
    x = 3
    print("---------")
    matrix = createMatrix(y, x, "|_|")
    print("---------")
    counter = 0
    playerBol = True
    while 1:
        firstHit = 0
        printMatrix(matrix)

        # Swap between X and O
        if counter % 2:
            char = "|O|"
        else:
            char = "|X|"

        counter += 1

        # Get a position to place the character
        if playerBol is True:
            print("Your turn!")
            firstHit = firstHit + 1
            posY = input("Set row to:  ")
            posX = input("Set a column (or q for quit): ")
            number1 = convertRowCol(int(posY), int(posX))
            if(firstHit == 1):
                checkArr.append(number1)
                print("First number busy in array")
                print(checkArr[0])
            else:
                #test if busy
                checkIfbusy(number1, firstHit)
            playerBol = False
        else:
            firstHit = 100
            print("Marvins turn")
            #marvin generate and test if numberes is in the matrix
            row1 = randint(0, 2)
            column1 = randint(0, 2)
            number1 = convertRowCol(int(row1), int(column1))
            checkIfbusy(number1, firstHit)
            posY = row1
            posX = column1
            playerBol = True

        if posY == "q" or posX == "q":
            break

        elif posY == "s" or posX == "s":
            saveMatrix(matrix)
            continue

        elif posY == "l" or posX == "l":
            loadMatrix(matrix)
            continue

        #Place the character
        matrix[int(posY)][int(posX)] = char



if __name__ == "__main__":
    print(__doc__)
    input("Press enter to continue.")
    main()
