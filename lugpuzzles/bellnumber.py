from operator import mul
from fractions import Fraction
"""
    $ pypy bellnumber.py
"""
def comb(n, k):
    return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

# kinda sorta uses http://mathworld.wolfram.com/BellNumber.html
# also used
# http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
# to save you from having to install scipy. you're welcome.

bk = [1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975]

n = 10

# find the lowest n for which bell number is divisible by one million
while(True):
    n += 1
    sigma = 0
    for k in range(n):
        sigma += (bk[k]*comb((n-1), k))
    bk.append(sigma)
    if (sigma % 1000000 == 0):
        print "bell number " + str(n) + " is "+ str(sigma)
        exit()
