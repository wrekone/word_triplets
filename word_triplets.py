# Import collections to use collections.Counter
from collections import Counter
# Import re for regex functions.
import re
# Import sys for access to system specific parameters and functions.
import sys

# Better to remove apostrophes or leave them in? Shouldnt or Shouldn't ?
# Is raw output preferred? Or output to a file, or prettified output, or ...?
# Don't forget to write documentation for project, classes, and functions.
# Don't forget to create test cases.
# Don't forget to update or delete comments.
# What if there are less than three words in source material?

def text_open(file_name):
	"""Read file contents."""
	with open(file_name) as f:
		text = f.read()
	return text

def text_input():
	"""Take input from file(s) or stream."""
	print("Processing text...")
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
	text = re.sub(r"[‘’]+", "'", text) # Replace curly single quotes with straight single quotes.
	text_arr = text.split()
	if len(text_arr) < 3: # Check for minimum of 3 words.
		print("Please provide a minimum of three words.")
		sys.exit()
	else:
		return text_arr

def text_triple_maker(arr):
	"""Create list of all triples from text."""	
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

