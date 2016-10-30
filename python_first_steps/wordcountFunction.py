from textFunction import *
#version 1 -works but count makes it slow
# def word_count(text, case = False):   #right now the fucntion is case sensitive 
	# clean = cleanText(text)   #use the function i have already created to clean out the punctuation
	# if (case):
		# text = text.lower()
		
	# textSplit = text.split()
	# newDict = dict()
	
	# for i in textSplit:    #i takes on the letter of each word
		
		# newDict.update({i : textSplit.count(i)})
			
	# return newDict
	
#version 2 - works
def word_count(text, case = False): 

	if (case):
		text = text.lower()
		
	clean = cleanText(text)   
	newDict = dict()
	
	for i in clean:
		
		if newDict.has_key(i):
			newDict[i] += 1
		else: 
			newDict[i] = 1
		
		#newDict[i] = newDict.get(i, 0) + 1 #this is the shortest way
				
	return newDict
	
	
# def suffix_prefix(a, b):
	# suffix = []
	# if (len(a) < len(b)):
		# smallString = a
	# else:
		# smallString = b
	# if (smallString == a):
		# otherString = b
	# else:
		# otherString = a
		
	# for i in smallString:
		# if(i in otherString):
			# suffix.append(i)
		
	# return suffix

def suffix_prefix(a, b):  #version 2 works
	if (len(a) < len(b)):
		smallString = a
	else:
		smallString = b
	newList = []
	for i in range(0 , len(smallString)):
		if (b[i] == a[i]):
			newList.append(a[i])
	return newList
	
def longest_common_subsequence(a, b):  #version 3 works

	testList = []
	returnList = []
	for i in range(0, len(a)):
	
		for x in range(0, len(b)):
		
			variable = suffix_prefix(a[i:], b[x:]) 

			if (len(variable) > len(testList)):
			
				testList = variable
				returnList = variable
				
	return returnList 
	


		
	
	
	
	
	
	
	
	
# def longest_common_subsequence(a, b):
	# list = []

	# for i in b:  # b = "pqwxy cde abx"
		
		# if(i in a):  #a = "ab cde f"
			
			# if (a[a.index(i)+1] == b[b.index(i)+1]): 
			
			# #print a[a.index(i)]
			
			# #if(i == a[a.index(i)-1]):    #if i can get this loop to go through once before it starts checking it should work

				# list.append(i)
				
	# return list  #ties to return c d e a b
	
	
	# # list = []
	# # for i in b:
		# # #print i
		# # for x in range (0, len(b)):
			# # #print x
			# # #print a
			# # if(i in a):
				# # list.append(i)
	# # return list
			
		