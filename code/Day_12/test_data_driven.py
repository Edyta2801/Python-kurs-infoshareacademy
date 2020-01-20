from ddt import ddt, data
import unittest


# metoda którą będziemy testowali:
def larger_that_two(number):
    return number > 2


@ddt
class FooTestCase(unittest.TestCase):
    def test_undecorated(self):
        self.assertTrue(larger_that_two(24))

    @data(1, 2, 3, 4, 45, 65, -3)
    def test_larger_than_two(self, value):
        self.assertTrue(larger_that_two(value))


if __name__ == '__main__':
    unittest.main()
