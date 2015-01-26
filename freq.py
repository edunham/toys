#! /usr/bin/env python
import sys
import collections
import re

def main():
    if len(sys.argv) < 2:
        exit("please invoke with filename")
    f = open(sys.argv[1], 'r')
    message = f.read()
    d = collections.defaultdict(int)
    # ignore all the little comment things
    message = re.sub(r'\[[a-zA-Z0-9 ]\]', '', message)
    splitty = message.split()
    singles = collections.defaultdict(int)
    doubles = collections.defaultdict(int)
    triples = collections.defaultdict(int)
    for s in splitty:
        if len(s) == 1:
            singles[s] += 1
        elif len(s) == 2:
            doubles[s] += 1
        elif len(s) == 3:
            triples[s] += 1
    message = re.sub(r'\s','',message)
    for c in message:
        d[c] += 1
    tokens = message.split()
    p = collections.Counter(tokens).items()
    q = sorted(p, key=lambda x : x[1])
    sing = sorted(singles, key=lambda x : singles[x])
    doub = sorted(doubles, key=lambda x : doubles[x])
    trip = sorted(triples, key=lambda x : triples[x])
    order = sorted(d, key=lambda x : d[x])
    for thing in order:
        print thing + '\t' + str(d[thing]) 
    print "======================================================="
    for thing in sing:
        print thing + '\t' + str(singles[thing])
    print "======================================================="
    for thing in doub:
        print thing + '\t' + str(doubles[thing])
    print "======================================================="
    for thing in trip:
        print thing + '\t' + str(triples[thing])




if __name__ == "__main__":
    main()
