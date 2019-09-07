from collections import Counter
import re

x, y = 0, 3

# Open and read text file
with open("moby_dick.txt") as f:
	moby_d = f.read()
	moby_clean = re.sub('\W', ' ', moby_d)
	arr = moby_clean.split()

# Iterate through 3 word lists, transform to strings, 
# and count occurences of string in text file.
# Not sure why some strings return count of 0.
while x < len(arr)-2:
	triplist = (arr[x:y])
	tripstr = ' '.join(triplist)
	print(tripstr)
	if tripstr.find("'") > -1:
		print(tripstr)
		break
	count = moby_clean.count(tripstr)
	print(count)
	#for g in arr:
	#	name = (f"{g}")
	#	print(name)
	x += 1
	y += 1