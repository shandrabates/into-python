'''
Practice for loops
Keyword: for
'''

cities = ['London', 'New York', 'Madrid', 'Paris', 'Salt Lake City', 'Bangkok', 'Tokyo']
# Iterate over this list
for city in cities:
    print(city)


d = {'alice':'801-123-45-8988',
     'pedro': '956-445-78-8966',
     'john':'651-321-66-4477'}
# Iterate over this dictionary
for item in d:
    print(item)  # Prints just the key
    print(item, "=>", d[item]) # Prints the key with the data associated with that key


