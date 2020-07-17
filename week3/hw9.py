#################################################
# 15-112-n18 hw9
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Andrew ID of People I Collaborated With: jeromef
# Your Section: A
#################################################

from tkinter import *
import random

#################################################
# Extra Features I did
#################################################

# Hard drop
# High Score List
# Pausing
# Instructions

#################################################
# Helper Functions
#################################################

# This function creates the starting board


def createBoardList(data):
    board = []
    for rows in range(data.rows):
        tempRow = []
        for cols in range(data.cols):
            tempRow.append(data.emptyColor)
        board.append(tempRow)
    return board

# This function draws the board


def drawBoard(canvas, data):
    for row in range(len(data.board)):
        for col in range(len(data.board[0])):
            drawCell(canvas, data, row, col, data.board[row][col])

# This function draws each specific cell


def drawCell(canvas, data, row, col, color):
    data.x0 = data.smallMargin + col * data.cellWidth
    data.x1 = data.smallMargin + (col + 1) * data.cellWidth
    data.y0 = data.smallMargin + row * data.cellHeight
    data.y1 = data.smallMargin + (row + 1) * data.cellHeight
    canvas.create_rectangle((data.x0, data.y0), (data.x1, data.y1), fill=color)

# Contains all the different pieces


def Pieces():
    iPiece = [[True, True, True, True]]
    jPiece = [[True, False, False], [True, True, True]]
    lPiece = [[False, False, True], [True, True, True]]
    oPiece = [[True, True], [True, True]]
    sPiece = [[False, True, True], [True, True, False]]
    tPiece = [[False, True, False], [True, True, True]]
    zPiece = [[True, True, False], [False, True, True]]
    return [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]

# Chooses a random piece and puts it on the top center of the grid


