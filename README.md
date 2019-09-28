# word_triplets
Counts occurrences of the 100 most common three word groupings in a source text. Returns results as a list of tuples.

This program assumes proper use of en dashes, em dashes, and hyphens. Hyphens will be retained. Hyphenated words will be treated as single words. En dashes and em dashes will be ignored. 
All single quotes (curly and straight) will be treated as straight quotes. 
All other punctuation will be ignored. Numerics will be ignored.

Usage:
`python3 word_triplets.py TEXTFILE`

Example:
`python3 word_triplets.py moby_dick.txt`

Also accepts streams as input.

Example1:
`echo "This is a test" | python3 word_triplets.py`

Example2:
`python3 word_triplets.py < origin.txt`

Tests usage: `python3 test_word_triplets.py`

Several example input texts are provided. Examples are provided free of copyright.

TODO: allow group size to be set at runtime, allow number of results returned to be set at runtime, allow pretty output option to be set at runtime, improve tests
