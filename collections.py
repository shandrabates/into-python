"""
Learn about collections: Tuples, Strings, Range, List
"""

def do_tuples():
    """
    Practice tuples
    :return: nothing
    """
    # Use () to define a tuple - immutable sequence of arbitrary objects
    t = ("Ogden", 1.99, 2)
    print(t, type(t))
    print("Size ", len(t))
    print("One member", t[0])  # by index notation
    # to iterate over a tuple
    for item in t:
        print(item)

    # single tuples
    t1 = (6,)      # adding the comma changes from an integer to a tuple (as integer is preferred)
    print(t1, type(t1))
    #another way to create tuples
    # Parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))


def min_max(items):
    """
    Return the minimum and maximum elements of a collection
    :param items: collection
    :return: the minimum and maximum
    """
    return min(items), max(items)



def main():
    """
    test function
    :return: nothing
    """
    # do_tuples()

    output = min_max([56, 79, 11, 12, 90])
    print("min", output[0])
    print("max", output[1])
    # tuple unpacking  => this turns these back into integers
    lower, upper = min_max([56, 79, 11, 12, 90])
    print("min", lower)
    print("max", upper)



if __name__ == '__main__':
    main()
    exit(0)