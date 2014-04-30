#! /usr/bin/env python2.7
import subprocess
import os
import re
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
        m = l.lower().translate(None, punctuation + ' ') # munge string
        if last == m: 
            group.append(l)
        else:
            write_best(group, new)# This will write unless group empty
            group = [l]
            last = m
    write_best(group, new) # don't forget that last line!
    old.close()
    new.close()
    bash = 'rm ' + pathtofile + '; mv ' + pathtofile + '-new ' + pathtofile
    os.system(bash)

def tagstrip(quiz):
    print quiz
    tags = ['category', 'category', 'music', 'tv/movies',
            'trivia', 'games', 'general', 'general knowledge',
            'geographic', 'geographic trivia', 'geography', 
            'astrology', 'astronomy', 'useless trivia', 
            'what word means']
    q = quiz.split(':')
    for el in q:
        if el.strip().lower() in tags:
            q.remove(el)
    out = ' '.join(x.strip() for x in q)
    return out

def strip_tags(pathtofile):
    print "Stripping tags from " + pathtofile
    old = open(pathtofile, 'r')
    new = open(pathtofile + '-new', 'w')
    for l in old.readlines():
        new.write(tagstrip(l))
    old.close()
    new.close()
    bash = 'rm ' + pathtofile + '; mv ' + pathtofile + '-new ' + pathtofile
    os.system(bash)

def main():
    files = os.listdir(dir)
    for f in files:
        # dedup_lines(dir + f)
        strip_tags(dir + f)
main()
