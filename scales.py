#! /usr/bin/env python2.7

import argparse

"""
Learning music theory by automating the process of figuring out which notes go
in which scales. Print tab for normally-tuned guitar.
"""

class Tab():
    def __init__(self):
        pass
    def pprint(self):
        pass

def get_freqs(fn = 'a440'):
    fd = open(fn, 'r')
    # each lines is note name, frequency in Hz, wavelength in cm
    lines = [l.split() for l in fd.readlines()]
    lines = [[l[0], float(l[1]), float(l[2])] for l in lines]
    fd.close()

def scale(f, note, type='major'):
    scales = {'major':[2, 2, 1, 2, 2, 2, 1],
              'natural minor':[2, 1, 2, 2, 1, 2, 2],
              'melodic minor':[2, 1, 2, 2, 2, 2, 1], # nat. minor when descending
              'harmonic minor':[2, 1, 2, 2, 1, 3, 1],
              'chromatic':[1,1,1,1,1,1,1,1,1,1,1,1,1],
              }
              # pentatonic is all strange though
    

def main():
    f = get_freqs()
    strings = ['E4', 'B3', 'G3', 'D3', 'A2', 'E2']    

if __name__ == "__main__":
    main()