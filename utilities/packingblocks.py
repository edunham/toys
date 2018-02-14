#! /usr/bin/env python

# From IRC:
#
# "I was thinking about a toy idea for my kid to teach multiplication through
# area representation.  2x3 is a two-inch-by-three-inch slab of something with
# lines on it, etc.  I'd need 45 pieces (since AxB = BxA, you can drop almost
# half) but if I wanted to put it away in almost equal 9x9 layers, how many
# layers would be required?"

# Let's draw a picture. We have a times table, a square from 1 to 9 each side,
# but a bunch of blocks are duplicates so I will X them out because we don't
# need to make them:

#  123456789
# 1 XXXXXXXX
# 2  XXXXXXX
# 3   XXXXXX
# 4    XXXXX
# 5     XXXX
# 6      XXX
# 7       XX
# 8        X
# 9

# First off I wanted to know if there's any hope of packing with no gaps. So I
# find the volume of units that it'll all take up. The function row() tells me
# the total area of the pieces in each row -- for row 3, I have a 3x1 piece, a
# 3x2 piece, and a 3x3 piece, so the total area is 18 units.

def row(end):
     sum = 0
     for i in range(1,end+1):
             sum += end * i
     return sum

# So to get the total volume of a set of times-table blocks going up to n (n has
# been 9 so far) I'll express which rows I have -- range(1,n+1) -- and sum up
# all their areas. Note that area of them all spread out, and volume, are
# synonymous here since I'm assuming they're 1 unit thick. This may come in
# handy later so I can put the blocks away making the best use of the 3d box,
# like if some go in vertically while others are horizontal. Again, here I'm
# just looking for a set size and box size that have a **chance** of packing
# into a box with a square footprint.

def math_toy_volume(n):
    return sum(map(row, range(1,n+1)))

# I happen to know from the original problem that the set had 45 pieces. If I
# try other set sizes, though, I would also like to know how many pieces they
# have. Easy, but easier to name it.

def math_toy_pieces(n):
    return sum(range(1,n+1))

# Anyways I want the ones that have any hope of packing into a square box so I
# need to get the factors of the area and then find dups in the list of factors.
# From https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
# I get:

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


for i in range(1,21):
    n = math_toy_volume(i)
    print str(n) + "\t" + str(sorted(factors(n)))
