"""
Python Info HERE:
"""

import time

def banner(message, border='*'):
    """
    Print message in banner form
    :param message: String to print
    :param border: border character for string
    :return: printed banner
    """
    print('\n')  # add some space before the banner printing
    print(border*len(message)+4*border)
    print(border, message, border)
    print(border*len(message)+4*border)


def add_spam(menu=None):
    """
    Add spam to the menu list
    :param menu: an input parameter or Python's version of null
    :return: menu list
    """
    if menu is None:
        menu = []
    menu.append('spam')
    return menu


def main():
    """
    test function
    :return: nothing
    """
    # Use the banner function with both the message and border parameters
    banner('Weber State', '-')
    # Use the banner function without the optional border parameter
    banner('University of Utah')
    print(add_spam())

    breakfast = ['eggs', 'bacon']
    print('Before', breakfast)
    add_spam(breakfast)
    print("After", breakfast)


if __name__ == '__main__':
    main()
    exit(0)