from twitter_util import*

def cleanText(read):
	lower = read.lower()
	textFile = lower.split()	
	punc = (['!', '@', ')', '(', '.', "'", '"', ',', '.', ':', '-', '"', ';','/'])
	for i in range(0,len(textFile)):	
		for x in punc:  		
			if (textFile[i].startswith(x)): 
				a = textFile[i].strip(x) 
				print (textFile[i])
				print (a)
				textFile[i] = a				
			if(textFile[i].endswith(x)):
				b = textFile[i].strip(x)
				textFile[i] = b										
	return textFile

def standard_punc_list():
	return ['!', '@', ')', '(', '.', "'", '"', ',', '.', ':', '-', '"', ';','/','\n']

def get_words(text, punct=standard_punc_list()):
	for p in punct:
		text = text.replace(p, ' ')
	return filter(lambda x: not(x in ['', ' ']), text.lower().split(' '))
	
def get_sentiment_codes(filename):
	lines = open(filename, 'r').readlines()
	codes = {}
	for line in lines:
		words =line.lower().replace("\t", ' ').replace("\n", ' ').strip().split(' ')
		codes[words[0]] = float(words[len(words)-1])
	return codes
	
def score_sentiment(text, codes):
	words = get_words(text)
	wordCount = 0.0
	scoreSum = 0.0
	for w in words:
		if (codes.has_key(w)):
			wordCount += 1
			scoreSum += codes[w]
	scale_score = 0.0
	if (wordCount>0.0):
		scale_score = scoreSum/wordCount
	return (text, scoreSum, scale_score)