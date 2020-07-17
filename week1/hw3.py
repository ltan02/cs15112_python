#################################################
# 15-112-m18 hw3
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

#################################################
# hw3 problems
#################################################


def vowelCount(s):
  vowelCounter = 0
  text = s.lower()
  for looking in text:
    if looking in "aeiou":
      vowelCounter += 1
  return vowelCounter


def areAnagrams(s1, s2):
  s1lower = s1.lower()
  s2lower = s2.lower()
  counter1 = 0
  if len(s1lower) == len(s2lower):
    while counter1 < len(s1lower):
      tempLetter = s1lower[counter1]
      currCounts1 = s1lower.count(tempLetter)
      currCounts2 = s2lower.count(tempLetter)
      if currCounts1 == currCounts2:
        counter1 += 1
      else:
        return False
  else:
    return False
  return True


def patternedMessage(message, pattern):
  pattern = pattern.strip()
  message = message.replace(" ", "")
  newMessage = ""
  counter = 0

  for rows in range(len(pattern)):
    if pattern[rows] == " ":
      newMessage += " "
    elif pattern[rows] == "\n":
      newMessage += "\n"
    else:
      if counter == 0:
        newMessage += message[counter]
        counter += 1
      elif len(message) == 1:
        newMessage += message
      elif counter % (len(message) - 1) != 0:
        newMessage += message[counter]
        counter += 1
      else:
        newMessage += message[counter]
        counter = 0
  print(newMessage)
  return newMessage


#################################################
# hw3 Test Functions
#################################################


def testVowelCount():
  print("Testing vowelCount()...", end="")
  assert(vowelCount("abcdefg") == 2)
  assert(vowelCount("ABCDEFG") == 2)
  assert(vowelCount("") == 0)
  assert(vowelCount("This is a test.  12345.") == 4)
  assert(vowelCount(string.ascii_lowercase) == 5)
  assert(vowelCount(string.ascii_lowercase * 100) == 500)
  assert(vowelCount(string.ascii_uppercase) == 5)
  assert(vowelCount(string.punctuation) == 0)
  assert(vowelCount(string.whitespace) == 0)
  print("Passed!")


def testAreAnagrams():
  print("Testing areAnagrams()...", end="")
  assert(areAnagrams("", "") == True)
  assert(areAnagrams("abCdabCd", "abcdabcd") == True)
  assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
  assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
  assert(areAnagrams("abc", "abcc") == False)
  print("Passed!")


def testPatternedMessage():
  print("Testing patternedMessage()...", end="")
  # this set of test cases is a bit more cumbersome, but more rigorous
  parms1 = [
      ("Go Pirates!!!", """
***************
******   ******
***************
"""),
      ("Three Diamonds!", """
  *     *     *
 ***   ***   ***
***** ***** *****
 ***   ***   ***
  *     *     *
"""),
      ("Go Steelers!", """
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
""")]
  solns1 = [
      """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
""",
      """
  T     h     r
 eeD   iam   ond
s!Thr eeDia monds
 !Th   ree   Dia
  m     o     n
""",
      """
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
  ]
  # this set of test cases is easier to debug
  parms2 = [("A-C D?", """
*** *** ***
** ** ** **
"""),
            ("A", "x y z"),
            ("The pattern is empty!", "")
            ]
  solns2 = [
      """
A-C D?A -CD
?A -C D? A-
""",
      "A A A",
      ""
  ]

  # Test Cases 1
  # Comment the for loop below in for more rigorous test cases.
  # They are a bit harder to debug.

  for i in range(len(parms1)):
    msg, pattern = parms1[i]
    soln = solns1[i]
    soln = soln.strip("\n")
    observed = patternedMessage(msg, pattern)
    assert(observed == soln)

  # Test Cases 2
  # These test cases are easier to debug.
  # for i in range(len(parms2)):
   # msg, pattern = parms2[i]
  #  soln = solns2[i]
   # soln = soln.strip("\n")
  #  observed = patternedMessage(msg, pattern)
  #  assert(observed == soln)
  print("Passed!")


#################################################
# hw3 Main
################################################

def testAll():
  testVowelCount()
  testAreAnagrams()
  testPatternedMessage()


def main():
  testAll()


if __name__ == '__main__':
  main()
