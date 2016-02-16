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
def playOnce(wallet):
  # Play loop
  firstRoll = True
  while True:
    total = rollDice(2)
    if firstRoll:
      # 7 or 10 wins
      # 2, 3, 12 loss
      if (total == 7) or (total == 10):
        print total
        wallet = wallet + 10
        print "You win - remaining balance $",wallet
        return wallet
      elif (total == 2) or (total == 3) or (total == 12):
        print total
        wallet = wallet - 10
        print "You lose - remaining balance $",wallet
        return wallet
      else:
        print total
        point = total
        firstRoll = False
    else:
      if (total == 7):
        print total
        wallet = wallet - 10
        print "You lose - remaining balance $",wallet
        return wallet
      elif (total == point):
        print total
        wallet = wallet + 10
        print "You win - remaining balance $",wallet
        return wallet
      else:
        continue


wallet = playOnce(wallet)
while True:
  if ( wallet <= 0 ):
    print "Sorry, you're broke."
    quit()
  print "Play again?"
  choice = raw_input().lower()
  if ( choice == "yes" ):
    wallet = playOnce(wallet)
    continue
  elif ( choice == "no" ):
    break
  else:
    print "Please enter \"yes\" or \"no\""


