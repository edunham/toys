#! /usr/bin/env python

"""
So, I need a list of all DeBruijn sequences for a small alphabet and a
reasonably small length because of a crafts project. 

It turns out that the commonly available DeBruijn algorithms generate only
*one* result, and for B(2, 5) there are 2048 possible. The internet is also
unhelpful about providing a more general generation algorithm -- apparently
proving that 2046 of the B(2, 5) sequences exist is enough for most
mathematicians, without actually enumerating the things in a way that would be
useful for people who actually want to use them. See also, "I hate maths"...
"""

def allstrings(abc, size):
    # yay for
    # http://code.activestate.com/recipes/425303-generating-all-strings-of-some-length-of-a-given-a/
    c = []
    e = []
    for i in range(size):
        c = [[x]+y for x in abc for y in c or [[]]]
    for d in c:
        e.append(''.join(d))
    return e

def idx(big, small): # where in big does small occur?
    ls = len(small)
    lb = len(big)
    for n in range(lb - ls):
        if big[n:(n + ls)] == small:
            return n
    n = lb - ls
    while n < lb:
        wrapped = big[n:] + big[:((n + ls) - lb)]
        if wrapped == small:
            return n
        n += 1
    return -1

def check(find, candidate):
    for f in find:
        if idx(candidate, f) == -1:
            return False
    return True

def bruteforce(a, k):
    lres = len(a)**k # length of each debruijn sequence for these values
    find = allstrings(a, k)
    candidates = allstrings(a, lres) # ow
    found = []
    for c in candidates:
        if check(find, c):
            found.append(c)
    return found # not distinct strings, but otherwise correct -- they're
                 # allowed to wrap

def prettify(d): # d is a dict of dicts, such as out of bruteforce
    for a in d:
        print ''.join(a)
