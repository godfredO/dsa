"""Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the 
same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false


Given the root of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same 
if they are structurally identical, and the nodes have the same value. By structure we mean if one tree is root, leftChild, rightChild, the 
second tree has to have the same. In addition these nodes should contain the same values ie tree= [rootVal, leftVal,righVal] has to be the 
same for both trees.

So the way to go about this is to compare node values one node at a time. If the root node is None for both nodes we return True ie if we
get to the child of a leaf node. If only one node is None or they don't have the same values then the trees differ structurally and have
different values so we return False. So those are the two base cases. Both nodes are None, True. One node is None or the values differ.
Then we recursively call the funcion  on the left children and the right children  and we return True if both are True or False if both
are False or one is False ie return rec(root1.left,root2.left) and rec(root1.right,root2.right).

Now, if we find that the root nodes are not the same value, then there is no need to go further. This means that we visit the currentNode
before going left and then right. As such this solution is a preorder dfs. Another preorder dfs question is validateBSTII.py.
 """


"""Same pre-order Dfs, just cleaner coding"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p , q) :
    if not p or not q: #if either node is None then True if both are None, False if only one is None
        return not p and not q #so check if both are None
        
    if p.val != q.val: #at this point neither is None so if their values don't match return False
        return False
        
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right) #if values match, compare left subtrees and right subtrees


"""Preorder Dfs"""
#O(p+ q) time | O(d(p)+ d(q)) space
def isSameTree(headOne, headTwo):
    if headOne is None and headTwo is None: #base case, end of a branch
        return True
    
    # if the binary trees are structurally different (None node vs Bst node) or differ in value, return False,
    if (headOne is None and headTwo is not None) or (headOne is not None and headTwo is None) or (headOne.value != headTwo.value):
        return False
    
    #if current node is the same the check left subtree and right subtree and return the result of checking both subtrees
    return isSameTree(headOne.left, headTwo.left) and isSameTree(headOne.right, headTwo.right)


"""Preorder Dfs- different coding, same solution"""
def isSameTree(p, q): 

    if not p and not q: #if both nodes are None, not q = True , not q = True, not p and not q = True and True = True
        return True

    #False if only one is None (already took care of both being None, we only hit this if only one is None) or If values dont match
    if not p or not q or p.val != q.val : 
        return False

    
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


