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
# Am I pickint up partial words, such as "sea" in the phrase "of the seamen"?
# Check for consitency of quote marks.

triples_list = []
x, y = 0, 3

# Parse command line
#if file_name_given:
#	text = open(file_name_given)
#else:
#	text = sys.stdin

def text_open(file_name):
	with open(file_name) as f:
		text = f.read().lower()
		return text

def text_transform(text):
	text = re.sub(r"[\-\",.;:!?—‘’“”]+", " ", text)
	text_arr = text.split()
	return text_arr

def text_triple_maker(arr):
	while x < len(arr) - 2:
		triple = (arr[x:y])
		triple_string = " ".join(text_triple)
		triples_list.append(text_triple_string)
		x += 1
		y += 1

def triple_count(triples):
	triple_count = Counter(triples).most_common()
	return triple_count

def close(triple_count):
	with open("output.txt", "w") as f:
		for triple in triple_count:
			f.write(f"{triple_count}\n")

# Open and read text file. Convert to all lower case.
with open("moby_dick.txt") as f:
	text = f.read().lower()
	# Remove unwanted characters.
	text_cleaner = re.sub(r"[\-\",.;:!?—‘’“”]+", " ", text_d)
	# Split string into list of words.
	arr = text_cleaner.split()

# Iterate through 3 word lists, transform to strings, 
while x < len(arr)-2:
	# Create list of 3 words.
	triplist = (arr[x:y])
	# Turn list into string.
	tripstr = ' '.join(triplist)
	# Append tripstr string to triples list.
	triples.append(tripstr)
	# Iterate (slide the window)
	x += 1
	y += 1

triple_count = Counter(triples).most_common()
# Output to file.
with open("test_output.txt", "w") as f:
		for triple in triple_count:
			f.write(f"{triple}\n")

if text is not sys.stdin:
	text.close()