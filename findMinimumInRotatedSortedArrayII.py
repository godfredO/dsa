"""Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array 
nums = [0,1,4,4,5,6,7] might become: [4,5,6,7,0,1,4] if it was rotated 4 times. [0,1,4,4,5,6,7] if it was rotated 
7 times. Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], 
a[0], a[1], a[2], ..., a[n-2]]. Given the sorted rotated array nums that may contain duplicates, return the minimum 
element of this array. You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [1,3,5]
Output: 1

Example 2:
Input: nums = [2,2,2,0,1]
Output: 0
 
Constraints:
n == nums.length ;  1 <= n <= 5000 ; -5000 <= nums[i] <= 5000 ; nums is sorted and rotated between 1 and n times.

So this question extends from findMinimumInRotatedSortedArray.py, the only difference being that here, we can have
duplicates in the rotated array. As such we apply a technique used in searchInRotatedSortedArrayII.py which also
differs from its counterpart by containig duplicates. In this techniqe, before we even calculate mid, we shift
the left and right pointer to remove duplicates. If the next value after the left pointer is the same as the left
pointer value, we increment the left pointer. If the previous value before the right pointer is the same as the 
right pointer value, we decrement the right pointer. This is done to avoid having the situation where nums[left],
nums[mid], nums[right] all point to the same value, in which case we have no logical way of moving the pointers.
Eg [3,3,1,3]

Now we can right this solution in a better way which handles the duplicates and conducts the binary search all in 
the same operations. So we know from findMinInRotatedSortedArray.py that we are testing for unsortedness. So here
if we determine that the left subarray is unsorted, ie nums[left] > nums[mid], we know the min value is in the 
left subarray (read findMinimumRotatedSortedArray.py), but in addition we know that nums[left] cant be the minimum
value since we know that its at least greater than nums[mid]. In otherwords, we know the minimum value is in
[left + 1, mid]. So we move right pointer to mid and increment the left pointer before repeating binary search ie
right = mid, left += 1. The significance of left += 1 is that if nums[left] is has duplicates, we either consider
a new instance of the duplicate, or we even remove that value from consideration.Either way we know that it cant be 
our minimum value. This is how we combine removing duplicates with binary search.

On the other hand if the right subarray is unsorted, ie nums[mid] > nums[right], we know that the minimum value 
must be in the right subarray, and in addition, we know that nums[mid] cant be the minimum value because we know 
that its at least greater than nums[right]. In otherwords, the minimum value is in [mid+1, right]. Here, we move 
left = mid + 1 and that's all that we need to do. If mid is a duplicate, we move to a new instance of that 
duplicate value and if its not we just removed it from consideration. This is how we combine removing duplicates
with binary search. 

What if nums[left] <= nums[mid] <= nums[right]? Can we assert here that the entire array between left and right
is in sorted order like we did in findMinInRotatedSortedArray.py? Not quite. Take the example of [3,3,1,3]. If
left = 0, right = 3, mid = 1 and nums[0] <= nums[mid] <= nums[3] ie 3<=3<=3. But looking at the (sub) array 
contained between left and right pointer, its not actually sorted. And this is because of the duplicates which
make it appear sorted when its not. But if it were sorted, we know that the answer would not be the value at the
right pointer, it would be at the left pointer. In otherwords, we cant say the array is sorted for sure and as 
such we cant say the number at the left pointer is the minimum but we can say for sure that the number at the right 
pointer is definitely not the minimum, so we can remove it from consideration. So what do we do here? We shorten 
the array by moving right pointer inwards. In otherwords, if both subarrays appear sorted, remove the right pointer
value because we know that it can't be the duplicate. This way we get our right pointer even closer to the left 
pointer just in case the entire array is actually sorted, otherwise we get to possibly remove a duplicate or at 
least we remove a value that we know can't be the minimum value, ie the right pointer value. At the end, the minimum 
value will be at the left pointer in any case, so once our pointers cross, we return the number at the left pointer.


"""

def findMin(nums):
    left , right = 0 , len(nums) - 1

    while left < right:
        while left<right and nums[left] == nums[left+1]:
            left+=1
        while left<right and nums[right] == nums[right-1]:
            right-=1

        mid = left + (right  - left) // 2
            
        if nums[left] > nums[mid]:          #if the left subarray is unsorted
            right = mid
        elif nums[mid] > nums[right]:       #if the right subarray is unsorted
            left = mid + 1
        else:                               #if both subarrays are sorted
            return nums[left]
    return nums[left]                       #can combine this return with one above using left <= right
        

def findMin(nums) :
    left , right = 0 , len(nums) - 1
        
    while left < right:
 
        mid = left + (right  - left) // 2

        if nums[left] > nums[mid]:          #if the left subarray is unsorted
            right = mid                   
            left += 1                       #left cant be min so remove it
                
        elif nums[mid] > nums[right]:       #if the right subarray is unsorted
            left = mid + 1
        else:                               #if both arrays appear sorted
            right -= 1                      #right cant be min so remove it
    return nums[left]
