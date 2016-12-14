
#orthoginal
#reminder this file is a module
#simpel function that adds 3 numbers 
#def add3 (a, b, c):
	#return a + b + c
	
# Print a greeting
#def say_hello(person):
	#print("hello " + str(person))	
	#print ('A': " + str(a))
	#print('B': " +str(b))
	#print('rest': ' + str(rest))	
	
#def add_nums (a, b, *rest):
#This is the manual way
	# sum = a + b 
	# for v in rest:
		# sum += v	
	# return sum
	#return a + b + sum(list(rest))
	
#def sum_thirds(nums):
	# write a function that sums up every 3 consecutive number in nums
	# and puts them intoi a new list. This new list is returned
	# example sum_thirds([1,1,1,2,2,2,3,3,3])= ([3,6,9)]
	
	#sum_nums = sum(nums[:3])
	#return sum_nums
	
	#for i in length(nums)
		#sum = sum + i[:3]
	
    	
	#print(nums)	
		
	#for i in(nums):
		#for j in range(3):
		    #sums = list()
			#sums = 0
			#sums = sums + nums[j]	
			# nums[1] + nums[2] + nums[3]
			#print sums
	    #return sums
	 
    #for i in nums:
		#sum += i
	#return sum
	
# def sum_thirds2(nums2):
	# print(nums2)
	# sum = 0
	# for i in nums2:
		# sum = sum(nums2[:3])
		# print sum
	# return sum
	
# def sum_thirds4(nums4):
	
	# sum1 =sum(nums4[:3])
	# sum2 = sum(nums4[3:6])
	# sum3 = sum(nums4[6:])
	# print sum1
	# print sum2
	# print sum3
	# return ([sum1, sum2, sum3])
	
	
# def sum_thirds3(nums3):
	# print(nums3)
	# while nums3 == 1:
		# sum = sum(nums3 [:3])
	# else:
		# sums = sums(nums3 [4:6])
	# print sum + sums

# def sum_thirds(nums):
	# sums = 0
	# i = 0
	# for i in range(0,len(nums), 3):
		# return sums.append(sums(nums[i:(i+3)]
		
	
		
# def sum_thirds1(nums1):
	# print(nums1)
	# sums = 0
	# allsums = 0
	# for i in nums1:
		# for j in range (3):
			# sums = sums + i
			# allsums[i] = sums
		# return allsums
		
    
	#while (nums = nums[:3]):
		#print(sum(nums))
	#else:
		#print("test")
	 
	#sum = 0
	#for i in nums[:3]:
		#sum = sum+1
	#return sum
	
		
	
	#sum_nums1 = nums[::3]
	#return sum_nums1
	
# compute the sum of all integers from a to b inclusive, doing so with recursion
def	srr(a, b):
	if a==b:
		return a
	return srr(a, b-1) + b 
	
def rRev(list):
	if len(list) == 0:
		return list
	return [list[-1]] + rRev(list[:-1])
	
def fac(n): #works
	if n==1:
		return n
	return n * fac(n-1)
	
def fib1(first, second, n): #both fibs work 11/06/2016
	if n == 1:
		return first
	if n == 2:
		return second
	return fib1(second, first+second, n-1)
	
def fib(first, second, n): #works 11/09/2016
	if n == 1:
		return first
	if n == 2:
		return second
	return fib(first, second, n-2) + fib(first, second, n-1)

#dynamic programming to solve the same problem 	
def dFib(first, second, n, h = {}): 
	if n == 1:
		return first
	if n == 2:
		return second
	if h.has_key(n):
		return h[n]
	h[n] = dFib(first, second, n-2) + dFib(first, second, n-1)
	return h[n]

def cart_loop3list(a, b, c): 
	list = []
	for i in a:
		for j in b:
			for l in c:
				list.append(i)
				list.append(j)
				list.append(l)
	return list
	
#get the cartesian product of any number of sets
def cart_prod(*sets):
	if sets == []:
		return []
	if len(sets) == 1:
		return map(lambda x: [x], sets[0])
	else:
		rest = cart_prod(*sets[1:])
		prod_list = map(lambda x: map(lambda y: [x] + y, rest),sets[0])
		return reduce(lambda x,y: x + y, prod_list)

def all_perms(n):  
	if len(n) == 1:
		return [n]
	result = []		
	for i in range(0, len(n)): 
		rest = list(n) 
		front = rest.pop(i)		
		rest_perms = all_perms(rest)
			
		result += map(lambda x: [front] + x, rest_perms)
	return result
	
			
def hannoi(A, B, C, n):
	if n == 1:
		print("move top disk from  " + str(A) + " to " + str(C)) 
	else:
		hannoi(A, C, B, n-1)
		hannoi(A, B, C, 1)
		hannoi(B, A, C, n-1)
			
def encode(word):
	newDict = dict()
	for w in word:
		if (newDict.has_key(w)):
			newDict[w] += 1
		else:
			newDict[w] = 1
	return newDict


def find_anagrams(word, word_list):
		anagram = [] 
		for w in word_list:
			if (encode(word) == encode(w)):
				anagram.append(w)
		return anagram
		

		
	
	
	


	
	
	
	
	
		