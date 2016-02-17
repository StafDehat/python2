# Author: Andrew Howard

# Import data from inFile into 2d list 'data'
def importData(data, inFile):
  lineCount = 0
  for line in inFile:
    lineCount += 1
    tmpList = []
    try:
      tmpList.append(int(line[0:2]))    # 0 Month
      tmpList.append(int(line[2:4]))    # 1 Day
      tmpList.append(int(line[4:8]))    # 2 Year
      tmpList.append(float(line[8:13])) # 3 Precipitation
      tmpList.append(int(line[14:]))    # 4 High temp
    except ValueError:
      print "Invalid data on line %d: %r" % (lineCount, line)
      continue
    data.append(tmpList)

# Print report by-month of all data in list
def monthlyReport(data):
  # Initialize almanac
  # Report format:
  # 0 Number of samples
  # 1 Average high
  # 2 Max high
  # 3 Min high
  report = []
  for x in xrange(13):
    report.append([0,0,0,9999])
  # Record records
  for day in data:
    month=day[0]
    # Recalculate new average temp
    #print "Report[month]:",report[month]
    #print "Day:          ",day
    oldAvg = report[month][0] * report[month][1]
    report[month][0] += 1
    newAvg = float(oldAvg + day[4]) / report[month][0]
    report[month][1] = newAvg
    # If temp higher than max, record new max
    if day[4] > report[month][2]:
      report[month][2] = day[4]
    # If temp lower than min, record new min
    if day[4] < report[month][3]:
      report[month][3] = day[4]
  print "Month  AvgTemp  MaxHigh  MinHigh"
  month=0
  for samples,avgTemp,maxHigh,minHigh in report:
    if samples == 0:
      continue
    month += 1
    print "%5d  %3.2f  %7d  %7d" % (month,avgTemp,maxHigh,minHigh)

file2012 = open("tmpprecip2012.dat", "r")
data2012 = []
importData(data2012, file2012)
print "2012 report:"
monthlyReport(data2012)

file100 = open("tmpprecip.dat", "r")
data100 = []
importData(data100, file100)
print "100-year report:"
monthlyReport(data100)


