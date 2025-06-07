"""Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any 
subarray is minimized. Return the minimized largest sum of the split. A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
 

Constraints:

1 <= nums.length <= 1000  ;   0 <= nums[i] <= 106    ;    1 <= k <= min(50, nums.length)

This question is surprisingly a binary search question ( binarySearchII.py ) and demonstates that binary search is widely 
applicable when you have some sort of monotonicity and a condition such that the answer is the minimal value for which
the condition is true. The backtracking solution is demonstated before the binary search approach.

You are given an integer array nums and an integer k, and we are required to split nums into k non-empty subarrays in such 
a way that minimizes the largest subarray sum. So there are two main aspects to this solution; splitting into k non-empty 
subarrays, and minimizing the subarray sum. Since there has to be k subarray non-empty subarrays, the smallest subarray has 
to contain at least 1 element from the array. There will also be an upper bound on the largest group. Basically the largest
group can be at most n-k+1. Eg if there are 5 elements and 3 groups needed, the largest group can be 5 - 3+ 1=3, leaving 
the other two groups with an element each. The first way to solve this is the brute force approach. So basically, we can
choose the first group as the elements from index 0 to index n-k+1, and then we make another call with a smaller array, a
new starting index and a reduced m. So if nums = [7,2,5,10,8] and k=2 the first group can be [7] ,[7,2], [7,2,5], [7,2,5,10] 
and the corresponding second group for each will be [2,5,10,8], [5,10,8], [10,8], [8]. Now for a large array and large k, 
going through all the possibilities would be exceedingly inoptimal. This backtracking solution can be cached, and as such
this solution can also be done in a dynamic programming way. The backtracking solution as coded here can be described as
partition backtracking, and can also be found in partitionToKEqualSumSubsets.py, matchsticksToSquare.py. Anyway we pass in
a starting index and k. In each iteration we loop from startIdx to len(nums) -k + 1, and we initialize a curSum to which we
add the number in the loop, and we make another call for the next number. Notice here that in the next call, we increment
startIdx, but decrement k. Decrementing k ensures that the for loop (startIdx, len(nums) - k + 1), adjusts itself, both in
the starting index and the ending index. Eg if n = 5, k = 3, then when startIdx = 0, endIdx = 5-3+1=3, so range(0,3) will 
be indices 0,1,2 and when startIdx is 1, k = 2 and endIdx = 5 - 2 + 1 = 4 so that range(1,4) = 1,2,3. Also realize that we 
are looking at subarray sums, there is no reason to remove the previous addend from the current sum because we are interested 
in the sum of a subarray ending at a particular index. The base case is that if k = 1, to just sum the nums[startIdx:]. When 
we receive sum of the next subarray we track the max subarray sum. If we get to a point where the current subarray sum is 
greater than previous path's max subarray sum, then there is no point in continuing because we want the path with the 
minimum subarray sum, so we break out of the loop, cache and return up the tree. 

But there is an even better solution using binary search. Binary search is useful where there is some monotonicity of linear 
relationship betweeen two extremes a low end and a high end. The property of  monotonicity here is that as the number of 
partions increase, the maximum subarray sum decreases linearly. So the idea is that the low end of the binary search approach 
is the largest value in the array which corresponds to when partitions = n, and the high end is the sum of all values in the 
array which happens when number of partitions = 1. What do we mean by this. We are trying to find the maximum subarray sum 
after splitting into k non-empty subarrays. So if we first think of the maximum subarray sum portion, we know that a subarray 
must have at least 1 element, and at most all the elements. Now the maximum subarray sum of size 1 is the subarray with only 
the largest elements in it and the maximum subarray sum of all the elements is the sum of all the elements. Another way of 
saying it is that the maximum subarray sum when the number of partitons equals the length of the array (where each subarray 
has only 1 element) is the maximum element in the array. The maximum subarray sum when number of partitions is 1 is the sum of 
all the elements in the array. Then as is typical of binary search we add the low and high, floor divide by 2 to yield a middle 
value and ask ourselves the question: Is it possible to split the array into k subarrays such that the greatest subarray sum is 
less or equal to than (ie at most) the middle value.

So now the question becomes, how can we determine if we can take the input array, split it into k groups where the maximum 
subarray sum is less than the middle value. That part uses a greedy algorithm. So we would start from the first value and keep 
calculating a cumulative subarray sum as long as the cumulative sum is less than the mid value. So once we determine that 
adding the next number will go over the mid value, we have finished with the first split, and have started another subarray
and the current value is the first value in the new subarray and as such we set the cumulative sum equal to the current array
value.This greedy algorithm, we correctly yield the number of partitions such that the max subarray sum is the mid value, though 
not necessarily the partitions that have the mid value as their max subarray sum. Eg if [1,2,3] is the aray, the max subarray 
sum if partitions, k or days is 2 is 5. If we use this and the cumulative sum approach, we get [1,2] and [3], instead of [1], 
[2,3] but we still end up with the right number of partitions. So now that we have the number of splits how do we write our
return statement such that the answer to the original question is the minimal value that returns True. So think about it,
if the number of partitions is 1, the max subarray sum = sum(nums). If number of partitions is n, the max subarray sum =
max(nums). So lets arrange this in terms of our low and high end of the search space and the corresponding partitionns : 
max(nums) < largest < sum(nums) ; n > k > 1. So you see, since 'largest' is the minimal value for the max subarray
sums from largest to sum(nums), k is the maximum value from k to 1. As such our return statement which minimizes the max
subarray sum values for which the condition is True will be if the partitions is less than our equal to k . In otherwords,
as partitions increase from 1 to k, we are minimizing largest subarray sum from sum(nums) to largest. Remember, we are 
trying to find the minimal max subarray sum for which our condition returns True, and that corresponds to True if the 
number of subarrays is less than or equal to k and this is due to the inverse relationship betwen max subarray sum search 
space and the number of partitions or splits. Another thing ot realize too is that sum(nums) is actually our right pointer
and so if our condition function returns True, we move right to mid otherwise to mid + 1.

The binary search portion is log(n)and iterating as long as the cumulative sum is less than the middle value is O(n), giving 
an overall time complexity of O(n*log(n)). Apparently writing binary search as (l+r)// 2 can lead to overflow but writing as 
l+((r-l)//2) doesnt.
"""

