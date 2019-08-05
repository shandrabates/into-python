'''
We will use this files to figure out how to define and later call up functions
Learn about functions/definitions
Use the keyword: def <name>():

'''


def even_or_odd(number):
    """Find if a number is even or odd.
    :param number: input number
    print "even" on even numbers
          "odd" on odd numbers
    """
    if number % 2 ==0:
        print('even')
    else:
        print('odd')


#Call function
print(__name__)
even_or_odd(89)
even_or_odd(72)