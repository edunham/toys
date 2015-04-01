#! /usr/bin/env python
import sys

"""
Write a program that translates english text to pig latin (Pig Latin takes the
first consonant (or consonant cluster) of an English word, moves it to the end
of the word and suffixes an ay, or if a word begins with a vowel you just add
way to the end.) (bonus points for translating back from piglatin to english)
"""

vowels = 'aeiouy'

def lat(w):
    if w[0] in vowels:
        return w+'way'
    idx = 0
    while w[idx] not in vowels:
        idx += 1
    return w[idx:]+w[:idx]+"ay"

def latinate(text):
    out = []
    text = text.split()
    for t in text:
        out.append(lat(t))
    return ' '.join(out)

def ang(w):
    if w[0] in vowels and w[-3:] is 'way':
        return w[:-3]
    else:
        return 'nope'

def anglicize(text):
    out = []
    text = text.split()
    for t in text:
        out.append(ang(t))
    return ' '.join(out)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "gimme a phrase in quotes"
        exit(-1)
    print latinate(' '.join(sys.argv[1:]))

