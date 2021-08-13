domname tools
=============

Tools to find your next domain name

Example use case
----------------

print all available .com and .net from a list of names in a file

    cat names.txt | add_tld.py .com .net | curl_check.py

Generate 20 five-letter .com and .io domain names,
check with google domains if it exact match exists and print the domain name if it exists

    perm_gen.py 5 20 | add_tld.py .com .io | gdom_check.py

Find all available 3 character .com .net .org from google domains.

    combi.py 3 | gdom_check.py
