"""Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
nums is sorted in a strictly increasing order.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

So this question is exactly the same question as minHeightBst.py. Just that instead of telling as the sorted array has unique elements
they instead say that the array is sorted in strictly increasingly order, and this information is tucked away at the end of the
question.

So read minHeightBst.py for the solution explanation. But this is what I will say here, binary tree and binary search tree question 
that are solved with depth-first search may be preorder, inorder or postorder. This solution is preorder. The visit step here involves
calculating the middle index value, extracting the middle value, creating the root of the current subtree. Going left is calling the
recursive function on values from startIdx to midIdx - 1 and setting the returned node as the left child and really left subtree of the
current root nde. Going right is calling the recursive function on values from midIdx + 1 to endIdx and seting the returne node as the
right child (subtree) of the current root node. By the time a child node is returned that entire subtree would have been completed.

There is another question that expands this idea to a linked list 

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums) :
        return helper(nums, 0, len(nums) - 1)


def helper(nums, startIdx, endIdx):
    if startIdx > endIdx:
        return None
    
    midIdx = (startIdx + endIdx) // 2
    midVal = nums[midIdx]
    
    root = TreeNode(midVal)
    
    root.left = helper(nums, startIdx, midIdx - 1)
    root.right = helper(nums, midIdx + 1, endIdx)
    
    return root
        