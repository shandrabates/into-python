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



def main():
    """
    test function
    :return: nothing
    """
    run_take()


if __name__ == '__main__':
    main()
    exit(0)