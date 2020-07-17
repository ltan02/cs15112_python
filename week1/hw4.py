#################################################
# 15-112-n18 hw4
# Your Name: Alistair (Lance) Tan
# Your Andrew ID: alistait
# Your Section: A
#################################################

import math
import string

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


def shortString(s1, s2):
    if len(s1) < len(s2):
        return s1
    else:
        return s2


def longString(s1, s2):
    if len(s1) > len(s2):
        return s1
    else:
        return s2


#################################################
# hw4 problems
#################################################

def longestCommonSubstring(s1, s2):
    commonSubstring = ""
    shorter = shortString(s1, s2)
    longer = longString(s1, s2)
    for string2 in range(0, len(shorter)):
        for string1 in range((string2 + 1), len(longer)):
            match = shorter[string2:string1]  # Making all the possible strings that can be made in s1
            if match in longer:  # Checking to see if one of the possible strings in s1 is in s2
                if len(match) > len(commonSubstring):  # if match is greater then it would set commonSubstring to match
                    commonSubstring = match
                elif len(match) == len(commonSubstring):  # if they are the same then the lower ord() of the two would be the commonSubstring
                    if match < commonSubstring:
                        commonSubstring = match
    return commonSubstring


def bestStudentAndAvg(gradebook):
    newGradebook, maxPerson, maxGrade, currentAverage = "", "", -10**7, 0
    for eachLine in gradebook.splitlines():  # Splitting the lines
        if not(eachLine.startswith('#')):  # Removing lines that start with #
            newGradebook = eachLine
        for line in newGradebook.splitlines():  # Looping through all lines in newGradebook
            tempLine = line.split(',')  # Seperating everything that has commas
            for grade in range(1, len(tempLine)):  # Looping through all the grades in the temporary Line
                currentName = tempLine[0]  # Setting name to first index in seperated list
                currentAverage += int(tempLine[grade])  # adding all of the grades
            currentAverage = roundHalfUp(currentAverage / (len(tempLine) - 1))  # dividing by number of grades and rounding it
            if currentAverage > maxGrade:
                maxGrade, maxPerson = currentAverage, currentName
                currentAverage = 0
            else:
                currentAverage = 0
    return str(maxPerson) + ":" + str(maxGrade)


def encodeColumnShuffleCipher(message, key):
    lengthOfKey = len(key)
    if len(message) % lengthOfKey == 0:
        initialMessage = message
    else:
        initialMessage = message + ('-' * (lengthOfKey - (len(message) % lengthOfKey)))
    newMessage = ""
    for rows in range(lengthOfKey):
        sector = int(key[rows])
        for cols in range(sector, len(initialMessage), lengthOfKey):
            newMessage += initialMessage[cols]
    return str(key) + newMessage

# These two are bonus questions.


def decodeColumnShuffleCipher(message):
    return 42


def mostFrequentLetters(s):
    s = s.lower()
    fixedString = ""
    newString = ""
    for fixingString in range(len(s)):
        if s[fixingString].isalpha():
            fixedString += s[fixingString]
    for eachWord in range(len(s)):
        maxLetter = ''
        maxCount = 0
        for eachLetter in fixedString:
            if fixedString.count(eachLetter) > maxCount:
                maxCount = fixedString.count(eachLetter)
                maxLetter = eachLetter
            elif fixedString.count(eachLetter) == maxCount:
                maxCount = fixedString.count(eachLetter)
                if eachLetter < maxLetter:
                    maxLetter = eachLetter
        fixedString = fixedString.replace(maxLetter, "")
        newString += maxLetter
    return newString
    # Loop through
    # Find the count of highest and the letter
    # Add the letter to the new string
    # Remove it from the old string
    # Do the same thing over and over again until it loops through the entire string and the beginning string is empty

#################################################
# hw4 Test Functions
################################################


def testLongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("", "abqrcdest") == "")
    assert(longestCommonSubstring("abcdef", "") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed!")


def testBestStudentAndAvg():
    print("Testing bestStudentAndAvg()...", end="")
    gradebook = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) == "wilma:92")
    gradebook = """
#   ignore  blank   lines   and lines   starting    with    #'s
wilma,93,95

fred,80,85,90,95,100
betty,88
"""
    assert(bestStudentAndAvg(gradebook) == "wilma:94")
    gradebook = "fred,0"
    assert(bestStudentAndAvg(gradebook) == "fred:0")
    gradebook = "fred,-1\nwilma,-2"
    assert(bestStudentAndAvg(gradebook) == "fred:-1")
    gradebook = "fred,100"
    assert(bestStudentAndAvg(gradebook) == "fred:100")
    gradebook = "fred,100,110"
    assert(bestStudentAndAvg(gradebook) == "fred:105")
    gradebook = "fred,49\nwilma" + ",50" * 50
    assert(bestStudentAndAvg(gradebook) == "wilma:50")
    print("Passed!")


def testEncodeColumnShuffleCipher():
    print("Testing encodeColumnShuffleCipher()...", end="")

    msg = "ILOVECMUSOMUCH"
    result = "021IVMOCOCSU-LEUMH"
    assert(encodeColumnShuffleCipher(msg, "021") == result)

    msg = "WEATTACKATDAWN"
    result = "0213WTAWACD-EATNTKA-"
    assert(encodeColumnShuffleCipher(msg, "0213") == result)

    msg = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    result = "210DNAIRBWHNYRCSYRUEYHEBTTIESNOBESDLWTAIIPKEALEH"
    assert(encodeColumnShuffleCipher(msg, "210") == result)

    print("Passed!")


def testDecodeColumnShuffleCipher():
    print("Testing decodeColumnShuffleCipher()...", end="")
    msg = "0213WTAWACD-EATNTKA-"
    result = "WEATTACKATDAWN"
    assert(decodeColumnShuffleCipher(msg) == result)

    msg = "210DNAIRBWHNYRCSYR-UEYHEBTTIESNOBE-SDLWTAIIPKEALEH-"
    result = "SUDDENLYAWHITERABBITWITHPINKEYESRANCLOSEBYHER"
    assert(decodeColumnShuffleCipher(msg) == result)

    print("Passed!")


def testMostFrequentLetters():
    print("Testing mostFrequentLetters()...", end="")

    s = "We attack at Dawn"
    result = "atwcdekn"
    assert(mostFrequentLetters(s) == result)

    s = "Note that digits, punctuation, and whitespace are not letters!"
    result = "teanioscdhpruglw"
    assert(mostFrequentLetters(s) == result)

    s = ""
    result = ""
    assert(mostFrequentLetters(s) == result)

    print("Passed!")


#################################################
# hw4 Main
################################################

def testAll():
    testLongestCommonSubstring()
    testBestStudentAndAvg()
    testEncodeColumnShuffleCipher()
#    testDecodeColumnShuffleCipher()
    testMostFrequentLetters()


def main():
    testAll()


def f(s1, s2, c):
    print(-(s1.find(c)))
    return s2[-(s1.find(c))]  # hint: don’t miss the negative!


def ct1(s1, s2):
    result = ""
    for c in s1:
        print("%s : %s" % (c, f(s1, s2, c)))
        result = c + result
    return result


if __name__ == '__main__':
    main()
    print(ct1("abcd", "efgh"))
