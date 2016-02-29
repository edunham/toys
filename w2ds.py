#! /usr/bin/env python

def condense(w):
    return w[0] + str(len(w)-2) + w[-1:]

def expand(w):
    length = int(w[1:-1]) + 2
    for word in get_words(length):
        if word.startswith(w[0]) and word.endswith(w[-1:]):
            print word


def get_words(length, filename = '/usr/share/dict/words'):
  return (word.strip() for word in open(filename) if len(word) == length)

if __name__ == "__main__":
    print "Words With Numbers In Them Thing"
    while(True):
        w = raw_input("Word: ")
        print "Condensed: "
        print ' '.join(condense(p) for p in w.split())
        try:
            print "Expanded: "
            expand(w)
        except:
            print "Could not expand " + w
