	
#print ( sum_thirds([0,0,0,0,0,0,0,0,0,0,0,0]))   this would be list1
#print (sum_thirds([1,1,1,2,2,2,3,3,3,4]))   this would be nums
# the output of this function would look like this 
# ([1,1,1,2,2,2,3,3,3,4,0,0])


def doubleloop (nums, list1):
	for i in range(0, len(nums)):
		list1[i] = nums[i]
	return list1
	
	
# so here list1 would be 12 0's and nums would be 10 numbers the idea is to
# have the 10 numbers take the place of 10 of the 0's but with 2 still left 
# on the end
	
	
	
