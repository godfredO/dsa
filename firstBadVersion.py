"""You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of 
your product fails the quality check. Since each version is developed based on the previous version, all the versions after 
a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which 
causes all the following ones to be bad. You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1


This is a binary search question that follows the generalized template in binarySearchII.py. Since the product numbers are 
sorted in ascending order, and since all the versions after the first bad version will all be bad, the answer is the minimal
version number for which the API isBadVersion(version) returns True. Here we initialize left as the first version, 1 and 
right as our last version, n, thus capturing the space of possibilities in ascending order. We dont have to write the condition,
however, we just have to call it, since Leetcode will implement that on the backend. 
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left , right = 1 , n
        
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

def isBadVersion(i):
    pass