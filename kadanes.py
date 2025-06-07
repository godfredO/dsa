"""The input is a non-empty array of integers and the question asks to write a function that returns the maximum sum of a subarray of the
input array. Now it is important to realize that the question doesnt ask to find the subarray with the maximum sum, just to return the 
maximum subarray sum. Now if this question were had only positive integers, then the max subarray sum would be the sum of all the integers
since the array is a subarray of itself. However if there are negative numbers in the array, there is no immediate way of knowing if those
should be part of the subarray since there is no clear way of knowing if positive numbers that come after it have the ability to offset the
reduction to a running sum caused by the negative number.

The technique used here is the ending at index technique where we reformulate the problem for the sub-aray ending at each index. The first 
thing to note is that we are assured that the array is non-empty so no need to handle the edge case of empty array. The next thing is the
base case, that a single element array is the max subaray sum to itself, whether the single element is negative or positive. Then, the
next thing is to realize that as we go through the array, we will have to decide whether to extend the current subarray or start a new
subarray at the current index. How do we decide? Extending the current subarray means adding the current number to the running subarray
sum, and starting a new subarray means a new subarray ending and starting at the current index. So we compare the maximum of the current
number and the sum of the current number and the running subarray sum. In the case of negative numbers, we will extend the subarray sum
if the postive number that comes after the negative sufficiently offsets the reduction to the running sum such that the updated sum is
greater than the positive number itself. Eg if the runing sum before a negative number is 50 and the negative number is -10 and after 
that there is a 20, the running sum at the negative number is equal to the runnning sum before the negative number plus the negative 
number ie 50-10 = 40, therefore we compare max(40+20, 20) = max(60,20). So in this case it is worth it to extend the existing subarray 
from before the negative number to after the negative number for an updated running sum of 60 instead of starting a new subarray whose
sum will be 20. But lets say the negative number were -60, then the running sum at the negative number is 50-60 = -10 so we compare
max(-10+20, 20) = max(10,20) = 20 so we start a new subarray running sum at 20. This also happens with adjacent negative numbers
ie [-10 -2], the max subarray sum is -2 ie max(-10-2,-2) = -2. 

So as we go through the array we check for the maximum of adding the current number to the running sum vs the num and that result is 
the new running sum . Then with the maxSubarray sum, we keep track of the maximum subarray sum seen so far in case down the line we
start a new subarray."""

#O(n) time | O(1) space
def kadanesAlgorithm(array):
    maxEndingHere = array[0] #initialize as first value, base case
    maxSoFar = array[0]      #initialize as first value, base case
    for i in range(1,len(array)): #start looping from second number
        num = array[i]
        maxEndingHere = max(num,maxEndingHere + num) #main step, compare num to the previousSum + num due to negative numbers
        maxSoFar = max(maxSoFar,maxEndingHere)
    return maxSoFar

array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
print(kadanesAlgorithm(array))
