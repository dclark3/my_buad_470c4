#define a one line mymax - finds the max element of a list in one line
#2 fzip, take in lists apply each elemement then put into tuple 

# example of applying a function
# def applyFunction(f, val):
	# return f(val)

def fZip(f, a, *rest):
	function = f
	#print function
	#print [a]
	#print(rest)
	lst = [a] + list(rest)
	zipList = zip(*lst) #zipList is a list of tuples
	

	#tuple to list, list to * to be passed to f
	
	#tf = #take in a tuple and applies f to its values, map(tf, zipList)
	#tf = lambda x,y: zipList #y is the tuple  once lambda is made it all works

	print zipList
	
		
	tf = lambda x,y: zipList

	print tf


	return ""

	
	
	
	


	
	
#reduce(lambda x,y: x < y ? y : x, list)

#reduce(lambda x,y: if(x < y) y else x, list)

#myMax = reduce(lambda x,y: y if(x < y) else x, list)

#myMax = reduce(lambda x,y: y if(x < y) else x)       <-why doesnt this work
#myMax = lambda x,y: y if(x < y) else x 
#reduce(myMath(list))