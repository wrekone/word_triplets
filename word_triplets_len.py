# Import collections to use collections.Counter
from collections import Counter
# Import re for regex functions.
import re
# Import sys for access to system specific parameters and functions.
import sys
# Import argparse to parse command line options.
import argparse

# Don't forget to accept streams OR files. DONE!
# Don't forget to write documentation for project, classes, and functions.
# Don't forget to create test cases.
# Don't forget to update or delete comments.
# Strings to test against: "one of the" (text contains: "bone of the", "one of them", "none of them", etc.)
# Am I picking up partial words, such as "sea" in the phrase "of the seamen"?
# Check for consistency of quote marks.
# Create class "PhraseCount" or "TripCheck" or "TripletsCounter" to hold functions.
# Should I make this an executable?
# Classes could be file handling & file manipulation. Maybe just using modules would be better. Simpler for sure.

# Can I take an argument to choose the size of text groupings at run time??? That would be a good addition! Let's try it.
# Using positional arguments is not working because the arg is in a different place depending on whether input is a stream of a file.
# Going to look into using optional arguments instead.
# Will want to create help text if using run time arguments. Looks like this is included in argparse.
# Should I keep it simple and not worry about command line args or make it more robust?

# group_size = 3

def text_open(file_name):
	"""Read file contents."""
	with open(file_name) as f:
		text = f.read()
	return text

def text_input():
	"""Take input from file or stream."""
	global group_size
	# sys.stdin.isatty() returns false if there's something in stdin. I could understand this better.
	if not sys.stdin.isatty():
		text = sys.stdin.read()
		return text
	# Read the argparse documentation!
	parser = argparse.ArgumentParser(description="Count the number of word groups in a file.")
	# This seems overly verbose. Also, the default is set in multiple places in the file.
	parser.add_argument("file"* help="input file(s)")
	parser.add_argument("--size", type=int, default=3,
						help="the size of the group (default is 3)")
	parser.add_argument("--write", help="write output to FILE")
	args = parser.parse_args()
	if args.size:
		# How can I do this without using global variable?
		group_size = args.size
	# I think I can handle this more gracefully.
	elif sys.stdin.isatty() and not args.file:
		print("usage: word_triplets_len.py [-h] [--file FILE] [--size SIZE]")
		print("Try 'word_triplets_len.py --help' for more information.")
		sys.exit()
	else:
		text = text_open(args.file)
		return text

def text_transform(text):
	"""Prepare text for processing. Return as list."""
	text = text.lower()
	text = re.sub(r"[\-\",.;:!?–“—”]+", " ", text)
	# Replace stupid fancy single quotes. Edge cases galore here so write good tests!
	text = re.sub(r"[‘’]+", "'", text)
	text_arr = text.split()
	return text_arr

# Should group_size have a default or just be assigned globally?
def text_triple_maker(arr, group_size):
	"""Create list of all triples from text."""
	# Double check this reaches end of text.
	x, y = 0, group_size
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
	triple_count = Counter(arr).most_common()
	return triple_count

def close(output):
	"""Output processed text to file."""
	with open("output.txt", "w") as f:
		for triple in output:
			f.write(f"{triple}\n")

words = text_input()
word_list = text_transform(words)
word_triples = text_triple_maker(word_list, group_size)
triples_counted = triple_count(word_triples)
close(triples_counted)

