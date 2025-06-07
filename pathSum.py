"""Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all 
the values along the path equals targetSum. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

So it seems like this is the targetSum binary tree version like twoSum.py, threeSum.py, fourSum.py array questions. Anyway, we use a 
preorder dfs where the visit step only occurs at leaf nodes. So we initialize a runningSum with the additive identity ie 0 and make a
recursive call starting from the root. Now the solution is written assuming that the root node is not going to be None. So we increment 
the running sum with the current node value .We then check if the current node is a leaf node in which case we visit ie check if the 
running sum equals the targetSum and return the boolean answer. If the current node is not a leaf node, we make recursive calls
to the left and right subtrees with this updated runningSum and return the result of rec(left) or rec(right), ie di we find the target
sum at a leafnode in the right or left subtrees? Since some nodes might have a None child, if the call Node is None we simply return
False. The underlying idea is that we are computing every possible root to leaf path sum aka branch sum and whenever we get to the
leaf node, we check if this sum is the target and we bubble it up the tree. 
"""
def hasPathSum(root, targetSum) :
    runningSum = 0
    return helper(root, targetSum, runningSum)

def helper(node, targetSum, runningSum):
    if not node:
        return False
    
    runningSum += node.val
    if node.left is None and node.right is None:
        return runningSum == targetSum

    return helper(node.left, targetSum, runningSum) or helper(node.right, targetSum, runningSum)