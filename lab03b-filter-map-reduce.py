# Author: Andrew Howard

aList = range(2,18,3)

evenList = []
squareList = []
listSum = 0

for x in aList:
  if ( x % 2 == 0 ):
    evenList.append(x)
  squareList.append(x*x)
  listSum += x

print aList
print evenList
print squareList
print listSum
