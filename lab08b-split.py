import string

text = open("split.txt", "r").read().lower()
words = "".join(char for char in text if char not in string.punctuation)
wordHist = {}
for word in words.split():
  wordHist[word] = wordHist.get(word,0) + 1

print "Unique words:",len(wordHist)
print "Frequency:"
for freq,word in sorted(zip(wordHist.values(),wordHist.keys()),reverse=True):
  print "%5d  %s" % (freq,word)

