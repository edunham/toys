#!/usr/bin/env python2
"""
For bad reasons, I need to copy all open PRs from a source to a fork on
GitHub.

Create ghcreds.py of the form:
token="asdfjkl"

where token comes from https://github.com/settings/tokens
"""

repo="homu"
originator="barosl" # whose issues are we copying?
forker="servo" # where are we recreating the issues?
base = "master" # Branch on forker's repo where PRs will be filed

from github import Github, GithubException
import ghcreds
g = Github(ghcreds.token)

source = g.get_user(originator).get_repo(repo)
fork = g.get_user(forker).get_repo(repo)

pulls = source.get_pulls(state="open")

for p in pulls:
    new_title = p.title
    new_body = """
PR ported from [%s](%s). Originally submitted by @%s on %s. 
""" % (str(p.number), p.html_url, p.user.login, p.created_at.strftime('%c'))

    if p.body:
        new_body += """
------------------------------------------------------------------------------

%s

""" % p.body
    for c in p.get_comments():
        new_body += """
------------------------------------------------------------------------------
\n"""
        new_body += "On %s, %s commented:\n" % (c.created_at.strftime('%c'), c.user.login)
        for l in c.body.splitlines(True):
            new_body += "> %s\n" % l
    if p.head.repo and p.head.ref: # the place the PR comes from still exists
        head = "%s:%s" % (p.user.login, p.head.ref)
        try:
            fork.create_pull(title=new_title,body=new_body,base=base, head=head)
        except GithubException as e:
            print "Failed to port %s. " % new_title
            print e
