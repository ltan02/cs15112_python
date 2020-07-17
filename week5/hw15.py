#################################################################
# 15-112-n18 hw15
# Your Name: Alistair Tan
# Your Andrew ID: alistait
# Your Section: A

#################################################################


class Asteroid(object):
    def __init__(self, cx, cy, radius, speed, direction=(0, 1), color="purple"):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.speed = speed
        self.direction = direction
        self.color = color

    # Setting a class to a string
    def __repr__(self):
        return ("%s at (%d, %d) with radius=%d and direction %s" %
                (type(self).__name__, self.cx, self.cy, self.radius,
                    self.direction))

    def setDirection(self, newDirection):
        self.direction = newDirection

    def getDirection(self):
        return self.direction

    def isCollisionWithWall(self, width, height):
        # Checks to see if the edges are at the ends of the screen
        return ((self.cx + self.radius >= width) or (self.cx - self.radius <= 0)
                or (self.cy + self.radius >= height) or
                (self.cy - self.radius <= 0))

    def moveAsteroid(self):
        # Moves the asteroid in accordance to the direction and speed
        self.cx += self.direction[0] * self.speed
        self.cy += self.direction[1] * self.speed

    def getPositionAndRadius(self):
        return (self.cx, self.cy, self.radius)

    def reactToBulletHit(self):
        # Stops the asteroid from moving if it gets stunned
        self.direction = (0, 0)

    def draw(self, canvas):
        cx, cy, r = self.cx, self.cy, self.radius
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                           fill=self.color, outline=None)

    def wrapAround(self, width, height):
        if self.cx - self.radius >= width:
            self.cx = self.radius
        if self.cx + self.radius <= 0:
            self.cx = width - self.radius
        if self.cy + self.radius <= 0:
            self.cy = height - self.radius
        if self.cy - self.radius >= height:
            self.cy = self.radius


class ShrinkingAsteroid(Asteroid):
    def __init__(self, cx, cy, radius, speed, direction=(0, 1), shrinkAmount=5,
                 color="pink"):
        super().__init__(cx, cy, radius, speed, direction)
        self.shrinkAmount = shrinkAmount
        self.color = color

    def reactToBulletHit(self):
        # Shrinks if it is hit by a bullet
        self.radius -= self.shrinkAmount

    def bounce(self):
        # Sets the direction to the opposite of it when it bounces
        if self.direction[0] == -1 and self.direction[1] == -1:
            self.direction = (1, 1)
        elif self.direction[0] == -1 and self.direction[1] == 1:
            self.direction = (1, -1)
        elif self.direction[0] == 1 and self.direction[1] == -1:
            self.direction = (-1, 1)
        elif self.direction[0] == 1 and self.direction[1] == 1:
            self.direction = (-1, -1)
        elif self.direction[0] == 0 and self.direction[1] == 1:
            self.direction = (0, -1)
        elif self.direction[0] == 0 and self.direction[1] == -1:
            self.direction = (0, 1)
        elif self.direction[0] == -1 and self.direction[1] == 0:
            self.direction = (1, 0)
        elif self.direction[0] == 1 and self.direction[1] == 0:
            self.direction = (-1, 0)


class SplittingAsteroid(Asteroid):
    def __init__(self, cx, cy, radius, speed, direction=(0, 1), color="blue"):
        super().__init__(cx, cy, radius, speed, direction)
        self.color = color

    def reactToBulletHit(self):
        # Returns two different instances of the splitting asteroid with a
        # smaller radius
        return(SplittingAsteroid(self.cx - self.radius, self.cy - self.radius,
                                 self.radius / 2, self.speed),
               SplittingAsteroid(self.cx + self.radius, self.cy + self.radius,
                                 self.radius / 2, self.speed))

#################################################################

# Starter Code begins here. Read and understand it!


import random
import math

# Helper function for drawing the Rocket


def drawTriangle(canvas, cx, cy, angle, size, fill="black"):
    angleChange = 2 * math.pi / 3
    p1x, p1y = (cx + size * math.cos(angle),
                cy - size * math.sin(angle))
    p2x, p2y = (cx + size * math.cos(angle + angleChange),
                cy - size * math.sin(angle + angleChange))
    p3x, p3y = (cx, cy)
    p4x, p4y = (cx + size * math.cos(angle + 2 * angleChange),
                cy - size * math.sin(angle + 2 * angleChange))

    canvas.create_polygon((p1x, p1y), (p2x, p2y), (p3x, p3y), (p4x, p4y),
                          fill=fill)

# Read this class carefully! You'll need to call the methods!


class Rocket(object):
    def __init__(self, cx, cy):
        self.cx = cx
        self.cy = cy
        self.angle = 90

    def rotate(self, numDegrees):
        self.angle += numDegrees

    def makeBullet(self):
        offset = 10
        dx, dy = (offset * math.cos(math.radians(self.angle)),
                  offset * math.sin(math.radians(self.angle)))
        speedLow, speedHigh = 20, 40

        return Bullet(self.cx + dx, self.cy - dy,
                      self.angle, random.randint(speedLow, speedHigh))

    def draw(self, canvas):
        size = 30
        drawTriangle(canvas, self.cx, self.cy,
                     math.radians(self.angle), size, fill="green2")

