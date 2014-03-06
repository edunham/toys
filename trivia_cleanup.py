#! /usr/bin/env python2.7
import subprocess
import os
from string import punctuation

dir = '/home/miea/repos/triviabot/questions/'
#dir = '/home/miea/code/toys/test/'

def score(line):
    score = 0
    score += sum(x.isupper() for x in line)
    count = lambda l1, l2: len(list(filter(lambda c: c in l2, l1)))
    score += count(line, punctuation)
    return score

def write_best(arr, fd):
    if len(arr) == 0:
        return
    if len(arr) == 1:
        fd.write(arr[0])
        return
    scores = []
    for n in arr:
        scores.append(score(n))
    fd.write(arr[scores.index(max(scores))])    

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
