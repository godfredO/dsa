"""This question finds the maximum value in a rotated sorted array. Take [1,2,3,4,5], mid is 3, both subarray appear 
sorted ie nums[left] <= nums[mid] <= nums[right] and since we are assured of distinct values, we can be certain that
the array between left and right is sorted. And if sorted, the answer is the value at the right pointer. Take the
array [4,5,1,2,3],, the left subarray appears unsorted and we can see that the maximum value is in the left subarray.
Take [2,3,4,5,1], the right subarray appears unsorted and we can see tha the maximum value is in the right subarray.

So the solution is simple really, since we are assured of distinct values, if both subarrays appear sorted we can
definitely say the array is sorted as is and we return the value at the right pointer. Otherwise we test for 
unsortedness and if the left subarray is unsorted we repeat binary search on the left subarray by moving the right
pointer to mid - 1. If the right subarray is unsorted, we repeat binary search on the right subarray by moving the
left pointer to mid. Our loop condition is while left < right so if pointers cross, both left and right will be
pointing to the same element so we return nums[left]. Alternatively, we could change the loop condition to while
left <= right in which case we will definitely hit the inner return statement for when both subarray are sorted.
Read findMaxInRotatedSortedArrayII.py for an explanation of how we tweak the algorithm to handle a rotated sorted
array with duplicates.
"""


def findMax(nums) :
    left , right = 0 , len(nums) - 1
        
    while left < right:
 
        mid = left + (right  - left) // 2

        if nums[left] > nums[mid]:          #if the left subarray is unsorted
            right = mid  - 1                # mid cant be max so remove it                                                          
                
        elif nums[mid] > nums[right]:       #if the right subarray is unsorted
            left = mid                  
                                 
        else:                               #if both arrays appear sorted
            return nums[right]
    return nums[left]


nums = [4,5,1,2,3]
print(findMax(nums))