"""There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values). Before 
being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the 
resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, 
[0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4]. Given the array nums 
after the rotation and an integer target, return true if target is in nums, or false if it is not in nums. You must 
decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000 ; -10^4 <= nums[i] <= 10^4 ; nums is guaranteed to be rotated at some pivot. 
-10^4 <= target <= 10^4
 

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this 
affect the runtime complexity? How and why?


Now this question is an extension of searchInRotatedSortedArray.py (and shiftedBinarySearch.py), and the difference
here is that there are duplicate values in the array. So the main addition to that algorithm is that before we
calculate our mid value, we ensure that we remove all duplicates from the left and right pointer. That is if the
next value after the left pointer is the same as the left pointer value, then we increment the left pointer until
the next value is different. Similarly if the previous value before the right pointer is the same as the right 
pointer value, we decrement the right pointer until the previous value is different. Once we ensure that the left
pointer and right pointer are pointing to the only instance of those values in the window between the two pointers,
we go ahead to calculate the mid value and apply the same logic as in searchInRotatedSortedArray.py. 

Why do we need to ensure that for any window between left and right pointers, the left and right pointer values are 
the only such instance. One idea is that if we dont skip the duplicates, we could end up in a situation where the
values at left, mid , right are the same value in which case we cant decide which part of the array is sorted. 
Eg 1,0,1,1,1] target = 0. To do this we advance the left pointer as long as the next value equals the current left
pointer value and left pointer is less than right pointer. We do the same for the right pointer. This way, if there
are a series of duplicates, the left pointer will be pointing to the last of the duplicates, and the right 
pointer will be pointing to the first of the duplicates since we increment the left pointer and decrement the right
pointer.

Now is there a way of combining the step where we skip over duplicates with binary search. First we realize that the
issue with the duplicates is that left, mid, right could be pointing to the same value. So after checking if mid
is the target, we check if left, right, mid are all the same value, in which case, we increment the left pointer and
decrement the right pointer. And that is it.
"""
def search(nums , target) :
    left, right = 0, len(nums) - 1
        
    while left <= right:
        while left<right and nums[left] == nums[left+1]:
            left+=1
        while left<right and nums[right] == nums[right-1]:
            right-=1

        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        elif nums[left] <= nums[mid]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False



def search(nums , target) :
    left, right = 0, len(nums) - 1
        
    while left <= right:
        
        mid = (left + right) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] == nums[left] == nums[right]:
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return False