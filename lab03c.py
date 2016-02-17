# Author: Andrew Howard

myFile = open("trees.dat", "r")

lineNum=0
treeList = []
for line in myFile:
  lineNum += 1
  try:
    height = int(line)
    treeList.append(height)
  except ValueError:
    print "Invalid data on line %d: %r" % (lineNum, line)

print "Trees:      %d" % (len(treeList))
print "Avg height: %.1f" % (float(sum(treeList))/len(treeList))
print "Tallest:    %d" % (max(treeList))
print "Shortest:   %d" % (min(treeList))

