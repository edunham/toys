#! /usr/bin/env python2

import urllib2

def handletaken(handle):
    try:
        resp = urllib2.urlopen('https://twitter.com/' + handle)
        page = resp.read()
        if "we're going to fix it up and have things back to normal soon." in page:
            return False
        return True
    except:
        return False

print handletaken('edunham')

print handletaken('dadsfdasfldsafhldsakjfhlkdsajhflkjdsahfldf')
