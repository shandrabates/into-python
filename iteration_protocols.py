"""
Learn about iterable, iterator objects

"""


def first(iterable):
    """
    Return the next member of the list IF available
    :param iterable: iterable object
    :return: Next member or
    :except: ValueError for StopIteration
    """
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")


def main():
    """
    test function
    :return: nothing
    """
    iterable = ['Spring', 'Summer', 'Fall', 'Winter']
    iterator = iter(iterable)  #give me an iterator
    print(type(iterator), iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    b = first(iterable)
    print("First iterable:", b)



if __name__ == '__main__':
    main()
    exit(0)