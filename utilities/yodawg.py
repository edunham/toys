#!/usr/bin/python3
import random
import sys

braces = [("[","]"), ("{","}"), ("(",")")]
def yo(dawg):
    iheard = random.choice(braces)
    out = iheard[0]
    if random.random() < .5:
        if random.random() < .7 and len(dawg)>0:
            like = random.randint(0, len(dawg))
            i, heard = dawg[:-like], dawg[-like:]
            out += yo(i) + ", " + yo(heard)
        else:
            out += yo(dawg)
    else:
        out += dawg
    return out + iheard[1]

if __name__ == "__main__":
    print(yo(sys.argv[1])) 
            
