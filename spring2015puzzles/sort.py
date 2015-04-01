#! /usr/bin/env python
import random

orig = range(20)
random.shuffle(orig)
print "Initial list:"
print orig 
print "Here's that, but sorted:"
orig.sort()
print orig
