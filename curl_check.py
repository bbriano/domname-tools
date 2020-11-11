import sys
import subprocess

tlds = [".com"]

for line in sys.stdin:
    basename = line[:-1]

    for tld in tlds:
        domname = basename + tld
        command = ["curl", domname]
        if subprocess.call(["curl", domname],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL) != 0:
            print(domname)
