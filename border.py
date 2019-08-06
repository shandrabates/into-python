"""
Python Info HERE:
"""


def banner(message, border='*'):
    """
    Print message in banner form
    :param message: String to print
    :param border: border character for string
    :return: printed banner
    """
    print(border*len(message)+4*border)
    print(border,message,border)
    print(border*len(message)+4*border)


def main():
    """
    test function
    :return: nothing
    """
    # Use the banner function with both the message and border parameters
    banner('Weber State', '-')
    # Use the banner function without the optional border parameter
    banner('University of Utah')


if __name__ == '__main__':
    main()
    exit(0)