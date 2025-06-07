"""Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


This is a greedy algorithm question like optimalPartitionOfString.py. Anyway, we will be counting the number of 1's in the
array. If the current value is a 1, we increment our count and we do a max comparison with our maxCount variable. If its 
a 0, we initialize the count to 0. The count variable thus tracks the current number of consecutive ones. The maxCount 
variable tracks the maximum number of consecutive ones seen.
"""
#O(n) time | O(1) space
def findMaxConsecutiveOnes(nums) :
        consecutive = 0
        maxConsecutive = 0
        
        for val in nums:
            if val == 1:
                consecutive += 1
                maxConsecutive = max(maxConsecutive, consecutive)
            else:
                consecutive = 0
        return maxConsecutive
        