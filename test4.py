import re

s = """strin-g. ! !With., Punctuation?
hello 67, help's"""
s = re.sub(r"[.,;:!?]+"," ",s)
print(s)