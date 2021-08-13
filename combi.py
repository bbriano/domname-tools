#!/usr/bin/env python3
# Usage: 3c.py n

import string
import sys

def main():
    try:
        n = int(sys.argv[1])
    except:
        print("Usage: 3c.py n")
        return

    abc = string.ascii_lowercase
    for name in combi(abc, n):
        print(name)

def combi(alphabet, n=3):
    # res: [""] -> [a,b,..,z] -> [aa,ab,..,zz] -> ..
    res = [""]
    for _ in range(n):
        res = [pre+post for pre in res for post in alphabet]
    return res

if __name__ == "__main__":
    main()
