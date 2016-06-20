# Print the first x numbers of the fibonacci sequence
def fib(x):
  counter = 0
  oneBack = 0
  twoBack = 1
  while (counter < x):
    nextNum = oneBack + twoBack
    twoBack = oneBack
    oneBack = nextNum
    print nextNum
    counter += 1

print "fib(10):"
fib(10)
