#this is a test for first_mod module

from first_mod import *

#print("sum of 3, 5, and 7: " + str(add3(3,5,7))) #first test
#say_hello('Daniel') #test second function

print (add_nums(3,5))
print('----')
print(add_nums(3,5,7))
print('---------')
print(add_nums(2,3,4,5,6,7,8))
print('---------------')
extras = [4,5,6,7,8,9]
print(add_nums(2,3, *extras))
print(add_nums(*extras))
