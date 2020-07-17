#################################################
# 15-112-n18 hw5-bonus
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

#################################################
# hw5-bonus problems
#################################################


def runSimpleProgram(program, args):
    newProgram = []
    numLines = 0
    currentLine = 0
    localVariables = []
    for line in program.splitlines():
        if not(line.startswith("!")):
            line = line.split()
            newProgram.append(line)
            numLines += 1

    print(newProgram)

    while currentLine != numLines:
        if newProgram[currentLine][0].startswith('L'):
            if newProgram[currentLine][1] == '-':
                if newProgram[currentLine][2] == 'A0':
                localVariables.append()
            localVariables.append()

        #################################################
        # hw5-bonus tests
        #################################################


def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1 + 2 + 3 + 4 + 5)
    assert(runSimpleProgram(sumToN, [10]) == 10 * 11 // 2)
    print("Passed!")

#################################################
# hw5-bonus Main
################################################


def testAll():
    testRunSimpleProgram()


def main():
    testAll()


if __name__ == '__main__':
    main()
