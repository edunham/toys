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

        if last == m: 
            group.append(l)
        else:
            write_best(group, new)
            group = [l]
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
