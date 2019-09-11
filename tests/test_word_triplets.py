import unittest
import word_triplets

class TestWordTripletFunctions(unittest.TestCase):
	"""Test functions for word_triplets.py"""

	def test_can_test(self):
		"""Can I even run a test?"""
		self.assertEqual('foo'.upper(), 'FOO')

	def test_can_open_text_file(self):
		"""Can a text file be read?"""
		words = word_triplets.text_open("sample_text.txt")
		self.assertEqual(words, "This is a test.")

	#def test_can_take_piped_input(self):
	#	pass

	def test_hyphen_not_en_dash_not_em_dash(self):
		"""Documentation"""
		en_dash = "–"
		em_dash = "—"
		hyphen = "-"
		self.assertNotEqual(en_dash, em_dash)
		self.assertNotEqual(en_dash, hyphen)
		self.assertNotEqual(em_dash, hyphen)

	def test_text_lowercase(self):
		"""Is text stripped of punctuation and in lower case?"""
		sample = "RGB`-\",.;:!–?—“”"
		processed_sample = word_triplets.text_transform(sample)
		self.assertEqual(processed_sample, "rgb")

	#def test_punctuation_is_removed(self):
	#	pass

	#def test_text_triple_maker_returns_triples(self):
	#	pass

	#def test_triple_counter_does_something(self):
	#	pass

if __name__ == "__main__":
	unittest.main()