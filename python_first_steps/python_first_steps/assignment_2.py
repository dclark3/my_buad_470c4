def powerSet(n):
	if n== []:
		return []
	result =[[]]
	number = []
	for x in n:
		print x
		
		for y in result:
			print y
			
			#number.append(y + x)
			number.append([x])
			number.append([y])
		result += number
	return result

# def flatten(list):
	# x = []
	# for i in list:
		# print i
		# #if i #is a list:  type(list)  make subproblem structure			
		# else:
			# x.append(i)		
	# return x
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

def standard_punc_list():
	return ['!', '@', ')', '(', '.', "'", '"', ',', '.', ':', '-', '"', ';','/']
	
def get_words(text, punct=standard_punc_list()):
	for p in punct:
		text = text.replace(p, ' ')
	return filter(lambda x: not(x in ['', ' ']), text.lower().split(' '))
	
def infer_word_sentiments(code, text):
	h = {}
	for t in text:	
		s = score_sentiment(t, code)[2]
		words = get_words(t)
		for w in words:
			if not(code.has_key(w)):
				if not(h.has_key(w)):
					h[w]=(0,0)
					hs, hc = h[w]
					h[w] = (hs+s, hc+1)					
	return map(lambda x,y: x/y, h)
	
#def infer_tweet_word_sentiments(codes, tweets):
#just need to get the tweets as text and then call it on infer_word_sentiment


# def top_n_words(sentiment_score_dict, n, direction =1):
	# #got to use sort somehow
	# if (direction)==1:
		
	# else if (direction==0)//:
		# stuff
	# else:
		# print 'Please enter either 1 or 0'