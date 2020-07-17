#################################################
# 15-112-n18 hw14
# Your Name: Alistair Tan
# Your Andrew ID: alistait
# Your Section: A

#################################################


class Book(object):
    def __init__(self, title, author, pages, currentPage=1, bookmark=None):
        self.title = title
        self.author = author
        self.pages = pages
        self.currentPage = currentPage
        self.bookmark = bookmark

    # Turning a class into a string
    def __repr__(self):
        if self.bookmark == None:
            # Checks if it is bookmarked or not
            if self.pages == 1:
                # Since page is 1, then number of pages doesn't end with a 's'
                return "Book<%s by %s: 1 page, currently on page %d>" % (
                    self.title, self.author, self.currentPage)
            else:
                # More than 1 page, so pages ends with a 's'
                return "Book<%s by %s: %d pages, currently on page %d>" % (
                    self.title, self.author, self.pages, self.currentPage)
        else:
            if self.pages == 1:
                return("Book<%s by %s: 1 page, currently on page %d," % (
                    self.title, self.author, self.currentPage) +
                    " page %d bookmarked>" % self.bookmark)
            else:
                return("Book<%s by %s: %d pages, currently on page %d," % (
                    self.title, self.author, self.pages, self.currentPage) +
                    " page %d bookmarked>" % self.bookmark)

    # Checking if two instances are the same
    def __eq__(self, other):
        return (isinstance(other, Book) and (self.title == other.title) and
                (self.author == other.author) and (self.pages == other.pages)
                and (self.currentPage == other.currentPage) and
                (self.bookmark == other.bookmark))

    def __hash__(self):
        return hash((self.title, self.author, self.pages, self.currentPage,
                     self.bookmark))

    def turnPage(self, number):
        self.currentPage += number

        # Makes sure that the current page doesn't go off the book
        if self.currentPage > self.pages:
            self.currentPage = self.pages

        # Makes sure that the current page is less that 0 because it does not
        # exist
        if self.currentPage <= 0:
            self.currentPage = 1

    def getCurrentPage(self):
        return self.currentPage

    def placeBookmark(self):
        # Sets the bookmark to the current page
        self.bookmark = self.currentPage

    def getBookmarkedPage(self):
        # Gets bookmarked page
        return self.bookmark

    def turnToBookmark(self):
        if self.bookmark != None:
            self.currentPage = self.bookmark

    def removeBookmark(self):
        self.bookmark = None


class Asteroid(object):
    def __init__(self, cx, cy, radius, speed, direction=(0, 1)):
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.speed = speed
        self.direction = direction

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
        return ((self.cx + self.radius == width) or (self.cx - self.radius == 0)
                or (self.cy + self.radius == height) or
                (self.cy - self.radius == 0))

    def moveAsteroid(self):
        # Moves the asteroid in accordance to the direction and speed
        self.cx += self.direction[0] * self.speed
        self.cy += self.direction[1] * self.speed

    def getPositionAndRadius(self):
        return (self.cx, self.cy, self.radius)

    def reactToBulletHit(self):
        # Stops the asteroid from moving if it gets stunned
        self.direction = (0, 0)


class ShrinkingAsteroid(Asteroid):
    def __init__(self, cx, cy, radius, speed, direction=(0, 1), shrinkAmount=5):
        super().__init__(cx, cy, radius, speed, direction)
        self.shrinkAmount = shrinkAmount

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
    def __init__(self, cx, cy, radius, speed, direction=(0, 1)):
        super().__init__(cx, cy, radius, speed, direction)

    def reactToBulletHit(self):
        # Returns two different instances of the splitting asteroid with a
        # smaller radius
        return(SplittingAsteroid(self.cx - self.radius, self.cy - self.radius,
                                 self.radius / 2, self.speed),
               SplittingAsteroid(self.cx + self.radius, self.cy + self.radius,
                                 self.radius / 2, self.speed))

        #################################################################
        # Homework 14 Test Functions
        #################################################################


