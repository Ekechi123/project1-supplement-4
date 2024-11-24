import unittest
from project1_supplement_4 import next_ten_numbers

class TestProject1Supplement4(unittest.TestCase):
    def test_next_ten_numbers(self):
        self.assertEqual(next_ten_numbers(5), "6,7,8,9,10,11,12,13,14,15")
        self.assertEqual(next_ten_numbers(0), "1,2,3,4,5,6,7,8,9,10")
        self.assertEqual(next_ten_numbers(-3), "-2,-1,0,1,2,3,4,5,6,7")

