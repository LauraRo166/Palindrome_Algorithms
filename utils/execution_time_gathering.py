import time
import pandas as pd
from algorithms.isPalindromeReverse import isPalindromeReverse
from algorithms.isPalindromeIterative import isPalindromeIterative
from algorithms.isPalindromeRecursive import isPalindromeRecursive

def measure_execution_time(algorithm, case):
    """
    Measures the execution time of a palindrome checking algorithm.

    :param algorithm: Palindrome function.
    :param case: String to be checked.
    :return: Execution time in seconds.
    """
    start_time = time.time()
    algorithm(case)
    return time.time() - start_time

def gather_execution_times(cases_sizes):
    """
    Collects execution times for different string sizes.

    :param cases_sizes: List of string sizes to test.
    :param samples_per_size: Number of samples per size.
    :return: Pandas DataFrame with execution times.
    """
    results = []

    for size in cases_sizes:
        print(f"Computing size {size}")
        times_iterative = []
        times_reverse = []
        times_recursive = []

        cases = [
            "a" * size,                                           # Single repeating character
            "ab" * (size // 2),                                   # Alternating pattern
            "racecar" * (size // 5),                              # Repeated palindrome
            "abcdefgh" * (size // 8),                             # Random non-palindrome pattern
            "A" * (size // 2) + "B" + "A" * (size // 2),          # Symmetric large palindrome
            "level" * (size // 2),                                # Repeated short palindrome
            "abcddcba" * (size // 2),                             # Structured palindrome
            "a" * (size // 3) + "b" * (size // 3) + "a" * (size // 3),  # Three-segment palindrome
            "madam" + "x" * (size - 5) + "madam"[::-1],          # Palindrome with noise in the middle
            "12345678987654321",                                  # Numeric palindrome
            "abcdefghijklmnoonmlkjihgfedcba",                    # Long palindrome with unique characters
            "a" * (size // 2) + "bc" + "a" * (size // 2),        # Almost palindrome (fails at "bc")
            "".join(chr(65 + (i % 26)) for i in range(size)),    # Alphabetic sequence (non-palindrome)
            "aaabaaa" * (size // 7),                             # Almost palindrome with slight variation
            "abccba" * (size // 6) + "z",                        # Structured palindrome with one extra character
        ]

        for case in cases:
            times_iterative.append(measure_execution_time(isPalindromeIterative, case))
            times_reverse.append(measure_execution_time(isPalindromeReverse, case))
            times_recursive.append(measure_execution_time(isPalindromeRecursive, case))

        results.append({
            'Size': size,
            'Iterative': sum(times_iterative) / len(cases),
            'Recursive': sum(times_recursive) / len(cases),
            'Reverse': sum(times_reverse) / len(cases),
        })
    return pd.DataFrame(results).groupby("Size", as_index=False).mean()