def newFallingPiece(data):
    randomIndex = random.randint(0, len(data.tetrisPieces) - 1)
    data.fallingPiece = data.tetrisPieces[randomIndex]
    data.fallingPieceColor = data.tetrisPieceColors[randomIndex]
    data.fallingPieceRow = 0
    data.fallingPieceCol = (data.cols // 2) - (len(data.fallingPiece[0]) // 2)

# Drawing the actual falling piece


def drawFallingPiece(canvas, data):
    for eachRow in range(len(data.fallingPiece)):
        for eachPiece in range(len(data.fallingPiece[eachRow])):
            if data.fallingPiece[eachRow][eachPiece] == True:
                drawCell(canvas, data, eachRow + data.fallingPieceRow,
                         eachPiece + data.fallingPieceCol,
                         data.fallingPieceColor)

# THis function allows the piece to actually move


def moveFallingPiece(data, drow, dcol):
    data.fallingPieceCol += dcol
    data.fallingPieceRow += drow
    if not(fallingPieceisLegal(data)):
        data.fallingPieceCol -= dcol
        data.fallingPieceRow -= drow
        return False
    return True

# Checks to see if the move is legal or not


def fallingPieceisLegal(data):
    for eachRow in range(len(data.fallingPiece)):
        for eachPiece in range(len(data.fallingPiece[eachRow])):
            if data.fallingPiece[eachRow][eachPiece] == True:
                newRow = data.fallingPieceRow + eachRow
                newCol = data.fallingPieceCol + eachPiece
                if newCol < 0:
                    return False
                elif newCol > data.cols - 1:
                    return False
                elif newRow > data.rows - 1:
                    return False
                elif data.board[newRow][newCol] != data.emptyColor:
                    return False
    return True

# Rotates the piece counter clockwise


def rotateFallingPieceCCW(data):
    oldPiece = data.fallingPiece
    oldCol, oldRow = data.fallingPieceCol, data.fallingPieceRow

    newRow = (oldRow + len(data.fallingPiece) // 2 -
              len(data.fallingPiece[0]) // 2)
    newCol = (oldCol + len(data.fallingPiece[0]) // 2 -
              len(data.fallingPiece) // 2)

    newPiece = []
    for row in range(len(data.fallingPiece[0]) - 1, -1, -1):
        tempList = []
        for col in range(len(data.fallingPiece)):
            tempList.append(data.fallingPiece[col][row])
        newPiece.append(tempList)

    data.fallingPiece = newPiece
    data.fallingPieceRow = newRow
    data.fallingPieceCol = newCol

    if not(fallingPieceisLegal(data)):
        data.fallingPiece = oldPiece
        data.fallingPieceRow = oldRow
        data.fallingPieceCol = oldCol

# Places the falling piece and sets it in play, can't move after being placed


def placeFallingPiece(data):
    for row in range(len(data.fallingPiece)):
        for col in range(len(data.fallingPiece[0])):
            if data.fallingPiece[row][col]:
                (data.board[data.fallingPieceRow + row]
                    [data.fallingPieceCol + col]) = data.fallingPieceColor

# Adds the game over at the top of the screen when the game ends


def drawGameOver(canvas, data):
    if data.gameOver == True:
        canvas.create_rectangle(0, 40, data.width, 200, fill="black")
        canvas.create_text(data.width / 2, 100, text="Game Over!", fill="white",
                           font="ComicSansMS 50")
        canvas.create_text(data.width / 2, 160, text="Press 'r' to restart",
                           fill="white", font="ComicSansMS 20")

# Removes all the rows that aren't empty


def removeFullRows(data):
    newBoard = []
    data.fullRows = 0
    for eachRow in range(len(data.board) - 1, -1, -1):
        if data.emptyColor in data.board[eachRow]:
            newBoard.append(data.board[eachRow])
        else:
            data.fullRows += 1

    if data.fullRows == 0:
        pass
    else:
        for addingRows in range(data.fullRows):
            newBoard.append([data.emptyColor] * data.cols)
        data.board = newBoard[::-1]
    data.score += data.fullRows ** 2

# Draws the score on the canvas


def drawScore(canvas, data):
    text = "Score: " + str(data.score)
    canvas.create_text((data.width - (data.bigMargin / 2) - 10), 30, text=text,
                       fill="PaleTurquoise1", font="ComicSansMS 30")

# Creates a square containing what the next piece is


def drawNextPieceBox(canvas, data):
    x0 = (data.width - data.bigMargin) + 10
    y0 = data.height * (1 / 10)
    x1 = x0 + 160
    y1 = y0 + 150
    canvas.create_rectangle(x0, y0, x1, y1, fill="white")
    x0 = x0 + 10
    y0 = y0 + 10
    x1 = x1 - 10
    y1 = y1 - 10
    canvas.create_rectangle(x0, y0, x1, y1, fill="black")

# Creates a high score list and changes everytime the game restarts


def drawHighScoreList(canvas, data):
    x0 = (data.width - data.bigMargin) + 10
    y0 = (data.height / 2.5)
    x1 = x0 + 160
    y1 = y0 + (data.height - y0 - 30)
    canvas.create_rectangle(x0, y0, x1, y1, fill="LightPink1")
    cx = (x0 + x1) / 2
    text = "High Scores:"
    canvas.create_text(cx, y0 + 30, text=text, fill="blue2",
                       font="ComicSansMS 25")
    scoresList = []
    for eachScore in data.highScoreList:
        scoresList.append("\n" + str(eachScore) + "\n")

    scores = "".join(scoresList)

    canvas.create_text(cx, ((y0 + y1) / 2) + 20, text=scores, fill="blue2",
                       font="ComicSansMS 20")


# The keypress for the actual game
def gameKeyPressed(event, data):
    if event.keysym == "Right" or event.char == "d":
        moveFallingPiece(data, 0, 1)
    elif event.keysym == "Left" or event.char == "a":
        moveFallingPiece(data, 0, -1)
    elif event.keysym == "space":
        while moveFallingPiece(data, 1, 0):
            pass
    if event.keysym == "Down" or event.char == "s":
        moveFallingPiece(data, 1, 0)
    elif event.keysym == "Up" or event.char == "w":
        rotateFallingPieceCCW(data)

    if event.char == "r":
        tempScore = data.score
        tempScoreList = data.highScoreList
        init(data)
        data.mode = "Game"
        for eachScore in range(len(tempScoreList)):
            if tempScoreList[eachScore] == 0:
                tempScoreList[eachScore] = tempScore
                break
            elif tempScore > tempScoreList[eachScore]:
                tempScoreList.insert(eachScore, tempScore)
                tempScoreList.pop()
                break
        data.highScoreList = tempScoreList

    pausedKeyPressed(event, data)
    instructionsKeyPressed(event, data)

# The keypress function for when the game is paused


def pausedKeyPressed(event, data):
    if event.char == "p":
        if data.mode == "Pause":
            data.mode = "Game"
        else:
            data.mode = "Pause"

# The keypress function for when the instruction screen is on


def instructionsKeyPressed(event, data):
    if event.keysym == "Return":
        if data.mode == "Instructions":
            data.mode = "Game"
        else:
            data.mode = "Instructions"

# The timerfired function for when the game is occuring


def gameTimerFired(data):
    if data.gameOver == False:
        if not(moveFallingPiece(data, 1, 0)):
            placeFallingPiece(data)
            newFallingPiece(data)
            removeFullRows(data)
            if not(fallingPieceisLegal(data)):
                data.gameOver = True


def pausedTimerFired(data):
    pass


def instructionsTimerFired(data):
    pass

# The redrawall for when the game is occuring


def gameRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="midnight blue")
    drawBoard(canvas, data)
    drawFallingPiece(canvas, data)
    drawScore(canvas, data)
    drawNextPieceBox(canvas, data)
    drawHighScoreList(canvas, data)
    if data.gameOver == True:
        drawGameOver(canvas, data)

# The redrawall for when the game is paused


def pausedRedrawAll(canvas, data):
    x0, y0 = data.smallMargin, (data.smallMargin + 25)
    x1 = data.width - data.bigMargin - 23
    y1 = y0 + 150
    canvas.create_rectangle(x0, y0, x1, y1, fill="orange")
    centerX = (x0 + x1) / 2
    centerY = ((y0 + y1) / 2) - 20
    text1 = "The Game Is Paused"
    canvas.create_text(centerX, centerY, text=text1, fill="black",
                       font="ComicSansMS 30 bold")
    text2 = "Press 'p' to unpause the game"
    canvas.create_text(centerX, centerY + 30, text=text2, fill="black",
                       font="ComicSansMS 20")

# The redrawall for the instruction screen


def instructionsRedrawAll(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height, fill="white")
    text = "Instructions: "
    canvas.create_text(data.width / 2, data.height * (1 / 8), text=text,
                       fill="black", font="ComicSansMS 50")
    instructions = ("Press Left Arrow Key or 'a' to move the block left" + "\n"
                    + "Press Right Arrow Key or 'd' to move the block right" +
                    "\n" + "Press the Up Arrow Key or 'w' to rotate the block" +
                    "\n" + "Press the Down Arrow Key or 'd' to go down" + "\n" +
                    "Press the Space Key to hard drop the piece" + "\n" +
                    "Press 'p' to pause the game" + "\n" +
                    "Press 'r' to restart the game" + "\n" +
                    "Press the Enter Key to go to the instructions page")
    canvas.create_text(data.width / 2, data.height / 2, text=instructions,
                       fill="black", font="ComicSansMS 22")
    end = "Press Enter to exit the instructions screen"
    canvas.create_text(data.width / 2, data.height - 20, text=end, fill="black",
                       font="ComicSansMS 15")


#################################################
# MVC
#################################################


def init(data):
    data.rows = 15
    data.cols = 10
    data.smallMargin = 25
    data.bigMargin = 200
    data.cellHeight = (data.height - 2 * data.smallMargin) / data.rows
    data.cellWidth = ((data.width - data.bigMargin - 2 *
                       data.smallMargin) / data.cols)
    data.emptyColor = "black"
    data.board = createBoardList(data)
    data.tetrisPieces = Pieces()
    data.tetrisPieceColors = ["red", "yellow", "magenta", "pink", "cyan",
                              "green", "orange"]
    data.tetrisInnerColors = ["#8b0000", "#808000", "#8b008b",
                              "#e75480", "#008B8B", "#006400", "#ee7600"]
    newFallingPiece(data)
    data.timerDelay = 500
    data.gameOver = False
    data.score = 0
    data.highScoreList = [0, 0, 0, 0, 0]
    data.mode = "Instructions"


def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    # use event.char and event.keysym
    if data.mode == "Instructions":
        instructionsKeyPressed(event, data)
    elif data.mode == "Pause":
        pausedKeyPressed(event, data)
    elif data.mode == "Game":
        gameKeyPressed(event, data)


def timerFired(data):
    if data.mode == "Instructions":
        instructionsTimerFired(data)
    elif data.mode == "Pause":
        pausedTimerFired(data)
    elif data.mode == "Game":
        gameTimerFired(data)


def redrawAll(canvas, data):
    gameRedrawAll(canvas, data)
    if data.mode == "Instructions":
        instructionsRedrawAll(canvas, data)
    elif data.mode == "Pause":
        pausedRedrawAll(canvas, data)
    elif data.mode == "Game":
        gameRedrawAll(canvas, data)


####################################
# do not change code below
####################################


def playTetris(width=600, height=600):
    run(width, height)


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

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init

    class Struct(object):
        pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100  # milliseconds
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
              mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
              keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


####################################
# Test Cases
####################################


def testFn():
    class Struct(object):
        pass
    data1 = Struct()
    data1.rows = 15
    data1.cols = 10
    data1.emptyColor = "black"
    print("Testing createBoardList()...", end='')
    assert(createBoardList(data1) == [["black"] * 10] * 15)
    data1.rows = 5
    data1.cols = 3
    assert(createBoardList(data1) == [["black"] * 3] * 5)
    print("passed!")

    data2 = Struct()
    data2.fallingPiece = [[True, True, True, True]]
    data2.fallingPieceRow = 12
    data2.fallingPieceCol = 8
    data2.rows = 15
    data2.cols = 10
    data2.emptyColor = "black"
    data2.board = ([["black"] * 10] * 15)
    print("Testing fallingPieceisLegal()...", end='')
    assert(fallingPieceisLegal(data2) == False)
    data2.fallingPieceRow = 10
    data2.fallingPieceCol = 5
    assert(fallingPieceisLegal(data2) == True)
    print("passed!")

    data3 = Struct()
    data3.fallingPiece = [[True, True, True, True]]
    data3.fallingPieceRow = 8
    data3.fallingPieceCol = 3
    data3.rows = 15
    data3.cols = 10
    data3.board = ([["black"] * 10] * 15)
    data3.emptyColor = "black"
    print("Testing rotateFallingPieceCCW()...", end='')
    rotateFallingPieceCCW(data3)
    assert(data3.fallingPiece == [[True], [True], [True], [True]])
    rotateFallingPieceCCW(data3)
    assert(data3.fallingPiece == [[True, True, True, True]])
    print("passed!")

    data4 = Struct()
    data4.fallingPiece = [[True, True, True, True]]
    data4.fallingPieceRow = 10
    data4.fallingPieceCol = 4
    data4.fallingPieceColor = "red"
    data4.board = ([["black"] * 10] * 15)
    print("Testing placeFallingPiece()...", end='')
    placeFallingPiece(data4)
    assert((data4.board[data4.fallingPieceRow]
            [data4.fallingPieceCol]) == data4.fallingPieceColor)
    data4.fallingPieceRow = 5
    data4.fallingPieceCol = 5
    assert((data4.board[data4.fallingPieceRow]
            [data4.fallingPieceCol]) == data4.fallingPieceColor)
    print("passed!")

    data5 = Struct()
    data5.fullRows = 0
    data5.board = ([["black"] * 10] * 14)
    data5.emptyColor = "black"
    data5.score = 0
    data5.cols = 10
    print("Testing removeFullRows()...", end='')
    removeFullRows(data5)
    assert(data5.fullRows == 0)
    assert(data5.score == 0)
    print("passed!")


testFn()
playTetris()
