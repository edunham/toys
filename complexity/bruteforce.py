#!/usr/bin/env python

def brute_force_search(l, value):
    for i in range(len(l)):
        if l[i] == value:
        return i
    return -1

if __name__ == "__main__":
    array = range(42)
    found = brute_force_search(array, 20)
