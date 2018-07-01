import unittest

from solutions.HLO import hello_solution


class TestSum(unittest.TestCase):
    def test_hlo(self):
        self.assertEqual(hello_solution.hello('test'), 'hello test')


if __name__ == '__main__':
    unittest.main()
