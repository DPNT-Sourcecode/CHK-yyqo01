# encoding: utf-8

import unittest
from parameterized import parameterized

from solutions.CHK import checkout_solution


class TestSum(unittest.TestCase):
    @parameterized.expand([
        ('e',),
        (2,), 
        ('&',), 
        ('£',)
    ])
    def test_invalid_input(self, fail_char):
        self.assertEqual(
            checkout_solution.checkout(fail_char), -1)
    
    def test_chk_special_offers(self):
        self.assertEqual(
            checkout_solution.checkout('AAABBCD'), 
            210)
    
    @parameterized.expand([
        ('A', 50),
        ('B', 30), 
        ('C', 20), 
        ('D', 15)
    ])
    def test_chk_single_values(self, char, value):
        import pdb;pdb.set_trace()
        self.assertEqual(
            checkout_solution.checkout(char), 
            value)
    
    def test_chk_empty_string(self):
        self.assertEqual(
            checkout_solution.checkout(""), 
            0)


if __name__ == '__main__':
    unittest.main()
