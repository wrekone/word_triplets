# word_triplets
Counts occurrences of the 100 most common three word groupings in a source text. Returns a nicely formatted list for human consumption.

This program assumes proper use of en dashes, em dashes, and hyphens. Hyphens will be retained. Hyphenated words will be treated as single words. En dashes and em dashes will be ignored. 
All single quotes (curly and straight) will be treated as straight quotes. 
All other punctuation will be ignored.

Usage: 
`python3 word_triplets.py TEXTFILE`  

Example: 
`python3 word_triplets.py moby_dick.txt`

Alternatively, you can pipe text into the program with `cat`, `echo`, etc.

Tests usage: `python3 test_word_triplets.py`

Several example input texts are provided. Examples are provided free of copyright.

TODO: allow group size to be set at runtime, allow number of results returned to be set at runtime, allow raw-output option to be set at runtime, improve tests