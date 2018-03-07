#! /usr/bin/env python

abc = "abcdefghijklmnopqrstuvwxyz"

def letter(n):
    return abc[n-1]


lanyard = "20 08 09 19 09 19 20 08 05 11 05 25 19 20 15 14 05 08 05 14 07 05"
numbers = [int(i) for i in lanyard.split(' ')]
letters = ''.join(letter(n) for n in numbers)
print letters
