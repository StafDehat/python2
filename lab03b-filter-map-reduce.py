# Author: Andrew Howard

aList = range(2,18,3)

evenList = []
squareList = []
listSum = 0

for x in aList:
  # This is filtering:
  if ( x % 2 == 0 ):
    evenList.append(x)
  # This is mapping:
  squareList.append(x*x)
  # This is reducing:
  listSum += x

print aList
print evenList
print squareList
print listSum
