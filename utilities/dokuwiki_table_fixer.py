#! /usr/bin/env python
# I ran a script on a DokuWiki dump which was supposed to turn it into ReStructuredText. 
# It worked okay, except for the tables. 
# This script takes a file with a DokuWiki table and prints out the table in a format
# that Sphinx will render prettily.

import sys

def get_doku_table():
    if len(sys.argv) < 2:
        print """Please pass the name of the file containing your dokuwiki 
                table as an argument to this script."""
        exit()
    path = sys.argv[1]
    fd = open(path)
    raw = fd.read()
    fd.close()
    return raw

def get_headers_lines_widths(r):
    lines = r.split('\n')
    # the slice compensates for leading and trailing marks
    headers = [h.strip() for h in lines[0].split('^')[1:-1]]    
    # slice of lines is to ignore headers
    lines = [[c.strip() for c in l.split('|')[1:-1]] for l in lines[1:]]
    cols = len(headers)
    col_widths = [0]*cols
    for h in range(cols):
        col_widths[h] = len(headers[h])
    for l in lines:
        if len(l) == cols:
            for c in range(cols):
                w = len(l[c])
                if w > col_widths[c]:
                    col_widths[c] = w
    return headers, lines, col_widths

def line(cols, arr):
    out = '|'
    for c in range(len(cols)):
        pad = arr[c] - len(cols[c])
        out = out + ' ' + cols[c] + ' ' * pad + ' |'
    return out

def symbols(s, arr):
    out = '+'
    for c in range(len(arr)):
        # the magic 2 is for leading and trailing spaces in lines
        out = out + s * (arr[c] + 2) + '+'
    return out

def main():
    r = get_doku_table()
    h, l, w = get_headers_lines_widths(r)
    print symbols('-', w)
    print line(h, w)
    print symbols('-', w)
    for n in l:
        print line(n, w)
        print symbols('-', w)

main()
