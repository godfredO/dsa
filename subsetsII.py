"""Given an integer array nums that may contain duplicates, return all possible subsets (the power set). The solution set must not contain 
duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

So this question is an extension of subsets.py (and powerset.py), only difference is that here, we can have duplicate values. So if you 
take the input [1,2,2], we know the powerset will always include the empty set as a subset [], now the single element subsets are [1],[2] 
(not [1],[2],[2]), and the double element subsets are [1,2], [2,2] ( and not [1,2], [1,2], [2,2]) and the last subset is [1,2,2]. So how do 
we avoid the duplicate [2] and [1,2] which our solution from subsets.py will give. We are already using a binary decision tree so are there
other techniques that will give us additional control in order to avoid these duplicates. And the answer is sorting. In otherwords the 
technique used in combinationSumII.py, which makes sense because we have are essentially getting some type of combination here.

So we first sort the input array, so that duplicate values are next to one another. Then in the left subtree, we choose a single instance 
of the current value and increment the index, meaning we could choose a duplicate value. In the left subtree, we choose no instance of the
value chosen in the left subtree. Hence we remove the chosen value, then use a while loop to advance the pointer till its pointing to the
last instance of the value we appended and popped, then we increment the index to make the recursive call that includes no instance of the
value chosen for the left subtree. When we get to the base case ie the leafnode of the current path, the index will be out of bounds (or
if we are slicing the arrays, we call with an empty nums array), in which case we append a copy of the current subset and return. We return
a copy because we are choosing to append and pop instead of creating new arrays.

There are 2^n subsets and we have n recursive calls so O(n*2^n) time and space complexity. Also 
"""

def subsetsWithDup(nums) :
    nums.sort()
    result = []
    subset = []
    dfs(0, nums, result, subset)
    return result


def dfs(idx, nums, result, subset):
    if idx >= len(nums):
        result.append(subset[:])
        return
    
    # All subsets that include nums[idx]
    subset.append(nums[idx])
    dfs(idx + 1, nums, result, subset)

    subset.pop() #backtrack

    # All subsets that dont include nums[idx]
    while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
        idx += 1
    dfs(idx + 1, nums, result, subset)
        
        