import math
import string

myFile = open("alice_in_wonderland.dat", "r")
data = myFile.read()

countTotal = 0
countE = 0

for char in data:
  if char in string.letters:
    countTotal += 1
    if char in "eE":
      countE += 1

print "Total e's:   ",countE
print "Total chars: ",countTotal
print "Percentage of 'eE': ",round(float(countE*100)/countTotal,2)
