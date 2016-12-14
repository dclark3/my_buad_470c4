# def cleanText(read):
	# textFile = read
	# cleanString = []
	# letters = (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', ' ', '\''])
	# textFile = textFile.replace('.',' ')
	# for i in range(0,len(textFile)):
		# for x in range(0,len(letters)):
			# if (textFile[i] == letters[x]):
				# cleanString.append(textFile[i])
	# cleanFile = ''.join(cleanString)	          
	# return cleanFile.split()

# def cleanText(read):
	# textFile = read.split()
	# letters = (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
	# for i in range(0,len(textFile)):
		# for x in range(0,len(letters)):
			# if (textFile[i] != letters[x]): 
				# textFile[i].append('')			
	# return textFile
	
def cleanText(read):
	textFile = read.split()
	punc = (['!', '@', ')', '.', "'", '"', ',', '.', ':'])
	for i in range(0,len(textFile)):
	
		for x in punc:  
		
			if (textFile[i].startswith(x)): #this part returns true
				a = textFile[i].strip(x)  #this just strips it doesnt save
				print (textFile[i])
				print (a)
				textFile[i] = a
				
			if(textFile[i].endswith(x)):
				b = textFile[i].strip(x)
				textFile[i] = b
										
	return textFile   #only issue i see here is what if ther are multiple bad characters at the beginning
		