"""Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain 
duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

The question is actually asking us to return the powerset of an array of unique integers, and is the same question as powerset.py.
The solutions here are the same as in powerset.py. For a detailed explanation of the solutions, read powerset.py. The only reason
for this file is so that it is clear that its related to subsetsII.py.
"""

""" Breadth-first search style technique / Iterative / Dynamic programming solution """
def subsets(nums) :
    output = [[]] #base case
        
    for num in nums:
        size = len(output)    
        for i in range(size):
            newSubset = output[i] + [num]
            output.append(newSubset)            
    return output
        
"""Pre-order Depth-First Search Backtracking technique"""
def subsets(nums):
    result = [] #output array
    subset = [] #initial subset of the empty subset
    dfs(nums, 0, result, subset)
    return result

def dfs(nums, idx, result, subset):
    if idx >= len(nums):
        result.append(subset[:])
        return

    dontAdd = subset[:] #you need to make a copy, when choosing not to add the current element
    dfs(nums, idx + 1, result, dontAdd)

    doAdd = subset + [nums[idx]] #you need to make a copy, when choosing not to add the current element
    dfs(nums, idx + 1, result, doAdd)


"""Post-order Depth-First Search Backtracking technique"""
def subsets(nums):
    idx = len(nums) - 1
    return dfs(nums, idx)

def dfs(nums, idx):
    if idx < 0:
        return [[]]
    
    subsets = dfs(nums, idx - 1)

    size = len(subsets)
    for i in range(size):
        newSubset = subsets[i] + [nums[idx]]
        subsets.append(newSubset)
    
    return subsets