"""
Learn about collections: Tuples, Strings, Range, List

Also do join method to combine large strings
"""


def main():
    """
    test function
    :return: nothing
    """
    s1 = "This is super cool"
    print("size of s1", len(s1))
    # Concatenation "+"
    s2 = "Weber" + "State" + "University"
    print(s2)
    # Test out join() method instead of + operator
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = " : ".join(teams)
    print(record)
    record = "\n".join(teams)
    print(record)
    # Now use the split operator -> creating a list
    print(record.split("\n"))
    # Partitioning Strings  - > you can use underscore as a dummy variable to pull out the separator
    departure, _, arrival = "London:Edinburgh".partition(":")
    print(departure)
    t = "London:Edinburgh".partition(":")  # you can also turn this into a tuple with partition
    print(t, type(t))
    # string formatting using format()
    print("The age of {0} is {1}".format("Mario", 34))
    print("The age of {0} is {1}, and the birthday of {0} is {2}".format("Mario", 34, "August 6th"))

if __name__ == '__main__':
    main()
    exit(0)