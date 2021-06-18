import unittest

input_true = ([1,2, 3, 4, 5, 6, 7],[2, 4, 6, 8, 10, 12, 14])
input_false = ([1, 2, (7.5), 3, 4, 5],[ 1, 2, 3, "jhfsa"])

class Test_test_1(unittest.TestCase):
    def test_A(self):
        for str in list_input_false:
            self.assertFalse(check.fieldTest(str))
    def test_B(self):
        for str in list_input_true:
            self.assertTrue(check.fieldTest(str))

if __name__ == '__main__':
    unittest.main()
