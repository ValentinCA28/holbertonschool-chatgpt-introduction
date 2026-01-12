import sys

def factorial(n):
    if n < 0:
        print("Error: negative number", file=sys.stderr)
        sys.exit(1)
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except (IndexError, ValueError):
        print("Usage: ./factorial.py <positive integer>", file=sys.stderr)
        sys.exit(1)