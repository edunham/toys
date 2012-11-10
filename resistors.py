#! /usr/bin/env python

"""
Resistors: Given several different values available, figure out the
fewest that can be globbed together, and in what configuration, to 
get a desired value

"""
# all values in ohms unless otherwise stated
start = [287.0, 706.0, 569.0, 411.0, 4.87]
desired = 1.65
DBG = True

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

def in_parallel(r1, r2):
    return 1/((1/r1.v)+(1/r2.v))

def in_series(r1, r2):
    return r1.v + r2.v

def makes(l1, l2):
    out = []
    tol = .05
    for a1 in l1:
        a = r(a1, tol) if not isinstance(a1, r) else a1
        for b1 in l2:
            b = r(b1, tol) if not isinstance(b1, r) else b1
            c = g(in_parallel(a,b), a, b, pl)
            if DBG: print "appending " + c.p()
            if DBG: print "\t val is " + str(c.v) + " size " + str(c.s)
            c = g(in_series(a,b), a, b, ss)
            if DBG: print "appending " + c.p()
            if DBG: print "\t val is " + str(c.v) + " size " + str(c.s)
            out.append(c)
    return out

def make_nth(d, n):
    # outermost loop is because a 5-res glob could be 1+4 OR 2+3
    out = []
    #TODO: fix off-by-one where n=2
    for i in range(0, (n-2)+1):
        for a in d[n-i]:
            for b in d[i]:
                out.append(g(in_parallel(a,b), a, b, pl))
                out.append(g(in_series(a,b), a, b, ss))
    out.sort(key = lambda x: x.v)
    if DBG: print out
    return out

def main():
    n = 5
    d = [start]
    if DBG: print d
    """    for i in range(0, n+1):
        d.append(make_nth(d, i))
    if DBG:
        print d[0]
        for a in d[1:]:
            print "["
            for b in a:
                print b.p()
            print "]"
    """
    app = makes(d[0], d[0])
    print app
    app.sort(key = lambda x: x.v)
    #d.append(app) # d[1] is globs s=2
    #d.append(makes(d[0], d[1]))                     # d[2] is globs s=3
    #app = makes(d[2], d[0]) + makes(d[1], d[1]) 
    #d.append(app) # d[3] is globs s=4
main()     


