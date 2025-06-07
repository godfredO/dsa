"""Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node. This question is obviously a foundational question to node depths sum question. In that 
question we dont use the recursive stack but implement our own stack to supply node depths and sum them up. We do the same thing here, but 
this time we track the greatest depth we encounter. The reason is because the question is obviously asking , what is the depth of the binary 
tree. So we start at the root, and use breadth-first search to process the nodes one layer at a time, skipping over None nodes but instead of 
summing up the node depths, we take the maximum depth seen , which will be the depth of the deepest node. We could also do a recursive version 
by instantiating a class object that tracks the max depth seen. 

Now for whatever reason, maximum depth is defined in terms of number of the number of nodes along the longest path from the root node to the 
farthest leaf node instead of the number of edges between a node and the deepest leaf node. So we initialize the root node with a depth of 1 
instead of 0. So as a note, in binary tree, depth, height questions, make sure to check the definition because even on algoexpert, the 
binaryTreeDiameter.py question gives a leaf node a height of 1 (ie defining in terms of number of nodes) but the heightBalancedTree.py does 
the right thing of giving a leaf node a height of 0 (ie defining in terms of the number of edges). 

The recursive solution is a preorder dfs since our base case is the root ie we know that the depth of the root is 1 and we bubble this down 
to calculate depth of every node. An optimization that can be added is that in the visit step (updating the max depth seen), we know the only
node's worth considering really are leaf nodes, so we can surround this check in an if statement to only visit if the current node is a leaf
node otherwise just skip visiting and go left then go right. There are some questions where the visit step only takes place at a leaf node.
For a fun reversed version of this question checkout minDepthOfBinaryTree.py where it is essential that the visit step only happen at a leaf
node.
"""


"""Breadth-first search Iterative Version"""
#O(n) time | O(n) space
def maxDepth(root):
        maxDepth = 0
        stack = [[root, 1]]
        while stack:
            current, depth = stack.pop()
            if current is None:
                continue
            maxDepth = max(maxDepth, depth)
            stack.append([current.left, depth + 1])
            stack.append([current.right, depth + 1])
        return maxDepth


"""Recursive version, PreOrder Depth-first Search"""
#O(n) time | O(d) space
class Depth:
    def __init__(self,value):
        self.value = value

def maxDepth(root):
    deepest = Depth(0)
    return helper(root, 1, deepest)

def helper(node, depth, deepest):
    if node is None:
        return
    
    deepest.value = max(deepest.value, depth)

    helper(node.left, depth + 1, deepest)
    helper(node.right, depth + 1, deepest)


"""Recursive version, PreOrder Depth-first Search - only visiting leaf node"""
#O(n) time | O(d) space
class Depth:
    def __init__(self,value):
        self.value = value

def maxDepth(root):
    deepest = Depth(0)
    return helper(root, 1, deepest)

def helper(node, depth, deepest):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        deepest.value = max(deepest.value, depth)

    helper(node.left, depth + 1, deepest)
    helper(node.right, depth + 1, deepest)