"""
Tags: Binary Tree; Hard

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder
traversal of the same tree, construct and return the binary tree. preorder and inorder consist of unique values. Each value of inorder
also appears in preorder. preorder is guaranteed to be the preorder traversal of the tree. inorder is guaranteed to be the inorder
traversal of the tree.

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]


In order to fully create a tree, we need its root node, the root's left subtree and after connecting the root node with its subtrees
we can return the root node of the completed tree. The root node value, is the value at index 0 of the preorder traversal. To create
the left and right subtrees and return the root of those subtrees we will need to call our recursive function with the preorder and
inorder array corresponding to the left subtree and right subtrees.

So how do we slice a given arrays into the left and right preorder and inorder arrays. First we need to realize that a preorder
traversal = [rootNode, leftSubtree, rightSubtree], and the inorder traversal is [leftSubtree, rootNode, rightSubtree]. We are told
that this tree contains unique values. So if we find the index of the rootNode in the inorder array, that index gives us the length of
the left subtree and we can use that to split the preorder and inorder traversals into left and right subarrays. ie rootVal = preOrder[0],
rootIdx = inorder.index(rootVal), leftSubarrays = preorder[1:rootIdx + 1], inorder[ : rootIdx] and rightSubarrays = preorder[rootIdx + 1 : ],
inorder[rootIdx + 1 : ]. At the end of the child recursive calls, we return the completed (sub)tree rooted at rootNode, the node with rootVal,
after connecting it with the returned root of the left and right subtrees. There are n nodes in the trees, so there will be n recursive calls
and inside each of these, we do a slice, the entire time complexity is O(n^2) and a space complexity of O(n) for the recursive call stack.
Since we have to build the entire left and right subtrees before we can complete the current (sub) tree and return its root, this is a
post-order dfs. Our base case is if we make recursive calls with empty arrays, we have a None node. If the input is valid and our logic is
correct the preorder and inorder slice arrays should always have the same length, meaning if one is empty, the other should be empty. But to
handle a potentially invalid input, we say if either array is empty, the tree in question is just a None node.
"""


"""Post-order dfs"""
# O(n^2) time | O(n) space
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder and not inorder:    # if the preorder and inorder lists are empty, None child
        return None                     # None child of a leaf node

    rootVal = preorder[0]               # root node of current preorder and inorder lists
    rootIdx = inorder.index(rootVal)    # O(N), get the index of unique root node value

    leftSubtree = buildTree(preorder[1: rootIdx+1], inorder[: rootIdx])  # O(n)
    rightSubtree = buildTree(preorder[rootIdx+1:], inorder[rootIdx+1:])  # O(n)

    return TreeNode(rootVal, leftSubtree, rightSubtree)  # return the root node of current subtree


"""Same solution, different class node interface"""

# O(n^2) time | O(n) space


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def buildTree(preOrder, inOrder):
    if not preOrder or not inOrder:  # if both lists are empty, its a None child
        return None

    root = BinaryTreeNode(preOrder[0])  # create root node
    # the number of values that come before the root node in the inOrder array is mid
    mid = inOrder.index(preOrder[0])    # index of root node in inorder array
    root.left = buildTree(preOrder[1:mid+1], inOrder[:mid])  # left subtree
    root.right = buildTree(preOrder[mid+1:], inOrder[mid+1:])
    return root


"""Given two integer arrays, preorder and inorder, where preorder is the preorder traversal of a binary tree and inorder is the
inordervtraversal of the same tree, construct and return the binary tree. We assume unique values.
preOrderTraversal = [rootNode, leftSubtree , rightSubtree ],      eg  2 < 1 > 3 = [1, 2, 3]
inOrderTraversal =  [leftSubtree , rootNode, rightSubtree ]       eg  2 < 1 > 3 = [2, 1, 3]

There are a couple of observations. One, the first value in the preOrder traversal array is always going to be the root of the binary
(sub)tree. This is because preorder traversal visits the root and proceeds to process the entire left subtree  before processing the
entire right subtree, ie the preOrder = [rootNode, leftSubtree , rightSubtree ]. In order traversal on the other hand  visits the
entire left subtree before visiting the root node and then right subtree ie inOrder = [leftSubtree , rootNode, rightSubtree ]. We
are assured of unique values in this tree. This means for any subtree, we know the rootNode is at index 0 in the preOrder, and we also
know that in the inOrder array, every value that occurs before this rootNode is in the leftsubtree. So after selecting the rootnode
value (index 0 of the preorder) we can find its position in the inorder and once we find this we know that every value that occurs
before it in the inorder array must be in its left subtree. To find the position of the root node in the inorder array, we can use
list.index(value) method to find the index of the root node in the inorder traversal ie idx = inorder.index(rootVal). This value, the
index tells us the size of the leftsubtree in the preorder traversal. Eg if the root node (index 0 in preorder), occurs at index 1 in
inorder, then we know that the leftsubtree has a size of 1. If the root node (index 0 in preorder), occurs at index 0 in the inorder
array, then we know that this root node has a None left child. So using this index, we can slice up the preorder array to select the
left subtree elements ie leftSubtree = preOrder[1:idx+1], making sure to start from the second value and using an endIdx of mid + 1
due to the slice end-exclusivity in Python. We also use this index to slice up the inOrder array for the left subtree ie leftSubtree
= inOrder[:mid], since we know that the leftSubtree will come right before the root node in the inorder array.

For the right subtree we can use the fact that in the preOrder traversal, the right subtree is visited after the entire left subtree
has been visited. Thus, if we know that the leftSubtree = preOrder[1:idx+1], then the right subtree must start from index idx to the
end of the preorder array, ie rightSubtree = preOrder[idx+1:]. We also use this index to slice up the inOrder array since we know that
the right subtree comes after the root node in the inOrder array ie rightSubtree= inOrder[idx+1:], since we know that the right subtree
willl come right after the root node in the inorder array.

So this is exactly what the code does. We choose the first element as the index 0 of preorder, get this unique root value's index in
the inorder and use this index to slice up the inorder and preorder arrays to yield array representing the left subtree and right
subtree. The recursive function returns the root node at the end, so after creating the root Node, we set the left attribute to the
result of the recursively calling the function on the leftSubtree slices and the right child attribute to the result of recursively
caling the function the rightSubtree slices. If we ever make a recursive call where one array is empty, we return None as the child
node.
"""
