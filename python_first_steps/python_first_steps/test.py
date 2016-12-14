#this is a test for first_mod module

#from first_mod import *
from program import *
from functionalPrograms import *

#print("sum of 3, 5, and 7: " + str(add3(3,5,7))) #first test
#say_hello('Daniel') #test second function

#print (add_nums(3,5))
#print('----')
#print(add_nums(3,5,7))
#print('---------')
#print(add_nums(2,3,4,5,6,7,8))
#print('---------------')
#extras = [e54,5,6,7,8,9]
#print(add_nums(2,3, *extras))
#print(add_nums(*extras))

#print (sum_thirds([1,1,1,2,2,2,3,3,3]))
#print (sum_thirds1([1,1,1,2,2,2,3,3,3]))
#print (sum_thirds2([1,1,1,2,2,2,3,3,3]))
#print (sum_thirds3([1,1,1,2,2,2,3,3,3]))
#print (sum_thirds4([1,1,1,2,2,2,3,3,3]))

a = [1,2,3]
b = [4,5,6]
function = lambda x: x + 1
print(fZip(function, a,b))