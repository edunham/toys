#! /usr/bin/env python2.7
import subprocess
import os

#dir = '/home/miea/repos/triviabot/questions/'
dir = '/home/miea/code/toys/test/'

def write_best(arr, fd):
    if len(arr) == 0:
        return
    fd.write(arr[0])    

def dedup_lines(pathtofile):
    print "deduplicating " + pathtofile
    old = open(pathtofile, 'r')
    new = open(pathtofile + '-new', 'w')
    group = []
    last = ''
    for l in old.readlines():
        m = l.lower().translate(None, ":,;!@#$%^&*()[]?. /\#-") # munge string

        # It'd be nice to find the better-punctuated string and write it, but
        # that's hard to handle edge cases of n "matching" strings and picking
        # the best of them.


        if last == m: 
            group.append(l)
            print "found dup " + l
        else:
            write_best(group, new)
            group = [l]
            last = m

        """
        if last == m:
            group.append(l)
            continue
        if len(group) > 0: # just finished a group of matchies
            new.write(pick_best(group))
            group = []
        else:
            new.write(l)
        if last != m:
            new.write(l)
        else:
            print "found duplicate: " + l
        last = m
        """

    old.close()
    new.close()
    bash = 'rm ' + pathtofile + '; mv ' + pathtofile + '-new ' + pathtofile
    os.system(bash)

def main():
    files = os.listdir(dir)
    for f in files:
        dedup_lines(dir + f)

main()
