"""A conveyor belt has packages that must be shipped from one port to another within days days. The ith package on the 
conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order 
given by weights). We may not load more weight than the maximum weight capacity of the ship. Return the least weight 
capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

Example 1:
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into 
parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.

Example 2:
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1



This question is an application of splitArrayLargestSum.py question, and hence can be solved with binary search 
since it follows the same logic as that questiion. The reason it is a binary search question is that it follows the 
same monotonicity or linear relationship between the max subarray sum and the number of subarrays. If number of 
subarrays is 1, then the maximum subarray is the sum of all the weights (this is also the only possible partitioning). 
If the number of subarrays is equal to the number of packages, the maximum subarray sum is the maximum package weight. 
That if k=1 maxSubSum = sum(weights) and if k=n maxSubSum= max(weights). if k = 2,  maxSubSum[k=n] < maxSubSum[k=2] < 
maxSumSum[k=1]. In fact maxSubSum[k=n] < maxSubSum[k=n-1] < maxSubSum[k=n-2] < ... maxSubSum[k=1]. So we have our
monotonicity ie the maxSumSum moves in ascending order as k moves in as descending order. Now we have our k, and we 
are asked to find the maxSumSum of that k. What is the condition in this case? The condition has to be in such a form 
that the answer is the minimal value that returns True for the condition. The condition is the same as used in 
splitArrayLargestSum.py. That is for each max subarray sum mid value, we count how many subarrays we can form such 
that the subarray sums are either equal or less to the mid value. So we initialize our cumulative sum at 0, iterate 
and add the numbers and if this sum exceeds our target, we know we just ended one partition (day here) and started 
another one, so we increment our subarray count and set the cumulative sum to the current number ie the current number 
becomes the first value in a new subarray. This greedy algorithm, we correctly yield the number of partitions such that 
the max subarray sum is the mid value, though not necessarily the partitions that have the mid value as their max 
subarray sum. Eg if [1,2,3] is the aray, the max subarray sum if partitions, k or days is 2 is 5. If we use this and 
the cumulative sum approach, we get [1,2] and [3], instead of [1], [2,3] but we still end up with the right number of 
partitions. 

Now how do we structure the condition boolean return statement. So if we had to ship all packages on the same day, 
we would need a ship that can carry sum(weights). If days = 1, ship = sum(weights). Similarly if days = len(weights),
ship = max(weights). So lets array this in terms of our low end and our high end in weights and the corresponding
days : max(weights) < ship < sum(weights) ; n > days > 1. So you see, since ship is the minimal value for the weights 
from ship to sum(weights), d is the maximum value from d to 1. As such our return statement which minimizes the weight 
values for which the condition is True will be if the subarray count is less than our equal to days . Remember, we are 
trying to find the minimal weight for which our our condition returns True, and that corresponds to True if the number 
of subarrays is less than or equal to days and this is due to the inverse relationship betwen weight search space and 
the corresponding days.


The partitions in this question is days, and the minimum value that returns a number of partions (days) that is equal 
or greater than days will be the weight of the ship we want.
"""

"""Optimal Solution"""
def shipWithinDays(weights, days) :
        left, right = max(weights), sum(weights)
        res = right   
        while left < right:
            mid = left + ((right - left)//2)
            if canSplit(weights,mid,days):
                res = mid
                right = mid 
            else:
                left = mid + 1
        return res

def canSplit(nums,largest,k):
    subarray = 0
    curSum = 0
    for n in nums:
        curSum += n
        if curSum > largest:
            subarray += 1
            curSum = n
    return subarray + 1 <= k