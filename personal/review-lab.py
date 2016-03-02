# Solution:
# https://dl.dropboxusercontent.com/u/68071780/labdone.py

# Author: Andrew Howard
import random
import math
import sys

# Initialize
wallet = 100
print "Beginning balance: $",wallet

# Roll 1 die, return value
def dieRoll():
  #return int(math.ceil(random.random() * 6))
  return random.randint(1,6)

# Roll X dice, return sum
def rollDice(count):
  total = 0
  while count > 0:
    total = total + dieRoll()
    count = count - 1
  return total

# Play a round
def playOnce(bet):
  # Play loop
  firstRoll = True
  while True:
    total = rollDice(2)
    if firstRoll:
      # 7 or 11 wins
      # 2, 3, 12 loss
      if (total == 7) or (total == 11):
        print total
        print "You won $",bet
        return bet
      elif (total == 2) or (total == 3) or (total == 12):
        print total
        print "You lost $",bet
        return 0-bet
      else:
        print total,
        point = total
        firstRoll = False
    else:
      if (total == 7):
        print total
        print "You lost $",bet
        return 0-bet
      elif (total == point):
        print total
        print "You won $",bet
        return bet
      else:
        print total,
        continue


bet = 10
wallet = wallet + playOnce(bet)
while True:
  if ( wallet <= 0 ):
    print "Sorry, you're broke."
    quit()
  print "Remaining balance: $",wallet
  print "Play again? [y/n] ",
  choice = raw_input().lower()
  if ( choice in "Yy" ):
    wallet = wallet + playOnce(bet)
    continue
  elif ( choice in "Nn" ):
    break
  else:
    print "Please enter \"y\" or \"n\""


