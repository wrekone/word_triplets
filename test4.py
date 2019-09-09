import fileinput
import sys

# for line in fileinput.input():
#    print(line)

if sys.argv[1:]:
	print("args")
elif sys.stdout:
	print("pipe")
else:
	print("no args")

