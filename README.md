toys
====

Small scripts, mostly python, bigger than snippets but smaller than projects. 
Usually to answer a "what is..." or "how is..." or "can I..." question. 

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
