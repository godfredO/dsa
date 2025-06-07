"""This question is an extension of findMinimumInRotatedSortedArrayII.py. This is an extension of the second solution
in that question to find the maximum in a rotated sorted array. Basically, If you take [5,1,2,2,4], mid=2 and the 
left subarray tests True for unsortedness since nums[left] > nums[mid] , the max value is in the left subarray and
since nums[left] > nums[mid] we know that mid cant be the max value since left is greater than it. Similarly, if you
take [2,2,4,5,1], the right subarray tests True for unsortedness, since nums[mid] > nums[right] , we notice that the 
max value is actually in the right subarray, and we know that the right value cant be the maximum since we know at 
least one value that is greater than it. If both subarrays appear sorted, we cant actually conclude that the array
between left and right are sorted due to the existence of duplicates. Take [2,2,2,5,2], mid, left, right are all
2, so even though nums[left] <= nums[mid] <= nums[right],  we can see that the array between left and right isnt 
sorted. As such, we cant just return the value at right pointer, but we can certainly say is that if the array were
sorted, the max value would not be at the left pointer. 

So in the code, we calculate the mid value and if the left subarray is unsorted, we move the right pointer to mid -1.
if the right subarray is unsorted, we move the left pointer to mid and decrement the right pointer by 1. Otherwise
if both subarrays appear sorted, we increment the left pointer by 1. The loop condition is while left < right, so 
when the loop terminates left and right will be equal and pointing to the maximum, value so we return nums[left].
In findMaxInRotatedSortedArray.py, we write the same solution for a rotated sorted array with no duplicates.
"""

def findMax(nums) :
    left , right = 0 , len(nums) - 1
        
    while left < right:
 
        mid = left + (right  - left) // 2

        if nums[left] > nums[mid]:          #if the left subarray is unsorted
            right = mid  - 1                # mid cant be max so remove it                                                          
                
        elif nums[mid] > nums[right]:       #if the right subarray is unsorted
            left = mid                      
            right -= 1                      #right cant be max so remove it
        else:                               #if both arrays appear sorted
            left += 1                       #left cant be max so remove it
    return nums[left]


nums = [2,2,2,3,4,5,0,1,1]
print(findMax(nums))