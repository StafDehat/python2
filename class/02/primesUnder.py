#!/usr/bin/python

import math

def isPrime(x):
  root = int(math.sqrt(x))
  for i in xrange(2,root+1):
    if ( x%i == 0 ):
      return False
  return True
#END isPrime()

def primesUnder(x):
  for i in xrange(2,x):
    if isPrime(i):
      print i
#END primesUnder()

primesUnder(100)

