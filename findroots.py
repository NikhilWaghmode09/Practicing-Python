#calc roots of linear equations.
#python program to demonstrate using libraries.

import numpy
d = []
n =int(input("Enter order of equation: "))
for i in range(n+1):
    inp=int(input("Enter coefficient: "))
    d.append(inp)
print("Roots of equation are: ",numpy.roots(d))
