from primes import primes
import math

"""
To run: 

    yaourt -S pypy
    pypy goldbach.py

"""
ops = 0
goldbach = 33
i = 0
while(True):
    i = 0
    breakdown = None
    potentials = []
    while (primes[i] <= goldbach):
        potentials.append(primes[i])
        i += 1
    if potentials[-1:] == goldbach:
        goldbach += 2 # NOT COMPOSITE
    else:
        for p in potentials:
            ops += 3
            mth =  math.sqrt((goldbach - p) / 2.0)
            if mth == int(mth): # nasty hax to check it's square of int
                breakdown = [p, mth]
        if breakdown != None:
            goldbach += 2
        else:
            print "we have a winner!"
            print goldbach
            print "how many operations: " + str(ops)
            print "at one operation per minute, years to calculate by hand: "
            print ops/(60*24*7*52.0)
            exit()
