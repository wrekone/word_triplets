from collections import Counter
import re

# Probably want to create tuples of (string, count). Maybe dictionaries instead, ie {"string": count}.
# Count possibly create tuples of each and zip them.
# Don't forget to create test cases. One string you can test against is "out of the".
# Am I pickint up partial words, such as "sea" in the phrase "of the seamen"?

x, y = 0, 3
word_triplets = dict()

# Open and read text file. Convert to all lower case.
with open("moby_dick_snippet.txt") as f:
	moby_d = f.read().lower()
	# Remove non-word characters.
	# Isn't removing commas yet.
	moby_cleanish = re.sub(r"[^\w\d'\s]+", "", moby_d)
	moby_cleaner = re.sub('\n', ' ', moby_cleanish)
	# Split string into list of words.
	arr = moby_cleaner.split()

# Iterate through 3 word lists, transform to strings, 
# and count occurences of string in text file.
# Not sure why some strings return count of 0.
# Actually, it's returning 0 because it's comparing
# cleaned text to the original uncleaned text, but I'm not
# sure why it's doing that.
while x < len(arr)-2:
	# Create list of 3 words.
	triplist = (arr[x:y])
	# Print list to confirm contents. Delete later.
	#print(triplist)
	# Turn list into string
	tripstr = ' '.join(triplist)
	# For testing purposes, check if string has apostrophe.
	# Delete this block later.
	# I don't think it works anyhow.
	if tripstr.find("'") > -1:
		print(tripstr)
		break
	# Count occurences of each 3-word string.
	count = moby_cleaner.count(tripstr)
	# Print string and its count
	print(f"{count}: {tripstr}")
	# Iterate
	x += 1
	y += 1
	#temp_tup = ()
	#try:
	#	with open("test_output.txt", "a") as f:
	#		temp_tup = temp_tup + f
	#		trip_list_str = ' '.join(temp_tup)
	#		f.write(trip_list_str)
	#except SyntaxError:
	#	pass