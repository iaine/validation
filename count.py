'''
   Find the number of times a word occurs in a text
   and then print the text out by the count and 
   identify all unique words. 

   Playing around with ideas from Stephen Ramsay's book
'''
import sys
from collections import Counter

infile = sys.argv[1]
fulltxt = sys.argv[2]

alltexts = Counter()
poem = Counter()
keys = []

f = open(fulltxt, 'r')
for ln in f.read().splitlines():
    for m in ln.split():
        alltexts[m] += 1

poem_count = []
poems_count = []
with open(infile, 'r') as f:
    data =f.read()
    for d in data.split('\n'):
        for r in d.split():
            # Add word to list and keep in order for the later count
            if r not in keys:
                keys.append(r)
            # Count the number of occurences of the word
            poem[r] +=1

    for d in data.split('\n'):
        tmp = [str(poem[word]) for word in d.split()]
        poem_count.append(tmp)
        tmp = [str(alltexts[word]) for word in d.split()]
        poems_count.append(tmp)

# print the line out with the count of the words
print ("Count of words within text")
for line in poem_count:
    print(' '.join(line))

print ("Count of words within all texts")
for line in poems_count:
    print(' '.join(line))
