#! /usr/bin/env python2.7

import subprocess
import os
import datetime

"""
Find unloved projects.

I have ~/code/ on my system, which is full of git repositories. I'd like to
list those projects and: 
    * Complain about those which aren't initialized as git repos
    * Sort by most distant date of latest commit
    * Complain about the ones lacking licenses  
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

repos = '/home/miea/code/'

projects = os.listdir(repos)

needs_git = []
dates = {}

for p in projects:
    try:
        s = subprocess.check_output('git show', shell = True, #stdout = '/dev/null',
                                    cwd = repos + p).split('\n')
        dates[parse_date(s[2])] = p
    except:
        needs_git.append(p)

print "Projects that need love"

for i in sorted(dates):
    print '\t' + dates[i] + ' had its last commit on ' + str(i) 

print "Projects that need Git"

print needs_git
