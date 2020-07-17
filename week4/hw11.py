#################################################
# 15-112-n18 hw11
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

import string


def alternatingSum(lst):
    adding = False

    if len(lst) == 0:
        return 0
    else:
        if not(adding):
            # Since adding is false, it will minus the two numbers
            adding = True
            return lst[0] - alternatingSum(lst[1:])
        else:
            # Since adding is true, it will add the two numbers
            adding = False
            return lst[0] + alternatingSum(lst[1:])


def binarySearchValuesHelper(L, v, start, end, stepsList):
    mid = (start + end) // 2
    if start == end:
        return stepsList
    else:
        if L[mid] == v:
            stepsList.append((mid, v))
        elif L[mid] < v:
            stepsList.append((mid, L[mid]))
            # start is inclusive and it already checked the middle, so it is
            # set to middle + 1
            start = mid + 1
            return binarySearchValuesHelper(L, v, start, end, stepsList)
        else:
            stepsList.append((mid, L[mid]))
            end = mid
            return binarySearchValuesHelper(L, v, start, end, stepsList)
    return stepsList


def binarySearchValues(L, v):
    start = 0
    end = len(L)
    stepsToValue = []
    return binarySearchValuesHelper(L, v, start, end, stepsToValue)


def generateLetterString(s):
    if len(s) != 2:
        return ""
    elif s[0] == s[1]:
        return s[0]
    else:
        if s[0] < s[1]:
            return s[0] + generateLetterString(chr(ord(s[0]) + 1) + s[1])
        else:
            return s[0] + generateLetterString(chr(ord(s[0]) - 1) + s[1])

    #################################################################
    # Homework 11 Test Functions
    #################################################################


def alternatingSumTest1():
    print("Testing alternatingSum()...", end='')
    assert(alternatingSum([]) == 0)
    assert(alternatingSum([100]) == 100)
    assert(alternatingSum([1, 2, 3, 4, 5]) == 3)
    assert(alternatingSum([1, 10, 6, 2, 9]) == 4)
    assert(alternatingSum([6000, 2, 3]) == 6001)
    print("passed!")


def binarySearchValuesTest1():
    print("Testing binarySearchValues()...", end='')
    assert(binarySearchValues(['a', 'c', 'f', 'g', 'm', 'q'], 'c') == [
        (3, 'g'), (1, 'c')])
    assert(binarySearchValues(['a', 'b', 'c', 'h', 'z'], 'c') == [(2, 'c')])
    assert(binarySearchValues(['a', 'k', 'z'], 'z') == [(1, 'k'), (2, 'z')])
    assert(binarySearchValues(['a', 'k', 'z'], 'a') == [(1, 'k'), (0, 'a')])
    assert(binarySearchValues(['a', 'a', 'a', 'a', 'a'], 'a') == [(2, 'a')])
    print("passed!")


def generateLetterStringTest1():
    print("Testing generateLetterString()...", end='')
    assert(generateLetterString("a") == "")
    assert(generateLetterString("aa") == "a")
    assert(generateLetterString("ko") == "klmno")
    assert(generateLetterString("me") == "mlkjihgfe")
    assert(generateLetterString("az") == "abcdefghijklmnopqrstuvwxyz")
    assert(generateLetterString("za") == "zyxwvutsrqponmlkjihgfedcba")
    print("passed!")

#################################################################
# Homework 11 Main
#################################################################


def testAll():
    alternatingSumTest1()
    binarySearchValuesTest1()
    generateLetterStringTest1()


def main():
    testAll()


if __name__ == '__main__':
    main()
