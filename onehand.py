#! /usr/bin/python

# I assume https://github.com/vinces1979/pwgen/ knows what he's doing, so I'll
# get entropy the same way
import random
import string
import pickle

choice = random.choice

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

def handedwords(hand, words):
    handed = []
    for w in words:
        w = w.strip(' \t\n\r')
        if typeable(w, hand):
            handed.append(w)
    return handed

def notletters(maybeletters):
    return [m for m in maybeletters if not m in string.ascii_letters]

def dump_hands():
    wordfile = '/home/miea/repos/toys/wordfile'
    rh = handedwords(righthand, open(wordfile))
    lh = handedwords(lefthand, open(wordfile))
    pickle.dump( rh, open( "right.hand", "wb" ) )
    pickle.dump( lh, open( "left.hand", "wb" ) )

def nuke_a_letter(w):
    return w #TODO fix all this
    if len(w) < 3:
        return w
    n = 2 #TODO randomly pick which letter to omit
    if choice([True, False]):
        return + w[:-n]+w[-(n+1):]
    else:
        return w[:-n]+w[-(n-1):]


def correcthorse(c):
    nl = notletters(righthand)
    rh = pickle.load( open( "right.hand", "rb" ) )
    pas = ''
    for i in range(c):
        w = choice(rh)
        if choice([True, False]):
            w = nuke_a_letter(w)
        else:
            if choice([True, False]):
                pas = pas + w
            else:
                for q in range(choice(range(i))):
                    pas = pas + choice(nl)
    return pas

#dump_hands()
for i in range(20):
    print correcthorse(i)
