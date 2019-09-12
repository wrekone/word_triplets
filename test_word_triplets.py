import unittest
import word_triplets

class TestWordTripletFunctions(unittest.TestCase):
	"""Test functions for word_triplets.py"""

	def test_can_open_text_file(self):
		"""Can a text file be read?"""
		words = word_triplets.text_open("sample_text.txt")
		self.assertEqual(words, "This is a test.")

	def test_can_handle_multiple_file_input(self):
		pass

	#def test_handles_lack_of_input_gracefully(self):
	#	inputty = word_triplets.text_input()
	#	self.assertEqual(inputty, "Error: No input. Please provide something to process.")

	def test_text_transform(self):
		"""Does program ignores punctuation, line endings, and case?"""
		sample = "ABC`DEF-\"GHI,.;JKL:!–?—“”...XYZ\n"
		processed_sample = word_triplets.text_transform(sample)
		self.assertEqual(processed_sample, ['abc', 'def', 'ghi', 'jkl', 'xyz'])

	#def test_punctuation_is_removed(self):
	#	pass

	#def test_text_triple_maker_returns_triples(self):
	#	pass

	#def test_triple_counter_does_something(self):
	#	pass

if __name__ == "__main__":
	unittest.main()