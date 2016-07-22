#! /usr/bin/env python
import string

ciphered = "LVFU XAN YIJ UVXRB RKOYOFB"

def make_rot_n(n):
    # http://stackoverflow.com/questions/3269686/short-rot13-function
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = string.maketrans(lc + uc,
                             lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: string.translate(s, trans)


for i in range(26):
    rotator = make_rot_n(i)
    deciphered = rotator(ciphered)
    print str(i) + ' ' + deciphered
