"""
Learn about generator functions:
- Describe iterable series with code functions
- Are lazy evaluated: the next value in the sequence is computed on demand
- Can model infinite series/sequences: data streams, mathematical series with no end
- Can use pipelines

Use the yield keyword
"""


def gen123():
    """
    Generate the integers 1, 2, and 3
    :return: 1, 2, or 3 depending on the previous yield point
    """
    # Do operations in between yields...
    yield 1
    yield 2
    yield 3

def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")


def main():
    """
    test function
    :return: nothing
    """
    g = gen123()
    print(g, type(g))
    # yield next value
    print(next(g))
    # Iterate over the generator function
    for v in gen123():
        print(v)



if __name__ == '__main__':
    main()
    exit(0)