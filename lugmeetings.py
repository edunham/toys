#! /usr/bin/env python

"""
Fun with DateTime:
Given a start date, generate appropriate LUG events for the following 7
Tuesdays. start date is of format m/d/yyyy. 

Output Location: ../OSULUG-Website/content/events/yyyymmdd_wkx.mkd
"""

import sys
import datetime as dt

def get_dt(mmddyyyy):
    # turn mm/dd/yyyy into a datetime date object
    date = mmddyyyy.split('/')
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    return dt.date(year, month, day)


def next_tuesday(date):
    # find first tuesday which follows the given date object
    # day:   S M T W R F S
    # wkd:   6 0 1 2 3 4 5
    # delta: 2 1 0 6 5 4 3
    wkd = date.weekday()
    if wkd <= 1: 
        date = date + dt.timedelta(days = (1 - wkd))
    else:
        date = date + dt.timedelta(days = (8 - wkd)) 
    return date


def prev_tuesday(date):
    wkd = date.weekday()
    if wkd <= 1: 
        date = date - dt.timedelta(days = (1 - wkd))
    else:
        date = date - dt.timedelta(days = (8 - wkd)) 
    return date


def z(i):
    # give two digits. append leading 0 if necessary.
    if i <= 9:
        return '0' + str(i)
    return str(i)


def make_file(mm, dd, yy, wk, prefix = "../OSULUG-Website/content/events/"):
    mm = z(mm)
    dd = z(dd)
    yy = z(yy)
    wk = str(wk)
    filename = prefix + yy + mm + dd + "_wk" + wk + ".mkd"
    f = open(filename, 'w')
    lines = [
        'title: Week ' + wk + ' meeting, topic TBD\n',
        'datetime: ' + yy + '-' + mm + '-' + dd + ' 18:00:00\n',
        'category: events\n',
        'slug: meeting' + yy + mm + dd + '\n'
        "preview: Check back for updates on this week's schedule\n",
        'location: KEC 1007\n',
        '\n---\n\n',
        'There will be a meeting this week. We\'ll update this page when we know what it is.\n\n',
        'When: 6pm\n\n', 
        'Where: Kelley Engineering Center room 1007\n'
        ]
    for l in lines:
        f.write(l)
    f.close()


def main():
    if len(sys.argv) < 2: 
        print "Need first day of term, in the format mm/dd/yyyy"
        print "`mm/dd/yy print` tells meeting dates without creating files."
        exit()
    action = 0
    if len(sys.argv) == 3 and sys.argv[2][0] == 'p':
       action = 1 
    startdate = get_dt(sys.argv[1])
    tues = next_tuesday(startdate)
    for i in range(0, 9): 
        weeknumber = i + 1
        if action == 0:
            make_file(tues.month, tues.day, tues.year, weeknumber)
        elif action == 1:
            print str(tues) + " week " + str(weeknumber)
            
        tues = tues + dt.timedelta(weeks = 1)


if __name__ == "__main__":
    main()
