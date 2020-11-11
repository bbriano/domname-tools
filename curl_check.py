#!/usr/local/bin/python3
import sys
import subprocess

for line in sys.stdin:
    domname = line[:-1]

    command = ["curl", domname]
    if subprocess.call(["curl", domname],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL) != 0:
        print(domname)
