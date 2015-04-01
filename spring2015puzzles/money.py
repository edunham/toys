#! /usr/bin/env python
import sys

def count_coins(amount):
    pennies = int(amount * 100)
    quarters = pennies/25
    pennies = pennies - quarters * 25
    dimes = pennies/10
    pennies = pennies - dimes * 10
    nickels = pennies/5
    pennies = pennies - nickels * 5

    print "It would take "+str(quarters)+" quarters, "+str(dimes)+" dimes, "
    print str(nickels)+" nickels, and "+str(pennies)+" pennies"
    print "to make change for "+str(amount)+"."

if __name__ == "__main__":
    if len(sys.argv)<2:
        print "Please specify an amount."
        exit(-1)
    try:
        amount = float(sys.argv[1])
    except:
        print "Specify the amount as a number, like 12.34"
        exit(-1)
    count_coins(amount)

