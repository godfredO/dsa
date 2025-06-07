"""
Tags: Binary Tree; Hard

Better summary
The diameter of a binary tree is the length of the longest path in the tree even if that path doesnt pass through the root of the tree.
A path in a tree is a collection of connected nodes in the tree such that each node in the path is connected to at most two other nodes.
So at each node we want to know the longest path that goes through it. If we have a root node with 1 right child and a left child, the
longest path in the subtree rooted at the root node goes from the right child to the root and to the left child ie the diameter of each
subtree will extend from one leaf node to another leaf node. How do we calculate this path?

We use the height of the child nodes and add 1 for the edge from the each child to the root. Since the height depends on the length of the
path to the deepest node, we choose which the child node with the greater height ie height = 1 + max(left.height, right.height). Then since
the diameter of the subtree is the path that extends from the deepest leaf node in the left subtree through the root to the deepest node in
the right subtree, diameter = 1 + left.height + 1 + right.height. Since a leaf node has a height of 0, when we get to a None node we return
a height of -1, so that 1 + max(-1,-1) is 0.

Now because we need to calculate the diameter of the subtree rooted at each node, we need to bubble up the height infomation from its left
and right subtrees. In addition we need to keep track of the largest diameter seen so far. So we need a way of comparing the calculated
diameter to the largest diameter seen so far in the left subtree and the right subtree. So each node will first make a recursive call to its
left child , and then to its right child. Each call will return the height of the child node and the largest diameter seen so far in that
subtree. The parent uses the height information to calculate its own height and diameter and updates the largest diameter seen by comparing
to the same values from both subtrees. To keep track we use an object which stores height and largest height seen in a subtree. At then
end we return this object up the tree. This solution thus uses a postorder dfs to go left, go right all the way down to leaf nodes before
visiting ie determing height diameter, updating largest diameter and returning an object with these two values."""

# Input class


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


""""Postorder Dfs -I"""


class TreeInfo:
    def __init__(self, value):
        self.value = value


def diameterOfBinaryTree(root):
    treeDiameter = TreeInfo(0)
    postorderDfs(root, treeDiameter)    # update diameter object in dfs
    return treeDiameter.value           # return diameter object value after dfs updates


def postorderDfs(node, diameter):
    if node is None:
        return TreeInfo(-1)  # height of None child is -1 so leaf node currentHeight is 0

    leftInfo = postorderDfs(node.left, diameter)    # get left child height
    rightInfo = postorderDfs(node.right, diameter)  # get right child height

    currentHeight = 1 + max(leftInfo.value, rightInfo.value)  # height of node
    currentDiameter = 1 + leftInfo.value + 1 + rightInfo.value  # diameter of node

    # update value stored in treeDiameter object being passed around
    diameter.value = max(currentDiameter, diameter.value)  # compare node diameter to max so far

    return TreeInfo(currentHeight)  # return height of node to its parent


"""PostOrder Dfs _ II, I bundle together the diameter information with height information"""


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

# preorder dfs


def binaryTreeDiameter(tree):
    return dfs(tree).diameter


def dfs(node):
    if node is None:
        return TreeInfo(0, -1)

    leftInfo = dfs(node.left)
    rightInfo = dfs(node.right)

    nodeHeight = 1 + max(leftInfo.height, rightInfo.height)
    nodePath = 2 + leftInfo.height + rightInfo.height
    treeDiameter = max(leftInfo.diameter, rightInfo.diameter, nodePath)
    return TreeInfo(treeDiameter, nodeHeight)


"""Recursive solution - algoexpert"""
# this class allows us to use dot notation in our code instead of


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

# O(n) time | O(h) space n= number of nodes in tree, h= height (depth) of tree


def binaryTreeDiameter(tree):
    return getTreeInfo(tree).diameter

# recursive function


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)  # return this object with specified diameter and height for Null node

    leftTreeInfo = getTreeInfo(tree.left)  # calculate diameter, height for left child subtree
    rightTreeInfo = getTreeInfo(tree.right)  # calculate diameter, height for right child subtree
    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height  # root Path for subtree
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)  # max diameter
    # compare root Path to descendant diameter
    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    # calculate height for ancestor to use
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)  # return the diameter, height to ancestor


