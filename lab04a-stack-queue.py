# Author: Andrew Howard

def push(theList, value):
  theList.append(value)

stack = []
queue = []

print "The stack:"
print stack
for x in xrange(5):
  push(stack, x)
  print "Pushed",x
  print stack
while True:
  if len(stack) == 0:
    break
  x = stack.pop()
  print "Popped",x
  print stack

print "The queue:"
for x in xrange(5):
  print "Inserted",x
  queue.insert(0,x)
  print queue
print queue
while True:
  if len(queue) == 0:
    break
  x=queue.pop()
  print "Popped",x
  print queue
