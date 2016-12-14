def suffix_prefix(a, b):
	if (len(a) < len(b)):
		smallString = a
	else:
		smallString = b
	newList = []
	for i in range(0 , len(smallString)):
		if (b[i] == a[i]):
			newList.append(a[i])
	return newList
	
def longest_common_subsequence(a, b):

	testList = []
	returnList = []
	for i in range(0, len(a)):
	
		for x in range(0, len(b)):
		
			variable = suffix_prefix(a[i:], b[x:]) 

			if (len(variable) > len(testList)):
			
				testList = variable
				returnList = variable
				
	return returnList 