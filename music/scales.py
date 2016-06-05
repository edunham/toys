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

def print_tab(notes, freqs):
    names = [l[0] for l in freqs]
    strings = ['E4', 'B3', 'G3', 'D3', 'A2', 'E2']
    stringnames = ['E','B','G','D','A','e']
    n_frets = 15
    frets = []
    for s in range(len(strings)):
        start = names.index(strings[s])
        frets.append(names[start:start+15])
    """
    e ------------------------------------------------
    b ------------------------------------------------
    g ------------------------------------------------
    d ------------------------------------------------
    a ------------------------------------------------
    E ------------------------------------------------
    """
    for s in range(len(strings)):
        print stringnames[s] + ' -' + '-'.join(frets[s])
        

def get_freqs(fn = 'a440'):
    fd = open(fn, 'r')
    # each lines is note name, frequency in Hz, wavelength in cm
    lines = [l.split() for l in fd.readlines()]
    lines = [[l[0], float(l[1]), float(l[2])] for l in lines]
    fd.close()
    return lines

def scale(freqs, root, type='major'):
    scales = {'major':[2, 2, 1, 2, 2, 2, 1],
              'natural minor':[2, 1, 2, 2, 1, 2, 2],
              'melodic minor':[2, 1, 2, 2, 2, 2, 1], # nat. minor when descending
              'harmonic minor':[2, 1, 2, 2, 1, 3, 1],
              'chromatic':[1,1,1,1,1,1,1,1,1,1,1,1,1],
              }
              # pentatonic is all strange though
    names = [l[0] for l in freqs]
    out = [root]
    scale = scales[type]
    idx = names.index(root)
    for i in scale:
        idx = idx + i
        out.append(names[idx])
    return out

def main():
    freqs = get_freqs()
    test_scale = scale(freqs, 'A2')
    print_tab(test_scale, freqs)

if __name__ == "__main__":
    main()
