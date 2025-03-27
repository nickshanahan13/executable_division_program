#!/usr/bin/env python3

import sys

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return a / b

if __name__ == "__main__":
    if len(sys.argv)!= 3:
        print("Usage: divide.py <number1> <number2>")
        sys.exit(1)
    
    try:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        result = divide(a, b)
        print(result)
    except ValueError:
        print("Error: Invalid number format")
        sys.exit(1)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        sys.exit(1)

