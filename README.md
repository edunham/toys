toys
====

Small scripts, mostly python, bigger than snippets but smaller than projects. 
Usually to answer a "what is..." or "how is..." or "can I..." question. 

cc
--

Dropping the Cookie Clicker token thingy here so I can finally have peace.

chatbot
-------

A bad idea from a writing class a long time ago. It's supposed to argue that
it's sentient. I didn't know things about software architecture at the time,
but I tried anyways.

cyoa-arrays
-----------

A derpy and short choose-your-own-adventure story, to demonstrate a technique
for making such games to a newbie coder who didn't want to learn about finite
state machines or even data structures at the time. Doesn't handle endgames
gracefully... boo hoo. 

debruijn
--------

A De Bruijn sequence is "a cyclic sequence of a given alphabet A with size k
for which every possible subsequence of length n in A appears as a sequence of
consecutive characters exactly once." [[wikipedia]][debruijn].

For reasons tangentially related to an arts and crafts project, I happen to
want a list of all debruijn sequences B(2,5). Ideally I'd figure out a general
algorithm to generate arbitrary De Bruijn sequences, but it currently finds
them by brute force search through all strings of the appropriate alphabet and
length. 

[debruijn]:http://en.wikipedia.org/wiki/De_Bruijn_sequence 

fixer
-----

Fixes tables. Specifically, takes tables garbled by wiki2rst.py and makes them 
prettily sphinxified.

TODO: Allow setting arbitrary max column widths and wrapping all lines which exceed them.

freq
----

Guesses what symbol goes with what English letter when given a file with
space-separated symbols, of letter-to-symbol encrypted English (probably).

lugmeetings
-----------

The [lug website][lugsite] is made with [wok][wok], a static website
generator. Wok is cool because it lets us be very lazy, and we only have to
write the content. 

[lugsite]:http://lug.oregonstate.edu/
[wok]:https://github.com/mythmon/wok

However, one does have to create the file for each event manually. With 9
meetings per term and thus 9 events to create as we plan the term, I
inevitably screw something up -- change part of an event template that
shouldn't be changed, or miss changing something in a way that breaks the
website. 

As a solution, this script automates the process of creating a term's worth of
meetings with the correct dates and stuff. Grab the term's start date from the
[course catalog][catalog].

[catalog]:http://catalog.oregonstate.edu/

> create meetings for the term that starts on april 1, 2013
> 
> $ python lugmeetings.py 04/01/2013
> 
> just print the dates on which the term's meetings will occur
> 
> $ python lugmeetings.py 04/01/2013 print


names
-----

WIP.


orcbot
------

A great misfortune of C that didn't deserve its own repo.


playlistmaker
-------------

For the Mbox project. See docstrings in the file for links.


resistors
---------

Work in progress, as the values are currently hard-coded and it's generally a
mess.

When volunteering in the ieee store, I'm occasionally asked for esoteric
resistor values by novice electrical engineers who don't know how to build the
value they want from standard components. We have basically unlimited numbers
of each of a handful of standard resistances, so I wrote this to answer the
question "how close to the desired value can we build a resistor out of
standard ones, and how should they be assembled to get that value?"

TODO:
* Update value lists to something realistic
* Handle tolerances or value ranges
* Interactivity and prettier output
* Tests?!


scales
------

Every so often I attempt to teach myself some music theory. This might be to
try to do maths about guitars. Incomplete, and rather tricky to test without
already grokking music theory.


synonyms
--------

Uses thesaurus service provided by words.bighugelabs.com, so you'll need an api key obtained from [here][apikey].

First, you enter the word about which you're curious at the prompt.
The next part is a little slow, so it prints progress. This is where it looks up all the synonyms of 'hello', 
then all of *their* synonyms.

Then we get results. It tells you how many unique synonyms-of-synonyms were found,
and the frequency with which each of those words was reached.

And finally, it lists as many of the most frequently occurring synonyms-of-synonyms as it can, under a few constraints.
These are: 
* Don't list any word that occurred only once
* If listing any words of that occurred a particular number of times, list all of the words which occurred that often
* Display 20 or fewer words in this output.

[apikey]:http://words.bighugelabs.com/getkey.php


trivia cleanup
--------------

For automating the repair of https://github.com/rawsonj/triviabot


tux
---

An adventure in inkscape with trying to make the LUG a logo for T-shirts. Well, it started with Inkscape; 
who knows where it'll end up. Hopefully with a good-looking kernel source penguin.


unloved
-------

Finds least-recently-active Git repo in a directory full of them.


wordmatch
---------

Nothing to worry about here, move along. Was trying to brute-force some
puzzles. 
