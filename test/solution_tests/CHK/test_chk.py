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
    
    def test_chk_multiple_special_offers(self):
        self.assertEqual(
            checkout_solution.checkout('AAAAAAAABBCDE'), 
            450)
    
    def test_chk_get_free(self):
        self.assertEqual(
            checkout_solution.checkout('ABCDEE'), 
            165)
    
    def test_chk_get_2_free(self):
        self.assertEqual(
            checkout_solution.checkout('ABBCDEEEE'), 
            245)
    
    def test_chk_get_free_multiple_offers(self):
        self.assertEqual(
            checkout_solution.checkout('AAAAAAAABBCDEE'), 
            475)
    
    @parameterized.expand([
        ('FFF', 20),
        ('FF', 20), 
        ('FFFF', 30), 
        ('FFFFFF', 40)
    ])
    def test_chk_get_free_same_item(self, skus, value):
        self.assertEqual(
            checkout_solution.checkout(skus), 
            value)
    
    def test_chk_get_free_multiple_offers_same_item(self):
        self.assertEqual(
            checkout_solution.checkout('AAAAAAAABBCDEEFFF'), 
            495)
    
    @parameterized.expand([
        ('A', 50),
        ('B', 30), 
        ('C', 20), 
        ('D', 15),
        ('E', 40),
        ('F', 10),
    ])
    def test_chk_single_values(self, char, value):
        self.assertEqual(
            checkout_solution.checkout(char), 
            value)
    
    def test_chk_empty_string(self):
        self.assertEqual(
            checkout_solution.checkout(""), 
            0)


if __name__ == '__main__':
    unittest.main()
