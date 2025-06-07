"""Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000.


The question extends from maxConsecutiveOnes.py. We are told that we can only flip a single 0. This means that we want
to find the greatest subarray that contains only a single 0 which we can flip and make into a 1. So we use the variable
width sliding window approach here. If the current value is 0, we increment a zeroCount. If this zeroCount is greater
than 1, we need to shift our left pointer to bring it equal or less than 1. Shifting the left pointer involves increasing
it by 1 but before we do this, we first check if the value at current left pointer is 0, in which case we decrement our 
zeroCount. When we exit this while loop, the zeroCount will be equal or less than the allowable number of flips, so we
take the length of our current window, and track the maximum window (we are assured that our window only has 0's and 1's).
The key to this problem is realizing that the question can be rephrased as the longest subarray with a single 0 and also
that keeping a zeroCount helps us solve the question. Alternatively we could have counted ones and subtracted from the 
length of the window like is done in questions like longestRepeatingCharacterReplacements.py and shifting our left pointer
as long as this subtraction is greater than 1.
"""

def findConsecutiveOnes(nums):
    
    zeroCount  = 0 
    maxLength = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeroCount += 1
        
        while zeroCount > 1:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1

        length = right + 1 - left
        maxLength = max(maxLength, length)
    
    return maxLength


nums = [1,0,1,1,0]
print(findConsecutiveOnes(nums))