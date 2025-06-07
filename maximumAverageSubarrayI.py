"""You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose length is 
equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be 
accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000


So this is a classic fixed width sliding window problem. We initialize the left and right pointers at index 0, and we add the
right pointer value to a total, and keep adding until the window size equals k, then we calculate the average by dividing the
total with the number of values in our window, which is k. We then do a maximum comparision with a maxAvgVal variable to track
the greatest window average. Then its time to consider the next window, which starts from index 1, but before we have to remove
the value at index 0 from our total, by decrementing the total with the value at the current left pointer before incrementing 
the left pointer.
"""
def findMaxAverage(nums, k) :
        left = 0
        total = 0
        maxAverageValue = float("-inf")
        
        for right in range(len(nums)):
            total += nums[right]
            
            if right + 1 - left == k:
                averageValue = total / k
                maxAverageValue = max(maxAverageValue, averageValue)
                total -= nums[left]
                left += 1
        
        return maxAverageValue
            