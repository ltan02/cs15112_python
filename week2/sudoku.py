from tkinter import *
import math
import string
import copy
import decimal


def starterBoard():
    return [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 8, 1, 3, 9, 6, 2, 4],
        [4, 9, 6, 8, 7, 2, 1, 5, 3],
        [9, 5, 2, 3, 8, 1, 4, 6, 7],
        [6, 4, 1, 2, 9, 7, 8, 3, 5],
        [3, 8, 7, 5, 6, 4, 0, 9, 1],
        [7, 1, 9, 6, 2, 3, 5, 4, 8],
        [8, 6, 4, 9, 1, 5, 3, 7, 2],
        [2, 3, 5, 7, 4, 8, 9, 1, 6]
    ]


def isPerfectSquare(number):  # taken from hw1 written by me
    if math.sqrt(number) ** 2 == number:
        return True
    else:
        return False


def drawThickerLines(canvas, data):
    boardLength = len(data.board)
    x0, y0 = data.margin, data.margin
    x1, y1 = data.margin, data.width - data.margin
    increment = ((data.width - (data.margin * 2)) / int(math.sqrt(boardLength))
                 - 2)

    for eachCol in range(0, boardLength + 1, int(boardLength ** 0.5)):
        canvas.create_line((x0, y0), (x1, y1), width=5)
        x0 += increment
        x1 += increment

    x0, y0 = data.margin, data.margin
    x1, y1 = data.height - data.margin, data.margin

    for eachRow in range(0, boardLength + 1, int(boardLength ** 0.5)):
        canvas.create_line((x0, y0), (x1, y1), width=5)
        y0 += increment
        y1 += increment


def addingNumbers(canvas, data):
    boardLength = len(data.board)
    distanceBetweenLines = ((data.width - data.margin) // boardLength) - 1
    # Finding the length of each square, where the number goes
    startCenter = data.margin + (distanceBetweenLines / 2)
    centerX, centerY = startCenter, startCenter
    for eachRow in range(boardLength):
        for eachCol in range(boardLength):
            if data.board[eachRow][eachCol] != 0:
                text = str(data.board[eachRow][eachCol])
                if data.newArray[eachRow][eachCol]:
                    # The color is different if it isn't an number on the
                    # initial board
                    textColor = "black"
                else:
                    textColor = "blue"
                canvas.create_text(centerX, centerY, text=text, fill=textColor,
                                   font="Arial 20")

            centerX += distanceBetweenLines
        centerX = startCenter
        centerY += distanceBetweenLines


def notChangingInitialNumbers(data):
    newArray = []
    for eachRow in range(data.boardLength):
        tempArray = []
        for eachCol in data.board[eachRow]:
            if eachCol != 0:
                tempArray.append(0)
            else:
                tempArray.append(1)
        newArray.append(tempArray)
        # a list of 1s and 0s that correspond to whether it is empty or has a
        # number, before anything is entered
    return newArray


def drawSudokuBoard(canvas, data):
    for eachRow in range(len(data.board)):
        for eachCol in range(len(data.board[0])):
            if (eachRow == data.highlightedRow) and (
                    eachCol == data.highlightedCol):
                color = "yellow"
                # creates the highlighted box
            else:
                color = "white"

            (x0, y0) = ((data.blockDistance * eachCol) + data.margin,
                        (data.blockDistance * eachRow) + data.margin)
            (x1, y1) = ((data.blockDistance * (eachCol + 1)) + data.margin,
                        (data.blockDistance * (eachRow + 1)) + data.margin)
            canvas.create_rectangle((x0, y0), (x1, y1), fill=color)

    addingNumbers(canvas, data)
    drawThickerLines(canvas, data)

    if victory(data):
        canvas.create_rectangle(0, 0, data.width, data.height, fill="white")
        canvas.create_text(data.width / 2, data.height / 2,
                           text="Victory Royale", font="Arial 90")


def areLegalValues(values):
    if len(values) == 0:
        return False

    for eachValue in values:
        if not(isinstance(eachValue, int)):
            # Checks if it is an int
            return False
        elif eachValue < 0:
            # Makes sure it is a positive number
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


def direction(event, data):
    # Changes the highlighted box depending on which arrow key is pressed
    if event.keysym == "Up":
        data.highlightedRow -= 1
        if data.highlightedRow < 0:
            data.highlightedRow = (data.boardLength - 1)
    elif event.keysym == "Down":
        data.highlightedRow += 1
        if data.highlightedRow >= data.boardLength:
            data.highlightedRow = 0
    elif event.keysym == "Right":
        data.highlightedCol += 1
        if data.highlightedCol >= data.boardLength:
            data.highlightedCol = 0
    elif event.keysym == "Left":
        data.highlightedCol -= 1
        if data.highlightedCol < 0:
            data.highlightedCol = (data.boardLength - 1)


def victory(data):
    for eachRow in range(data.boardLength):
        for eachCol in range(data.boardLength):
            if data.board[eachRow][eachCol] == 0:
                return False
    return True


####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.board = starterBoard()
    data.margin = 5
    data.highlightedCol, data.highlightedRow = 0, 0
    data.blockDistance = ((data.width - data.margin) // len(data.board)) - 1
    data.boardLength = len(data.board)
    data.boardPixelLength = ((data.width - (data.margin * 2)) / int(math.sqrt(
        data.boardLength)))
    data.number = 0
    data.x0 = (data.boardPixelLength + (data.blockDistance *
                                        data.highlightedCol))
    data.y0 = (data.boardPixelLength + (data.blockDistance *
                                        data.highlightedRow))
    data.x1 = (data.boardPixelLength + (data.blockDistance *
                                        (data.highlightedCol + 1)))
    data.y1 = (data.boardPixelLength + (data.blockDistance *
                                        (data.highlightedRow + 1)))
    # The coordinates are all for working out where to draw the highlighted box
    data.newArray = notChangingInitialNumbers(data)


def mousePressed(event, data):
    # use event.x and event.y
    col = event.x // data.blockDistance
    row = event.y // data.blockDistance
    data.highlightedCol = col
    data.highlightedRow = row


def keyPressed(event, data):
    # use event.char and event.keysym
    direction(event, data)
    if event.keysym == "BackSpace" and data.newArray[data.highlightedRow][
            data.highlightedCol]:
        data.board[data.highlightedRow][data.highlightedCol] = 0
    elif event.keysym.isdigit() and int(event.keysym) > 0 and int(
            event.keysym) < 10:
        beforeValid = data.board[data.highlightedRow][data.highlightedCol]
        # Takes in what was inside the cell to make sure that the player isn't
        # adding numbers that is incorrect.
        data.board[data.highlightedRow][data.highlightedCol] = int(event.keysym)
        if not(isLegalSudoku(data.board)):
            # if it isn't a legal move then it will revert back to what it was
            # before.
            data.board[data.highlightedRow][data.highlightedCol] = beforeValid
        data.number = event.keysym


def redrawAll(canvas, data):
    # draw in canvas
    drawSudokuBoard(canvas, data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

        # Set up data and call init
    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
              mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
              keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(600, 600)
