import unittest
import word_triplets


class TestWordTripletFunctions(unittest.TestCase):
    """Test functions for word_triplets.py"""

    def test_can_open_text_file(self):
        """Can a text file be read?"""
        sample = word_triplets.text_open(["sample_text.txt"])
        self.assertEqual(sample, "This is a test. ")

    def test_can_handle_multiple_file_input(self):
        """Can multiple files be passed into the program at one time?"""
        sample = word_triplets.text_open(["sample_text.txt", "sample_text_too.txt"])
        print(sample)
        self.assertEqual(sample, "This is a test. This is a test too. ")

    def test_handle_lack_of_input_file(self):
        """Can the program handle not being passed any input?"""
        sample = word_triplets.text_open("")
        self.assertEqual(sample, None)

    def test_handle_bad_input(self):
        """Can the program handle bad input?"""
        with self.assertRaises(SystemExit):
            word_triplets.text_open("non_existent.txt")

    def can_take_stream_as_input(self):
        """Are streams accepted as input?"""
        pass

    def test_all_groups_are_of_three(self):
        """Is text split into triplets?"""
        pass

    def test_text_transform(self):
        """Are punctuation, line endings, and case converted?"""
        sample = "ABC`DEF-\"GHI,.;JKL:!–?—“”...XYZ\n"
        processed_sample = word_triplets.text_transform(sample)
        self.assertEqual(processed_sample, ['abc', 'def', 'ghi', 'jkl', 'xyz'])

    def test_punctuation_is_removed(self):
        """Is all unwanted punctuation removed?"""
        pass

    def test_triple_counter_does_something(self):
        pass


if __name__ == "__main__":
    unittest.main()
