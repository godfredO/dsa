"""The min-product of an array is equal to the minimum value in the array multiplied by the array's sum. For example, the 
array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20. Given an array of integers nums, return 
the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7. Note 
that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the 
maximum min-product without modulo will fit in a 64-bit signed integer. A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.

Example 2:
Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.

Example 3:
Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.


So the question states that the min-product of an array is equal to the minimum value in the array multiplied by the array's
sum, and it asks us to find the maximum min-product of any non-empty subarray of nums. In otherwords, for the brute force 
approach, we need to generate all subarrays of the input array, and for any subarray, we are to find the minimum value in 
the subarray and multiply it by the subarray's sum. Generating every subarray is O(n^2), getting the sum and min value of the 
subarray is going to be O(n) giving a total of O(n^3) time. So take an array [2,1], the possible subarrays are [2],[2,1],[1]. 
So the possible min-products are 2*2=4 , 1*3=3 , 1*1=1, and the maximum is 4. 

This problem can be solved in O(n^2) time using a left / right boundary two pointer approach. Take nums = [2,4,6,3,7,1,5],
we iterate through the array, and at each number, we find the largest subarray for which the current number is the minimum,
calculate the sum of that subarray, multiply with the current number for the min-product and track the maximum min-product.
In otherwords, this question is really the same as largestRectangleInHistogram.py / largestRectangleSkyline.py, but instead
of width, we have subarray sum (height and current number are equivalent). So we expand leftward as long as the previous 
number is greater or equal to the current number; and we expand rightward as long as the next number is greater or equal to
the current number. Then once we have the indices for left/right boundaries for the current number, we get the subarray sum
as sum(nums[leftIdx:rightIdx + 1]). This is O(n^2), O(1) space. Note that when we slice and then sum, that both operations 
are O(n), and when we expand leftward and rightward, both operations are O(n). So for each index, we do four O(n) operations
resulting in a total O(n^2) time. We can however pre-compute the presums at each index, and when we have the presums, we are
able to do the subarray sum step with a simple subtraction. In otherwords, to get the subarraysum from the left and right
boundary indices, we recognize that we simply do preSum[right] - preSum[left - 1] if left != 0 else its preSum[right], where
subarray sum  is the sum of all the values from right to left inclusive. Note that the preSum or prefix array used here is 
simply the sum of all values up to and including the value at any index. So to get the subarray sum of values [left,right]
inclusive, we need to subtract the prefix sum before left from the prefix sum at right to remove the prefix sum before 
left from the prefix sum at right unless there is nothing before left in which case the prefix sum at right only includes the
values in the subarray [left,right] inclusive.


Now just like largestRectangleInHistogram.py / largestRectangleSkyline.py, we are able to obtain a O(n) time solution by using
a stack, specifically an ascending (non-decreasing) stack. So if the incoming value is smaller than the current peek value we
have reached the end of the subarray for which the current peek value is the minimum. So we pop the current peek value and now
we can say that the next smaller for the popped value is the incoming value and the previous smaller is the new peek if the
current is non empty. Now to more cleanly align with the left/ right boundary solution, we can go ahead and say that since we 
know that the next / previous smaller are technically not a part of the subarray for which the current element is minimum, we
will be storing left and right boundary values, where leftBoundary[i] = prevSmaller[i] + 1 and rightBoundary[i] = nextSmaller[i]
- 1. This way, we can use the same formula as above to obtain the subarray sum from the prefixSums. ie subarraySum = 
prefix[right] - prefix[left - 1] if left!= 0 else prefix[right]. We also initialize left boundary as 0 and right boundary as
len(nums) - 1. 

There are cleaner more sophisticated ways of coding this solution, but the key the essence is the same. Also, since we have to
use space in the form of a stack, writing it in this uncomplicated manner has higher pedagogical value. Anyway, the main point
is to realize that largestRectangleSkyline.py / largestRectangleInHistogram.py are generalizations of finding the largest 
subarray for which the current value is the minimum and we can use the left/right boundary two pointer method or we can use a
next/previous smaller stack and obtain our left/right boudnary from it, and then use the left/ right boundary in the width 
calculations ; though in this question we need the prefix sum information.
"""



# #O(n^2) time | O(n) space - with presum and storing all left/right boundary values
# def maxSumMinProduct(nums):
#     n = len(nums)
#     leftBoundary = [0]*n    #could also initialize at list(range(n)) instead of 0 everywhere
#     for i in range(n):
#         currentHeight = nums[i]
#         leftIdx = i 
#         while leftIdx - 1 >= 0 and nums[leftIdx - 1] >= currentHeight:
#             leftIdx -= 1
#         leftBoundary[i] = leftIdx
    
#     rightBoundary = [n-1]*n   #could also initialize at list(range(n)) instead of 0 everywhere
#     for i in range(n):
#         currentHeight = nums[i]
#         rightIdx = i
#         while rightIdx + 1 < n and nums[rightIdx + 1] >= currentHeight:
#             rightIdx += 1
#         rightBoundary[i] = rightIdx
    
#     preSum = [0]*n
#     preSum[0] = nums[0]
#     for i in range(1,n):
#         preSum[i] = preSum[i-1]+nums[i]
    
#     subarraySum = [0]*n
#     for i in range(n):
#         right = rightBoundary[i]
#         left = leftBoundary[i]

#         subarraySum[i] = preSum[right] - preSum[left-1] if left != 0 else preSum[right]


#     return [leftBoundary, rightBoundary, preSum, subarraySum]

#O(n^2) time | O(1) space - with slice 
def maxSumMinProduct(nums):
    maxMinProduct = 0
    for i in range(len(nums)):
        currentHeight = nums[i]
        leftIdx = i 
        while leftIdx - 1 >= 0 and nums[leftIdx - 1] >= currentHeight:
            leftIdx -= 1
            
        rightIdx = i
        while rightIdx + 1 < len(nums) and nums[rightIdx + 1] >= currentHeight:
            rightIdx += 1

        subArraySum = sum(nums[leftIdx:rightIdx+1])
        area = currentHeight * subArraySum
        maxMinProduct = max(maxMinProduct, area) 
    return maxMinProduct%(10**9+7)


def maxSumMinProduct(nums):
    n = len(nums)

    leftBoundary = [0]* n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

        if stack:
            leftBoundary[i] = stack[-1] + 1   #leftBoundary = prevSmaller + 1

        stack.append(i)
    
    rightBoundary = [n-1]*n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            stackTop = stack.pop()
            rightBoundary[stackTop] = i - 1   #rightBoundary from nextSmaller
        stack.append(i)
    
    preSum = [0]*n
    preSum[0] = nums[0]
    for i in range(1,n):
        preSum[i] = preSum[i-1]+nums[i]
    
    maxMinProduct = 0
    subarraySum = [0]*n
    for i in range(n):
        left = leftBoundary[i]
        right = rightBoundary[i]

        subarraySum[i] = preSum[right] - preSum[left-1] if left != 0 else preSum[right]
        
        minProduct = subarraySum[i] * nums[i]
        maxMinProduct = max(maxMinProduct, minProduct)
        
    return maxMinProduct%(10**9+7)




nums = [1,2,3,2]
print(maxSumMinProduct(nums))