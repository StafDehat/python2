#!/usr/bin/python

import datetime

def next20Leaps():
  now = datetime.datetime.now()
  currentYear = now.year
  testYear = currentYear + 1
  counter = 0
  while ( counter < 20 ):
    if ( testYear % 4 == 0 ):
      if (testYear % 400 == 0):
        print testYear
        counter += 1
      elif ( testYear%100 == 0 ):
        continue
      else:
        print testYear
        counter += 1
      #END if
    #END if
    testYear += 1
  #END while
#END next20Leaps()

next20Leaps()

