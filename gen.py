"""
Module for demonstrating the use of generator functions

"""


def take(count, iterable):
    """
    Take items from the front of an iterable
    :param count: maximum number of items to retrieve
    :param iterable: The source series
    :yields: At most 'count' items for 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    """
    Test the take() function
    :return:
    """
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """
    Return unique items by eliminating duplicates
    :param iterable: The source series
    :yields: Unique elements in order from 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)
        # print(seen) to see this being built/run


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)



def main():
    """
    test function
    :return: nothing
    """
    #run_take()
    run_distinct()


if __name__ == '__main__':
    main()
    exit(0)