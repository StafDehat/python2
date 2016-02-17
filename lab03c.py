# Author: Andrew Howard

myFile = open("trees.dat", "r")

treeList = []
for line in myFile:
  treeList.append(line)

print treeList