def testBookClass():
    print("Testing Book class...", end="")
    # A Book has a title, and author, and a number of pages.
    # It also has a current page, which always starts at 1. There is no page 0!
    book1 = Book("Harry Potter and the Sorcerer's Stone",
                 "J. K. Rowling", 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
                         "J. K. Rowling: 309 pages, currently on page 1>")
    book2 = Book("Carnegie Mellon Motto", "Andrew Carnegie", 1)
    assert(str(book2) == "Book<Carnegie Mellon Motto by Andrew Carnegie: " +
                         "1 page, currently on page 1>")

    # You can turn pages in a book. Turning a positive number of pages moves
    # forward; turning a negative number moves backwards. You can't move past
    # the first page going backwards or the last page going forwards
    book1.turnPage(4)  # turning pages does not return
    assert(book1.getCurrentPage() == 5)
    book1.turnPage(-1)
    assert(book1.getCurrentPage() == 4)
    book1.turnPage(400)
    assert(book1.getCurrentPage() == 309)
    assert(str(book1) == "Book<Harry Potter and the Sorcerer's Stone by " +
                         "J. K. Rowling: 309 pages, currently on page 309>")
    book2.turnPage(-1)
    assert(book2.getCurrentPage() == 1)
    book2.turnPage(1)
    assert(book2.getCurrentPage() == 1)

    # You can also put a bookmark on the current page. This lets you turn
    # back to it easily. The book starts out without a bookmark.
    book3 = Book("The Name of the Wind", "Patrick Rothfuss", 662)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " +
                         "662 pages, currently on page 1>")
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(9)
    book3.placeBookmark()  # does not return
    assert(book3.getBookmarkedPage() == 10)
    book3.turnPage(7)
    assert(book3.getBookmarkedPage() == 10)
    assert(book3.getCurrentPage() == 17)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " +
           "662 pages, currently on page 17, page 10 bookmarked>")
    book3.turnToBookmark()
    assert(book3.getCurrentPage() == 10)
    book3.removeBookmark()
    assert(book3.getBookmarkedPage() == None)
    book3.turnPage(25)
    assert(book3.getCurrentPage() == 35)
    book3.turnToBookmark()  # if there's no bookmark, don't turn to a page
    assert(book3.getCurrentPage() == 35)
    assert(str(book3) == "Book<The Name of the Wind by Patrick Rothfuss: " +
                         "662 pages, currently on page 35>")

    # Finally, you should be able to compare two books directly and hash books
    book5 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book6 = Book("A Game of Thrones", "George R.R. Martin", 807)
    book7 = Book("A Natural History of Dragons", "Marie Brennan", 334)
    book8 = Book("A Game of Spoofs", "George R.R. Martin", 807)
    book9 = Book("A Game of Thrones", "George R.R. Martin", 200)
    assert(book5 == book6)
    assert(book5 != book7)
    assert(book5 != book8)
    assert(book5 != book9)
    s = set()
    assert(book5 not in s)
    s.add(book5)
    assert(book6 in s)
    assert(book7 not in s)
    s.remove(book6)
    assert(book5 not in s)
    book5.turnPage(1)
    assert(book5 != book6)
    book5.turnPage(-1)
    assert(book5 == book6)
    book6.placeBookmark()
    assert(book5 != book6)
    print("Done!")


def getLocalMethods(clss):
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = []
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)


