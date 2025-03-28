import re
def isPalindromeReverse(s):
    """
    Checks if a string is a palindrome by reversing it and comparing it to the original.

    Complexity:
    - Lowercasing the string: O(n)
    - Removing non-alphanumeric characters: O(n)
    - Reversing the string: O(n)
    - Comparing strings: O(n)
    - Total complexity: O(n)

    :param s: String to evaluate.
    :return: If palindrome True, otherwise False.
    """
    s = re.sub(r'\W+', '', s.lower())
    return s == s[::-1]