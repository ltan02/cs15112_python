#################################################
# 15-112-n18 hw5
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

import math
import string
import copy

#################################################
# Helper functions
#################################################


def almostEqual(d1, d2, epsilon=10**-7):
    return (abs(d2 - d1) < epsilon)


import decimal


def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def getScore(letterScores, word):
    score = 0
    for letters in word:
        score += letterScores[ord(letters) - 97]  # adds the score of the letter to the running total
    return score


def numOfLetters(word, letterscore):
    length = len(letterscore)
    alphabet = [0] * length  # creates an array of 0s corresponding to each letter in the alphabet
    for letter in word:
        alphabet[ord(letter) - 97] += 1  # counts how many times a certain letter appears in the word
    return alphabet


def canItFormWords(word, hand, letterscore):
    length = len(letterscore)
    countWords = numOfLetters(word, letterscore)
    countHand = numOfLetters(hand, letterscore)
    for eachLetter in range(length):
        if countHand[eachLetter] < countWords[eachLetter]:  # Checks to see if the word can be formed with the hand
            return False
    return True

#################################################
# hw5 problems
#################################################


def lookAndSay(a):
    answer = []
    counter = 1  # counter set to one because the counter would always because we count starting with 1 and not 0
    if len(a) == 0:
        return answer

    for eachDigit in range(1, len(a)):
        if a[eachDigit] == a[eachDigit - 1]:  # Compares the current digit and the digit before it in the list
            counter += 1
        else:
            tempTuple = (counter, a[eachDigit - 1])  # the tempTuple will hold the number of instances and the number
            answer.append(tempTuple)
            counter = 1
    tempTuple = (counter, a[eachDigit])
    answer.append(tempTuple)
    return answer


def inverseLookAndSay(a):
    answer = []

    for eachTuple in a:
        for repeatedNumbers in range(eachTuple[0]):  # since the first digit in the tuple is always the number of instances, this is how many times the number needs to be added to the list
            answer.append(eachTuple[1])

    return answer


def bestScrabbleScore(dictionary, letterScores, hand):
    wordsItCanForm = []
    scores = []

    for diffWords in dictionary:
        if canItFormWords(diffWords, hand, letterScores):
            wordsItCanForm.append(diffWords)  # adds all of the words that can be formed from the hand and that is in the dictionary

    if len(wordsItCanForm) == 0:
        return None

    for words in wordsItCanForm:
        scores.append(getScore(letterScores, words))  # adds all the scores to each index of the scores list corresponding to the word

    maxS = []
    score = 0
    for eachScore in range(len(scores)):
        if scores[eachScore] > score:
            maxS = []
            score = scores[eachScore]
            maxS.append(wordsItCanForm[eachScore])
        elif scores[eachScore] == score:
            maxS.append(wordsItCanForm[eachScore])

    if len(maxS) == 1:
        maxS = "".join(maxS)  # if maxS only has 1 word then it needs to be a string

    return ((maxS, score))

    #################################################
    # hw5 problems
    # Note:
    #   There are fewer test cases than usual below.
    #   You'll want to add your own!
    #################################################


def _verifyLookAndSayIsNondestructive():
    a = [1, 2, 3]
    b = copy.copy(a)
    lookAndSay(a)  # ignore result, just checking for destructiveness here
    return (a == b)

# add more test cases here!


def testLookAndSay():
    print("Testing lookAndSay()...", end="")
    assert(_verifyLookAndSayIsNondestructive() == True)
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1, 1, 1]) == [(3, 1)])
    assert(lookAndSay([-1, -1, 2, 7]) == [(2, -1), (1, 2), (1, 7)])
    assert(lookAndSay([3, 3, 8, -10, -10, -10]) == [(2, 3), (1, 8), (3, -10)])
    assert(lookAndSay([0, 0, 1, 2, 0, 3]) == [(2, 0), (1, 1), (1, 2), (1, 0), (1, 3)])
    print("Passed!")


def _verifyInverseLookAndSayIsNondestructive():
    a = [(1, 2), (2, 3)]
    b = copy.copy(a)
    inverseLookAndSay(a)  # ignore result, just checking for destructiveness here
    return (a == b)

# add more test cases here!


def testInverseLookAndSay():
    print("Testing inverseLookAndSay()...", end="")
    assert(_verifyInverseLookAndSayIsNondestructive(), True)
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3, 1)]) == [1, 1, 1])
    assert(inverseLookAndSay([(2, -1), (1, 2), (1, 7)]) == [-1, -1, 2, 7])
    assert(inverseLookAndSay([(2, 3), (1, 8), (3, -10)]) == [3, 3, 8, -10, -10, -10])
    assert(inverseLookAndSay([(2, 0), (1, 1), (1, 2), (1, 0), (1, 3)]) == [0, 0, 1, 2, 0, 3])
    print("Passed!")

# there are lots of test cases here :)


def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")

    def dictionary1(): return ["a", "b", "c"]

    def letterScores1(): return [1] * 26

    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"]

    def letterScores2(): return [1 + (i % 5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) == ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) == (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) == ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) == None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) == (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) == (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) == ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) == ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) == None)
    print("Passed!")

#################################################
# hw5 Main
################################################


def testAll():
    testLookAndSay()
    testInverseLookAndSay()
    testBestScrabbleScore()


def main():
    testAll()


if __name__ == '__main__':
    main()
