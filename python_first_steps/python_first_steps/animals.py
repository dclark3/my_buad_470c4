import math
class Animal:

	def __init__(self, weight = 0.0, avg_lifespan = 0.0, age = 0.0, location = (0,0), name='Animal'):
		self.name = name
		self.weight = weight
		self.avg_lifespan = avg_lifespan
		self.age = age
		self.location = location
	
	def print_info(self): #good for debugging
		print('name' + str(self.name))
		print('weight: ' + str(self.weight))
		print('average life span: ' + str(self.avg_lifespan))
		print('age: ' + str(self.age))
		print('location: ' + str(self.location))
		print("\n")
		
	def eat(self, food_units):
		self.weight += food_units
		
	def move(self, new_location):
		self.location = new_location
	
class LandAnimal(Animal): #to make subclass of animal
	
	def __init__(self, name='Animal' , weight = 0.0, avg_lifespan = 0.0, age = 0.0, location = (0,0), num_legs = 4, orientation=(0,0)):
		self.name = name
		self.weight = weight
		self.avg_lifespan = avg_lifespan
		self.age = age
		self.location = location
		self.num_legs = num_legs
		self.orientation = orientation
	
	def walk(self, dist): #needs to move 5 by orientaion 2,3
		x, y = self.location
		xd, yd = self.orientation
		d = math.sqrt((xd**2) + (yd**2))
		scale_factor = dist / d
		self.move((x + xd * scale_factor,y + yd * scale_factor))
			
			
			

			
				
			
		
		#if (xd<=dist):                     #this only works if its perfect
			#xd = xd
		#if (yd <= (dist-xd)):
			#yd = yd
		#self.move((x + xd, y + yd))

		
				
				
				
		
	#TODO implement so new location changes by distance based on orientaion 
	#orientation (2, 3)
	#move 2 in x 3 in y
	
	