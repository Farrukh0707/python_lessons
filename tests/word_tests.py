import unittest
from tests import title_letter


class WordsTest(unittest.TestCase):
    def test_title_word(self):
        title_words = title_letter(['hello', 'hi', 'goodbye'])
        self.assertEqual(title_words, ['Hello', 'Hi', 'Goodbye'])

        

unittest.main()


