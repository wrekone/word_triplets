# Import collections to use collections.Counter
from collections import Counter
# Import re for regex functions.
import re
# Import sys for extension of standard library
import sys

# Don't forget to accept streams OR files.
# Don't forget to write documentation for project, classes, and functions.
# Don't forget to create test cases.
# Don't forget to update or delete comments.
# Strings to test against: "one of the" (text contains: "bone of the", "one of them", "none of them", etc.)
# Am I picking up partial words, such as "sea" in the phrase "of the seamen"?
# Check for consistency of quote marks.


file = "moby_dick.txt"

# Parse command line
#if file_name_given:
#	text = open(file_name_given)
#else:
#	text = sys.stdin

def text_open(file_name):
	with open(file_name) as f:
		text = f.read()
		return text

def text_transform(text):
	text = text.lower()
	text = re.sub(r"[\-\",.;:!?—“”]+", " ", text)
	# Replace stupid fancy single quotes. Edge cases galore here so write good tests!
	text = re.sub(r"[‘’]+", "'", text)
	text_arr = text.split()
	return text_arr

def text_triple_maker(arr):
	x, y = 0, 3
	triples_list = []
	while x < len(arr) - 2:
		triple = (arr[x:y])
		triple_string = " ".join(triple)
		triples_list.append(triple_string)
		x += 1
		y += 1
	return triples_list

def triple_count(arr):
	triple_count = Counter(arr).most_common()
	return triple_count

# I think I'm handling the file wrong, causing it to swell to a massive size.
def close(triple_count):
	with open("output.txt", "w") as f:
		for triple in triple_count:
			f.write(f"{triple_count}\n")

moby_dick = text_open(file)
moby_list = text_transform(moby_dick)
moby_triples = text_triple_maker(moby_list)
moby_triples_count = triple_count(moby_triples)
with open("output.txt", "w") as f:
	for triple in moby_triples_count:
		f.write(f"{triple}\n")
#close(moby_triples_count)

# Alternatively, you could nest the fuction calls like the following:
# moby_triples_count = triple_count(text_triple_maker(text_transform(text_open(file))))
# print(moby_triples_count)

