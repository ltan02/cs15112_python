#################################################
# 15-112-n18 hw10
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

#################################################
# Big-O Calculation Answers
#################################################

'''
def slow1(lst):  # N is the length of the list lst
    assert(len(lst) >= 2)
    a = lst.pop()
    b = lst.pop(0)
    lst.insert(0, a)
    lst.append(b)


The slow1 function is taking in a list of length greater than 2 and
switching the first and last element of the array. The Big O Time for each
line in the function is:
Line 1: 1
Line 2: 1
Line 3: N
Line 4: N
Line 5: 1

The Big O Time for the slow1 function is O(N)

def faster1(lst):
    lst[0], lst[len(lst) - 1] = lst[len(lst) - 1], lst[0]

The Big O Time for the faster1 function is O(1)


def slow2(lst):  # N is the length of the list lst
    counter = 0
    for i in range(len(lst)):
        if lst[i] not in lst[:i]:
            counter += 1
    return counter


The slow2 function is taking in a list and counting how many different
elements are in the list. The Big O Time for each line in the function is:
Line 1: O(1)
Line 2: Loops N times
Line 3: O(N)
Line 4: O(1)
Line 5: O(1)

The Big O Time for the slow2 function is O(N**2)

def faster2(lst):
    return len(set(lst))

The Big O Time for the faster2 function is O(1)


import string


def slow3(s):  # N is the length of the string s
    maxLetter = ""
    maxCount = 0
    for c in s:
        for letter in string.ascii_lowercase:
            if c == letter:
                if s.count(c) > maxCount or \
                   s.count(c) == maxCount and c < maxLetter:
                    maxCount = s.count(c)
                    maxLetter = c
    return maxLetter


The slow3 function looks through every letter in the string and checks
if it is a letter in the alphabet and records the letter with the highest
count in the word. The Big O Time for each line in the function is:
Line 1: O(1)
Line 2: O(1)
Line 3: Loops N times
Line 4: Loops 26 (constant) times
Line 5: O(N)
Line 6: O(1)
Line 7: O(N)
Line 8: O(1)

The Big O Time for the slow3 function is O(N**2)

def faster3(s):
    dictionary = {}
    letters = set(s)
    for letter in letters:
        dictionary[s.count(letter)] = letter

    return dictionary[max(dictionary)]

The Big O Time for the faster3 function is O(N)
'''


#################################################
# Invert Dictionary and Largest Sum of Pairs
#################################################


def invertDictionary(d):
    newDictionary = {}
    for element in d:
        tempElement = d[element]
        # Sets a temporary element to the value we are looking at
        tempSet = []
        for eachElement in d:
            # Checking if there are any other values that are the same
            if d[eachElement] == tempElement:
                # Adds the key to a temporary list
                tempSet.append(eachElement)
        newDictionary[tempElement] = set(tempSet)
        # The key is the value of the old dictionary and the value is the key of
        # the old dictionary
    return newDictionary


def largestSumOfPairs(a):
    if len(a) <= 1:  # O(N)
        return None  # O(1)

    max1 = max(a)  # O(N)
    # Gets the max of the list
    a.remove(max1)  # O(N)
    # Removes that max
    max2 = max(a)  # O(N)
    # Finds the second biggest number

    return max1 + max2  # O(1)

    #################################################################
    # Homework 10 Test Functions
    #################################################################


def invertDictionaryTest1():
    print("Testing invertDictionary()...", end='')
    assert(invertDictionary({}) == {})
    assert(invertDictionary({1: 2, 2: 3, 3: 4, 5: 3}) ==
           {2: set([1]), 3: set([2, 5]), 4: set([3])})
    assert(invertDictionary({0: 3, 10: 4, 2: 4, 3: 4, 1: 3}) ==
           {3: set([0, 1]), 4: set([10, 2, 3])})
    assert(invertDictionary({"hello": 3, "one": 4, "three": 4, 6: 4, 200: 3}) ==
           {3: set(["hello", 200]), 4: set(["one", "three", 6])})
    assert(invertDictionary({-1: 2, -3: 2, 100: 2, 300: 2}) ==
           {2: set([-1, -3, 100, 300])})
    print("passed!")


def largestSumOfPairsTest1():
    print("Testing largestSumOfParis()...", end='')
    assert(largestSumOfPairs([1, 3, 4, 6, 5]) == 11)
    assert(largestSumOfPairs([]) == None)
    assert(largestSumOfPairs([0]) == None)
    assert(largestSumOfPairs([1, 3, 2, 1, 2, 3]) == 6)
    assert(largestSumOfPairs([100, 300, 2, 3, 5]) == 400)
    assert(largestSumOfPairs([0, 0, 0, 0, 0]) == 0)
    print("passed!")

#################################################################
# Homework 10 Main
#################################################################


def testAll():
    invertDictionaryTest1()
    largestSumOfPairsTest1()


def main():
    testAll()


if __name__ == '__main__':
    main()
