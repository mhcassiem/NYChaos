import unittest
from bribes import minimumBribes


class Case0(unittest.TestCase):
    def test_something(self):
        inp = [2, 1, 5, 3, 4]
        out = minimumBribes(inp)
        exp_out = 3
        self.assertEqual(exp_out, out)


if __name__ == '__main__':
    unittest.main()
