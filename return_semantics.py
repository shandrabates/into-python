"""
Learn about Python return semantics and how Python functions
handle arguments
"""


def egg(var):
    """
    Returns the variable back to the user
    :param var: input object
    :return: input object
    """
    return var


def sum_two(num1, num2=8):
    """
    Sum the two integer objects
    :param num1: object 1
    :param num2: object 2 (optional), default is = 8
    :return: sum of objects
    """
    return num1 + num2


def main():
    """
    test function
    :return: nothing
    """
    c = [6, 10, 20]
    e = egg(c)
    print(c is e)
    # Test the sum_two function
    n1 = 3
    n2 = 9
    print(n1, ' + ', n2, " = ", sum_two(n1,n2))
    # Use the function using an option parameter
    print("Only one input", sum_two(n1))


if __name__ == '__main__':
    main()
    exit(0)