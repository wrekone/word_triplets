# Import collections to use collections.Counter
from collections import Counter
# Import re for regex functions.
import re
# Import sys for access to system specific parameters and functions.
import sys

# Don't forget to accept streams OR files.
# Don't forget to write documentation for project, classes, and functions.
# Don't forget to create test cases.
# Don't forget to update or delete comments.
# Strings to test against: "one of the" (text contains: "bone of the", "one of them", "none of them", etc.)
# Am I picking up partial words, such as "sea" in the phrase "of the seamen"?
# Check for consistency of quote marks.
# Create class "PhraseCount" to hold functions.

# Try the 'fileinput' module to read from stdin.
# import fileinput

#file = "moby_dick_snippet.txt"

def text_open(file_name):
	with open(file_name) as f:
		text = f.read()
	return text

def text_input():
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
	text = text.lower()
	text = re.sub(r"[\-\",.;:!?—“”]+", " ", text)
	# Replace stupid fancy single quotes. Edge cases galore here so write good tests!
	text = re.sub(r"[‘’]+", "'", text)
	text_arr = text.split()
	return text_arr

def text_triple_maker(arr):
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
	triple_count = Counter(arr).most_common()
	return triple_count

# I think I'm handling the file wrong, causing it to swell to a massive size.
def close(output_text):
	with open("output.txt", "w") as f:
		for triple in output_text:
			f.write(f"{triple}\n")

words = text_input()
# moby_dick = text_open(file)
words_list = text_transform(words)
words_triples = text_triple_maker(words_list)
words_triples_count = triple_count(words_triples)
close(words_triples_count)

#with open("output.txt", "w") as f:
#	for triple in words_triples_count:
#		f.write(f"{triple}\n")
#close(moby_triples_count)

# Alternatively, you could nest the fuction calls like the following:
# words_triples_count = triple_count(text_triple_maker(text_transform(text_open(file))))
# print(words_triples_count)

