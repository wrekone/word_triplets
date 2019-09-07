import fileinput
book = []
k = fileinput.input("moby_dick_snippet.txt")
for line in k:
	book.append(line)
	print(book)
print(fileinput.filename())
