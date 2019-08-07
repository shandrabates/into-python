"""
Learn about sets
An unordered collection of unique, immutable objects
Define it using { }
You can use the set() constructor
"""



def main():
    """
    test function
    :return: nothing
    """
    p = {6, 78, 21, 45}
    print(p, type(p))
    data = [1, 3, 5, 2, 88, 3, 1]
    print(data, type(data))
    # Eliminate the duplicates
    sdata = set(data)
    print(sdata, type(sdata))
    # Iterate with for
    for item in sdata:
        print(item)
    # Supports membership testing: in, not in
    print(5 in sdata)
    print(5 not in sdata)
    # Adding elements to sets:
    sdata.add(45)
    print(sdata)
    sdata.update([2, 99, 44, 33, 1, 2, 88])
    print(sdata)
    # Removing elements
    sdata.remove(44)
    print(sdata)
    #  sdata.remove(77)      trying to remove an element that doesn't exist generates a KeyError
    # discard() method: does not raise any Error
    sdata.discard(77)
    print(sdata)
    # Copying sets
    bk_data = sdata.copy()
    print(bk_data is sdata)
    print(bk_data == sdata)
    ##########0##  Define some sets
    blue_eyes = {"Olivia", "Harry", "Jack"}
    blond_hare = {"Amelia", "Harry", "Joshua", "Jack", "Nick"}
    smell_hcn = {"Harry", "Amelia"}
    taste_ptc = {"Harry", "Lily", "Amelia", "Leila"}
    o_blood = {"Mia", "Joshua", "Lily", "Olivia"}
    b_blood = {"Amelia", "Jack"}
    a_blood = {"Harry"}
    ab_blood = {"Leila", "Joshua"}
    print(blue_eyes.intersection(taste_ptc))
    print(blue_eyes.union(blond_hare))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blond_hare.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))


if __name__ == '__main__':
    main()
    exit(0)