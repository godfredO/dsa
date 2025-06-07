"""You are given a 0-indexed integer array nums and a target element target. A target index is an index i such 
that nums[i] == target. Return a list of the target indices of nums after sorting nums in non-decreasing order. 
If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:
Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:
Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:
Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
 
Constraints:
1 <= nums.length <= 100 ;  1 <= nums[i], target <= 100 .


So the first thing about this question is to realize that the answer is in the title. First sort, O(nlog(n)) 
and then find the indices. We can iterate from left to right, and at each index where the value in the sorted
array matches the target, we append the index to an output array. Since we iterate from left to right, we are
able to find the indices in increasing order. Now instead of using an O(n) loop to find all the target indices 
after sorting, we could use binary search. This doesnt improve the overall time complexity due to the required
sorting, but is just as a thought exercise in understanding binary search. So this solution is basically that
after sorting you use binary search to find the minimum index (left extremity) and the maximum index (right 
extremity) of the target value. And then you return a list of all the indices in between. In the code we 
initialize the target indices at -1 and update them whenever we find our target. So if any of our min / max
target indices is -1 we know that the target isnt in the aray, so we return an empty array otherwise we return
a list(range(left, right+1)) which will only append a single value if left == right else as many indices as
there are betwwen left and right since after sorting, the target indices will be next to one another. Other
than that, finding the left and right extremities is simply findFirstAndLastPositionOfElementInSortedArray.py.

The optimal solution, is actually based on counting sort and doesnt actually sort the array. We have to realize
what a 0-indexed array's indices convey for sorted array. Say the sorted array is [1,2,3], then index 1 tells
us there is exactly 1 element less than 2. Now this meaning isnt a hard and fast rule or anything. But in 
this solution, we count how many elements are less than the target value, to get the left extremity and how 
many are equal to the target value and the right extremity  will be count of less than + count of equal to. Now
if the target doesnt occur in the array, the count of equal to will be 0 so in that case we return an empty list.
"""
#O(nlog(n)) time | O(n) space
def targetIndices(nums, target):
    nums.sort()
    output = []
    for i, val in enumerate(nums):
        if val == target:
            output.append(i)
    return output

def targetIndices(nums, target):
    nums.sort()
    left = binarySearch(nums, target, True)
    right = binarySearch(nums, target, False)
    return list(range(left,right+1)) if left != -1 else []

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


def targetIndices(nums, target):
    lessCount , equalCount = 0, 0
    for num in nums:
        if num < target:
            lessCount += 1
        elif num == target:
            equalCount += 1
    return list(range(lessCount, lessCount+equalCount)) if equalCount != 0 else []

