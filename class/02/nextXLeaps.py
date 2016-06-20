#!/usr/bin/python

import datetime

def isLeapYear(year):
  if ( year % 4 == 0 ):
    if (year % 400 == 0):
      return True
    elif ( year%100 == 0 ):
      return False
    else:
      return True
    #END if
  #END if
#END isLeapYear()

def nextXLeaps(x):
  now = datetime.datetime.now()
  currentYear = now.year
  testYear = currentYear + 1
  counter = 0
  while ( counter < x ):
    if isLeapYear(testYear):
      print testYear
      counter += 1
    #END if
    testYear += 1
  #END while
#END nextXLeaps()  

def next20Leaps():
  nextXLeaps(20)
#END next20Leaps()

print "Next 20 Leap Years:"
next20Leaps()

print "Next 50 Leap Years:"
nextXLeaps(50)

