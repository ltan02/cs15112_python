#################################################
# 15-112-n18 hw1
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

import math

#################################################
# Helper functions
#################################################

#From lecture, do not change this function
def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)

#################################################
# hw1 problems
#################################################

#Edit these functions so they return the correct values.

def distance(x1, y1, x2, y2):
    dis = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    return dis

def isEquilateralTriangle(side1, side2, side3):
    if (almostEqual(side1, side2) and almostEqual(side2, side3) and almostEqual(side1, side3)):
        return True
    else:
        return False

def getKthDigit(n, k):
    new = abs(n) // (10 ** k)
    newmod = new % 10
    return newmod

def isPerfectSquare(n):
    if isinstance(n, int or float) and n >= 0:
        if (int(math.sqrt(n)) ** 2) == n:
            return True
        else:
            return False
    else:
        return False
        


#################################################
# hw1 Test Functions
################################################

def testDistance():
    print('Testing distance()...', end='')
    assert(almostEqual(distance(3.0, 0.0, 0.0, 4.0), 5.0))
    assert(almostEqual(distance(-1.0, 2.0, 3.0, 2.0), 4.0))
    assert(almostEqual(distance(-5, 5, 5, -5), 14.142135623730951))
    assert(almostEqual(distance(100.5, 50.2, 100.5, 50.2), 0.0))
    assert(almostEqual(distance(1000, 1000, -1000, -1000), 2828.42712474619))
    print('Passed.')

def testIsEquilateralTriangle():
    print('Testing isEquilateralTriangle()... ', end='')
    assert(isEquilateralTriangle(1,2,3) == False)
    assert(isEquilateralTriangle(1,2.0,3) == False)
    assert(isEquilateralTriangle(1.00000000000000001,1.0,1) == True)
    assert(isEquilateralTriangle(.3,.3, .1 + .1 + .1) == True)
    assert(isEquilateralTriangle(11,11,11) == True)
    assert(isEquilateralTriangle(1,1,3) == False)
    assert(isEquilateralTriangle(1,3,3) == False)
    assert(isEquilateralTriangle(1,3,1) == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

#################################################
# hw1 Main
################################################

def testAll():
    testDistance()
    testIsEquilateralTriangle()
    testGetKthDigit()
    testIsPerfectSquare()

def main():
    testAll()

if __name__ == '__main__':
    main()
