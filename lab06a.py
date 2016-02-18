# Author: Andrew Howard

import string
import sys

def usage():
  print "Usage: %s filename" % (sys.argv[0])

def printDict(data, lineLen):
  lineNum = 0
  while True:
    if lineNum*lineLen > len(hist):
      break
    print zip(  hist.keys()[ lineLen*lineNum : lineLen*(lineNum+1) ],
              hist.values()[ lineLen*lineNum : lineLen*(lineNum+1) ] )
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
  if not char.isalpha():
    continue
  hist[char] = hist.get(char,0) + 1

printDict(hist,5)
