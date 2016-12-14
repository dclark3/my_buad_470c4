
#would need to add an if statement if nums % 3 was 0 because than we would have 
# three random numbers on the back

# def sum_thirds(nums): #this function would take list1 instead of nums
	# sums = []
	# for i in range(0,len(nums), 3):
		# sums.append(sum(nums[i:(i+3)])) #look at i + 3
	# return sums
		

		
#def sum_thirds(nums): #this function would take list1 instead of nums
	#sums = []
	#for i in range(0,len(nums), 3):
		#sums.append(sum(nums[i:min((i+3), len(nums))])) #look at i + 3
	#return sums

def sum_by_n(nums, n):
	sums = []
	for i in range(0, len(nums) , n):
		sums.append(sum(nums[i:min((i+n), len(nums))]))
	return sums

	
		