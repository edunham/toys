#! /usr/bin/env python
import urllib
import time
from subprocess import call
url = "http://static-rust-lang-org.s3-website-us-west-1.amazonaws.com/dist/"
url += time.strftime("%Y-%m-%d/")
req = urllib.urlopen(url)
code = req.getcode()
message = "%s broken. fix it." % url
if code != 200:
    call("echo %s | write edunham" % message,shell=True)
