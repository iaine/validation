'''
 Uses http://digitalhumanities.org/dhq/vol/1/1/000005/000005.html
'''
import nltk
import string

formative = ["NN","VV","JJ"]

f = open('melville.txt','r')
lines = f.read()
symbols = []
sentences = nltk.sent_tokenize(lines) #tokenize sentences

for sentence in sentences:
    words = nltk.pos_tag(nltk.word_tokenize(str(sentence)))
    l = len(words)
    if l % 2 > 0:
        l = l-1
    for n in xrange(0, l ):
        if n+1 < l and words[n][0] not in string.punctuation:
            pars = []
            if words[n][1][:2] in formative and words[n+1][1][:2] in formative:
                pars.append((words[n][0], 1))
            elif words[n][1][:2] not in formative and words[n+1][1][:2] not in formative:
                pars.append((1, words[n][0]))
            else:
                pars.append((words[n][0], words[n+1][0]))
                n += 2

            for p in pars:
                a, b = p
                if a == 1:
                    symbols.append("F")
                elif b == 1:
                    symbols.append("S")
                else:
                    symbols.append("B")
        elif words[n][0] in string.punctuation:
            symbols.append(words[n][0])


print(symbols)     
fl = float(len(symbols))
print("F: {0} {1}".format(symbols.count("F"), (symbols.count("F")/fl)))
print("S: {0} {1}".format(symbols.count("S"), (symbols.count("S")/fl)))
print("B: {0} {1}".format(symbols.count("B"), (symbols.count("B")/fl)))

print("P: {0}".format(fl - (symbols.count("F") + symbols.count("S")+symbols.count("B"))))
