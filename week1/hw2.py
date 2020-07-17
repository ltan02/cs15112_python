#################################################
# 15-112-n18 hw2
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

import math

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)

#################################################
# hw2 problems
#################################################


def isPrime(n):  # Taken from the cs.cmu.edu/~112n18 notes
    if (n < 2):
        return False
    for factor in range(2, n):
        if (n % factor == 0):
            return False
    return True

def rotateNumber(x):
    if x >= 0 and isinstance(x, int):
        counter = 0
        Number = x
        while Number > 0:
            Number //= 10
            counter += 1

        if x == 0:
            counter = 1

        lastNum = x % 10  # To get the last digit
        otherNum = x // 10  # To get the first three digits
        newNum = (lastNum * (10**(counter - 1))) + otherNum
        return newNum

def isCircularPrime(x):
    if x >= 0 and isinstance(x, int):
        prime = 0
        counter = 0
        Number = x
        while Number > 0:
            Number //= 10
            counter += 1

        if x == 0:
            counter = 1

        z = x

        for y in range(counter):
            if isPrime(z) == True:
                prime += 1
                z = rotateNumber(z)

        if prime == counter:
            return True
        else:
            return False

def nthCircularPrime(n):
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if isCircularPrime(guess):
            found += 1
    return guess

def countDigit(n, d):
    count = 0
    while n > 0:
        currDigit = n % 10
        if currDigit == d:
            count += 1
        else:
            break
        n //= 10
    return count

def longestDigitRun(n):
    n = abs(n)
    if n < 10:
        return n
    maxCount = 0
    minDigit = 100
    while n > 0:
        currDigit = n % 10
        currCount = countDigit(n, currDigit)
        if((currCount > maxCount) or (currCount == maxCount and currDigit < minDigit)):
            maxCount = currCount
            minDigit = currDigit
        n //= 10
    return minDigit

    #################################################
    # hw2 Test Functions
    ################################################


def testRotateNumber():
    print('Testing rotateNumber()... ', end='')
    assert(rotateNumber(1234) == 4123)
    assert(rotateNumber(4123) == 3412)
    assert(rotateNumber(3412) == 2341)
    assert(rotateNumber(2341) == 1234)
    assert(rotateNumber(5) == 5)
    assert(rotateNumber(111) == 111)
    print('Passed!')


def testIsCircularPrime():
    print('Testing isCircularPrime()... ', end='')
    assert(isCircularPrime(2) == True)
    assert(isCircularPrime(11) == True)
    assert(isCircularPrime(13) == True)
    assert(isCircularPrime(23) == False) #remove
    assert(isCircularPrime(79) == True)
    assert(isCircularPrime(197) == True)
    assert(isCircularPrime(1193) == True)
    assert(isCircularPrime(42) == False)
    print('Passed!')


def testNthCircularPrime():
    print('Testing nthCircularPrime()... ', end='')
    assert(nthCircularPrime(0) == 2)
    assert(nthCircularPrime(4) == 11)
    assert(nthCircularPrime(5) == 13)
    assert(nthCircularPrime(11) == 79)
    assert(nthCircularPrime(15) == 197)
    assert(nthCircularPrime(25) == 1193)
    print('Passed!')


def testLongestDigitRun():
    print('Testing longestDigitRun()... ', end='')
    assert(longestDigitRun(117773732) == 7)
    assert(longestDigitRun(-677886) == 7)
    assert(longestDigitRun(5544) == 4)
    assert(longestDigitRun(1) == 1)
    assert(longestDigitRun(0) == 0)
    assert(longestDigitRun(22222) == 2)
    assert(longestDigitRun(111222111) == 1)
    print('Passed.')

#################################################
# hw2 Main
################################################


def testAll():
    testRotateNumber()
    testIsCircularPrime()
    testNthCircularPrime()
    testLongestDigitRun()


def main():
    testAll()


if __name__ == '__main__':
    main()