def testAsteroidClasses():
    print("Testing Asteroids classes...", end="")
    # A basic Asteroid takes in cx, cy, radius, speed, and optional direction.
    # It's default direction (dx, dy) is (0, 1), or moving down
    asteroid1 = Asteroid(25, 50, 20, 5)
    assert(type(asteroid1) == Asteroid)
    assert(isinstance(asteroid1, Asteroid))
    asteroid1.setDirection((-1, 0))
    assert(asteroid1.getDirection() == (-1, 0))
    assert(str(asteroid1) ==
           "Asteroid at (25, 50) with radius=20 and direction (-1, 0)")
    assert(str([asteroid1]) ==
           "[Asteroid at (25, 50) with radius=20 and direction (-1, 0)]")
    # isCollisionWithWall takes in the canvasWidth and canvasHeight
    # Asteroids collide with walls if any part of them is touching any side
    # of the canvas
    assert(asteroid1.isCollisionWithWall(400, 400) == False)
    asteroid1.moveAsteroid()
    assert(str(asteroid1) ==
           "Asteroid at (20, 50) with radius=20 and direction (-1, 0)")
    assert(asteroid1.getPositionAndRadius() == (20, 50, 20))
    assert(asteroid1.isCollisionWithWall(400, 400) == True)
    # A normal asteroid is stunned when it is hit by a bullet, and it freezes
    asteroid1.reactToBulletHit()
    assert(asteroid1.getDirection() == (0, 0))
    assert(getLocalMethods(Asteroid) == ['__init__', '__repr__',
                                         'getDirection', 'getPositionAndRadius',
                                         'isCollisionWithWall', 'moveAsteroid',
                                         'reactToBulletHit', 'setDirection'])

    # A Shrinking Asteroid takes in cx, cy, radius, speed,
    # an optional direction (that is (0, 1) by default),
    # and an optional shrinkAmount set to 5 pixels by default.
    # ShrinkAmount is how much the radius of the asteroid decreases when it is
    # hit by a bullet. A Shrinking Asteroid can also bounce off the walls.
    asteroid2 = ShrinkingAsteroid(200, 200, 50, 20)
    assert(type(asteroid2) == ShrinkingAsteroid)
    assert(isinstance(asteroid2, ShrinkingAsteroid))
    assert(isinstance(asteroid2, Asteroid))
    asteroid2.reactToBulletHit()
    assert(asteroid2.getPositionAndRadius() == (200, 200, 45))
    assert(str(asteroid2) == "ShrinkingAsteroid at (200, 200) with radius=45 " +
           "and direction (0, 1)")
    asteroid2.setDirection((1, -1))
    asteroid2.bounce()
    assert(asteroid2.getDirection() == (-1, 1))
    asteroid3 = ShrinkingAsteroid(100, 100, 40, 10,
                                  direction=(0, -1), shrinkAmount=20)
    # The asteroid's radius will decrease by the shrinkAmount
    asteroid3.reactToBulletHit()
    assert(asteroid3.getPositionAndRadius() == (100, 100, 20))
    assert(getLocalMethods(ShrinkingAsteroid) == ['__init__', 'bounce',
                                                  'reactToBulletHit'])

    # A Splitting Asteroid takes in cx, cy, radius, speed, and an optional
    # direction (set to (0, 1) by default). It splits into two smaller
    # Splitting Asteroids when hit by a bullet.
    # The each smaller Splitting Asteroid has radius that is half of
    # the original Splitting Asteroid's and has the original speed and direction
    asteroid4 = SplittingAsteroid(300, 300, 20, 15)
    assert(type(asteroid4) == SplittingAsteroid)
    assert(isinstance(asteroid4, SplittingAsteroid))
    assert(isinstance(asteroid4, Asteroid))
    assert(not isinstance(asteroid4, ShrinkingAsteroid))
    # reactToBulletHit returns 2 new instances of the SplittingAsteroid class
    asteroid5, asteroid6 = asteroid4.reactToBulletHit()
    # The new Splitting Asteroid centers are at the top-left and bottom-right
    # corners of the bounding box surrounding the original asteroid
    # See the test cases below for an example:
    assert(asteroid5.getPositionAndRadius() == (280, 280, 10))
    assert(asteroid6.getPositionAndRadius() == (320, 320, 10))
    assert(str(asteroid6) ==
           "SplittingAsteroid at (320, 320) with radius=10 " +
           "and direction (0, 1)")
    assert(getLocalMethods(SplittingAsteroid) == ['__init__',
                                                  'reactToBulletHit'])
    print("Done!")


#################################################################
# Homework 14 Main
#################################################################


def testAll():
    testBookClass()
    testAsteroidClasses()


def main():
    testAll()


if __name__ == '__main__':
    main()
