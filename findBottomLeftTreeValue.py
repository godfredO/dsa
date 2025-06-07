"""Given the root of a binary tree, return the leftmost value in the last row of the tree.

Example 1:
Input: root = [2,1,3]
Output: 1

Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

So as far as question groupings, this question reminds of binaryTreeRightSideView.py. Basically, we are looking for the deepest leftmost 
node in the tree. If all levels are filled up, we would just keep going left until we get to a leaf node. But in the general tree which 
may be lopsided, in which case the leftmost node in the last row may be in the right subtree of the current root. So like in 
binaryTreeRightSideView.py, we can use the depth-based bfs and we can initialize a leftMostNode at the root and a leftMostDepth variable 
at a depth of 0. We also initialize our queue with the the root node and depth 0. Inside the queue, we popleft(), skip if the current node 
is 0. Then we check if the current node's depth is greater than the leftMostDepth variable, and if it is, we update the leftMost to the 
current node and the leftMostDepth to the current depth. Then we add the current node's left and right child with incremented depth. Now
by adding the left child before the right child we ensure that the leftmost node from each level is added first, that way, since we only
check for greater than (instead of greater than or equal to), from each level, we will pop the leftmost node first and update leftMost
to this node after which all the other nodes on the same level will fail this test. Also, since we continually increment the depth info
each time, we will eventually update leftMost to the leftmost node in the last row of the tree. At the end we return the value of the 
leftMost node. 

The preorder dfs version of the bfs above, uses a custom object to track the depth and value of the deepest node encountered so far, 
and uses the same logic of using a greater than comparison and going left first before right. 

Also, we could also go right, go left in which case we use a greater than or equal because in that case the leftmost node on any level 
will be the last node we see. To further optimize, we dont even need the depth information if we go right to left, we can just make our
leftMost the last node we say, so this reference will keep moving from level to level right to left and the last time will be pointing
to the leftmost node from the last row in the tree. We can further optimize by only adding non-None child nodes to the queue.

"""
from collections import deque
def findBottomLeftValue(root) :
    queue = deque()
    queue.append([root, 0])

    leftMost = root
    leftMostDepth = 0

    while queue:
        node, depth = queue.popleft()
        if node is None:
            continue
        if depth > leftMostDepth:
            leftMostDepth = depth
            leftMost = node
        
        queue.append([node.left, depth + 1])
        queue.append([node.right, depth + 1])
    
    return leftMost


"""Dfs approach pre-order"""
class TreeInfo:
    def __init__(self, value, depth):
        self.value = value
        self.depth = depth

def findBottomLeftValue(root) :
    treeInfo = TreeInfo(root.val, 0)
    dfs(root,0, treeInfo)
    return treeInfo.value

def dfs(node, depth,  treeInfo):
    if node is None:
        return
    
    if depth > treeInfo.depth:
        treeInfo.value = node.val
        treeInfo.depth = depth
    
    dfs(node.left, depth + 1, treeInfo)
    dfs(node.right, depth + 1, treeInfo)

"""Bfs II going right to left"""
def findBottomLeftValue(root) :
    queue = deque()
    queue.append([root, 0])

    leftMost = root
    
    while queue:
        node= queue.popleft()
        
        leftMost = node.val
        
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    
    return leftMost

