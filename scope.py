"""
Learn about scoping in Python

Probably the best data analysis Python to use that is free is Anaconda package
"""

count = 0    # global object

def show_count():
    """
    Disply the current count
    :return: nothing
    """
    print(count)


def set_count(para):
    """
    Set global counter value to whatever parameter is input
    :param para: input number
    :return: nothing
    """
    global count    # this makes the variable "count" global
    count = para    # this becomes a local variable, so it does not change the global
    print(count)



def main():
    """
    test function
    :return: nothing
    """
    show_count()
    set_count(2)
    show_count()


if __name__ == '__main__':
    main()
    exit(0)