'''
Other languages discuss hashes, while Python utilizes dictionaries to house matrices
Dictionaries map keys to values.

In some languages are known as arrays, or hashes, or maps

Create them using { } containing a key-value pair.
Retrieve them by [key_value]
'''

d = {'alice':'801-123-45-8988',
     'pedro': '956-445-78-8966',
     'john':'651-321-66-4477'}
print(d, type(d))
# Access one element
print(d['alice'])
# Use command to return a line of the data
print(d.popitem())

# Add members to the dictionary, of names -> grades
roster ={}   #Empty dictionary

n = 0
# Input student names and grades
while n<3:
    # Get key value
    name = input('Enter a name')
    # Get value associated to key
    grade = input("Enter a grade")
    # Add element to dictionary.
    # Note: If key value exists, it will update the value otherwise it will be added to the dictionary
    roster[name] = grade
    n = n+1
#Print dictionary
print(roster)








