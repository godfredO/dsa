"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array 
nums = [0,1,2,4,5,6,7] might become:
[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], 
a[2], ..., a[n-2]]. Given the sorted rotated array nums of unique elements, return the minimum element of this array.
You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:
n == nums.length ; 1 <= n <= 5000 ; -5000 <= nums[i] <= 5000 ; All the integers of nums are unique. ; 
nums is sorted and rotated between 1 and n times.

So this question is like a question shiftedBinarySearch.py where we are tasked with finding the index of a target in
a rotated / shifted array, returning -1 if the target is not in the rotated array. Here we are tasked with finding the
minimum value in a rotated/shifted array. Note that rotating a sorted array one time means moving the last element to
the front of the array. So [1,2,3,4] after 1 rotation becomes [4,1,2,3]. After n rotations, the sorted array is back 
to its original sorted order. Thus after 4 rotations, [4,1,2,3], [3,4,1,2], [2,3,4,1], [1,2,3,4] we have the array.

Now the naive solution would to do a O(n) operation of scanning the array, tracking the minimum integer seen so far and 
at the end we return the minimum integer seen. But how can we use binary search to optimize this solution. 

So lets say our sorted unrotated array is [1,2,3,4,5], and we calculate mid to point to 3. If we compare mid to the left
and right pointers we observe that both subarrays are sorted ie nums[left] <= nums[mid] and nums[mid] <= nums[right].
Note that binary search effectively divides the array into two subarrays [left, mid] and [mid, right](though technically
its [left, mid] and [mid + 1, right]). So if we find that the left and right subarrays are sorted, then we know that the 
entire (sub)array between left and right pointers is sorted so we return nums[left]. 

However lets look at what happens when we rotate the array. In [5,1,2,3,4], the pivot (mid) is 2 and we recognize that 
the left subarray is unsorted since nums[left] > nums[mid] ie 5 > 2. The right subarray however is still sorted since 
nums[mid] <= nums[right] ie 2 <= 4. And here we realize that the minimum value, 1 is in the left subarray so we move the 
right pointer to mid and repeat binary search.  In [4,5,1,2,3], the left subarray is still unsorted since 4 > 1, where 1 
is the pivot, so we move the right pointer again to mid. The right subarray is sorted since 1 <= 3 . In [3,4,5,1,2], the 
left subarray is sorted since 3 <= 5 , where 5 is the pivot but this time, the right subarray is unsorted since 5 > 2 and 
we realize that the minimum value, 1 is in the right subarray. So, to find the minimum value in the rotated sorted array, 
we test not for sortedness, but rather for unsortedness. If the left subarray is unsorted, the minimum value is in the 
left subarray so we move the right pointer to mid and repeat binary seaarch. If the right subarray is unsorted, the 
minimum value is in the right subarray, so we move the left pointer to mid + 1 and repeat binary search. If both subarrays 
are sorted, then the array as a whole is sorted, so we return the number at the left pointer.


"""

#O(log(n)) time | O(1) space
def findMin(nums) :
    left , right = 0 , len(nums) - 1
        
    while left <= right:
        mid = left + (right  - left) // 2
            
        if nums[left] > nums[mid]:          #if the left subarray is unsorted
            right = mid
        elif nums[mid] > nums[right]:       #if the right subarray is unsorted
            left = mid + 1
        else:                               #if both subarrays are sorted
            return nums[left]
       



