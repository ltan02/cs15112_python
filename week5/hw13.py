#################################################
# 15-112-n18 hw13
# Your Name: Alistair Tan
# Your Andrew ID: alistait
# Your Section: A

#################################################
import os


def largestFileHelper(path, largestSize, largestFile):
    if os.path.isdir(path) == False:
        size = os.path.getsize(path)
        return size, path
    else:
        for filename in os.listdir(path):
            size, filepath = largestFileHelper(path + os.sep + filename, largestSize, largestFile)
            if size > largestSize:
                largestSize = size
                largestFile = filepath
        return largestSize, largestFile


def findLargestFile(path):
    largestFile = largestFileHelper(path, 0, "")[1]
    print(largestFile)
    return largestFile


def friendsOfFriends(d):
    result = {}
    # Checks every person in the dictionary
    for key in d:
        result[key] = set()
        for friend in d[key]:
            for friend2 in d[friend]:
                if friend2 != key and friend2 not in d[key]:
                    result[key].add(friend2)
    return result

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

# Don't forget to write test cases!


def testFindLargestFile():
    print("Testing findLargestFile()...", end="")
    assert(findLargestFile("sampleFiles" + os.sep + "folderA") ==
           "sampleFiles" + os.sep + "folderA" +
           os.sep + "folderC" + os.sep + "giftwrap.txt")
    assert(findLargestFile("sampleFiles" + os.sep + "folderB") ==
           "sampleFiles" + os.sep + "folderB" +
           os.sep + "folderH" + os.sep + "driving.txt")
    assert(findLargestFile("sampleFiles" + os.sep + "folderB" +
                           os.sep + "folderF") == "")
    assert(findLargestFile("sampleFiles" + os.sep + "folderB" + os.sep + "folderH" + os.sep + "driving.txt") == "sampleFiles" + os.sep + "folderB" + os.sep + "folderH" + os.sep + "driving.txt")

    # Write more test cases here!
    print("Passed!")


def testFriendsOfFriends():
    print("Testing friendsOfFriends()...", end="")
    d = {}
    d["spongebob"] = set(["sandy", "patrick", "mr.krabs", "squidward"])
    d["mr.krabs"] = set(["pearl", "spongebob", "squidward"])
    d["pearl"] = set(["mr.krabs"])
    d["sandy"] = set(["spongebob", "patrick"])
    d["patrick"] = set(["spongebob", "sandy"])
    d["squidward"] = set()

    assert(friendsOfFriends(d) == {
        'spongebob': {'pearl'},
        'mr.krabs': {'patrick', 'sandy'},
        'pearl': {'spongebob', 'squidward'},
        'sandy': {'mr.krabs', 'squidward'},
        'patrick': {'mr.krabs', 'squidward'},
        'squidward': set(),
    }
    )

    d1 = {}
    d1["Lance"] = set(["Jerome", "Kunal"])
    d1["Jerome"] = set(["Lance"])
    d1["Kunal"] = set(["Ben"])
    d1["Ben"] = set()

    assert(friendsOfFriends(d1) == {
        'Lance': {'Ben'},
        'Jerome': {'Kunal'},
        'Kunal': set(),
        'Ben': set()
    })

    # Write more test cases here!
    print("Passed!")


testFindLargestFile()
testFriendsOfFriends()

from tkinter import *
import math
import random

#########################################
# customize these functions for HFractal
#########################################


