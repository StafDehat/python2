# Author: Andrew Howard

import random

classSize = 23

# Return whether or not list contains a duplicate value
def has_duplicates(inList):
  for x in inList:
    if ( inList.count(x) > 1 ):
      return True
  return False

# Generate a birthday
def birth():
  return random.randint(1,365)

# Generate a list of birthdays for class of 'size'
def birthGroup(size):
  birthdays = []
  for x in xrange(size):
    birthdays.append(birth())
  return birthdays

# Return odds of 2+ students having same birthday
def oddsOfSharedBirthday(groupSize):
  iterations = 1000
  dupeCount = 0
  for x in xrange(iterations):
    if has_duplicates(birthGroup(groupSize)):
      dupeCount += 1
  return float(dupeCount)/iterations*100

print "Odds of shared birthday: %.2f%%" % (oddsOfSharedBirthday(classSize))

