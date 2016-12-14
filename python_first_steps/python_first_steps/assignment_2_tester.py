from assignment_2 import *
print('powerset test---------------------')

#print(powerSet([1,2,3]))
#print(powerSet([1,2,3,4]))


print('flatten test -------------------')
#print(flatten([[1,2,3], [[4],[5]], 6,7,8]))

print('sentiments test --------------------')
def get_sentiment_codes(filename):
	lines = open(filename, 'r').readlines()
	codes = {}
	for line in lines:
		words =line.lower().replace("\t", ' ').replace("\n", ' ').strip().split(' ')
		codes[words[0]] = float(words[len(words)-1])
	return codes

words = open('words_for_sentiment_test.txt', 'r')
codes = get_sentiment_codes('AFINN-111.txt')
print(infer_word_sentiments(words,codes))