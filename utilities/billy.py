#! /usr/bin/env python3

"""
Tell me what bookcases to buy to fit a wall. 
"""

import sys
def main():
    if len(sys.argv) < 2: 
        print("need inches of wall pls")
        exit()
    wall_remaining = float(sys.argv[1])
    cases = ""
    big_case = 31.5
    smol_case = 15.75
    while wall_remaining > big_case:
        cases += "big, "
        wall_remaining -= big_case
    while wall_remaining > smol_case:
        cases += "smol, "
        wall_remaining -= smol_case
    if len(cases) > 0:
        cases += f"and {wall_remaining} inches of blank wall"
    else:
        cases = "nothing fits"
    print(cases)

if __name__ == "__main__":
    main()
