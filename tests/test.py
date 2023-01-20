import os
import unittest
from main import WordCount


# python -m unittest tests/test.py
class TestWordCount(unittest.TestCase):
    """
    For Question 4: unit test
    """
    wc = WordCount()


    def test_empty_input(self):
        #  test Null and empty inputs for the first brute force approach
        self.assertEqual(self.wc.question_one_word_count(""), None)
        self.assertEqual(self.wc.question_one_word_count(None), None)

        #  test Null and empty inputs for the second improved approach
        self.assertEqual(self.wc.question_two_word_count(""), None)
        self.assertEqual(self.wc.question_two_word_count(None), None)

    def test_invalid_file(self):
        #  test invalid input for the first brute force approach
        self.assertEqual(self.wc.question_one_word_count("invalid.txt"), None)
        self.assertEqual(self.wc.question_one_word_count(1234534), None)

        #  test invalid input for the second improved approach
        self.assertEqual(self.wc.question_two_word_count("invalid.txt"), None)
        self.assertEqual(self.wc.question_two_word_count(34625), None)

    def test_empty_file(self):
        #  test valid input for empty content in the file , for both approaches
        fp = open("tests/empty.txt", "x")
        fp.write("  ")
        fp.close()
        self.assertEqual(self.wc.question_one_word_count("tests/empty.txt"), {})
        self.assertEqual(self.wc.question_two_word_count("tests/empty.txt"), {})
        os.remove("tests/empty.txt")

    def test_sample_file(self):
        #  test valid input for sample.txt , for both approaches; checking some random words' count
        #  here we can also compare the whole output with the expected output. But because of the large
        #  content, I randomly select some words and do the verification.
        #  The next test compare the whole output with a smaller content in the text.
        dictionary_1 = self.wc.question_one_word_count("data/sample.txt")
        highest_count_1 = self.wc.question_three_highest_count(dictionary_1)
        self.assertEqual(len(dictionary_1), 373)
        self.assertEqual(highest_count_1[0], 'non')
        self.assertEqual(highest_count_1[1], 12)
        self.assertEqual(dictionary_1.get("non"), 12)
        self.assertEqual(dictionary_1.get("quem"), 1)
        self.assertEqual(dictionary_1.get("maximum"), 1)
        self.assertEqual(dictionary_1.get("esse"), 9)
        self.assertEqual(dictionary_1.get("verum"), 3)
        self.assertEqual(dictionary_1.get("haec"), 3)
        self.assertEqual(dictionary_1.get("haec"), 3)
        self.assertEqual(dictionary_1.get("quod"), 11)
        self.assertEqual(dictionary_1.get("am"), None)

        dictionary_2 = self.wc.question_one_word_count("data/sample.txt")
        highest_count_2 = self.wc.question_three_highest_count(dictionary_1)
        self.assertEqual(len(dictionary_2), 373)
        self.assertEqual(highest_count_2[0], 'non')
        self.assertEqual(highest_count_2[1], 12)
        self.assertEqual(dictionary_2.get("non"), 12)
        self.assertEqual(dictionary_2.get("quem"), 1)
        self.assertEqual(dictionary_2.get("maximum"), 1)
        self.assertEqual(dictionary_2.get("esse"), 9)
        self.assertEqual(dictionary_2.get("verum"), 3)
        self.assertEqual(dictionary_2.get("haec"), 3)
        self.assertEqual(dictionary_2.get("haec"), 3)
        self.assertEqual(dictionary_2.get("quod"), 11)
        self.assertEqual(dictionary_2.get("am"), None)

    #  test valid input for a small text , for both approaches; compare the whole output with the expected output.
    def test_valid_file(self):
        fp = open("tests/valid_test_1.txt", "x")
        fp.write(
            "!this is %@ a test /t/n hello this is the /t second line /n what is the day today?~` That is right.,?? #")
        fp.close()

        expected_result = {'is': 4, 'the': 2, 'this': 2, 'a': 1, 'test': 1, 'tn': 1, 'hello': 1, 't': 1, 'second': 1,
                           'line': 1, 'n': 1, 'what': 1, 'day': 1, 'today': 1, 'that': 1, 'right': 1}

        dictionary_1 = self.wc.question_one_word_count("tests/valid_test_1.txt")
        self.assertEqual(len(expected_result), len(dictionary_1))
        self.assertTrue(expected_result == dictionary_1)

        dictionary_2 = self.wc.question_two_word_count("tests/valid_test_1.txt")
        self.assertEqual(len(expected_result), len(dictionary_2))
        self.assertTrue(expected_result == dictionary_2)

        os.remove("tests/valid_test_1.txt")

