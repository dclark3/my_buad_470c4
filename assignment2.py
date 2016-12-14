from sentiment_analysis import *
from twitter_util import *
#i used these imports because i was calling functions from both of them

#Daniel Clark
#Assignment 2


#------ 1. Flatten ---------------
#function flattens a list using recursion by breaking the lists into 
#sub problems and put it back together
def flatten(lists):  #recursively
	if lists == []:
		return []
	if type(lists[0]) == type([]):
		variable1 = lists[0]
		#print variable1
		variable2 = lists[1:]
		#print variable2
		return flatten(variable1) + flatten(variable2)
	else:
		variable1 = lists[0]
		variable2 = lists[1:]
		return [variable1] + flatten(variable2)

#function flatten2 relies on extend which I found while researching ways
#to use .append.  It works great but I kept it as a secondary option.		
def flatten2(lists):  #kinda recusive
	emptyList = []
	for i in lists:
		if type(i) == type([]):							
			emptyList.extend(flatten2(i))		
		else:
			emptyList.append(i)
	return emptyList
	
#flatten3 was one of my first attempts with loops. Im not actually sure why
#it doesnt work.  The idea behind it was to check if lists was a list or 
#int. If lists was type list break it into individual int elements
#and if lists was type int add it to x, the empty list. 
def flatten3(lists):
	x = []
	if type(lists) != type([]):
		x.append(lists)
	else:
		for i in lists:
			if type(i) == type([]):
				for j in i:
					flatten3(j)
			else:
				x.append(i)
	return x
	
#-------2. Power Set----------------
def powerSet(lists):  #with loops works
	x=[[]]
	for i in lists:
		for j in x:
			x = x + [j + [i]]
	return x
 
def powerSet3(lists): #recursively attempt doesnt work
	if len(lists) == 0:
		return []		
	else:
		return [lists] + powerSet3(lists[1:])


#--------3. Twitter Sentiment Analysis-----------
#brought this over to reverse a list
def rRev(list):
	if len(list) == 0:
		return list
	return [list[-1]] + rRev(list[:-1])


def infer_word_sentiments(code, text):  
	h = {}
	for t in text:
		s = (score_sentiment(t, code)[2])
		words = get_words(t)
		for w in words:
			if not(code.has_key(w)):  
				if not(h.has_key(w)):
					h[w]=(0,0)
					hs, hc = h[w]
					h[w] = (hs+s, hc+1)	
	return map(lambda x,y: x/y, h)
#this last part i cant figure out the value of h is 2 numbers (score, counter)
#to calculate the scaled score.  The map(lambda x,y: x/y, h) is supposed to
#divide the the score/counter in the dictionary and create just one value 
#that is the scaled score	
	
#this function assumes that the input has already been read in
#my tester for this function looked like 
#texts = read_texts('tweets/t1.txt') <read over from twitter_util
#print(infer_tweet_word_sentiments(codes, texts))	
def infer_tweet_word_sentiments(codes, tweets):
	return infer_word_sentiments(codes, tweets)

#this function takes in the tweets
#tester looked like this:
#print(infer_tweet_word_sentiments2(codes, 'tweets/t1.txt'))
def infer_tweet_word_sentiments2(codes, tweets):
	tweet = read_texts(tweets)	
	return infer_word_sentiments(codes, tweet)

#tester for this function:
#texts = read_texts('tweets/t1.txt')
#d = infer_tweet_word_sentiments(codes, texts[:20])
#print(top_n_words(d, 3, direction = 1))
def top_n_words(sentiment_score_dict, n, direction=1):
	if (direction==1):
		z = 0
		lists = []
		v = sorted(sentiment_score_dict.items(), key=lambda x: x[1])
		variable = rRev(v)  
		for i in range (0, n):
			lists.append(variable[z])
			z+=1
		return lists		
	if (direction==0):
		z = 0
		lists = []
		variable = sorted(sentiment_score_dict.items(), key=lambda x: x[1])
		for i in range (0, n):
			lists.append(variable[z])
			z+=1
		return lists
	else:
		return 'Please enter either 1 or 0'
