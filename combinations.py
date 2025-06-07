"""Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n]. You may return the answer 
in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:
Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


So just a comment, but if k was a specific number which we were assured was always going to be valid eg k=2 then we would use a couple of
nested for loops to solve. But k is a variable, so we dont know how nested how function will have to be. Backtracking allows us to write a 
general solution that can go as deep as needed. 

This question is obviously the precursor to combinationSum.py and combinationSumII.py but rather find it useful to review those questions 
first. To follow the pattern in those questions, I first declare a candidates array a lis from range(1,n+1) and loop over this with indices 
from range(n).So the first solution actually uses the same left/right subtree branching where we choose one element going left but dont 
choose that element again going right. Now since there are unique elements and each element can only be used once, when we go left, or go 
right, we pass in the same sub-array. In the code we use the start index of the subarray. Thus in when going left or right we still pass in 
idx+1. The first base case is to check if our current combination array is equal to length k. In which case we append the combination to the 
result array and return. The second place is if we are out of bounds ie idx == len(candiddates) in which case we return. That is if we have a 
valid combination and are out of bounds, we want to append and return otherwise we return. This solution is O(2^(n+k)) time and O(n+k) space. 
Can we do better?

And the answer is yes. And to do this we realize that we can compress our tall binary recursive tree, into an shorter n-ary recursive tree. 
So instead of going n levels before we choose the last element as a first value of a combination, we compress the tree, by making the first 
level be the level for choosing any of the n elements as the first value of a combination. Since we are using indices, we know that the
whatever for any idx chosen in the first level, the second level will start from idx + 1. Why are we able to do this? Well, we use a binary 
decision to give us more control to avoid having duplicate combinations. But in this question, we are given unique elements and wecan only use 
each element once ie we are neither in the combinationsSum.py nor combinationSumII.py situations. By a clever use of for loops we can compress
our decision tree and improve time complexity and space complexity.

How do we use a for loop to choose different values for the 1st, 2nd etc values of a combination in each level of our n-ary decision tree. We
have a for loop that loops over the indices from range(startIdx, n) and for any idx chosesn in this list we make the next call with idx + 1, 
and when the call concludes, we backtrack by poppinng and making another choice for whichever level we are at. That is the for loop is going 
to choose the values at different indices for our current level, and for each chosen value, goes to the next level. In this solution our for 
loop wont even run if we are out of bounds, so we only need to check for the case where the length of a passed combination equals k. This 
solution is O(n^k) time and O(k) space. 

The third and most optimized solution is essentially realizing that we dont need a candidates array which we loop over with indices. The
indices themselves can be our candidates. So our initial set of indices will be from 1 to n. As such we make our first dfs call with
startIdx of 1 and in the dfs we loop from 
"""

def combine(n, k) :
        candidates = list(range(1,n+1))
        result = []
        current = []
        dfs(0, current, candidates, result, k, n)
        return result

def dfs(idx, current, candidates, result, k, n):
    if len(current) == k:
        result.append(current[:])
        return
    if idx == n:
        return
    
    current.append(candidates[idx])
    dfs(idx + 1, current, candidates, result, k, n)
    
    current.pop()
    dfs(idx + 1, current, candidates, result, k, n)

       
"""Explicity defining a candidates array"""
def combine(n , k) :
        candidates = list(range(1,n+1))
        result = []
        dfs(0, [], candidates, result, k, n)
        return result

def dfs(startIdx, current, candidates, result, k,n):
    if len(current) == k:
        result.append(current[:])
    
    for i in range(startIdx, n):
        current.append(candidates[i])
        dfs(i+1, current, candidates, result, k, n)
        current.pop()


"""Optimized solution"""

#O(n^k) time | O(k) space
def combine(n, k) :
        result = []
        dfs(1, [], result,k,n)
        return result

def dfs(start, comb, result,k,n):
    if len(comb) == k:
        result.append(comb[:])
        return
    
    for i in range(start, n+1):
        comb.append(i)
        dfs(i+1, comb, result,k,n)
        comb.pop()

