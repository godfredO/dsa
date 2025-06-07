"""Given a n-ary tree, find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node 
down to the farthest leaf node. Nary-Tree input serialization is represented in their level order traversal, each group of children 
is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

This is the same as the maxDepthOfBinaryTree.py but generalized for a tree that can have many children nodes (chekout of the node
interface). Thus, the equivalent of a leaf node is a node whose children attribute is an empty list, and since the question is 
asking for the depth of the deepest leaf node, I optimize my code to only visit leaf node, where the visit step is updating the
stored maxDepth value. Also the go left , go right step is replaced by looping over the children nodes stored in the children 
atrribute list, and calling the recursive function, with the incremented depth information.
"""

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Depth:
    def __init__(self,value):
        self.value = value
        
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        deepest = Depth(float("-inf"))
        postOrderDfs(root, 1, deepest)
        return deepest.value 
  
def postOrderDfs(node, depth, deepest):
    if not node: #just return from None leaf child recursive call
        return 
    
    if not node.children: #a leaf node will have an empty children attribute list, 
        deepest.value = max(deepest.value, depth)
    
    for child in node.children:
        postOrderDfs(child, depth + 1, deepest)