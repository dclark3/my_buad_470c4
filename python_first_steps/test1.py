#from program import *
#from zerogen import *
#from doubleloop import *
#this puts in 2 lists and gets one back
#zeros =(zeroN([1,1,1,2,2,2,3,3,3,4]))  # this gives a list of zeros that is n + 3 long
#print zeros
#zeros1 =( doubleloop(([1,1,1,2,2,2,3,3,3,4]),zeros)) 
#print zeros1
#print (sum_thirds(zeros1)) #this inputs the new list divisible by 3
#print (sum_thirds([1,1,1,2,2,2,3,3,3,4,0,0]))
#print (sum_thirds([1,1,1,2,2,2,3,3,3,4,0,0])) #this is an example of what list1
#would contain
# print (sum_by_n(([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]), 5))
# print (sum_by_n(([1,1,2,2,3,3]), 2))
# print (sum_by_n(([1,1,1,1,2,3]), 4))
# print (sum_by_n(([1,1,1,1,1,1,1,1]),100))
# print(sum_by_n(([100, 5.08, 1, 2, 9, 12.5, 16.6]), 3)) #no doubles for n
# print(sum_by_n(([-1, -3, -2, 5, -6, 1, 2, 3, -9, 1, -1, 1]), 2))

from ma import * 

dataset = ([6,2,5,13,9,6,7])

print (avg(dataset))
# print (ma(dataset, 2))
# print (movingAverage(dataset, 2))
# print (movingAverage1(dataset, 2))
# #print (ma1(dataset, 3))

print (nbackAverage(dataset, 3, 2))
print (movingAverage(dataset, 2))

print (triangleSide(4))
print (triangleHeight(4))

print (numDivisors(13))

from textFunction import * 

file = open('textExample.txt', 'r')
read = (file.read())
print (cleanText(read))
