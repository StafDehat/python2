# Author: Andrew Howard

from string import printable

charStr=""
for x in range(32,127):
  charStr += chr(x)
print charStr

for x in printable:
  print "%r %d" % (x, ord(x))

