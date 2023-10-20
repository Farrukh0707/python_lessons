import unittest
from tests import even_nums


class EvenList(unittest.TestCase):
    def test_even_num(self):
        even = even_nums([1,2,3,7,10,15,20])
        self.assertEqual(even, [2,10,20])
        

unittest.main()