import re

with open("moby_dick.txt", encoding="utf-8") as f:
	moby_d = f.read()
	# Remove stupid curly quote characters.
	moby_cleanish = re.sub([r"’"], r"''", moby_d)
	print(moby_cleanish)

	# Fuk this little guy -> ’