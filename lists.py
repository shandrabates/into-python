'''
Learn about lists
Unlike strings, lists are mutable
You can update, and append elements to it
'''
# use [] to define a list
l = [1, 2, 3]
print('List', l, type(l))
# A list of objects (any type of objects)
a = ['apple', 'orange', 'pear']
# Access by index notation
print(a, a[1])
# Replace an element
a[0]= 'tomato'
print(a, a[1])
a[1] = 3.14
print(a, a[1])


# Begin with an empty list
names = []
# Ask a user to enter 3 names, and add them to the list
n = 0
while n <= 2:
    name = input('Enter a name')
    names.append(name)
    print(name)
    n = n +1
print(names)




