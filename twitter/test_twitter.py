from twitter_util import *
from sentiment_analysis import *
from random import *

texts = read_texts('tweets/t1.txt')  #this is where to read in whatever tweets i select dont by python stream_reader -access secret_account -track ....words....
print('-- testing tweet reading-----')

n= 65
for t in texts[:n]:
	print(t)
	
print('\n-- testing code parsing-----')	

codepath = '../util-data-files/AFINN-111.txt'
codes = get_sentiment_codes(codepath)
for (code, val) in codes.items()[:20]:
	print(code, val)
	
print('\n-- testing word splitting-----')	

for t in texts[:20]:
	print(get_words(t))
	
print('\n-- testing sentiment analysis-----')
n = 100
sp = sample(texts, n)	
for t in sp:
	print(score_sentiment(t, codes))