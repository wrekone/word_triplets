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
	"""Take input from file(s) or stream."""
	# sys.stdin.isatty() returns false if there's something in stdin
	try:
		if not sys.stdin.isatty():
			text = sys.stdin.read()
		elif sys.argv[1]:
			text = ""
			inputArgs = sys.argv
			for argument in inputArgs:
				text += text_open(argument)
				text += " "
	except IndexError:
		print("Error: No input. Please provide something to process.")
		sys.exit()
	except FileNotFoundError:
		print(f"{sys.argv[1]}: No such file")
		print("usage: word_triplets_len_test.py [FILE]...")
	return text

def text_transform(text):
	"""Prepare text for processing. Return as list."""
	text = text.lower()
	# How should I handle hyphens, en dashes, and em dashes?
	# I'm thinking there are mixed uses of hyphens, en dashes, and em dashes in sample text "Moby Dick".
	# Proper English grammar uses hyphens to join two or more words together into compound words.
	# En dash: Twice as long as a hyphen, the en dash is a symbol (--) that is used in writing or printing to indicate a range, connections or differentiations, such as 1880-1945 or Princeton-New York trains.
	# Em dash: Longer than the en dash, the em dash can be used in place of a comma, parenthesis, or colon to enhance readability or emphasize the conclusion of a sentence. For example, She gave him her answer --- No!
	text = re.sub(r"[`\-\",.;:!–?—“”]+", " ", text)
	# Replace curly single quotes with straight single quotes. Edge cases galore here so write good tests!
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
	# Could end program here if I don't want to make output pretty or output to file by default.
	return triple_count

# Determine whether better to output to file or to terminal.

def save_output(output_text):
	"""Output processed text to file."""
	with open("output.txt", "w") as f:
		for triple in output_text:
			f.write(f"{triple}\n")

def pipe_out(output_text):
	"""Print processed text to terminal."""
	print("The most common groupings are:")
	for triple in output_text:
		print(f"{triple}")

#words = text_input()
#words_list = text_transform(words)
#words_triples = text_triple_maker(words_list)
#words_triples_count = triple_count(words_triples)
#pipe_out(words_triples_count)
#save_output(words_triples_count)

