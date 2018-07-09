'''
    Script that uses the extract method from McGann and Samuels's
    Deformance and Interpretation paper
'''
import nltk

formative = ["NN","VV","JJ"]

f = open('coleridge.txt','r')
lines = f.read().splitlines()

prose_poem =  ' '.join(lines)

nouns = []
verbs = []
line = ""
reading2 = ""
for sentence in lines:
    words = nltk.pos_tag(nltk.word_tokenize(str(sentence)))
    
    for word in words:
        # Capture only the nouns, else print length of words for empty space
        if word[1].startswith('N'):
            line += word[0] + ' '
        else:
            line += ' ' * len(word[0])

        if word[1].startswith('V'):
            reading2 += word[0] + ' '
        else:
            reading2 += ' ' * len(word[0])

    nouns.append(line + "\n")
    line = ""
    verbs.append(reading2 + "\n")
    reading2 = ""

print("Prose poem")
print(prose_poem.replace("   ", " "))

print("Noun Reading")
print("\n".join(nouns))

print("Verb Reading")
print("\n".join(verbs))
