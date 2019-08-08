"""
Random class notes



Collections:

tuple - hererogeneous immutable sequence
    delimited by () but accessed by []  t[index]

dict - defined by {} and accessed by [] key

str -  defined by " "   and accessed by [] index

list - delimited/defined by [] and accessed by [] index



range - do operations at a group level - defined by []

set - do operations at a group level - defined by {}
        can do difference, symmetric difference, and issubset


**Suggest using Visual Studio Code for an editor**


A good example of how to do a lazy calculation is to use a generator
Ex: generator_objects => sum(x*x for x in range(1, 1000001))
This is only generating one value at any given time as opposed to building a table of all 1M elements
This methodology is only looking at one element at a time and storing only one element
I.E. this is way way less memory and less computation taxation


You can see how to format the size of your results in my_iterations
Ex: print('maximum ={:5.1f}, average ={:4.1f}, minimum ={:6.1f}'.format(max(temps), mean(temps), min(temps)))
{:6.1f} => six chars width, 1 decimal precision, floating point


To test for membership
'in' and 'not in'


You can comment out sections in Python using CTRL + /


How python looks for variables - Order of Operations
L-local
E-enclosing
G-global
B-built-in

"""