"""Brute Force Approach"""
#O(n^2*n) time | O(n^2*n) space
# def splitArray(nums, k):
#     cache = {}
#     return dfs(0, k, cache, nums)


# def dfs(startIdx,k, cache, nums):
#     if k == 1:                  #for the last subarray sum (k reduced to 1 remaining, return the sum of the passed array)
#         return sum(nums[startIdx:])
    
#     if (startIdx,k) in cache:          #tuples are hashable
#         return cache[(startIdx,k)]   
    

#     res, curSum = float('inf'), 0
#     for j in range(startIdx,len(nums)-k + 1):
#         curSum += nums[j]
#         maxSum = max(curSum, dfs(j+1, k-1, cache, nums))   #the max subarray sum from this path
#         res = min(res,maxSum)                              #compare the maxSum of all paths and store the minimum 
#         if curSum > res:   #optimization, if curSum is greater than the min seen, break bcos increasing size will only increase curSum
#             break
#     cache[(startIdx, k)] = res   #cache the minimum seen by choosing the subarray ending at current index as the kth partition
#     return res


"""Optimal Solution"""
def splitArray(nums, k):
    left, right = max(nums), sum(nums)     #linear search space, possible max subarray sum
    while left < right:
        mid = left + ((right - left)//2)
        if canSplit(nums,mid,k):
            right = mid 
        else:
            left = mid + 1
    return left

def canSplit(nums,largest,k):
    subarray = 0
    curSum = 0
    for n in nums:
        curSum += n
        if curSum > largest:
            subarray += 1               # we just finished another subarray
            curSum = n                  # we also just started another subarray
    return subarray + 1 <= k            # +1 because we dont count the last subarray.

nums = [7,2,5,10,8]
k = 2
print(splitArray(nums,k))





"""

"""