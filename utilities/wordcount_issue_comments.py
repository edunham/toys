#!/usr/bin/env python2
"""
People are arguing over whether the new github feature
(https://github.com/blog/2111-issue-and-pull-request-templates) would be
useful. I want to know the most frequent words that occur in the comments on a
given organization's repositories.

Create ghcreds.py of the form:
token="asdfjkl"

where token comes from https://github.com/settings/tokens
"""

from github import Github, GithubException
import ghcreds
from collections import Counter
import sys

g = Github(ghcreds.token)
counts = Counter()

if len(sys.argv) <=2:
    print "Invoke me with `python "+sys.argv[0]+" orgname reponame"

org = sys.argv[1] 

print sys.argv

if len(sys.argv) == 2: 
    repos = g.get_user(org).get_repos()
else:
    repos = [g.get_user(org).get_repo(r) for r in sys.argv[2:]]

seen = 0

for r in repos:
    print "repo " + r.name
    if r.has_issues:
        issues = r.get_issues()
        for i in issues:
            seen += 1
            print str(i.number) + "\t" + i.title
            if seen % 100 == 0: 
                for w in counts.most_common(100):
                    print "\t\t" + str(w)
            if i.comments >0:
                comments = i.get_comments()
                for c in comments:
                    for w in c.body.split():
                        counts[w] += 1
