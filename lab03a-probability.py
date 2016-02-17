import random

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

rollCount=1000
outcomes = 13 * [0]

for x in range(0,rollCount):
  roll = rollDice(2)
  outcomes[roll] = outcomes[roll]+1

for x in outcomes[2:]:
  print "%3d %.2f" % (x, float(outcomes[x])/rollCount*100)

