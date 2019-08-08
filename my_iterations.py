"""
When working with iterations, generators, etc
Look at the documentation for the itertools module

"""

from itertools import islice, count

from list_comps import is_prime

from statistics import mean

from itertools import chain


def main():
    """
    test function
    :return: nothing
    """
    ten_thousand_primes = islice((x for x in count() if is_prime(x)), 10000)
    print(ten_thousand_primes, type(ten_thousand_primes))
    # This is useful to do the operation quickly, depending on how many operations you want to do
    # print('List of first 10k prime numbers:', list(ten_thousand_primes))
    # Note: If you need to use the object again, you need to re-generate it
    ten_thousand_primes = islice((x for x in count() if is_prime(x)), 10000)
    print('Sum of first 100k prime numbers:', sum(ten_thousand_primes))
    # Other built-ins use with itertools: any, all
    print(any([False, False, True]))  # Or -> are any of these the same?
    print(all([False, False, True]))  # And - > are all of these the same?
    # Are there any prime numbers in the range 1328 to 1361
    print('There are prime numbers between 1328 and 1361?', any(x for x in range(1328, 1362) if is_prime(x)))
    # Another method
    print(any(is_prime(x) for x in range(1328, 1362)))
    print(list(x for x in range(1328, 1362) if is_prime(x)))
    # Check to see if all names in an iterable are in title form: First letter capitalized
    names = ['London', 'New York', 'OgDen']
    print(all(name == name.title for name in names))
    # Another built-in: zip()
    sunday = [2, 2, 5, 7, 9, 10, 9, 6, 4, 4]
    monday = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9, 8, 8]   # if you add extra values, it will ignore the extra data
    tuesday = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12]
    # wednesday = [12, 12]  # if you have incomplete data, it will limit calculations on all data
    # Calculate the minimum, maximum, and average of all points
    # See the formatting stuff below to know how to format the print
    for temps in zip(sunday, monday, tuesday):
        print('maximum ={:5.1f}, average ={:4.1f}, minimum ={:6.1f}'.format(max(temps), mean(temps), min(temps)))

    # Chain




if __name__ == '__main__':
    main()
    exit(0)