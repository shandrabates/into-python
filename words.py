'''
Get a file from the web:
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt

Task #1: Count the number of words in the document
'''

from urllib.request import urlopen
from functions import even_or_odd

file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

n = 0

with urlopen(filename) as story:
    for line in story:
        lists = line.decode('utf-8').split() #must decode into strings and then separate with spaces
        #print(lists)
        for list in lists:
            n += 1

print("total number of words", n)

count = 0
data ={}
with urlopen(file) as story:
    for line in story:
        lists = line.decode('utf-8').split() #must decode into strings and then separate with spaces
        # print lists
        #print(lists)
        for list in lists:
            #check to see if key is already in the dictionary (data)
            if list in data:
                data[list] +=1
            #if not, assign a new key
            else:
                data[list] =1
            count += 1


# print("Total data", data)
# Sort by key values
for key in sorted(data.keys()):
    print(key, data[key])


print('Even or Odd word count')
even_or_odd(count)
