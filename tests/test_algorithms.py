import unittest
from algorithms.isPalindromeIterative import isPalindromeIterative
from algorithms.isPalindromeRecursive import isPalindromeRecursive
from algorithms.isPalindromeReverse import isPalindromeReverse

class TestPalindromeMethods(unittest.TestCase):
    def test_palindromes(self):
        """Tests for palindromic words"""
        palindromes = ["madam", "racecar", "A man a plan a canal Panama", "No 'x' in Nixon"]
        for s in palindromes:
            with self.subTest(s=s):
                self.assertTrue(isPalindromeReverse(s))
                self.assertTrue(isPalindromeRecursive(s))
                self.assertTrue(isPalindromeIterative(s))

    def test_non_palindromes(self):
        """Tests for no palindromic words"""
        non_palindromes = ["hello", "world", "python", "12345"]
        for s in non_palindromes:
            with self.subTest(s=s):
                self.assertFalse(isPalindromeReverse(s))
                self.assertFalse(isPalindromeRecursive(s))
                self.assertFalse(isPalindromeIterative(s))
