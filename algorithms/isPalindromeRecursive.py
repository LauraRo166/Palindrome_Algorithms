import re

def isPalindromeRecursiveHelper(s):
    """
    Recursively checks if a cleaned string is a palindrome.

    :param s: String to evaluate.
    :return: If palindrome True, otherwise False.
    """
    length = len(s)
    if length == 0 or length == 1:
        return True
    if s[0] != s[length-1]:
        return False
    return isPalindromeRecursiveHelper(s[1:length-1])

def isPalindromeRecursive(s):
    """
    Checks if a string is a palindrome using recursion.

    Complexity:
    - Recursive calls up to half the string length: O(n/2) = O(n)
    - Character comparison in each call: O(1)
    - Total complexity: O(n)

    :param s: String to evaluate.
    :return: If palindrome True, otherwise False.
    """
    s = ''.join(c.lower() for c in s if c.isalnum())
    return isPalindromeRecursiveHelper(s)
