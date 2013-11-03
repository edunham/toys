#! /usr/bin/env python
import sys
import collections

def main():
    if len(sys.argv) < 2:
        exit("please invoke with filename")
    f = open(sys.argv[1], 'r')
    message = f.read()
    tokens = message.split()
    p = collections.Counter(tokens).items()
    q = sorted(p, key=lambda x : x[1])
    print q
    letterlist = ['e','t','a','o','n','i','s','r','h']
    guess = message[:]
    for i in range(len(letterlist)):
        print q[i][0]
        guess = guess.replace(' ' + q[i][0] + ' ', ' ' + letterlist[i] + ' ')
    print guess

if __name__ == "__main__":
    main()
