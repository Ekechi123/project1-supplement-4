import unittest
from project1_supplement_4 import next_ten_numbers

class TestProject1Supplement4(unittest.TestCase):
    def test_next_ten_numbers(self):
        self.assertEqual(next_ten_numbers(5), "6,7,8,9,10,11,12,13,14,15")
        self.assertEqual(next_ten_numbers(0), "1,2,3,4,5,6,7,8,9,10")
        self.assertEqual(next_ten_numbers(-3), "-2,-1,0,1,2,3,4,5,6,7")


from project1_supplement_4 import list_to_comma_string

class TestProject1Supplement4(unittest.TestCase):
    # Existing test remains...
    def test_list_to_comma_string(self):
        self.assertEqual(list_to_comma_string(["a", "b", "c"]), "a,b,c")
        self.assertEqual(list_to_comma_string(["1", "2", "3"]), "1,2,3")
        self.assertEqual(list_to_comma_string([]), "")


import os
from project1_supplement_4 import write_to_csv

class TestProject1Supplement4(unittest.TestCase):
    # Existing tests remain...
    def test_write_to_csv(self):
        test_headers = "Header1,Header2,Header3"
        test_data = "1,2,3"
        filename = "test_output.csv"
        write_to_csv(filename, test_headers, test_data)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as f:
            content = f.read()
            self.assertIn(test_headers, content)
            self.assertIn(test_data, content)
        os.remove(filename)  # Clean up

