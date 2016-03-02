import string

gdpFile = open("gdp.txt", "r")
gdpList = []
lineNum = 0
for gdpEntry in gdpFile:
  lineNum += 1
  lineItem = gdpEntry.split(",")
  try:
    lineItem.insert(0, float(lineItem[1])/int(lineItem[2]))
  except ValueError:
    print "Invalid data on line %d: %r" % (lineNum,gdpEntry)
    continue
  gdpList.append(lineItem)

gdpList = sorted(gdpList, reverse=True)

for gdpEntry in gdpList:
  print "%.5f  %s" % (gdpEntry[0],gdpEntry[1])

