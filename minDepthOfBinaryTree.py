"""Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node 
down to the nearest leaf node. Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 
This is basically asking what is the depth of the shallowest leaf node. The general logic is the same as maxDepthOfBinaryTree.py and
as such we use preorder dfs since our base case, the node with a known depth is the root. The three main points are that first since we
are doing a minimum comparison, we initialize our result variable at +inf. Secondly, we should only compare the depths of leaf nodes
in this question otherwise we know the root will have the shallowest depth of all. The final point is that we should handle the case of
an empty tree ie None root, where we return 0 since depth in this question is defined in terms of the number of nodes not number of edges.
Another preorder dfs question where the visit step is surrounded in an if statement , although this applies to every node, not just the
leaf nodes is the sameTree.py question ie if the root of the current subtree doesnt have the same structure or value don't go further 
(visit), otherwise go left then go right. 
"""

"""Preorder Depth-first search"""
#O(n) time | O(d) space
class Depth:
    def __init__(self,value):
        self.value = value
        
def minDepth(root ) :
    if not root:
        return 0
    deepest = Depth(float("inf"))
    helper(root, 1, deepest)
    return deepest.value 

def helper(node, depth, deepest):
    if node is None:
        return
    
    if node.left is None and node.right is None:   #visit step, visit only leaf nodes
        deepest.value = min(deepest.value, depth)
    
    helper(node.left, depth + 1, deepest)         #visit left
    helper(node.right, depth + 1, deepest)        #visit right
        