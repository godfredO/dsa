"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that 
nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

The trick is that for any duplicate we want to compare it to its closest duplicate value as far as index is concerned. This
is because the question is basically asking if for any duplicate the distance between them is k or less. So if a duplicate
value is farther than  k away from its other closest duplicate, there is no need comparing with the other farther duplicates.
So we iterate and add the values (as key), and their indices to a hashtable. If the value is already existing, then we found
a duplicate, so we check if the distance between them is at least k, if it is we return True otherwise, we replace the index
of that value key with the current index. 
"""

def containsNearbyDuplicate(nums, k) -> bool:
    indexMap = {}
    for idx, val in enumerate(nums):
        if val in indexMap and abs(indexMap[val] - idx) <= k:
            return True
        indexMap[val] = idx
    return False