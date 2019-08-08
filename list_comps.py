"""
List Comprehensions
Readable, expressive, and effective.
"""

from math import factorial as fact
from pprint import pprint as pp
from math import sqrt



def is_prime(num):
    """
    Test to see if a number is prime
    :param num: Determine if a number is prime
    :return: True for prime numbers or False for none-prime numbers
    """
    if num < 2:
        return False
    for i in range(2, int(sqrt(num))+ 1):
        if num % i == 0:
            return False

    return True


def main():
    """
    test function
    :return: nothing
    """
    words = "Today I am very happy to learn about list comprehensions in Python".split()
    print(words)
    data = []    # empty list
    for word in words:
        # Some analysis ...
        data.append(word)

    # "Filter" data
    print(data)

    # task find the length of the first 20 factorial numbers
    array = []  # empty list
    for x in range(20):
        # print(fact(x))
        value = (len(str(fact(x))))
        array.append(value)
    print(array, type(array))

    # now use a comprehension instead
    # use a list comprehension: []
    info = [len(str(fact(x))) for x in range(20)]
    print(info, type(info))

    # Set Comprehensions: {}       => Eliminated duplicates
    info3 = {len(str(fact(x))) for x in range(200)}
    print(info3, type(info3))
    pp(info3)

    # Dictionary Comprehensions
    nba_teams = {'jazz':'SLC', 'warriors':'San Francisco', 'lakers':'LA', 'clippers':'LA'}
    pp(nba_teams)
    teams_nba = {city: mascot for mascot, city in nba_teams.items()}
    pp(teams_nba)

    # Filter predicates
    # Create a function to determine if a number is prime
    print(is_prime(3))

    # Check a large range of numbers to determine amount of prime numbers
    prime_list = [x for x in range(1,10001) if is_prime(x)]
    print(prime_list)
    print(len(prime_list), prime_list)



if __name__ == '__main__':
    main()
    exit(0)
