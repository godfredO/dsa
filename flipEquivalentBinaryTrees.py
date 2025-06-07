"""For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees. 
A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.Each tree 
will have unique node values

Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false


This question build on invertBinaryTree.py, where we invert a binary tree, really by flipping it or switching all the left and right
subtrees in the tree. Here a flip operation is defined as choosing any node and swapping the left and right child subtrees. A binary
tree X is flip equivalent to a binary tree Y if and only if we can make x equal to Y after some number of flip operations. Also, there
are unique values in the trees. Now we can start from the root nodes of both trees. If the values are not equal then we know that a 
flip operation cant fix that so we return False. If the values are the same however then we go to the left and right subtrees. Now in 
the case where the sturcuture and values of the left and right child of the root nodes are the same we can move further down the tree,
then we don't need a flip operation and are actually considered flip equivalent. On the other hand, if after a flip operation, the 
values and sturcuture of the left and right child is the same, we know that it is flip equivalent. If both nodes are None, they are
flip equivalent. If only one node is None they are not flip equivalent. 

In the code, we check the case where we are dealing with None values. If node1 is None or node2 is None, then we want to return whether
both of them are None, which will yield True if thats the case and False if only one is None. Then we say if check if the values of
the two nodes are the same. If they are, not we return False. If they are we need to check the subtrees. There are two cases, the no
flip case and the flip case. In the no flip case we compare corresponding children, ie left1 vs left2  and right1 vs right2 child. In
the no flip case, we compare opposite children ie left1 vs right2 and right1 vs left2 and we return the result of flip or no flip calls.
If one of them return True, it is flip equivalent, if both return False, then the values or structure are different and can't be fixed
with a flip operation. Since we visit the current node first before making the children calls, this follows a preorder dfs pattern.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""Preorder dfs """
#O(n) time | O(d) space
def flipEquiv(root1, root2):
    return helper(root1, root2)

    
def helper(node1, node2):
    if not node1 or not node2:   #if one of them is None, its flip equivalent if both are None else False
        return not node1 and not node2  #are both of them None
    
    if node1.val != node2.val: #visit, if root values are not the same return False, else check direct/ flip equivalency of child nodes
        return False
    
    noflip = helper(node1.left, node2.left)  and helper(node1.right, node2.right) #check direct equivalency of child nodes
    flip =   helper(node1.left, node2.right) and helper(node1.right, node2.left)  #check flip equivalency of child nodes
    
    return noflip or flip


