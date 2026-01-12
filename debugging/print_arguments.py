#!/usr/bin/python3
"""
Print all command-line arguments passed to the script.
"""
import sys


def main() -> None:
    """Print each argument on a new line."""
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Argument {i}: {arg}")


if __name__ == "__main__":
    main()
