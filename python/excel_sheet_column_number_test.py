import unittest
from excel_sheet_column_number import titleToNumber as to_test


INPUT_OUTPUT = [("A", 1), ("AB", 28), ("ABC", 731)]


class MyTestCase(unittest.TestCase):
    def test_something(self):

        for (i, o) in INPUT_OUTPUT:
            func_out = to_test(i)
            self.assertEqual(o, func_out)  # add assertion here


if __name__ == '__main__':
    unittest.main()
