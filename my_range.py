"""
Learn about range() collection
"""


def main():
    """
    test function
    :return: nothing
    """
    # Default
    for i in range(5):
        print(i)

    # To set the initial value: =5 to <10
    print("Now set the initial value")
    for i in range(5, 10):
        print(i)

    # Create a list from range
    l = list(range(5, 10))
    print(l, type(l))
    l2 = list(range(5, 10)) + list(range(30, 40))
    print(l2, type(l2))
    # Utilize the step argument (optional parameter): (begin, stop (not inclusive), step)
    l3 = list(range(0,20,2))
    print(l3, type(l3))
    # Iteration over list using index notation
    s = [0, 2, 3, 4, 6]
    for i in range(len(s)):
        print(s[i])
    # Better way
    for v in s:
        print(v)

    # enumerate(): returns an iterable series
    t = [6, 789, 123, 98, 3, 22]
    for p in enumerate(t):
        print(p)

    # Unpack the tuple using the enumerate
    for i,v in enumerate(t):
        print("i = {}, v = {}".format(i,v))





if __name__ == '__main__':
    main()
    exit(0)