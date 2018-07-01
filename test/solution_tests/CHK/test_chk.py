# encoding: utf-8

import unittest
from parameterized import parameterized

from solutions.CHK import checkout_solution


class TestCheckout(unittest.TestCase):
    @parameterized.expand([
        ('e',),
        (2,), 
        ('&',), 
        ('£',)
    ])
    def test_invalid_input(self, fail_char):
        self.assertEqual(
            checkout_solution.checkout(fail_char), -1)
    
    @parameterized.expand([
        ('HHHHH', 45),
        ('HHHHHHHHH', 85),
        ('AAABBCD', 210),
        ('KK', 150)
    ])
    def test_chk_special_offers(self, skus, value):
        self.assertEqual(
            checkout_solution.checkout(skus), value)
    
    @parameterized.expand([
        ('AAAAAAAABBCDE', 450),
        ('AAAAAAAABBCDEHHHHHHHH', 525)
    ])
    def test_chk_multiple_special_offers(self, skus, value):
        self.assertEqual(
            checkout_solution.checkout(skus), value)
    
    @parameterized.expand([
        ('ABCDEE', 165),
        ('NNNM', 120)
    ])
    def test_chk_get_free(self, skus, value):
        self.assertEqual(
            checkout_solution.checkout(skus, value))
    
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
        ('G', 20),
        ('H', 10),
        ('I', 35),
        ('J', 60),
        ('K', 80),
        ('L', 90),
        ('M', 15),
        ('N', 40),
        ('O', 10),
        ('P', 50),
        ('Q', 30),
        ('R', 50),
        ('S', 30),
        ('T', 20),
        ('U', 40),
        ('V', 50),
        ('W', 20),
        ('X', 90),
        ('Y', 10),
        ('Z', 50)
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
