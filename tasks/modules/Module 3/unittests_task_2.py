"""Unit tests for task_2 from Module 3."""

import unittest
from task_2 import my_split


class MyFirstTests(unittest.TestCase):
    """Class containg unit tests for my_split function from task_2.py."""

    def test_normal(self):
        """Check result when one character as separator."""
        self.assertEqual(my_split("raz dwa trzy", " "), ["raz", "dwa", "trzy"])

    def test_no_separator(self):
        """Check result when no separator in string."""
        self.assertEqual(my_split("razdwatrzy", " "), ["razdwatrzy"])

    def test_more_separators(self):
        """Check result when more than one separator between characters."""
        self.assertEqual(
            my_split("raz   dwa   trzy", " "),
            ['raz', '', '', 'dwa', '', '', 'trzy'])

    def test_argument_not_a_string(self):
        """Check if correct msg when argument is not a string."""
        with self.assertRaises(TypeError):
            my_split(15, " ")

    def test_separator_not_a_string(self):
        """Check if correct msg when separator is not a string."""
        with self.assertRaises(TypeError):
            my_split("raz dwa trzy", 15)

    def test_string_only_containing_separator(self):
        """Check result when string contains only separators."""
        self.assertEqual(my_split(",,,,", ','), ['', '', '', '', ''])

    def test_two_words(self):
        """Check result when string and separator are 2 different words."""
        self.assertEqual(my_split("Python", 'Javascript'), ["Python"])

    def test_separator_not_provided(self):
        """Check result when user does not provide separator argument."""
        self.assertEqual(my_split("raz dwa trzy"), ["raz", "dwa", "trzy"])

    def test_separator_is_empty_string(self):
        """Check result when provided separator is empty."""
        with self.assertRaises(ValueError):
            my_split("raz dwa trzy", "")


# Checking results of my_split() againt split()
    def test_compare_split_normal(self):
        """Check result when one character as separator."""
        string = "raz dwa trzy"
        separator = " "
        self.assertEqual(my_split(string, separator), string.split(separator))

    def test_compare_split_no_separator(self):
        """Check result when no separator in string."""
        string = "razdwatrzy"
        separator = " "
        self.assertEqual(my_split(string, separator), string.split(separator))

    def test_compare_split_more_separators(self):
        """Check result when more than one separator between characters."""
        string = "raz   dwa   trzy"
        separator = " "
        self.assertEqual(my_split(string, separator), string.split(separator))

    def test_compare_split_string_only_containing_separator(self):
        """Check result when string contains only separators."""
        string = ",,,,"
        separator = ","
        self.assertEqual(my_split(string, separator), string.split(separator))

    def test_compare_split_two_words(self):
        """Check result when string and separator are 2 different words."""
        string = "Python"
        separator = "Javascript"
        self.assertEqual(my_split(string, separator), string.split(separator))


if __name__ == '__main__':
    unittest.main()
