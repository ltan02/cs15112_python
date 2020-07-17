#################################################
# 15-112-n18 hw6
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

import math
import string
import copy
import decimal

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def isPerfectSquare(number):  # taken from hw1 written by me
    if math.sqrt(number) ** 2 == number:
        return True
    else:
        return False

#################################################
# hw6 problems
#################################################


def areLegalValues(values):
    if len(values) == 0:
        return False

    for eachValue in values:
        if not(isinstance(eachValue, int)):  # Checks if it is an int
            return False
        elif eachValue < 0:  # Makes sure it is a positive number
            return False
        elif not(isPerfectSquare(len(values))):  # makes sure the board is a perfect square
            return False
        elif eachValue > len(values):  # Makes sure the numbers are 0-N^2(inclusive)
            return False
        elif eachValue != 0 and values.count(eachValue) > 1:  # makes sure numbers only appear once, apart from 0
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

#################################################
# hw6 Test Cases
#################################################


def _verifyAreLegalValuesIsNondestructive():
    a = [1, 2, 3]
    b = copy.copy(a)
    areLegalValues(a)
    return (a == b)


def testAreLegalValues():
    print("Testing areLegalValues()...", end="")
    assert(_verifyAreLegalValuesIsNondestructive() == True)
    assert(areLegalValues([]) == False)
    assert(areLegalValues([0, 0, 1, 2, 3, 4, 5, 7, 0]) == True)
    assert(areLegalValues([1, 3, 2, 4]) == True)
    assert(areLegalValues([1, 2, 3, 0, 0]) == False)
    assert(areLegalValues([1, 1, 3, 2]) == False)
    assert(areLegalValues(['l', 1, 'k', 2]) == False)
    assert(areLegalValues([1, 4, 5, 3]) == False)
    assert(areLegalValues([0] * 64) == True)
    assert(areLegalValues([1] * 64) == False)
    print("Passed!")


def testIsLegalRow():
    print("Testing isLegalRow()...", end="")
    assert(isLegalRow([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 5) == True)
    assert(isLegalRow([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 11, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 2) == False)
    assert(isLegalRow([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 4, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 4) == False)
    assert(isLegalRow([
        [4, 3, 0, 0],
        [6, 0, 0, 1],
        [0, 2, 3, 0],
        [1, 0, 0, 0]
    ], 1) == False)
    assert(isLegalRow([
        [1, 2],
        [2, 1]
    ], 1) == False)
    print("Passed!")


def testIsLegalCol():
    print("Testing isLegalCol()...", end="")
    assert(isLegalCol([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 5) == True)
    assert(isLegalCol([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 11, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 1) == False)
    assert(isLegalCol([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 4, 6, 0, 0, 0, 3],
        [4, 0, 0, 0, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 3) == False)
    assert(isLegalCol([
        [4, 3, 0, 0],
        [6, 0, 0, 1],
        [0, 2, 3, 0],
        [1, 0, 0, 0]
    ], 0) == False)
    print("Passed!")


def testIsLegalBlock():
    print("Testing isLegalBlock()...", end="")
    assert(isLegalBlock([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 0) == True)
    assert(isLegalBlock([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 11, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ], 4) == False)
    assert(isLegalBlock([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 2, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 8, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 8, 0, 7, 9]
    ], 7) == False)
    assert(isLegalBlock([
        [4, 3, 0, 0],
        [6, 0, 0, 1],
        [0, 2, 3, 0],
        [1, 0, 0, 0]
    ], 1) == True)
    print("Passed!")


def testIsLegalSudoku():
    print("Testing isLegalSudoku()...", end="")
    assert(isLegalSudoku([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == True)
    assert(isLegalSudoku([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 3, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == True)
    assert(isLegalSudoku([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 9, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == False)
    assert(isLegalSudoku([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 2, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == False)
    assert(isLegalSudoku([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 'a', 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 2, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == False)
    assert(isLegalSudoku([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, -1, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 2, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == False)
    assert(isLegalSudoku([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 3, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 10, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]) == False)
    print("Passed!")

#################################################
# hw6 Main
#################################################


def testAll():
    testAreLegalValues()
    testIsLegalRow()
    testIsLegalCol()
    testIsLegalBlock()
    testIsLegalSudoku()


def main():
    testAll()


if __name__ == '__main__':
    main()
