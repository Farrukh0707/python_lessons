import unittest
from tests import max_numb

class NumbTest(unittest.TestCase):
    def test_max_son(self):
        max_number = max_numb(4,33,109)
        self.assertEqual(max_number, 109)
        


unittest.main()


