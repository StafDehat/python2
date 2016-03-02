# Author: Andrew Howard

import string

myFile = open("alice_in_wonderland.dat", "r")
data = myFile.read().lower()

for searchStr in ("caterpillar", "gryphon"):
  print "First %s: %d" % (searchStr, data.find(searchStr))
  print "Last  %s: %d" % (searchStr, data.rfind(searchStr))
  print "Total %s: %d" % (searchStr, data.count(searchStr))


