#! /usr/bin/env python2.7
import subprocess
import os

dir = '/home/miea/repos/triviabot/questions/'

def dedup_lines(pathtofile):
    print "deduplicating " + pathtofile
    old = open(pathtofile, 'r')
    new = open(pathtofile + '-new', 'w')
    last = ''
    for l in old.readlines():
        m = l.lower().translate(None, ":,;!@#$%^&*()[]?. /\#-") # munge string

        # It'd be nice to find the better-punctuated string and write it, but
        # that's hard to handle edge cases of n "matching" strings and picking
        # the best of them.

        if last != m:
            new.write(l)
        else:
            print "found duplicate: " + l

        last = m
    old.close()
    new.close()
    bash = 'rm ' + pathtofile + '; mv ' + pathtofile + '-new ' + pathtofile
    os.system(bash)

def main():
    files = os.listdir(dir)
    for f in files:
        dedup_lines(dir + f)

main()
