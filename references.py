"""
Learn about references and how Python uses them (ex: how Python points to things)
"""


def modify(k):
    """
    Modify the content of a list
    :param k: input list
    :return: nothing
    """
    # lists are passed by reference
    k.append(39)
    print("k = ", k)


def replace(g):
    """
    Replace input list, but creates a local copy (does nothing)
    :param g: input list
    :return: nothing
    """
    g = [17, 48, 89]
    print("g = ", g)


def replace_content(g):
    """
    Replace the content inside the input list
    :param g: input list
    :return: nothing
    """
    g[0] = 88
    g[1] = 22
    g[2] = 44
    print("g = ", g)


def main():
    """
    test function
    :return: nothing
    """
    m = [9, 15, 24]
    print("Before modify() m = ", m)
    modify(m)
    print("After modify() m = ", m)
    replace(m)
    print("After replace() m = ", m)
    replace_content(m)
    print("After replace_content() m = ", m)


if __name__ == '__main__':
    main()
    exit(0)