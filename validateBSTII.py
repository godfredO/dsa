"""Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 
Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

So this is the effectively the same question as validateBST.py but the definition of the right subtree is different here, it can 
only contain vaus that are greater. As such if a value is equal to its lower bound, the tree is invalid. Otherwise its the same
preOrder traversal. 

There is also a post-order dfs version but I believe the preorder dfs is more useful for similar questions. The reason is that 
in the preorder solution, once we find that a node is invalid, we return False immediately, there is no need to go all the way
down its subtrees and as such will perform better on average even though both solutions have the same time and space complexity.
The only situation where they will run in the same time is when dealing with a valid tree. Since in that case even the pre-order
will go all the way to the end of the tree and then back. So the optimized optimal solution is the preorder solution.
 
"""

"""Pre-order dfs way"""
#O(n) time | O(d) space
def isValidBST(root):
    return helper(root, float("-inf"), float("inf"))

    
def helper(node, lowerBound, upperBound):
    if node is None:
        return True
    
    if node.val <= lowerBound  or node.val >= upperBound:       #validate current node
        return False
    
    leftIsValid = helper(node.left, lowerBound, node.val)       #go left to validate left child  / subtree
    rightIsValid = helper(node.right, node.val, upperBound)     #go right to validate right child / subtree
    
    return leftIsValid and rightIsValid  #return the result of validate left and right (child / subtree)
        

    



"""Post-order dfs way"""
class Solution:
    def isValidBST(root):
        return helper(root, float("-inf"), float("inf"))

    
def helper(node, lowerBound, upperBound):
    if node is None:
        return True
    

    leftIsValid = helper(node.left, lowerBound, node.val)        #validate entire left subtree
    rightIsValid = helper(node.right, node.val, upperBound)     #validate entire right subtree
    
    nodeIsValid = node.val > lowerBound  and node.val < upperBound   #validate current node
     
    return leftIsValid and rightIsValid and nodeIsValid             #return result of validating entire subtre
        