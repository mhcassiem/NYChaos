import unittest
from bribes import minimumBribes


class Case0_1(unittest.TestCase):
    def test_something(self):
        inp = [2, 1, 5, 3, 4]
        out = minimumBribes(inp)
        exp_out = 3
        self.assertEqual(exp_out, out)


class Case0_2(unittest.TestCase):
    def test_something(self):
        inp = [2, 5, 1, 3, 4]
        out = minimumBribes(inp)
        exp_out = 'Too chaotic'
        self.assertEqual(exp_out, out)


class Case1_0(unittest.TestCase):
    def test_something(self):
        inp = [5, 1, 2, 3, 7, 8, 6, 4]
        out = minimumBribes(inp)
        exp_out = 'Too chaotic'
        self.assertEqual(exp_out, out)


class Case1_1(unittest.TestCase):
    def test_something(self):
        inp = [1, 2, 5, 3, 7, 8, 6, 4]
        out = minimumBribes(inp)
        exp_out = 7
        self.assertEqual(exp_out, out)


class Case2_0(unittest.TestCase):
    def test_something(self):
        inp = [1, 2, 5, 3, 4, 7, 8, 6]
        out = minimumBribes(inp)
        exp_out = 4
        self.assertEqual(exp_out, out)


if __name__ == '__main__':
    unittest.main()
