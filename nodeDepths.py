""" The depth of a node is the distance between the root node and the node itself. This means the root's depth is 0 since its a distance of 0
from itself. The node's children are a distance of 1 and therefore have a depth of 1. Thus as we go down the tree, we keep adding 1 to the
current node's depth to yield the depth of its children. So lets start with the recursive solution. In that solution we add a default depth 
value of 0 to the function called on the root node. Inside the function we say that we return the passed depth plus the result of calling 
the recursive function on the child node's with a depth+1 nodeDepth value. Because we are adding theses sums directly, we say that when we
reach a None node, return 0 so that we do not have to add up an integer and None type. Thus we keep calling the recursive function on child
nodes until we reach None child nodes of a leaf node. Then we return 0 from both None child nodes , evaluate the sum of the leaf node's depth
plus 0 plus 0 and return that to its parent who add its passed node to the nodeDepth sum of its children. Thus we evaluate the nodeDepth sums
from the bottom of the tree to the root where we return the sum of 0 + the nodeDepthsSum of LeftSubtree + nodeDepthsSum of RightSubtree.

The iterative version is actually a breadth-first search approach, since we add a node to a queue or stack and pop it and process all of its
children nodes, with an increment of the popped node's depth information. Since we are only returning the sum of node depths, instead of the
typical use of breadth-first search for shortest path, we can actually use a stack instead of a queue to add up the sum of node depths, since
order doesnt matter here, meaning we can add the right child node first before the left child node and we will still get the same sum. A
graph problem that implements breadth-first search in the way shown here for a binary tree (ie adding addtional information to nodes) is 
openTheLock.py. 

The recursive approach is rather depth-first search since we recursively go left down a tree, sum up all the depths down one branch, return up
the tree to go right and sum up all the depths down another branch with the updated node information. Now since the order doesnt matter here
we could still go down the right subtree before the left subtree here but we are still backtracking up the tree which is a depth-first search.

The difference between the iterative (breadth-first search) and recrusive (depth-first search) is the space of the queue/stack vs the recursive
stack, and backtracking ensures that the recursive stack is the height of the tree, while breadth-first search ensures that the queue/stack
could potentially be the size of the tree ie O(h) vs O(n)."""

"""Iterative approach"""
#O(n) time | O(h) space
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack)>0:
        nodeInfo = stack.pop()
        node,depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOfDepths  += depth #this is the counter that is taking in each nodes depth and calculating a running Sum
        stack.append({"node":node.left, "depth": depth + 1})
        stack.append({"node":node.right, "depth": depth + 1})
    return sumOfDepths


"""Recursive approach"""
def nodeDepths(root,depth=0):
    #base case
    if root is None: #when we call this function recursively on the left and right children of leaf nodes
        return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)