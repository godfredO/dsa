"""Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique 
values from 1 to n.
 
Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

This question is the same as binaryTreetopologies.py. Look in there for the explanation for how we go from dfs to dfs with memoization,
to dynamic programming.
"""
def numTrees(n):
    numWays = [0]*(n+1)
    numWays[0] = 1
    numWays[1] = 1

    for treeSize in range(2,n+1):
        for leftSubtreeSize in range(treeSize):
            rightSubtreeSize = treeSize - 1 - leftSubtreeSize
            unique = numWays[leftSubtreeSize] * numWays[rightSubtreeSize]
            numWays[treeSize]+= unique
    return numWays[-1]

n = 2
print(numTrees(n))