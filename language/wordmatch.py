#! /usr/bin/env python
import string
import copy

one = open("puzzle2clue.txt", 'r')
two = open("puzzle2.txt", 'r')

one = one.read()
two = two.read()

one = one.translate(string.maketrans("",""), string.punctuation).split()
twi = [int(x) for x in two.translate(string.maketrans("",""), string.punctuation).split()]

one.reverse()
two = two.split()

outrev = ''
cc = 0
for i in range(len(twi)): #n in twi:
    n = twi[i]
    if cc >= 75:
        outrev = outrev + '\n'
        cc = 0
    if two[i][-1] in ['.', ',', ';']:
        pct = two[i][-1]
        print pct
    else: pct = ''
    outrev = outrev + one[n] + pct + ' '
    cc += len(one[n])
print outrev

