#!/usr/bin/env python

# Problem: Many forked repos on GitHub fall behind from their origins.
# Solution:
# 1) Verify that `apt install myrepos` is available on the system.
# 2) Query GitHub API to find all of my repositories
# 3) Clone each *fork* into *~/repos/mynameofit*, such that place I forked it
#    from is git origin (or update, if it exists)
# 4) For each such clone, add *my fork* as a remote named after my GitHub
#    username
# 5) Also for each clone, `mr register` the repo
# Now custom `mr` commands can pull all origins and push to my remotes.

