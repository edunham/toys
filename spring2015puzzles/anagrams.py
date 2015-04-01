#! /usr/bin/env python
import itertools
import sys

def get_anagrams(word):
    return [''.join(p) for p in itertools.permutations(word)]

def in_dictionary(lsit):
    lsit.sort()
    idx = 0
    found = []
    with open('/usr/share/dict/words') as words:
        for w in words:
            if lsit[idx] == w:
                idx += 1
                found.append(w)
            elif lsit[idx]<w:
                idx += 1
            if idx >= len(lsit):
                break
    return found

if __name__ == "__main__":
    if len(sys.argv)<2:
        print "you must give a word"
        exit(-1)
    an = get_anagrams(sys.argv[1])
    print "Anagrams of the word:"
    print an
    print "Anagrams found in dictionary:"
    print in_dictionary(an)
