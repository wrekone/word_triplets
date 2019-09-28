import unittest
import word_triplets_processor


class TestWordTripletFunctions(unittest.TestCase):
    """Test functions for word_triplets_processor.py"""

    def setUp(self):
        self.sample = ["this", "is", "a", "test", "this", "is", "a", "test", "too"]

    def test_can_open_text_file(self):
        """Can a text file be read?"""
        opened = word_triplets_processor.text_open(["sample_text.txt"])
        self.assertEqual(opened, "This is a test. ")

    def test_accepts_multiple_files(self):
        """Can multiple files be passed into the program at one time?"""
        opened = word_triplets_processor.text_open(["sample_text.txt", "sample_text_too.txt"])
        self.assertEqual(opened, "This is a test. This is a test too. ")

    def test_handle_lack_of_input(self):
        """Can the program handle not being passed any input?"""
        unopened = word_triplets_processor.text_open("")
        self.assertEqual(unopened, "")

    def test_returns_groups_of_three(self):
        """Is text split into triplets?"""
        triples = word_triplets_processor.text_triple_maker(self.sample)
        triples_len = triples[1].split()
        self.assertEqual(3, len(triples_len))

    def test_text_transform(self):
        """Are punctuation, line endings, and case converted?"""
        transform_sample = "ABC`DEF\"GHI,.;JKL:!–?—“”...XYZ\n"
        processed_sample = word_triplets_processor.text_transform(transform_sample)
        self.assertEqual(processed_sample, ["abc", "def", "ghi", "jkl", "xyz"])

    def test_triple_counter_returns_list_of_tuples(self):
        """Is the output in the expected format?"""
        count = word_triplets_processor.group_count(self.sample)
        self.assertEqual(count, [('this', 2), ('is', 2), ('a', 2), ('test', 2), ('too', 1)])


if __name__ == "__main__":
    unittest.main()