# Older summaries
"""
How do we determine the height of a node? Well
the height of a node is the length of the path from the node to the deepest leaf node its connected to. The height of leaf nodes is 0,
and since the subtree at a node may be lobsided, the deepest leaf node in one subtree may be deeper than the other subtree. And so once
we have the height of child nodes we add 1 to the greater height to signify the path to the deepest leaf node. So since we only know the
height of the leaf nodes, we need to first go all the way down and work our way up the tree ie post order dfs. At each point after receving
the height information from the child nodes we calculate the height of the current node as 1 + max(left.height,right.height) and send that
up to the parent. Before we do that we also need to calculate the root path of the current subtree so 1 + left.height + 1 + right.height,
each 1 signifying each edge to the left and right child. If the child is None, we have the code returning a height of -1 to negate the +1
since there is no edge there. Then because we need to compare the root path of all the subtrees, our child nodes also return a diameter
information, and we compare the diameter of the current subtree """


"""A path in a tree is a collection of connected nodes in the tree such that each node in the path is connected to at most two other nodes.
A branch is thus a special path in that it must extend from the root node to a leaf node and no node in a branch path will be connected to
more than two nodes. Not all paths are branches however; they dont need to include the root node of the tree and can extend from one leaf
node to another leaf node, as long as none of the connected nodes of the path are connected to more than three nodes.

The height of a node in a tree is the number of edges on the longest path from that node to the deepest leaf node its connected to as we go
down from the node to this deepest leaf node. Another way of saying this is that the height of a node in a binary tree is the largest number
of edges (length) on a path from any leaf node to the target node, this time going up from the leaf nodes.

The diameter of a tree is the number of edges (length) on the longest path in a tree. Calculating the binary tree diameter involves
calculating the height of a binary tree. The height of a leaf node is 0, the height of a leaf node's parent is 1 if the leaf node in question
is the deepest leaf node its parent is connected to. The height of the root node in a binary tree is equal to the largest number of edges from
the root to the most distant leaf node. So we can observe that the depth of a binary tree (the number of edges from root to deepest leaf node)
is equal to the height of the binary tree (the number edges from the deepest leaf node to the root). The key to solving this problem is that
the longest path will go from one leaf node, through the root of some subtree and end at another leaf node, hence the need for height
information.

  """

""" To solve this problem, we do what we usually do with binary trees and reformulate the problem for the subtree rooted at each node. The
root diameter of any subtree is the path that includes the root of that subtree, its left child height and right child height. Now assuming
a subtree with a root and 2 leaf node children, the root diameter is 1+0+1+0 ie 1 + leftChild.height + 1 + rightChild.height. To simplify
the code, I choose to say a None value has a height of -1, so that a leaf node has 1-1+1-1= 0 height. Thus we need to know the left child
height, the right child height to calculate the root path. So at a particular node, what height do we bubble up the tree?  We bubble up the
height of the current subtree root node which depends on if the deepest leaf node its connected to is from its left or right chidld ie
height = 1 + max(left.height, right.height). Again for a leafNode, I choose to simplify by saying height = 1 + max(-1,-1) = 0. So using the
height information from child nodes we are able to calculate a node's height as well as the root path.

The diameter of the tree as whole will be equal to the root path of some subtree not neccessarily the root path of the actual root of the
tree. So we need some way of bubbling up the max diameter seen so far and for each node, the max diameter can be in its left subtree or
its right subtree. So in addition to bubbling up child node heights, we also need to determine the max diameter seen so far at each of the
child nodes. So since the tree diameter will be some root path, after calculating the root path through a node, we determine the max
diameter seen so far by comparing its root diameter to the max diameter seen by the left child and the right child. That is
treeDiameter = max(rootPath, left.diameter, right.diameter). For a leaf node, I choose to simplify my code so as to return the 0
from both None childValues so that treeDiameter = max(0,0,0) = 0. Then we bubble up the maxDiameter seen so far and the height of the
current node. As such we bundle these together and return an object TreeInfo(diameter, nodeHeight) That is, while in other question we update
a value stored in an object, here we actually return a new instance of the object each time with diameter and height information and each time
we receive objects, we access the information stored in them, use them for some logic and return another new instance of object, here called
TreeInfo. Now some algoexpert, initializes the None value height as 0 and calculates the curentHeight as 1+ max(left.height, right.height),
so that for a leaf node, the height is 1 instead of 0, and when this is returned in to the root of a threee-node tree, the roots height is
1 + max(1,1) = 2, but the reason they dont get a wrong answer is that when calculating the rootPath, the use left.height + right.height,
which for a leaf node, gives 0+0 = 0, the right answer and for the root of a three node tree, gives 1+1 = 2 again the right answer for the
diameter. So they are specifically returning values that will give the right diameter instead of the None height of -1 and using rootPath =
2 + left.height + right.height like I prefer, in order to access the correct height information. So they dont add 2 so that they can more
directly use left.height + right.height.
"""