def drawFractal(canvas, x, y, sizeWidth, sizeHeight, level):
    if level == 0:
        # Horizontal Line
        canvas.create_line(x - (sizeWidth // 2), y, x + (sizeWidth // 2), y)
        # Left Vertical Line
        canvas.create_line(x - (sizeWidth // 2), y - (sizeHeight // 2), x - (sizeWidth // 2), y + (sizeHeight // 2))
        # Right Vertical Line
        canvas.create_line(x + (sizeWidth // 2), y - (sizeHeight // 2), x + (sizeWidth // 2), y + (sizeHeight // 2))
    else:
        # Draws the main H in the middle
        drawFractal(canvas, x, y, sizeWidth, sizeHeight, level - 1)
        # Draws the H on the top left
        drawFractal(canvas, (x - sizeWidth // 2), (y - sizeHeight // 2), sizeWidth // 2, sizeHeight // 2, level - 1)
        # Draws the H on the top right
        drawFractal(canvas, (x + sizeWidth // 2), (y - sizeHeight // 2), sizeWidth // 2, sizeHeight // 2, level - 1)
        # Draws the H on the bottom left
        drawFractal(canvas, (x - sizeWidth // 2), (y + sizeHeight // 2), sizeWidth // 2, sizeHeight // 2, level - 1)
        # Draws the H on the bottom right
        drawFractal(canvas, (x + sizeWidth // 2), (y + sizeHeight // 2), sizeWidth // 2, sizeHeight // 2, level - 1)


def init(data):
    # load data.xyz as appropriate
    data.level = 0


def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    # use event.char and event.keysym
    if event.keysym in ["Up", "Right"]:
        data.level += 1
    elif event.keysym in ["Down", "Left"] and data.level > 0:
        data.level -= 1


def timerFired(data):
    pass


def redrawAll(canvas, data):
    # draw in canvas
    drawFractal(canvas, data.width // 2, (data.height // 2), data.width // 2, (data.height // 2), data.level)

    canvas.create_text(data.width // 2, data.height // 20, text="Level %d H-Fractal" % data.level, font="ComicSansMS 20")


####################################
# use the run function as-is
####################################

def runHFractal(width=300, height=300):
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


runHFractal(600, 600)

##############################################
# customize these functions for dotsGalore 2.0
##############################################


def init(data):
    # load data.xyz as appropriate
    data.gameMode = "Game"
    data.directions = ["Up", "Down", "Left", "Right"]
    data.colors = ["PeachPuff3", "green2", "DodgerBlue4", "light goldenrod", "green yellow"]
    data.dotsList = []
    data.counter = 0
    data.speed = 5


def mousePressed(event, data):
    # use event.x and event.y
    if data.gameMode == "Game":
        mousePressedGame(event, data)
    elif data.gameMode == "Paused":
        mousePressedPaused(event, data)


def mousePressedGame(event, data):
    poppingList = []
    for eachDot in range(len(data.dotsList)):
        # Checks if mouse is clicking on the dot
        x0, y0 = data.dotsList[eachDot][0], data.dotsList[eachDot][1]
        r = data.dotsList[eachDot][2]
        if getDistance(x0, y0, event.x, event.y) < r:
            # If it is then it puts the index of the dot in a list
            poppingList.append(eachDot)

    # Removes each dot from the list
    for eachPop in poppingList:
        data.dotsList.pop(eachPop)


def mousePressedPaused(event, data):
    pass


def keyPressed(event, data):
    # use event.char and event.keysym
    if data.gameMode == "Game":
        keyPressedGame(event, data)
    elif data.gameMode == "Paused":
        keyPressedPaused(event, data)


def keyPressedGame(event, data):
    if event.keysym == "p":
        data.gameMode = "Paused"

    if event.keysym == "r":
        for eachDot in range(len(data.dotsList)):
            if data.dotsList[eachDot][4] == "Up":
                data.dotsList[eachDot][4] = "Down"
            elif data.dotsList[eachDot][4] == "Down":
                data.dotsList[eachDot][4] = "Up"
            elif data.dotsList[eachDot][4] == "Right":
                data.dotsList[eachDot][4] = "Left"
            else:
                data.dotsList[eachDot][4] = "Right"


def keyPressedPaused(event, data):
    if event.keysym == "p":
        data.gameMode = "Game"


def timerFired(data):
    if data.gameMode == "Game":
        timerFiredGame(data)
    elif data.gameMode == "Paused":
        timerFiredPaused(data)


def timerFiredGame(data):
    data.counter += 1
    moveDot(data)
    collidingDots(data)
    # Checks if it has been 2 seconds
    if data.counter % 20 == 0:
        createDot(data)
    # Checks if it has been 5 seconds
    if data.counter % 50 == 0:
        for eachDot in data.dotsList:
            eachDot[2] += 5


def createDot(data):
    cx = random.randint(0, data.width)
    cy = random.randint(0, data.height)
    r = random.randint(5, 50)
    color = random.choice(data.colors)
    direction = random.choice(data.directions)
    # Adding the features of the dot to a 2D list
    data.dotsList.append([cx, cy, r, color, direction])


def getDistance(x0, y0, x1, y1):
    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)


def collidingDots(data):
    for eachDot in range((len(data.dotsList)) - 1):
        x0 = data.dotsList[eachDot][0]
        y0 = data.dotsList[eachDot][1]
        r0 = data.dotsList[eachDot][2]
        for dots in range(eachDot + 1, len(data.dotsList)):
            x1 = data.dotsList[dots][0]
            y1 = data.dotsList[dots][1]
            r1 = data.dotsList[dots][2]
        # Compares all dots an checks if the distance between the two dots is less than the radius combined
            if getDistance(x0, y0, x1, y1) < r0 + r1:
                # If it is then it changes the direction to the opposite direction
                if data.dotsList[eachDot][4] == "Up":
                    data.dotsList[eachDot][4] = "Down"
                elif data.dotsList[eachDot][4] == "Down":
                    data.dotsList[eachDot][4] = "Up"
                elif data.dotsList[eachDot][4] == "Right":
                    data.dotsList[eachDot][4] = "Left"
                else:
                    data.dotsList[eachDot][4] = "Right"

                if data.dotsList[dots][4] == "Up":
                    data.dotsList[dots][4] = "Down"
                elif data.dotsList[dots][4] == "Down":
                    data.dotsList[dots][4] = "Up"
                elif data.dotsList[dots][4] == "Right":
                    data.dotsList[dots][4] = "Left"
                else:
                    data.dotsList[dots][4] = "Right"


def moveDot(data):
    for eachDot in data.dotsList:
        d = eachDot[4]
        cx = eachDot[0]
        cy = eachDot[1]
        r = eachDot[2]
        # Changes the direction according to the speed and which way it is going. If it is off the screen then it will wrap around
        if d == "Up":
            if cy + r < 0:
                cy = data.height
            cy -= data.speed
        elif d == "Down":
            if cy - r > data.height:
                cy = 0
            cy += data.speed
        elif d == "Left":
            if cx + r < 0:
                cx = data.width
            cx -= data.speed
        else:
            if cx - r > data.width:
                cx = 0
            cx += data.speed
        eachDot[0] = cx
        eachDot[1] = cy


def timerFiredPaused(data):
    pass


def redrawAll(canvas, data):
    # draw in canvas
    drawDot(canvas, data)


def drawDot(canvas, data):
    # Goes through the list of dots and draws each dot.
    for eachDot in data.dotsList:
        cx = eachDot[0]
        cy = eachDot[1]
        r = eachDot[2]
        color = eachDot[3]
        canvas.create_oval((cx - r, cy - r), (cx + r, cy + r), fill=color)


####################################
# use the run function as-is
####################################


def runDotsGalore(width=300, height=300):
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


runDotsGalore(600, 600)
