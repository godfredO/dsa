"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a 
given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with 
O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:
0 <= nums.length <= 105 ; -109 <= nums[i] <= 109 ; nums is a non-decreasing array ; -109 <= target <= 109

Read searchForRange.py for the explanation. The reason for this file is to make it easy to find this solution
on leetcode as this file name matches leetcode's name for this question. Here we have a first solution that uses
the standard binary search interpretation, rigged to find the leftmost instance and the rightmost instance of
target.

Alternatively, we could right two versions of binary search, one to find the minimum index whose value is greater
than or equal to the target value (leftmost extremity) and another version to find the maximum index whose value 
is less than or equal to the target value, and both versions will return -1 if the target is not in the array 
otherwise it will return the found index. Why write such unnecessary code? Just a thought excercise, nothing else.
"""

"""Solution One"""
def searchRange(nums, target):
    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)
    return [left, right]

def binarySearch(nums, target, leftBias):
    left, right = 0, len(nums) - 1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:               #if we found target, then we want to know is it the left extremity or right extremity
            res = mid
            if leftBias:    #if looking for the left extremity, find the minimum index with target value
                right = mid - 1
            else:           #if looking for the right extremity, find the maximum index with target value
                left = mid + 1
    return res

"""Solution Two"""
def searchRange(nums, target):
    left = minBinarySearch(nums, target)
    right = maxBinarySearch(nums, target)
    return [left, right]

def minBinarySearch(nums, target) :
    left, right = 0, len(nums) - 1 
    res =  -1                         
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            res = mid
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return res 

def maxBinarySearch(nums, target) :
    left, right = 0, len(nums) - 1 
    res = -1                        
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            res = mid
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid  + 1
    return res


