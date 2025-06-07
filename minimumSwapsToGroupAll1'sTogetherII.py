"""A swap is defined as taking two distinct positions in an array and swapping the values in them. A circular array is 
defined as an array where we consider the first element and the last element to be adjacent. Given a binary circular array 
nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

Example 1:
Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

Example 2:
Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.

Example 3:
Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.
 

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1

Hint 1 : Notice that the number of 1’s to be grouped together is fixed. It is the number of 1's the whole array has.
Hint 2 : Call this number total. We should then check for every subarray of size total (possibly wrapped around), how many 
swaps are required to have the subarray be all 1’s.
Hint 3 : The number of swaps required is the number of 0’s in the subarray.
Hint 4 : To eliminate the circular property of the array, we can append the original array to itself. Then, we check each 
subarray of length total.
Hint 5 : How do we avoid recounting the number of 0’s in the subarray each time? The Sliding Window technique can help.



So this follows the same logic as minimumSwapsToGroupAll1sTogether.py, the only difference is the circular property. For an
array [1,1,0,0,1] the minimum number of swaps is 0 due to the circular property and 1 without the circular property. So how do
we handle the circular property. Simple we append the string to the end of itself. So [1,1,0,0,1] becomes [1,1,0,0,1,1,1,0,0,1].
But before we do this, we still have to get the width of the window using the total number of ones in the original array. And the
the answer will be the minimum number of 0's found in a sliding window of size, width.
"""
def minSwaps(nums):
    width = 0
    for val in nums:
        if val == 1:
            width += 1
    
    zeros = 0
    for i in range(width):
        if nums[i] == 0:
            zeros += 1
    
    minZeros = zeros
    circularNums = nums + nums  #list concatenation
    left = 0
    for right in range(width,len(circularNums)):
        if nums[left] == 0:
            zeros -= 1
        left += 1

        if nums[right] == 0:
            zeros += 1
        
        minZeros = min(minZeros, zeros)
    
    return minZeros