"""
Learn more about dictionaries
"""

from pprint import pprint as pp

def main():
    """
    test function
    :return: nothing
    """
    urls = {
        "google": "www.google.com",
        "yahoo": "wwww.yahoo.com",
        "twitter": "www.twitter.com",
        "wsu": "www.weber.edu"
    }
    print(urls, type(urls))
    # Access by key: [key]
    print(urls["wsu"])
    # Build dict with dict() constructor
    names_age = [('Alice', 32), ('Mario', 23), ('Hugo', 21)]
    d = dict(names_age)  # this will be problematic if you have a key that repeats (ex: Alice)
    print(d)
    # another method
    phonetic = dict(a='alpha', b='bravo', c='charlie', d='delta')
    print(phonetic)
    # make a copy
    e = phonetic.copy()
    print(e)
    # Updating a dictionary: update() method
    stocks = {'GOOG':891, 'APPL':416, 'IBM':194}
    print(stocks)
    stocks.update({'GOOG':999, 'YHOO':2})
    print(stocks)
    # Iteration default is by key value
    for key in stocks:
        print("{k} => {v}".format(k=key, v=stocks[key]))
    # Iterate by values:
    for val in stocks.values():
        print("val = ", val)
    # Iterate by both key and value with: items()
    for stock,value in stocks.items():   # separate/unpack the tuples by defining the two things we are returning
        print(stock," ",value)
    # Testing for membership via key: in and not in
    print('GOOG' in stocks)
    print('WINDOWS' not in stocks)
    #  print(999 in stocks)  - > cannot use this for values, only the keys since values are not unique
    # Deleting: del keywork
    del stocks['YHOO']
    print(stocks)
    # Mutability of dictionaries
    isotopes = {
        'H': [1, 2, 3],
        'He': [3, 4],
        'Li': [6, 7],
        'Be': [7, 9, 10],
        'B': [10, 11],
        'C': [11, 12, 13, 14]
    }
    pp(isotopes)  # use the pretty print built in function to help display one-by-one
    isotopes['H'] += [4, 5, 6, 7]
    print(isotopes)
    isotopes['N'] = [13, 14, 15]
    pp(isotopes)  # commonly you should display more than 80 characters wide in output


if __name__ == '__main__':
    main()
    exit(0)