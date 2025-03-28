import re
def isPalindromeIterative(s):
    """
    Checks if a string is a palindrome by comparing characters from both ends towards the center.

    Complexity:
    - String conversion and cleanup: O(n)
    - Iterating up to half the string: O(n/2) = O(n)
    - Character comparison in each step: O(1)
    - Total complexity: O(n)

    :param s: String to evaluate.
    :return: If palindrome True, otherwise False.
    """
    s = re.sub(r'\W+', '', s.lower())
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    return True