"""
This question gives an array of distinct integers and a targetSum and asks to return a pair of numbers in the array that sum up to the 
targetSum. The question also assures us that there will be at most one pair or no pair summing up to the target sum. The inoptimal 
approach, twoSumIII solution below, is to iterate through the array and choose a first number, then iterate through the array again for 
a second number, sum these up and check if the sum equals the targetSum. Because this solution uses a double for loop, this solution takes 
O(n^2) time and O(1) space. However we can use a hashtable or hashset to improve the time complexity to O(n) time and O(n) space. For this 
optimal solution (at least time complexity wise), iterate through the array, generate the complement of the current number and check if the 
complement of the current number is in a hashset or hashtable. The complement is targetSum - current integer, the addend need to sum with the 
current integer to yeild the targetSum. Since we are told the numbers are distinct and we only need to store distinct values without the need 
for addtional info, the use of a hashset makes more sense. We iterate through the array and add the current integer to the hashset.  But 
before adding the current integer, we calculate its complement and check if its complement is in the array, by checking if its complement has 
previously been added to the hashset.So if the complement of the current integer is in the hashset, we return the current integer and its 
complement. If the current integer's complement is in the array but occurs afterthe current integer, because we add the current integer to the 
hashset, when we get to its complement is in the array, when we get to it in the loop, we will find the current number as it's complement's 
complement, hope that makes sense. Phew!!!. Anyway, there is another solution, which requires that we first sort the array. If the array is 
already sorted, then this becomes the optimal solution because, we don't even need to use additional space for this solution. We can use two 
pointers , a right and left pointer, initialized at 0 and len(array) - 1 and do iterate through the array, and do some constant time operations 
and comparisons. So with l = 0 and r = len(array) - 1, we sum, array[l] + array[r]. If the sum equals the targetSum, we return array[l] and
array[r] as the pair. However if this isnt the case, we can move intelligently through the array based on how the currentSum compares to the
targetSum due to the fact that the distinct integers in the array are sorted in ascending order. If the currentSum < targetSum, the we want to
add a little more to our currentSum so we move the left pointer forward. This is because we know that all the numbers that come after current
array[l] are all greater than array[l] and the very next value, after it is the smallest forward jump we can make so we increment left pointer
by 1 and repeat the currentSum calculation as long the pointers don't cross, each other. If the currentSum > targetSum then we need to take
a little of the currentSum and we do this by moving the right pointer inwards by decrementing it. The reason is becausse we know that all the
numbers before the current array[r] are less than it and by moving one step inwards we can get closer to the targetSum. We keep moving the
pointers as long as the pointers don't cross each other because we are told that we cant return the same value twice meaning the pointers 
cannot be equal and represent the same value. So as long as l < r we keep calculating and comparing currentSum to targetSum. If l>=r, we
exit our loop and return an empty array. To illustrate this fine point I have a recursive solution, again that uses space in the recursive
stack so the iterative version is the best solution if the array is already sorted.
"""

"""Complement solution using a hashset instead of a hashtable. We are able to use a hashtable because we are assured of distinct integers."""
def twoNumberSum(array, targetSum):
	complementSet = set()
	
	for num in array:
		complement = targetSum - num
		if complement in complementSet:
			return [complement,num]
		complementSet.add(num)
	return []

"""Complement solution using a hashtable and storing indices because there are variations of this problem that require you
to return pairs of indices insted of the addend pairs, so this solution demonstrates how to store the indices with the integers."""
#O(n) time | O(n) space
def twoSumII(array,targetSum):
    complementDict = {}
    i=0

    while i < len(array):
        complement = targetSum - array[i]

        if complement in complementDict:
            return [array[i], complement]
    
        complementDict[array[i]]= i

        i+=1
    return []

"""Complement solution using a hashtable and storing complements instead of array integers. This is an unneccessary complication of the
solution but simply demonstrates an understanding of whats going on under the hood. Instead of storing the current integer and checking
if its complement is in the hashtable, we flip by logic, by storing the complement in the hashtable and checking if the current integer
exists in the hashtable."""
def twoSum(array, targetSum):
    complementDict = {}
    i=0

    while i < len(array):
        complement = targetSum - array[i]

        if array[i] in complementDict:
            return [array[i], complement]
        
        complementDict[complement]= i

        i+=1
    return []
        

"""This solution requires sorting. If the input array is already sorted, this because the optimal solution because its complexity
drops to O(n) time instead of the O(nlog(n)) stemming from the sorting step"""
#O(nlog(n)) time | O(1) space
def twoSumIII(array,targetSum):
    array.sort()  #this solution needs a sorted array. If input is already sorted skip this O(nlogn) step
    l, r = 0, len(array) - 1 #left pointer, right pointer

    while l < r:
        currentSum = array[l] + array[r]

        if currentSum == targetSum:
            return [array[l], array[r]]
        elif currentSum < targetSum:
            l +=1
        elif currentSum > targetSum:
            r +=1
    return []


"""
Generate pairs of integers using for loop and test if sum of pair is the targetSum. This is the naive solution, that is using only
what you are told in the question without any knowledge of data structures and how hashtables and hashsets give constant time access.
"""
def twoSumIV(array,targetSum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

"""Recursive approach of the sorting solution with worse complexity space complexity than the iterative version. This is done to 
illustrate the idea further."""
#O(nlog(n)) time | O(n) space
def twoNumberSum(array, targetSum):
	array.sort()
	return helper(array, targetSum, 0, len(array) -1)


def helper(array, targetSum, left, right):
	if left >= right:
		return []
	currentSum = array[left] + array[right]
	if currentSum == targetSum:
		return [array[left], array[right]]
	elif currentSum < targetSum:
		return helper(array, targetSum, left + 1, right)
	else:
		return helper(array, targetSum, left, right-1)


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

print(twoSumIV(array, targetSum))
