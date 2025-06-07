"""The question gives an array of integers and asks to return an array of two integers that represent the largest range of integers that
appear in the input array. A range is defined as as set of numbers that come right after each other in the set of real integers. Thus the
array [0,7] represents the range [0,1,2,3,4,5,6,7]. Thus returning [0,7] means that the all of the numbers [0,1,2,3,4,5,6,7] appear in the
array like an input array of [1,11,3,0,15,5,2,4,10,7,12,6]. This question obviously is going to use the left/right boundary technique 
somewhat, and since we need to check if the previous / next integer in the set of real integers exists in the input array for any input
array element, we need to use a hashtable for constant time access. 

Thus we iterate and store every in a hashtable with a value of True. Then do a second iteration to find the range each number is part of 
by expanding outwards from the current number in a loop and if the range extremities (left = num - 1, right = num + 1) are found in the 
hashtable, we continue expanding outwards (left / right) until you we dont find the next left / right extremeity number in the hashtable. 
Once we have the left / right extremities we compute the range length and store the range with the largest range. Now suppose for a range 
[0,7], we will effectively doing the same work of finding the same left and right extremities when we start from any of [0,1,2,3,4,5,6,7], 
so whenever we find the next left / right extremity in the hashtable, we convert its value (key:value pair) in the hashtable to False so 
that we don't repeat work. Again, the left / right boundary technique is a variation of getNeighbors function from graphs reduced for 1-d 
array so the True, False is our way of keeping track of what is visited and what is unvisited. This way we find and compute the length of 
each range in the array, once, which will be the first time we find the range. As a result, when at the step of finding ranges, we first 
check if the current number's value in the hashtable is False since this means we have already found its range and we found this current 
number when we were exploring from another input array element. Instead of computing the range length (number of elements) after getting 
the left and right extremities, we can actually compute it during the search / explorations for the left/ right extremities. Also since we 
are tasked with finding ranges of real integers, the numbers need not be distinct for the range to represent a set of (distinct) real 
numbers. Eg if the array is [4,0,2,2,3,1,1] the range contained is [0,4] using one 1 and one 2 to form the range. That is also why we use
a hashtable to track the distinct values since we only use one instance of duplicates.

Usually we use indices to find extremities, but since we are using the real integers themselves as centerIdx, leftIdx and rightIdx, make 
sure to decrement for left and increment for right in the respective while loops. Also since left / right extremities while loops terminate 
if the next left/right is not in the hashtable, we need to return [left + 1, right - 1], soft of like  those string arrays where we return 
slice indices (but not exactly like lol look at right, here right-1 there right due to slicing end-exclusivity). This is because our
asks that the first element in the outpur array be the first number in the range while the second number should be the last number in the
range."""

#O(n) time | O(n) space
def largestRange(array):
    bestRange = [] #to hold the indices of longest range found in array
    longestLength = 0 # for length of largest range, initialized at 1
    nums = {}

    #loop to add entire array to hashtable
    for num in array:
        nums[num] = True  #True means unvisited, if we have duplicates we basically re-add the same value.
    
    #loop to find the range in array each number is part of
    for num in array:
        if not nums[num]: #if value is False,skip, False means previously visited
            continue #marking as False, ensures we explore each number once, hence O(n)
        nums[num] = False #otherwise set to false because we about to find its contained range, mark as visited
        currentLength = 1 # initialize range length to 1 because of current num, which is its own range of length 1
        left = num - 1 #starting point of leftwards expansion for range in array
        right = num + 1 #starting point of rightwards expansion for range in array

        #find left extremity of range
        while left in nums:
            nums[left] = False #set to False to avoid repeated exploration
            currentLength += 1
            left -= 1 #keep moving west, lol
        
        #find right extremity of range
        while right in nums:
            nums[right] = False #set to False to avoid repeated exploration
            currentLength += 1
            right += 1 #keep moving east, lol
        
        #check if its the largest range
        if currentLength > longestLength: #always the case since currentLength always starts off at 1 and longestLength is initialized to 0
            longestLength = currentLength
            bestRange = [left+1,right -1] #we keep moving left/right until not in hashtable so left+ 1, right - 1

    return bestRange
    
            





array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(largestRange(array))
