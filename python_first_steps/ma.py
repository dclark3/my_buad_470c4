
def avg(list):
	Avg = (sum(list)) / (float(len(list))) # not sure how to use float 
	return Avg
	
# def ma(list, index):
	# length = len(list[index:len(list)])
	# average = ((sum(list[index:length])) / float(len(list[index:length])))
	# return average
	
# def movingAverage(list, n):
	# x = []
	# for i in range(0, len(list)):
		# x.append((list[i-n]))
	# return x 
	
# def movingAverage1(list ,index):
	# x = []
	# indexList = list[index:len(list)]
	# n = len(indexList)
	# for i in range(0, len(indexList)):
		# x.append((indexList[i-n]))
	# print (avg(x))
	# return x 

	# ([6,2,5,13,9,6,7]) 3, 2))  #i am looking for 
	#['None', 'None', 'None',  
	
def nbackAverage (list,index, nPeriods): 
	backAverageList = len(list[:nPeriods +1]) * ['None']	#creates list 
	for i in range(0, len(list[index:]) + (nPeriods-1)):  #this should be the len of the list starting after the nones
		backAverageList.append(avg(list[(index-nPeriods):index])) 
		index = index + 1
	return backAverageList
	
def movingAverage (list, nPeriods): 
	backAverageList = nPeriods * ['None']	 
	for index in range(nPeriods, len(list)):  
		backAverageList.append(avg(list[(index-nPeriods):index])) 
	return backAverageList	
	
	#return avg(list[(i-n):i]) <- #this gives the average for a single point

def triangleSide (side):
	for i in range (0, side): 
		print(('*') * (i+1))
	return ("^ triangle side ^")	
	
def triangleHeight (height):
	for i in range(0,height):
		print ('*' * (i + 1))
	for z in range(height, -1, -1):
		print ('*' * (z + 1))
	return("^ triangle height ^")
	
def numDivisors(num): 
	counter = 0
	for i in range(2, (num/2)):  
		divisors = num / float(i)
		intTester = int(divisors)
		if (intTester == divisors):
			counter = counter + 1
	return counter	