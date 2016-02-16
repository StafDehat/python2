# Author: Andrew Howard

import string

myFile = open("alice_in_wonderland.dat", "r")
data = myFile.read()

countTotal = 0

for char in data:
  if char.isalpha():
    countTotal += 1

countE = data.count('e')+data.count("e")

print "Total e's:   ",countE
print "Total chars: ",countTotal
print "Percentage of 'eE': ",round(float(countE*100)/countTotal,2)
