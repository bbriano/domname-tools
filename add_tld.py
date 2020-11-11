#!/usr/local/bin/python3
import sys

tlds = sys.argv[1:]
if len(tlds) == 0:
    tlds = [".com"]

for line in sys.stdin:
    line = line[:-1]  # remove newline
    for tld in tlds:
        print(line + tld)
