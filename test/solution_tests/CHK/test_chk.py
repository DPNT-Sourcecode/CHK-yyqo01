# encoding: utf-8

import unittest
from nose_parameterized import parameterized

from solutions.CHK import checkout_solution


class TestSum(unittest.TestCase):
    @parameterized.expand([('e',),(2,), ('&',), ('£',)])
    def test_invalid_input(self, fail_char):
        self.assertEqual(
            checkout_solution.checkout(fail_char), -1)
        
    def test_chk_special_offers(self):
        import pdb;pdb.set_trace()
        self.assertEqual(
            checkout_solution.checkout('AAABBCD'), 
            210)


if __name__ == '__main__':
    unittest.main()
