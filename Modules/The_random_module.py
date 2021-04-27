#program to use random() and randrange() function from random module
from random import random,randrange,seed

#The random() function return pseudorandom floating-point number x in the range 0<=x<1.
print("The random number generated is: ",random())

#The randrange() function return a pseudorandom integer value within a specified range.
print("The random number generated using randrange() function are: ")

for i in range(0,101):
    print(randrange(0,10),end=' ')

#program to use random(),seed(),and randrange() functions from random module
#from random import random,randeange,seed

#The seed() function sets the random number seed.
seed(222)

#The random() function returns pseudorandom floating-point number x in the range 0 <=x<1.
print("The random number generated is: ",random())

#The randrange() function returns a pseudorandom integer value within a specified range.
print("The random numbers generated using randrange() function are: ")
for i in range(0,100):
    print(randrange(1,1000),end=' ')
