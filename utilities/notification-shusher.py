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
def is_merged(url):
    r = requests.get(url)
    if (r.ok):
        repo = json.loads(r.text or r.content)
        if "closed" in repo["state"]:
            return True
    return False

def mark_read(n):
    u = 'https://api.github.com/notifications/threads/'
    u += n.id
    u += '?access_token='
    u += ghcreds.token
    resp = requests.patch(u)
    # print resp
    fixed += 1

user = g.get_user() # Calling this with any args returns a nameduser
notifications = user.get_notifications()

for n in notifications:
    if is_merged(n.subject.url):
        mark_read(n)
    if "Auto merge of" in n.subject.title:
        mark_read(n)

print "Cleared " + str(fixed) + " spurious notifications!"
