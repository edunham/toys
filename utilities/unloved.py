#! /usr/bin/env python2.7

import subprocess
import os
import datetime

"""
Find unloved projects.

I have a directory of all my code repositories on my system. This file resides
in the toys repo. Its purpose is to look up one directory, list those projects
and:

    * Complain about those which aren't initialized as git repos
    * Sort by most distant date of latest commit
"""

def parse_date(d):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
              'Oct', 'Nov', 'Dec']
    d = d.split()
    year = int(d[5])
    month = months.index(d[2]) + 1
    day = int(d[3])
    hour, minute, second = [int(x) for x in d[4].split(':')]
    # datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
    return datetime.datetime(year, month, day, hour, minute, second) 

repos = '../'

projects = os.listdir(repos)

needs_git = []
dates = {}

for p in projects:
    try:
        s = subprocess.check_output('git show', shell = True, #stdout = '/dev/null',
                                    cwd = repos + p).split('\n')
        dates[parse_date(s[2])] = p
    except:
        # TODO: handle case where dir contains no files (only subdirs) and
        # those subdirs are git repos. Perhaps recursively, without following
        # links.
        needs_git.append(p)

print "Projects that need love"

for i in sorted(dates):
    print '\t' + dates[i] + ' had its last commit on ' + str(i) 

print "Projects that need Git"

for g in needs_git:
    print "\t"+g
