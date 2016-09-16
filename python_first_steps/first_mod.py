
#orthoginal
#reminder this file is a module
#simpel function that adds 3 numbers 
#def add3 (a, b, c):
	#return a + b + c
	
# Print a greeting
#def say_hello(person):
	#print("hello " + str(person))	
	#print ('A': " + str(a))
	#print('B': " +str(b))
	#print('rest': ' + str(rest))	
	
def add_nums (a, b, *rest):
#This is the manual way
	# sum = a + b 
	# for v in rest:
		# sum += v	
	# return sum
	return a + b + sum(list(rest))
	
