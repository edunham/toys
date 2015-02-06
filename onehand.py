#! /usr/bin/python

# I assume https://github.com/vinces1979/pwgen/ knows what he's doing, so I'll
# get entropy the same way
from random import SystemRandom
import string
choice = SystemRandom.choice

righthand = ['7', '8', '9', '0', '-', '=', '&', '*', '(', ')', '_', '+', 'y',
'u', 'i', 'o', 'p', '[', ']', '\\', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|',
'g', 'h', 'j', 'k', 'l', ';', "'", 'G', 'H', 'J', 'K', 'L', ':', '"', 'b',
'n', 'm', ',', '.', '/', 'B', 'N', 'M', '<', '>', '?', ' ']

lefthand = ['`', '1', '2', '3', '4', '5', '6', '7', '~', '!', '@', '#', '$',
'%', '^', '&', 'q', 'w', 'e', 'r', 't', 'y', 'Q', 'W', 'E', 'R', 'T', 'Y',
'a', 's', 'd', 'f', 'g', 'h', 'A', 'S', 'D', 'F', 'G', 'H', 'z', 'x', 'c',
'v', 'b', 'n', 'Z', 'X', 'C', 'V', 'B', 'N', ' ']

def typeable(word, hand):
    for c in word:
        if c not in hand:
            return False
    return True

def correcthorse(hand, words):
    handed = []
    for w in words:
        w = w.strip(' \t\n\r')
        if typeable(w, hand):
            handed.append(w)
    return handed

def notletters(maybeletters):
    return [m for m in maybeletters if not m in string.ascii_letters]

print notletters(righthand)

testwords = ['loop', 'moon', 'manatee', 'sadder', 'hodor' ]
#correcthorse(righthand, testwords)
#correcthorse(righthand, open('/home/miea/repos/toys/wordfile'))
#correcthorse(righthand, open('/usr/share/dict/words'))


