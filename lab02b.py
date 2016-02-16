# Author: Andrew Howard

import string

myFile = open("tmpprecip2012.dat", "r")

lineNum = 0
rainyDays = 0
totalPrecip = 0
for line in myFile:
  lineNum += 1
  try:
    precip = float(line[8:13])
  except ValueError:
    print "Invalid data on line "+str(lineNum)+":",line
    continue
  if ( precip == 0 ):
    continue
  totalPrecip += precip
  rainyDays += 1

print "Rainy days:",rainyDays
print "Total wet:",totalPrecip

