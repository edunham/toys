#! /usr/bin/env python

"""
Resistors: Given several different values available, figure out the
fewest that can be globbed together, and in what configuration, to 
get a desired value

"""
# all values in ohms unless otherwise stated
start = [287.0, 706.0, 569.0, 411.0, 4.87]
start_tol = .05
desired = 1.65
DBG = False

pl = "parallel"
ss = "series"

class r():
    # one resistor
    def __init__(self, val, tol):
        self.v = val
        self.s = 1
        self.t = tol
    def p(self):
        return str(self.v)
    def components(self):
        return [self.v]

class g(r):
    # glob-of-resistors
    def __init__(self, v, a, b, how):
        self.v = v          # v = value of this glob
        self.l = a          # l = glob on left
        self.r = b          # r = glob on right
        self.c = how        # c = combination method -- STRING
        self.s = a.s + b.s  # s = size, # of total r in glob
        self.t = a.t + b.t  # t = tolerance, calc'd according to an ECE
    def p(self):
        # override
        return '(' + self.l.p() + ' ' + self.c + ' ' + self.r.p() + ')'
    def components(self):
        combo = self.l.components() + self.r.components()
        return combo.sort()

def in_parallel(r1, r2):
    return 1/((1/r1.v)+(1/r2.v))

def in_series(r1, r2):
    return r1.v + r2.v

def is_duplicate(g1, g2):
    if g1.v == g2.v and g1.components() == g2.components():
        return True
    return False

def makes(l1, l2):
    out = []
    vals = []
    for a in l1:
        for b in l2:
            for m in methods:
            c = g(in_parallel(a,b), a, b, pl)
            if DBG: print "appending " + c.p()
            if DBG: print "\t val is " + str(c.v) + " size " + str(c.s) + " tol " + str(c.t)
            out.append(c)

            c = g(in_series(a,b), a, b, ss)
            if DBG: print "appending " + c.p()
            if DBG: print "\t val is " + str(c.v) + " size " + str(c.s) + " tol " + str(c.t)
            out.append(c)
    out.sort(key = lambda x: x.v)
    return out

def build_d(start, tol):
    # TODO: be smart about tolerance and make d only as large as necessary
    # TODO: Also figure appends by looping rather than current derp 
    d = start
    d.append(makes(d[0], d[0]))     # d[1] is now globs s=2
    d.append(makes(d[0], d[1]))     # d[2] is globs s=3
    app = makes(d[2], d[0]) + makes(d[1], d[1])
    app.sort(key = lambda x: x.v)
    d.append(app)                   # d[3] is globs s=4
    return d

def lazy_matches(d, seek, tol):
    seek_min = seek * (1 - tol)
    seek_max = seek * (1 + tol)
    for i in range(0, len(d)):
        print 'Lazy matches of length ' + str(i+1) + ':'
        for j in d[i]:
            if j.v < seek_max and j.v > seek_min:
                print '\t' + j.p() + ' value ' + str(j.v)

def main(seek, tol):
    start_r = [[r(x, start_tol) for x in start]]
    d = build_d(start_r, tol)
    lazy_matches(d, seek, tol)
main(15, .2)


