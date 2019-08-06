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
    # Omitting the index
    print("The best nubmers are {} and {}".format(4, 22))
    # By field name
    print("Current position {latitude} {longitude}".format(latitude="60 N", longitude="5 E"))
    # Print elements of list
    print("Galatic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(85.6, 23.2, 99.0)))
    # Second version of "format" print(f"{variables}")  This method supported in Python 3.7
    # fname = "Waldo"
    # lname = "Weber"
    # print(f"The WSU mascot is {fname} {lname}")


if __name__ == '__main__':
    main()
    exit(0)