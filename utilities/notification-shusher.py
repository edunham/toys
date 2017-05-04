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

def peopleify(url):
    url = url.replace("api.github.com/repos","github.com")
    url = url.replace("issues","issue")
    url = url.replace("pulls","pull")
    return url

def is_merged(url):
    r = requests.get(url)
    if (r.ok):
        repo = json.loads(r.text or r.content)
        if "closed" in repo["state"]:
            return True
    return False

user = g.get_user() # Calling this with any args returns a nameduser
notifications = user.get_notifications()
for n in notifications:
    if "Auto merge of" in n.subject.title:
        print n
        print "^^ toss that one"
    else:
        print ""
        print n
        print "\tRepo: " + n.repository.name
        print "\t" + n.subject.title
        print "is merged?"
        print is_merged(n.subject.url)
        print "\t\t" + n.subject.url
        print "\t\t" + peopleify(n.subject.url)
        print "\t\t" + n.subject.type
        print "\tReason: " + n.reason
