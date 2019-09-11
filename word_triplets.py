# Import collections to use collections.Counter
from collections import Counter
# Import re for regex functions.
import re
# Import sys for access to system specific parameters and functions.
import sys

# Don't forget to accept streams OR files. DONE!
# Don't forget to write documentation for project, classes, and functions.
# Don't forget to create test cases.
# Don't forget to update or delete comments.
# Strings to test against: "one of the" (text contains: "bone of the", "one of them", "none of them", etc.)
# Am I picking up partial words, such as "sea" in the phrase "of the seamen"?
# Check for consistency of quote marks.
# Create class "PhraseCount" or "TripCheck" or "TripletsCounter" to hold functions.
# What if there are less than three words in source material?

# Can I take an argument to choose the size of text groupings at run time??? That would be a good addition!

def text_open(file_name):
	"""Read file contents."""
	with open(file_name) as f:
		text = f.read()
	return text

def text_input():
	"""Take input from file or stream."""
	# sys.stdin.isatty() returns false if there's something in stdin
	if not sys.stdin.isatty():
		text = sys.stdin.read()
	elif sys.argv[1]:
		text = text_open(sys.argv[1])
	# Should probably be error handling here.
	else:
		print("Error: Please submit text to process as file or stream.")
	return text

def text_transform(text):
	"""Prepare text for processing. Return as list."""
	text = text.lower()
	# Removed emdashes from regex. The results still aren't matching example. 
	# I'm thinking there are mixed uses of dashes and emdashes.
	text = re.sub(r"[\-\",.;:!?“”]+", " ", text)
	# Replace stupid fancy single quotes. Edge cases galore here so write good tests!
	text = re.sub(r"[‘’]+", "'", text)
	text_arr = text.split()
	# Check for length of array.
	return text_arr

def text_triple_maker(arr):
	"""Create list of all triples from text."""
	# Double check this reaches end of text.
	x, y = 0, 3
	triples_list = []
	while y <= len(arr):
		triple = (arr[x:y])
		triple_string = " ".join(triple)
		triples_list.append(triple_string)
		x += 1
		y += 1
	return triples_list

def triple_count(arr):
	"""Count triples and sort by most common."""
	triple_count = Counter(arr).most_common(100)
	return triple_count

def close(output_text):
	"""Output processed text to file."""
	with open("output.txt", "w") as f:
		for triple in output_text:
			f.write(f"{triple}\n")

words = text_input()
words_list = text_transform(words)
words_triples = text_triple_maker(words_list)
words_triples_count = triple_count(words_triples)
close(words_triples_count)

# Alternatively, you could nest the fuction calls like the following:
# words_triples_count = triple_count(text_triple_maker(text_transform(text_open(file))))
# print(words_triples_count)

