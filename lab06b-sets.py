# Author: Andrew Howard

import random

data = range(0,50)
control = set(random.sample(data,6))
setList = []
for x in xrange(1000):
  setList.append(set(random.sample(data,6)))

counter = 0
for aSet in setList:
  if len(aSet & control) > 1:
    counter += 1

print counter,"sets had 2+ duplicates with control"

