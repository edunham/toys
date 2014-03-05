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

def print_tab(notes, f): # calling the note list f is dumb and i need it everywhere
    strings = ['E4', 'B3', 'G3', 'D3', 'A2', 'E2']
    n_frets = 15
    frets = []
    for s in len(strings):
        start = f.index(strings[s])
        frets[s] = f[start:start+15]

def get_freqs(fn = 'a440'):
    fd = open(fn, 'r')
    # each lines is note name, frequency in Hz, wavelength in cm
    lines = [l.split() for l in fd.readlines()]
    lines = [[l[0], float(l[1]), float(l[2])] for l in lines]
    fd.close()
    return lines

def scale(f, root, type='major'):
    scales = {'major':[2, 2, 1, 2, 2, 2, 1],
              'natural minor':[2, 1, 2, 2, 1, 2, 2],
              'melodic minor':[2, 1, 2, 2, 2, 2, 1], # nat. minor when descending
              'harmonic minor':[2, 1, 2, 2, 1, 3, 1],
              'chromatic':[1,1,1,1,1,1,1,1,1,1,1,1,1],
              }
              # pentatonic is all strange though
    names = [l[0] for l in f]
    out = [root]
    scale = scales[type]
    idx = names.index(root)
    for i in scale:
        idx = idx + i
        out.append(names[idx])
    return out

def main():
    f = get_freqs()
    print scale(f, 'A2')
    strings = ['E4', 'B3', 'G3', 'D3', 'A2', 'E2']    

if __name__ == "__main__":
    main()
