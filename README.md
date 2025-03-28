# Palindrome_Algorithms

The following search algorithms are implemented:
+ Iterative
+ Recursive
+ Reverse

## Complexities Analysis
### Iterative
+ Best Case (O(1)): If the first and last characters do not match, it stops immediately.
+ Worst Case (O(N)): The loop runs until reaching the middle if all characters match.
+ Average Case (O(N/2)): On average, the function checks half of the characters before stopping.

### Recursive
+ Best Case (O(1)): If the string length is 0 or 1, it is immediately recognized as a palindrome.
+ Worst Case (O(N)): The function calls itself N/2 times until reaching the middle of the string.
+ Average Case (O(N/2)): On average, the recursion depth reaches half of the string length.

### Reverse
+ Best Case (O(1)): If the string is empty or a single character, the function returns immediately.
+ Worst Case (O(N)): The entire string must be reversed and compared.
+ Average Case (O(N)): Most cases require processing the entire string.

## Unit and coverage testing



## Test and visualization


