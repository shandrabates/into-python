"""
How to handle exceptions in Python.
"""

import sys

def convert(s):
    """
    Converts a string to integer
    :param s: string
    :return: integer
    """
    try:
         return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion Error {}"
              .format(str(e)), file=sys.stderr)
        pass
    return -1


def sqrt(x):
    """
    Compute the sqrt using the method of Heron of Alexandria
    :param x: Number to compute the sqrt off
    :return: The sqrt of x
    :raise ValueError() on ZeroDivisionError
    """
    guess = x
    i = 0
    try:
        while guess*guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        # re-raise the exception
        raise ValueError()

    return guess


def main():
    """
    test function
    :return: nothing
    """
    print(convert("11"))
    #print(convert("Hello"))
    #print(convert([1, 4, 8]))
    try:
        print(sqrt(64))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("Cannot compute the sqrt of negative numbers")
    print("Done")




if __name__ == '__main__':
    main()
    exit(0)