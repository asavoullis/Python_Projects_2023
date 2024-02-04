# Unit tests
import unittest
from String_Calculator_Application import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_newline_separator(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,3,-4")
        self.assertTrue("Negatives not allowed: -2, -4" in str(context.exception))

    def test_ignore_numbers_over_1000(self):
        self.assertEqual(self.calc.add("2,1001"), 2)

    def test_custom_delimiter_any_length(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)

    def test_multiple_delimiters(self):
        self.assertEqual(self.calc.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_delimiters_any_length(self):
        self.assertEqual(self.calc.add("//[**][%%%]\n1**2%%%3"), 6)

if __name__ == "__main__":
    unittest.main()