"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return 
the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
 

This question is an extension of binarySearchII.py. The only thing to note here is that since the target could be larger
than the greatest element in the sorted array, its positon could be equal to the length of the array ie it would be 
appended to the end of the sorted array. So, the main thing here, is to ensure that the right bound is len(nums) instead
of len(nums) - 1. Also, since we are to return the insert position if target is not in the array (instead of -1 like in
binarySearchII.py), we only need return the left pointer index.
"""

#O(n) time | O(1) space   - Linear time solution
def searchInsert(nums, target):
    idx = len(nums)
    for i,num in enumerate(nums):
        if num >= target:
            idx = i
            break
    return idx 


"""Standard binary search"""
#O(log(n)) time | O(1) space
def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
        
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left

"""Template version"""
#O(log(n)) time | O(1) space
def searchInsert(nums, target) :
    left, right = 0, len(nums)
        
    while left < right:
        mid = left + (right - left) // 2
            
        if condition(nums, mid, target):
            right = mid
        else:
            left = mid + 1
    return left
    
def condition(nums, mid, target):
    return nums[mid] >= target
        