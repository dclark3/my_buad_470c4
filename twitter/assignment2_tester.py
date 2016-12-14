from assignment2 import *
from sentiment_analysis import *
from twitter_util import *
from random import *


print('\n flatten test -------------------')
#print(flatten([[1,2,3], [[4],[5]], 6,7,8]))
#print(flatten2([[1,2,3], [[4],[5]], 6,7,8]))
#print(flatten3([[1,2,3], [[4],[5]], 6,7,8]))

print('powerset test---------------------')
print(powerSet([1,2,3]))
print(powerSet2([1,2,3]))
print(powerSet3([1,2,3]))
#print(getAllSubsets([1,2,3]))

print('\n sentiments test part 1 --------------------')
#words = open('words.txt', 'r')  #bunch of random word
words = open('text_test.txt', 'r')
codes = get_sentiment_codes('AFINN-111.txt') #codes from code file 
#print codes
#print(infer_word_sentiments(codes, words))


print('\n sentiments test part 2 --------------------')
texts = read_texts('tweets/t1.txt')
#print(infer_tweet_word_sentiments(codes, texts))
#print(infer_tweet_word_sentiments2(codes, 'tweets/t1.txt'))
#print(infer_tweet_word_sentiments(codes, texts[:20]))

print(' \n sentiment test part 3---------------')
m = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
n = {'a':100,'b':2,'c':1000000,'d':50}
l = {'a':1, 'b':3, 'c':0, 'd':-2, 'e':-1}
d = infer_tweet_word_sentiments(codes, texts[:20])
#print(top_n_words(d, 3, direction = 1))


	
