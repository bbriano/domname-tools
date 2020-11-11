import sys
import random
import string

def str_permutation(r, opts):
    res = ""
    n = len(opts)
    for _ in range(r):
        index = random.randint(0, n-1)
        res += opts[index]
    return res

try:
    nchars = int(sys.argv[1])
except:
    nchars = 4

try:
    nnames = int(sys.argv[2])
except:
    nnames = 10

chars = string.ascii_lowercase

TLDS = [".io"]

for _ in range(nnames):
    for tld in TLDS:
        sys.stdout.write("%s%s\n" % (str_permutation(nchars, chars), tld))
