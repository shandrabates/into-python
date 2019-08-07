"""
Learn more about lists
"""


def main():
    """
    test function
    :return: nothing
    """
    s = "show how to do it".split()
    print(s, type(s))
    # Access by index
    print("s[3]", s[3])
    print("Last member:", s[len(s)-1])  #Very unpythonic
    # Use negative index instead
    print("s[-1]:", s[-1])
    # Slicing
    print("From 1 to one before the last member", s[1:-1])
    print("From 1 to three member", s[1:3])
    # how to call from a position to the end or beginning to a position
    print("From 1 to the end", s[1:])
    print("From beginning to three member", s[:3])
    # doing this, we can make a new list that is a separate object from s
    print("From beginning to end", s[:])
    # Make a copy of s   -> shallow copy
    t = s
    print("s:", s)
    print("t:", t)
    print("t is s", t is s)
    # Make t a new object with the values of s   -> deep copy
    t = s[:]
    # You can also use( t = s.copy() ) or ( t = list(s) )
    print("t is s", t is s)
    print("t == s:", t == s)
    # Shallow copies
    # A list of lists
    a = [[1, 2], [3,4]]
    print(a)





if __name__ == '__main__':
    main()
    exit(0)