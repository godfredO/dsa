"""The distance of a pair of integers a and b is defined as the absolute difference between a and b. Given an 
integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] 
where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,1,1], k = 2
Output: 0

Example 3:
Input: nums = [1,6,1], k = 3
Output: 5
 
Constraints:
n == nums.length ; 2 <= n <= 104 ; 0 <= nums[i] <= 106 ; 1 <= k <= n * (n - 1) / 2 . 

So first off, whenever you see the kth smallest something, it indicates sorted order. When we can identify some
linear search space, we can use binary search to find the kth smallest element. Here we are asked to determine
the kth smallest pair distance where a distance is calculated between two points in the input array. What is
the search space? The minimum distance is obviously 0, if we have the same points, for example in the array
[1,3,1], the distance between the two 1's is 0. What is the maximum distance. The maximum distance will be the
distance between the smallest point and the largest point. In order to get this value, we have to subtract the
minimum value from the maximum value in the array. In otherwords, the search space is [0, max(arr) - min(arr)].

So now that we know that the search space is [0, max(arr) - min(arr)], what does the kth smallest distance mean.
It means that if we had a sorted order of all the distances in an array, the kth smallest distance will have 
exactly k elements that are less than or equal to it; all other distances greater than the kth smalles distance
will have more than k elements that are less than or equal. In otherwords, the kth smallest distance is the
minimum distance that has k or more elements that are less than or equal to it. So we will have a min binary 
search algorithm, that will take a guess as to the kth smallest distance and calculate how many distances are
less than or equal to the guess and check if that number is greater than or equal to k. 

Now a word about the sliding window for determining distances. We know that we only want distances that are less
than or equal to the guess. Take the sorted array [1,2,3,4,5,6,7] and a guess of say 3. If starting at 1, there
is [1,2]=1, [1,3]=2, [1,4]=3 and after 4 we know that the remaining points paired with 1, will have distances
greater than 3. We also know that [2,3]=1,[2,4]=2. [3,4]=1 are all valid distances. So between 1 and 4 we have
3 valid distances starting at 1, 2 valid distances startiing at 2 and 1 valid distance starting at 3, 3+2+1=6.
So as we go through the array we add right - left, so 0-0=0, 1-0=1,2-0=2,3-0=3 ie 3+2+1+0=6 but before we do
this we check if its time to advance the left pointer, and this happens whenever the current right pointer 
coupled with the current left pointer, yields a distance that is invalid ie greater than the guess. So in that
case we would keep moving the left pointer until we have a valid distance again before we add right - left to 
the count. This is because, since the array at this point is sorted, we know that if the distance between 1 and 
4 is valid, the distance [2,4] will be valid and so by adding right-left we count all the subsequent valid 
distances that share the same ending point. When we encounter an invalid distance, we move our left pointer 
until we have a valid distance again.

The sorting is nlog(n), the binary search is log(n) and inside it we do a O(n) sliding window operation to count 
the distances less than or equal to our guess giving the binary search as a whole a time complexity of O(nlog(n)) 
which is the overall complexity of the algorithm. Space complexity is O(1).
"""

def smallestDistancePair(nums,k):
    nums.sort()                                 #sort for condition function

    left, right = 0, nums[-1] - nums[0]        #max is last element , min is first element after sorting
    res = left                                 #initialize result variable 
    while left <= right:   
        mid = left + (right - left)//2
        count = condition(mid, nums, k)
        if count >= k:
            res  = mid
            right = mid - 1
        else:
            left = mid + 1
    return res           


def condition(guess, nums, k):
    count = 0
    left = 0
    for right, val in enumerate(nums):
        while val - nums[left] > guess:
            left += 1
        count += right - left
    return count
