# Author: Andrew Howard

import string
import sys

def usage():
  print "Usage: %s filename" % (sys.argv[0])

def maxLen(iterable):
  longest = 0
  for x in iterable:
    if len(str(x)) > longest:
      longest = len(str(x))
  return longest

def printDict(data, lineLen):
  lineNum = 0
  valLen = maxLen(data.values())
  keyLen = maxLen(data.keys())
  print "Max value length:",valLen
  print "Max key length:  ",keyLen
  sortedData = sorted(zip(data.values(),data.keys()), reverse=True)
  while True:
    for x in (xrange(5)):
      index = lineLen*lineNum + x
      if index >= len(sortedData):
        print; return
      theVal = format(str(sortedData[index][0]), str((valLen))+"s")
      theKey = format(str(sortedData[index][1]), str((keyLen))+"s")
      print "'%s':%s   " % (theKey,theVal),
    print
    lineNum += 1

try:
  text = open(sys.argv[1],"r").read().lower()
except IndexError:
  print "Error: Missing argument(s)"
  usage()
  quit()
except IOError:
  print "Error opening",sys.argv[1]
  quit()

hist = {}
for char in text:
  if char in string.whitespace:
    continue
  hist[char] = hist.get(char,0) + 1

printDict(hist,5)

