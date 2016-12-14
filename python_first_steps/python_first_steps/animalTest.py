from animals import *

#test basic functions

#Construct new animals instances
a1 = Animal(name = 'Daniel', weight = 170, age = 21, location = (0,0))

a2 = Animal(name = 'Chris', weight = 145, age = 30, location = (0,0))

#Print basic info
a1.print_info()
a2.print_info()

print('a1 eating 5 units')
a1.eat(5)
a1.print_info()

print('a1 moving (5,5)')
a1.move((5, 5))
a1.print_info()

a3 = LandAnimal(name = 'A3', orientation = (2,3), location = (0,0))
a3.print_info()
print("a3 walks 5")
a3.walk(5)
a3.print_info() 