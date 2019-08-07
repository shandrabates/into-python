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
    print(a, type(a))
    print("a[0][1]:", a[0][1])
    # Copy the list of lists
    b = a[:]
    print("b is a:", b is a)
    print("a[0]:", a[0])
    print("b[0]:", b[0])
    print("a[0] is b[0]:", a[0] is b[0])
    # Now lets change one element
    a[0] = [8, 9]
    print("Change a[0] to [8,9]")
    print("a[0]:", a[0])
    print("b[0]:", b[0])
    print("a[0] is b[0]:", a[0] is b[0])
    print("a[1] is b[1]:", a[1] is b[1])
    # Modify a[1]
    a[1].append(5)
    print("a[1]:", a[1])
    print("b[1]:", b[1])
    print("a[1] is b[1]:", a[1] is b[1])
    print("a:", a)
    print("b:", b)
    # Repetition
    c = [21, 37]
    d = c * 4
    print("c", c)
    print("d", d)
    # All point to the same object
    s = [[-1, 1]] * 5
    print("s:", s)
    s[1].append(7)
    print("s:", s)
    # index()
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print("the index of 'fox' entry is:", i, w[i])
    # If no index is found it will produce a ValueError
    # j = w.index('cat')
    # print("j is equal to", j)

    # Membership testing with: count()
    print("'the' value is ", w.count('the'))





if __name__ == '__main__':
    main()
    exit(0)