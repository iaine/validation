import math

lines = []

def NoteFreq(freq, n=False):
    power = 3
    if n is True:
        power = -3
    return  freq * math.pow(1.059463094359, power)

with open('poem.txt', 'rb') as f:
    lines = f.read().split('\n')

note = NoteFreq(440)

rev = lines[::-1]

for l in lines:
    print(note, len(l))
    note = NoteFreq(note, True)

print("Reverse")

for r in rev:
    print(note, len(r))
    note = NoteFreq(note)
