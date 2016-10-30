#define a one line mymax - finds the max element of a list in one line
#2 fzip, take in lists apply each elemement then put into tuple 

# example of applying a function
# def applyFunction(f, val):
	# return f(val)
	
# def fZip(a, b, c):
	# return a+1, b+2, c+3
	
# map(lambda x, max(x), zip(a, b, c))	 #this works but zips and then applies the function

# #myMax = filter(lambda x: max(x), list)	
# myMax = filter(lambda x: x==max(list), list) #this one works the best for #1
# myMax = reduce(lambda x: ,list)

# zip(map(lambda x: x+1, zip(a, b)) #does not work


# map(lambda x, y, z: x+y+z, a,b,c)
# zip(map(lambda x, y, z: x+y+z, a,b,c))

#ifZip(f = lambda x: x+1, a, b, c)
def fZip(f, a, *rest):
	function = f
	print function

	print [a]
	print(rest)
	lst = [a] + list(rest)

	zipList = zip(*lst)  #already take the min of the lists
	#zipList is a list of tuples
	
	print zipList
	print "list" + str(list(zipList[0]))
	#tuple to list, list to * to be passed to f
	
	#needs to apply to every tuple in ziplist each element in the tuple

	#zip list needs to be broken up into the tuples and then into each number in the tuple
	#using * will help but also other ways to do it
	
	tf = #take in a tuple and applies f to its values, map(tf, zipList)
	tf = lambda y: #y is the tuple  once lambda is made it all works
	#need to come up with a way to go through each element in each tuple
	#map(f, (zipList))   #this will give me the function and each tuple 
	
	return ""
	
	
	
	#one way to solve this would be to loop the function through each tuple and then
	#put it into a new list. 
	#for i in range(0,len(zipList)):
		#map(*zipList[i])
		



	
#reduce(lambda x,y: x < y ? y : x, list)

#reduce(lambda x,y: if(x < y) y else x, list)

#myMax = reduce(lambda x,y: y if(x < y) else x, list)

#myMax = reduce(lambda x,y: y if(x < y) else x)       <-why doesnt this work
#myMax = lambda x,y: y if(x < y) else x 
#reduce(myMath(list))