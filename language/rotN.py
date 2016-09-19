#! /usr/bin/env python
import string

ciphered = "LVFU XAN YIJ UVXRB RKOYOFB"
ciphered = "tcrh ttj lcf btgki ybdwjei"
ciphered = "tcrh tth fgs ncekw lsbwkvf"[::-1]
ciphered = "ehqqttxipqxnibeecnukdo"
def make_rot_n(n):
    # http://stackoverflow.com/questions/3269686/short-rot13-function
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    trans = string.maketrans(lc + uc,
                             lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: string.translate(s, trans)

def make_keyed_cesar(n):
    # http://stackoverflow.com/questions/3269686/short-rot13-function
    #lc =  "STONEHGABCDFIJKLMPQRUVWXYZ".lower()
    lc =  "DRUMESABCFGHIJKLNOPQTVWXYZ".lower()
    #uc = "STONEHGABCDFIJKLMPQRUVWXYZ"
    uc = "DRUMESABCFGHIJKLNOPQTVWXYZ"
    trans = string.maketrans(lc + uc,
                             lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: string.translate(s, trans)


def derp(ciphered):
    for i in range(26):
        rotator = make_keyed_cesar(i)
        deciphered = rotator(ciphered)
        print str(i) + ' ' + deciphered
