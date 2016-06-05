#! /usr/bin/env python
import urllib
import time
from subprocess import call
url =" http://static.rust-lang.org/dist/"
url += time.strftime("%Y-%m-%d")
url += "/rust-nightly-x86_64-unknown-linux-gnu.tar.gz"
req = urllib.urlopen(url)
code = req.getcode()
message = "%s broken. fix it." % url
if code != 200:
    call("echo %s | write edunham" % message,shell=True)
