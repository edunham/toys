#!/usr/bin/env python2
"""
The GitHub user interface shows me a list of notifications, but it's full of
things I don't care about. This tries to automatically mark as read the
categories of notifications that I don't want to get.

Create `ghcreds.py` containing:

token="asdfjkl"

where token comes from https://github.com/settings/tokens and has the
"notifications" scope.
"""


from github import Github, GithubException
import ghcreds
import requests
import json
g = Github(ghcreds.token)
fixed = 0
looked = 0
def is_merged(url):
    r = requests.get(url)
    if (r.ok):
        repo = json.loads(r.text or r.content)
        if "closed" in repo["state"]:
            return True
        else:
            print "\t" + str(repo["state"])
    if r.headers['X-RateLimit-Remaining'] == '0':
        exit("Rate limit exceeded. Try again later.")
    return False

def mark_read(n):
    global fixed
    u = 'https://api.github.com/notifications/threads/'
    u += n.id
    u += '?access_token='
    u += ghcreds.token
    resp = requests.patch(u)
    fixed += 1

user = g.get_user() # Calling this with any args returns a nameduser
notifications = user.get_notifications()

for n in notifications:
    global looked
    looked += 1
    # I don't want to be notified of merged changes.
    if is_merged(n.subject.url):
        mark_read(n)
    # I especially don't want to be notified of Homu's merges.
    elif "Auto merge of" in n.subject.title:
        mark_read(n)

print "Examined " + str(looked) + " notifications. "
print "Cleared " + str(fixed) + " spurious notifications!"
