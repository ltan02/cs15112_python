#################################################
# 15-112-n18 hw12
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

import math
import string
import copy
import decimal

#################################################################
# Homework 12 Helper Functions
#################################################################


def isPerfectSquare(number):  # taken from hw1 written by me
    if math.sqrt(number) ** 2 == number:
        return True
    else:
        return False


def areLegalValues(values):
    if len(values) == 0:
        return False

    for eachValue in values:
        if not(isinstance(eachValue, int)):  # Checks if it is an int
            return False
        elif eachValue < 0:  # Makes sure it is a positive number
            return False
        elif not(isPerfectSquare(len(values))):
            # makes sure the board is a perfect square
            return False
        elif eachValue > len(values):
            # Makes sure the numbers are 0-N^2(inclusive)
            return False
        elif eachValue != 0 and values.count(eachValue) > 1:
            # makes sure numbers only appear once, apart from 0
            return False
    return True


def isLegalRow(board, row):
    if areLegalValues(board[row]):  # checks every row is legal
        return True
    return False


def isLegalCol(board, col):
    tempColumn = []
    for eachRow in range(len(board)):
        tempColumn.append(board[eachRow][col])
    if areLegalValues(tempColumn):
        return True
    return False


def isLegalBlock(board, block):
    tempBlock = []
    rowIterations = (block // math.sqrt(len(board))) * math.sqrt(len(board))
    colIterations = (block % math.sqrt(len(board))) * math.sqrt(len(board))
    rowIterations, colIterations = int(rowIterations), int(colIterations)
    rowEnding = rowIterations + int(math.sqrt(len(board)))
    colEnding = colIterations + int(math.sqrt(len(board)))

    for eachRow in range(rowIterations, rowEnding):
        for eachCol in range(colIterations, colEnding):
            tempBlock.append(board[eachRow][eachCol])

    if areLegalValues(tempBlock):
        return True
    return False


def isLegalSudoku(board):
    for eachRow in range(len(board)):
        if not(isLegalRow(board, eachRow)):  # checks if rows are legal
            return False
        for eachCol in range(len(board)):  # checks if columns are legal
            if not(isLegalCol(board, eachCol)):
                return False
    for eachBlock in range(len(board)):  # checks if blocks are legal
        if not(isLegalBlock(board, eachBlock)):
            return False
    return True


def nextEmptyRowAndCol(board, row, col):
    # Looks for the next row and column that is empty rather than just looping
    # through every single element in the board
    while row < len(board) and col < len(board[0]):
        if board[row][col] == 0:
            return row, col
        col += 1
        if col == len(board):
            row += 1
            col = 0
    return row, col


def isCompletedSudoku(board):
    # Checks if the board is completed or not
    for eachRow in range(len(board)):
        for eachCol in range(len(board[0])):
            if board[eachRow][eachCol] == 0:
                return False
    return True


def validMove(board, row, col):
    lenOfBlock = int(math.sqrt(len(board)))
    # Finds the block in relation to the row and column
    block = row // lenOfBlock * lenOfBlock + col // lenOfBlock
    return(isLegalCol(board, col) and isLegalRow(board, row) and
           isLegalBlock(board, block))


def solveSudokuHelper(board, row=0, col=0):
    nextRow, nextCol = nextEmptyRowAndCol(board, row, col)
    if isCompletedSudoku(board):
        return board
    else:
        # Checks every number from 1 to the size of the board
        for number in range(1, len(board) + 1):
            # Sets the next row and col to the number being checked
            board[nextRow][nextCol] = number
            if validMove(board, row, col):
                # use recursion to get the next row and column and so on until
                # the board is complete
                tempSolution = solveSudokuHelper(board, nextRow, nextCol)
                if tempSolution != None:
                    return tempSolution
            # This is basically like an undo feature and will set the part of
            # the board back to 0 if it isn't legal
            board[nextRow][nextCol] = 0
    return None


#################################################################
# Homework 12 Solution
#################################################################

def solveSudoku(board):
    return solveSudokuHelper(board)


#################################################################
# Homework 12 Test Functions
#################################################################


def testSolveSudoku():
    print('Testing solveSudoku()...', end='')
    board1 = [
        [0, 1, 4, 2],
        [2, 0, 3, 0],
        [0, 3, 2, 0],
        [4, 2, 0, 0]]
    solved1 = solveSudoku(board1)
    solution1 = [
        [3, 1, 4, 2],
        [2, 4, 3, 1],
        [1, 3, 2, 4],
        [4, 2, 1, 3]]
    assert(solved1 == solution1)
    board2 = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solved2 = solveSudoku(board2)
    solution2 = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    assert(solved2 == solution2)
    board3 = [
        [0, 1, 2, 3],
        [0, 3, 1, 0],
        [1, 4, 0, 0],
        [0, 0, 4, 1]]
    solved3 = solveSudoku(board3)
    solution3 = [
        [4, 1, 2, 3],
        [2, 3, 1, 4],
        [1, 4, 3, 2],
        [3, 2, 4, 1]]
    assert(solved3 == solution3)
    print('Passed!')

#################################################################
# Homework 12 Main
#################################################################


def testAll():
    testSolveSudoku()


def main():
    testAll()


if __name__ == '__main__':
    main()