# Read this class carefully! You'll need to call the methods!


class Bullet(object):
    def __init__(self, cx, cy, angle, speed=20):
        self.cx = cx
        self.cy = cy
        self.r = 5
        self.angle = angle
        self.speed = speed

    def moveBullet(self):
        dx = math.cos(math.radians(self.angle)) * self.speed
        dy = math.sin(math.radians(self.angle)) * self.speed
        self.cx, self.cy = self.cx + dx, self.cy - dy

    def isCollisionWithAsteroid(self, other):
        # in this case, other must be an asteroid
        if(not isinstance(other, Asteroid)):
            return False
        else:
            return (math.sqrt((other.cx - self.cx)**2 +
                              (other.cy - self.cy)**2)
                    < self.r + other.radius)

    def draw(self, canvas):
        cx, cy, r = self.cx, self.cy, self.r
        canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                           fill="white", outline=None)

    def onTimerFired(self, data):
        self.moveBullet()

#################################################################


from tkinter import *

####################################
# customize these functions
####################################


def init(data):
    # load data.xyz as appropriate
    data.rocket = Rocket(data.width // 2, data.height // 2)
    # what else do you need to store here?
    data.bullets = []
    data.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    data.counter = 0
    data.asteroids = []
    data.frozen = []


def mousePressed(event, data):
    # use event.x and event.y
    pass


def keyPressed(event, data):
    # use event.char and event.keysym
    # make the rocket rotate and fire!
    if event.keysym == "Right":
        #Rotates right if right arrow key is pressed
        data.rocket.rotate(-(4 * math.pi))
    elif event.keysym == "Left":
        #Rotates left is left arrow key
        data.rocket.rotate(4 * math.pi)

    if event.keysym == "space":
        #Creates a bullet and stores it in a list
        data.bullets.append(data.rocket.makeBullet())


def makingAsteroid(data):
    #Creates a new asteroid every 2 seconds with random dimensions
    if data.counter % 20 == 0:
        cx = random.randint(0, data.width)
        cy = random.randint(0, data.height)
        r = random.randint(20, 40)
        speed = random.randint(5, 20)
        direction = random.choice(data.directions)
        typeOfAsteroid = random.choice([Asteroid, ShrinkingAsteroid,
                                        SplittingAsteroid])
        data.asteroids.append(SplittingAsteroid(cx, cy, r, speed, direction))
        #Adds the asteroid to a list


def hittingWall(data):
    #Checks if the asteroid is hitting the wall
    for eachAsteroid in data.asteroids:
        eachAsteroid.moveAsteroid()
        if(isinstance(eachAsteroid, ShrinkingAsteroid) and
                eachAsteroid.isCollisionWithWall(data.width, data.height)):
        #Bounces off a wall if the asteroid is a shrinking asteroid
            eachAsteroid.bounce()
        else:
        #Otherwise, the asteroid will wrap around
            eachAsteroid.wrapAround(data.width, data.height)


def hitByBullet(data):
    #Checking if the asteroid is hit by a bullet
    for bullets in data.bullets:
        for asteroids in data.asteroids:
            if bullets.isCollisionWithAsteroid(asteroids):
                if isinstance(asteroids, ShrinkingAsteroid):
                    #Checks to see if radius of shrinking asteroid is less than
                    #15
                    if asteroids.radius <= 15:
                        #If it is then it will remove the asteroid
                        data.asteroids.remove(asteroids)
                    else:
                        #If not then it will shrink
                        asteroids.reactToBulletHit()
                elif isinstance(asteroids, SplittingAsteroid):
                    #Checks to see if radius of splliting asteroid's radius is
                    #less than 10
                    if asteroids.radius <= 10:
                        #If it is then it removes it
                        data.asteroids.remove(asteroids)
                    else:
                        #If it isn't then it splits it into two smaller asteroid
                        asteroid1, asteroid2 = asteroids.reactToBulletHit()
                        data.asteroids.remove(asteroids)
                        data.asteroids.append(asteroid1)
                        data.asteroids.append(asteroid2)
                else:
                    #If it is a normal asteroid then it will freeze
                    asteroids.reactToBulletHit()


def removeAsteroid(data):
    #Checks if there are any frozen asteroids, if there is then it will remove
    #it when 10 seconds has passed
    if data.counter % 100 == 0:
        for asteroid in data.asteroids:
            if asteroid.direction == (0, 0):
                data.asteroids.remove(asteroid)


def timerFired(data):
    # it might be a good idea to define onTimerFired methods in your classes...
    data.counter += 1
    for eachBullet in data.bullets:
        eachBullet.moveBullet()

    makingAsteroid(data)
    hittingWall(data)
    hitByBullet(data)
    removeAsteroid(data)


def redrawAll(canvas, data):
    # draws the rocket and background
    canvas.create_rectangle(0, 0, data.width, data.height, fill="gray3")
    for eachBullet in data.bullets:
        #Draws bullets in bullets list
        eachBullet.draw(canvas)
    data.rocket.draw(canvas)

    for eachAsteroid in data.asteroids:
        #Draws asteroids in asteroids list
        eachAsteroid.draw(canvas)

    # don't forget to draw asteroids and bullets!

#################################################################
# use the run function as-is
#################################################################


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


run(600, 600)
