""" Now this question gives the root node of a binary tree and asks to return if it is height balanced. A binary tree is height balanced if 
for each node in the tree, the difference between the height of its leaf subtre and the height of its right subtree is at most 1. Thus
for the subtree rooted at a node we compare the heights of its left child and right child ie the number of edges between the left/right
child and the deepest leaf node in the left/right child subtree.  Final observation is that just like the diameter question, we use a tree 
info object to send data. So in this question, we bubble up the answers so that if one of the subtrees is not height balanced the False will
actually bubble up to the original call. So note that in math if you subtract two instances the same value you get 0 whether negative of
positive, so 2 - 2 = 0, -1 - (-1) = -1+1 = 0. So even though I like to initialize my None values with a height of -1 so that the leaf node
gets a height of 0, instead of algoexpert's choice of giving a None a height of 0 so that a leaf node has a height of 1, it still doesnt
matter because as long as the height values from leaf nodes are the same, their difference is 0 and this is less that 1 so the root of a
such a three node system will be height balanced, as will the left leaf node subtree and right leaf node subtree. So just like the diameter
question we need the height info from left/right subtree and we also need to know if those subtrees were height balanced. So using the
left/ right child heights, we calculate the current node's height as 1 + max(left.height, right.height), the height being the length of the
node to its deepest leaf node in either subtree. Then we return the height info as well as left.isBalanced and right.isBalanced and abs(
left.height - right.height) < = 1."""

class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

#when the base case of getTreeInfo is reached, it returns an instance of this object, easy to read, easy to translate
class TreeInfo:
    def __init__(self,isBalanced,height):
        self.isBalanced = isBalanced
        self.height = height


def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(node):
    #base case, 
    if node == None: #the value used here differs
        return TreeInfo(True,-1) #a null node is balanced  

    #recursive case , if the node is not None ,we want to get the TreeInfo for the right subtree and left subtree
    
    leftSubtreeInfo = getTreeInfo(node.left)
    rightSubtreeInfo = getTreeInfo(node.right)

    #we bubble up True for every node seen thus far is balanced, False for some node seen thus far is imbalanced
    isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced and abs(
        leftSubtreeInfo.height - rightSubtreeInfo.height) <= 1
    height = 1 + max(leftSubtreeInfo.height,rightSubtreeInfo.height) #this is the same as for the path question
    return TreeInfo(isBalanced,height)
