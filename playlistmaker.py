#! /usr/bin/env python2.7
# for i in {0..5}; do rm -rf $i; done

"""
http://arons.github.io/hack/arduino/2014/01/10/mbox-01.html

https://github.com/edunham/MBox

Drop this script in the directory with all the songs, prod the hard-coded
n_playlists down there to match the number of playlists you want to end pu
with, then `python this.py > list.txt` to get playlist printouts (1-based for
non-CS folk)
"""

import os
import sys
import shutil

songs = os.listdir('.')
music = []
for s in songs: 
    if s != sys.argv[0]:
        if s != 'list.txt':
            music.append(s)

#print "found %s songs" % len(music)

n_playlists = 6 
songs_per_list = len(music)/n_playlists

#print "Splitting into %s playlists with %s per list" % (n_playlists, songs_per_list)



songoflist = 0
whichlist = 0
lists = []

music.sort()

for i in range(n_playlists):
    os.mkdir(str(i + 1))
    lists.append([])

for i in range(len(music)):
    if songoflist >= songs_per_list:
        if whichlist < n_playlists - 1:
            whichlist += 1
            songoflist = 0
        # else we're filling the last list
    d = str(whichlist + 1)
    lists[whichlist].append(music[i])
    shutil.copy(music[i], d + '/' + str(songoflist) + '.mp3' )
    songoflist += 1
        
for l in range(len(lists)):
    print "==== list %s =====" % (l + 1)
    
    for s in range(len(lists[l])):
        print "%s: %s" % (s + 1, lists[l][s])

