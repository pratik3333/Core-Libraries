#program to use random() and randrange() function from random module
from random import random,randrange

#The random() function return pseudorandom floating-point number x in the range 0<=x<1.
print("The random number generated is: ",random())

#The randrange() function return a pseudorandom integer value within a specified range.
print("The random number generated using randrange() function are: ")

for i in range(0,101):
    print(randrange(0,10),end=' ')


