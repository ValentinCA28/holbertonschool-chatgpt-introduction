#!/usr/bin/python3
"""
Print all command-line arguments passed to the script.
"""
import sys


def main() -> None:
    """Print each argument on a new line."""
    for arg in sys.argv[1:]:
        print(arg)


if __name__ == "__main__":
    main()
