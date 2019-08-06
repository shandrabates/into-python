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
    # another way to create tuples
    # Parenthesis are optional
    t2 = 1, 2, 3, 5
    print(t2, type(t2))
    # tuple constructor: tuple()
    t_from_l = tuple([3, 77, 11])
    print(t_from_l, type(t_from_l))
    print(5 in (3, 6, 8, 5, 12))
    print(5 not in (3, 6, 8, 5, 12))

def min_max(items):
    """
    Return the minimum and maximum elements of a collection
    :param items: collection
    :return: the minimum and maximum
    """
    return min(items), max(items)


def swap(a, b):
    """
    Create a function that will swap values
    :param a:
    :param b:
    :return:
    """
    return b, a


def main():
    """
    test function
    :return: nothing
    """
    do_tuples()

    # output = min_max([56, 79, 11, 12, 90])
    # print("min", output[0])
    # print("max", output[1])
    # # tuple unpacking  => this turns these back into integers
    # lower, upper = min_max([56, 79, 11, 12, 90])
    # print("min", lower)
    # print("max", upper)
    # # Set up swap function
    # a = "jelly"
    # b = "bean"
    # print(a, b)
    # # call the swap function
    # a, b = swap(a, b)
    # print(a, b)
    # a, b = b, a
    # print(a, b)







if __name__ == '__main__':
    main()
    exit(0)