"""Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to 
the original key plus the sum of all keys greater than the original key in BST. As a reminder, a binary search tree is a tree that 
satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

All the values in the tree are unique. root is guaranteed to be a valid binary search tree.

Example 1:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Example 2:
Input: root = [0,null,1]
Output: [1,null,1]

So let's start at the root and ask what values are greater than the root value? The answer is all the node's in its right subtree. So
we will need to sum up all the values in the right subtree, so we will need to first make a recursive call to the right child. With 
this value, we increment the root's value. So go right, then visit. For the root's left child, what values are greater than it? And 
the answer is the root and the root's right subtree, so we will need to increment the left child's value with the updated value of the
root. So we will need some sort of running sum object that we can update, and we will need a reverse inorder dfs algorithm. 

We go to the right child of the current node, before visiting the current node and then we go to the left child of the leaf node. So
what does the visit step entail here. We store a temporary reference to the node's current original value, then we update the node's 
value with the current value stored in the running sum object. Then we update the value stored in the running sum object with the temp 
reference to the current node's original value before making the call to the left child of the current node.

So in a three-node system, now does it look like. We initialize the running sum object with a value of 0, then make a call to the right
child of the root. At the right child we make a call to its right child which is a None node so we return immediately from it. So we
visit the right child of the root. We first store a temporary value to the right child's value, increment its value with the 0 stored
in the running sum object, before updating the running sum object's value with the right childs original value. When execution returns
to the root parent, the running sum object has the value of the right child, so we store a temp value to the root's original value,
increment its value with the right childs value that is stored in the running sum object, then update the running sum object value with
the original value of the node before making a call to the left child. The left child will attempt a call to its right child first, which
returns, stores a reference to its original value before incremnting its value with the running sum value which now contains the root and
root's right child's values before incrementing the running sum object's value wih its own value and then makes a call to its left child
which is None and returns immediately. Execution returns to the root where all calls are completed and we return the root node.

This question is actually one of the few binary (search) tree questions that is an application of inorder dfs, the other being
rightSiblingTree.py. I find that sussing out what happens in the visit step of inorder dfs application questions isnt the most direct.
"""
def convertBST(root):
    greaterTree(root, 0)
    return root

def greaterTree(node, runningSum):
    if not node:
        return 
    
    greaterTree(node.right,runningSum)
    temp  = node.val  
    node.val += runningSum
    runningSum += temp
    greaterTree(node.left, runningSum)


class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        greaterSum = [0]
        self.dfs(root,greaterSum)
        return root
        
    def dfs(self,node,greaterSum):
        if not node:
            return
        self.dfs(node.right, greaterSum)
        greaterSum[0] += node.val
        node.val = greaterSum[0]
        self.dfs(node.left, greaterSum)