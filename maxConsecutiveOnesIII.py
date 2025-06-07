"""Given an array A of 0s and 1s, we may change up to K values from 0 to 1. Return the length of the longest (contiguous) 
subarray that contains only 1s. 

Example 1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1


So this is a direct continuation of maxConsecutiveOnesII.py and really I use the same solution with one change. Namely, we
shift the left pointer as long as the zeroCount is greater than k, instead of the hard-coded 1 in that solution. Thats all.
So read maxConsecutiveOnesII.py first.
"""
def longestOnes(A,K):
    zeroCount  = 0 
    maxLength = 0
    left = 0
    for right in range(len(A)):
        if A[right] == 0:
            zeroCount += 1
        
        while zeroCount > K:
            if A[left] == 0:
                zeroCount -= 1
            left += 1

        length = right + 1 - left
        maxLength = max(maxLength, length)
    
    return maxLength


A = [1,1,1,0,0,0,1,1,1,1,0] 
K = 2
print(longestOnes(A,K))