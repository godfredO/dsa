"""Given a binary array nums, you should delete one element from it. Return the size of the longest non-empty subarray 
containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.


The question is effectively asking to find the longest subarray in our binary array nums, that contains at most 1 0, then
delete that 0 and return the length of the subarray. As such I have repurposed the solution from maxConsecutiveOnesII.py,
where we are to flip the 0. Any way, we keep a zero count and if this zero count is greater than 1, we shift our left
pointer, but before we do that, we check if the current left pointer value is 0 in which case we decremeent the zero count.
Then we know that our window is valid, so we check its length, and we track the greatest valid length. At the end we delete
the 0, by returning the maxLength minus 1.
"""
def longestSubarray(nums) :
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

        return maxLength - 1