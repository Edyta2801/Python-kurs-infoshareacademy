import unittest
from unnecessary_math import multiply


class TestUnnecessaryMathM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_strings_a_3(self):
        self.assertEqual(multiply('a', 3), 'aaa')

    def test_strings_a_4(self):
        self.assertEqual(multiply('a', 4), 'aaaaa')

    def test_strings_3_4_negative_case(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(multiply(3, 4), 14)

    def test_strings_a_4_negative_case(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(multiply('a', 4), 'aaaaa')

    #failing test
    def test_strings_a_5_negative_case(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(multiply('a', 5), 'aaaaa')


if __name__ == '__main__':
    unittest.main()
