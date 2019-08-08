"""
Generator Objects are a cross between comprehensions and generator functions
Syntax: Similar to list comprehension:
    (expr(item) for item in iterable)                but use () not []

A lot of built-ins can be used on any collection: sum(), min(), max(), sort()
"""

from list_comps import is_prime

def main():
    """
    test function
    :return: nothing
    """
    # list with first 1 million square numbers
    m_sq = (x*x for x in range(1, 1000001))
    print(m_sq, type(m_sq))
    print('The sum of the first 1M square numbers is:', sum(m_sq))
    print('The sum of the first 1M square numbers is:', sum(x*x for x in range(1, 1000001)))
    # Calculate the sum of the prime numbers between 1 to 10K
    prime_sum = sum(x for x in range(1,10001) if is_prime(x))
    print('The sum of prime numbers from 1 to 10k is:', prime_sum)



if __name__ == '__main__':
    main()
    exit(0)