from collections import Counter
import re
import sys


def text_open(file_names):
    """Read file contents."""
    text = ""
    for file in file_names:
        try:
            with open(file) as f:
                text += (f"{f.read()} ")
        except FileNotFoundError:
            print("Error: file not found")
            sys.exit()
    return text


def text_input():
    """Take input from file(s) or stream."""
    try:
        if not sys.stdin.isatty():
            text = sys.stdin.read()
        elif sys.argv[1]:
            inputArgs = sys.argv[1:]
            text = text_open(inputArgs)
    except IndexError:
        print("Error: Please provide something to process.")
        print("Usage: word_triplets.py [FILE]...")
        sys.exit()
    return text


def text_transform(text):
    """Prepare text for processing. Return as list."""
    text = text.lower()
    text = re.sub(r"[’‘]+", "'", text)  # Replace curly quotes with straight.
    text = re.sub(r"[^a-z\-']+", " ", text)  # Remove punctuation.
    text_arr = text.split()
    if len(text_arr) < 3:  # Check for minimum of 3 words.
        print("Please provide a minimum of three words.")
        sys.exit()
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


def group_count(arr):
    """Count triples and sort by most common."""
    count = Counter(arr).most_common(100)
    return count





