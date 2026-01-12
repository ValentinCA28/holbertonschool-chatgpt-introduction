#!/usr/bin/python3
"""
Recursive factorial calculator

This script computes the factorial of a non-negative integer
provided as a command-line argument.

Usage:
    ./factorial_recursive.py N

Example:
    ./factorial_recursive.py 5
    → 120
"""

import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Function description:
        The factorial of a non-negative integer n (denoted n!) is the product
        of all positive integers less than or equal to n.
        By definition: 0! = 1
        This implementation uses recursion: n! = n × (n-1)!

    Parameters:
        n (int): A non-negative integer for which to compute the factorial.

    Returns:
        int: The factorial of n (n!)

    Note:
        - Very large values of n will cause a RecursionError due to Python's
          recursion depth limit (usually ~1000).
        - Negative numbers are not handled and will cause infinite recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    # Check if exactly one argument was provided (besides script name)
    if len(sys.argv) != 2:
        print("Usage: ./factorial_recursive.py N")
        print("  where N is a non-negative integer")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        if number < 0:
            print("Error: Please provide a non-negative integer")
            sys.exit(1)

        result = factorial(number)
        print(result)

    except ValueError:
        print("Error: Argument must be an integer")
        sys.exit(1)
    except RecursionError:
        print("Error: Number too large — recursion limit exceeded")
        sys.exit(1)
