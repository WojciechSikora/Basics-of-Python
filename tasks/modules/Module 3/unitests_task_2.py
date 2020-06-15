"""Unit tests for task_2 from Module 3."""

import unittest
from task_2 import my_split


class MyFirstTests(unittest.TestCase):
    """Class containg unit tests for my_split function from task_2.py."""

    def test_normal(self):
        """Check if splits correctly when one character as separator."""
        self.assertEqual(my_split("raz dwa trzy", " "), ["raz", "dwa", "trzy"])

    def test_no_separator(self):
        """Check if splits correctly when no separator in string."""
        self.assertEqual(my_split("razdwatrzy", " "), ["razdwatrzy"])

    def test_more_separators(self):
        """Check if splits correctly when more than one separator between characters."""
        self.assertEqual(my_split("raz   dwa   trzy", " "), ['raz', '', '', 'dwa', '', '', 'trzy'])

    def test_argument_not_a_string(self):
        """Check if correct msg when argument is not a string."""
        self.assertEqual(my_split(15, " "), "Argument is not a string")

    def test_separator_not_a_string(self):
        """Check if correct msg when separator is not a string."""
        self.assertEqual(my_split("raz dwa trzy", 15), "Separator is not a string")

    def test_string_only_containing_separator(self):
        """Check if splits correctly when string contains only separators."""
        self.assertEqual(my_split(",,,,", ','), ['', '', '', '', ''])

    def test_two_words(self):
        """Check if splits correctly when string and separator are 2 different words."""
        self.assertEqual(my_split("Python", 'Javascript'), ["Python"])


if __name__ == '__main__':
    unittest.main()
