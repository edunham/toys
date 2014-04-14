#!/usr/bin/env python
import urllib2
from collections import defaultdict
import operator

apikey = "59383480e751c6f844b6bf431ebd7b31"

"""
API key should be a string of letters and numbers obtained by pressing buttons
at http://words.bighugelabs.com/getkey.php. Free key gets you 10,000 requests
per day, and a few hours of testing and playing with this script used just
over 1,300 requests on my key. If you want to play with this without making
your own key, pm me and I'll let you borrow mine, but I don't feel like
publishing it for posterity.
"""

def get_synonyms(word):
    """
    result is in the form of many lines like this: 
        noun|syn|Word
    so we split on the | and currently discard part-of-speech and syn data,
    keeping only the actual synonym. We only want individual words -- nothing
    with spaces or hyphens.
    """

    print "Looking up " + word + "..."
    url = "http://words.bighugelabs.com/api/2/" + apikey + '/' + word + '/'
    try:
        response = urllib2.urlopen(url)
        raw = [l.split('|') for l in response.read().split('\n') if l is not '']
        return [w[2].lower() for w in raw if ' ' not in w[2] and '-' not in w[2]]
    except urllib2.HTTPError:
        return ''

def all_cousins(word):
    cousins = defaultdict(int)
    siblings = get_synonyms(word)
    if word.lower() in siblings:
        siblings.remove(word.lower())
    for s in siblings:
        for w in get_synonyms(s):
            if w not in siblings:
                cousins[w] += 1
    return cousins

def prettyprint(d, num):
    # num is the maximum number of results which we shall print.
    # this prints all keys of d which occur with a given frequency, 
    # until we could not print any more without exceeding the max to print.
    d = sorted(d.iteritems(), key = operator.itemgetter(1), reverse = True)
    i = 0
    print str(len(d)) + " cousin-words were examined, with this distribution: "
    sizes = defaultdict(int)
    for w in d:
        sizes[w[1]] += 1
    for k in sizes: 
        print "\t " + str(sizes[k]) + " words occurred " + str(k) + " times"
    th = d[0][1] + 1 # make sure we print at least the highest-value matchlist
    print "Here are the top words, and their strength of relation:"
    while (num > 0) and th > 1:
        th -= 1
        num -= sizes[th]
    while (d[i][1] > th):
        print "\t" + d[i][0] + " (" + str(d[i][1]) + ")"
        i += 1

if apikey == "":
    print """    This script will NOT WORK without an API key from 
    http://words.bighugelabs.com/getkey.php. Aborting."""
    exit()

print """
This is a little language-game, played in a thesaurus. If being synonyms is
like being siblings, it finds words who are cousins of the one you enter at
the prompt: they're the words which most commonly occur as synonyms of your
choice's synonyms, without being direct synonyms themselves. 

To play, enter a single word at the prompt. You'll see progress as the script
runs through its queries, then get results in the form of "word (relatedness)"

Sorry the threshholding is a little derpy; I don't like it when it dumps a
huge long list of fifty-something twice-occurring words to the console.

To quit, send EOF (ctrl + d). Have fun! 
"""

while(True):
    word = raw_input("> ")
    l = all_cousins(word)
    print "--- results for the word '" + word + "' ---"
    prettyprint(l, 20)
