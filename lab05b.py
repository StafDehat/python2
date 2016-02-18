"""
This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results. 
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

import sys

def fahrenheit_to_centigrade(*xtmps):
  print xtmps,type(xtmps)
  for xtmp in xtmps:
    if ( not isinstance(xtmp,(int,float)) ):
      continue
    nutmp = 5.0 / 9.0 * (xtmp - 32)
    print '%.1f degrees Fahrenheit is %.1f degrees Centigrade' % (
        xtmp, nutmp)
    

temp = 72
fahrenheit_to_centigrade(temp)
fahrenheit_to_centigrade(10,20,30,"a",40,50)    

for x in sys.argv[1:]:
  try:
    tempHeh = float(x)
  except ValueError:
    print "Invalid data:",x
    continue
  fahrenheit_to_centigrade(tempHeh)
