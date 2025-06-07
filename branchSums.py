"""
Tags: Binary Search Tree; Dfs; Hard

The question gives the root node of a binary search tree and asks to return the sum of branches from the leftmost branch to the rightmost
branch. A branch is a path of nodes in a tree that starts at the root node and ends at any leaf node. The first observation is to notice that
the root node's value will be added to every branch sum because the root node is part of every branch. The root's left / right child's value
will be added left/right subtree branch sums and so on and so forth. The second key is realizing what a leaf node is. A leaf node is a node
that has None as left child and None as right child. The third key is realising that some node's may have one None child node and one BST
child node. So the idea is to initialize a running Sum as 0 and initialize the output as an empty list. We then call a helper function with
the root node, the running sum and the output. Inside the helper function we increment the runningSum with the current node's value, then
we check if the current node is a leaf node. If it is a leaf node we append the updated runningSum to the output and then return, this is
one base case. If we don't hit this return we call the helper function on the current node's left child with the updated runningSum and output
followed by the current node's right child with the updated runningSum and output. It is essential to call on the left child first since this
is the custom with binary trees and also because the question asks that the branch sums be ordered left to right, and calling on the left child
first and the right child next ensures that we reach leaf nodes from left to right and thus append branch sums from left to right. Finally,
we add the other 'base' case of a None node at the very top where we just return. This is to handle the case where we call the helper function
from a node that has one None child and one BST child. This is an actual first 'base' case since we could add lines to check if a child is not
None before calling the helper function on it. The main thing is do the leaf node check and append and return at the leaf node since this is the
'actual' base case, here checked second to to avoid accessing the value attribute on a None value. If we mistakenly add the appending step to
the None node return statement we will append each branch sum multiple times, 2 times for each leaf node, and one additional time for the nodes
with one None child. So the real base case is to check if the currentNode is a leaf node and append and return. The None node check is just for
simplification of code. Also I would like to make a note about how variables work in recursion. Since we are increment the sum with a node's
value, when the recursion goes down the left and back up to the current node, the sum varible accessed by the right call does not reflect
what was done in the left child call, it still whatever the value was before the left child call. This is an important general realization.

This solution uses depth-first search to traverse the tree, since we go down the tree recursively and then come back up when we reach a
base case. And the key lies in updating the running sum before checking for the second base case of a leaf node, and understanding that the
state of the running when execution returns back up the tree. """


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(N) time | O(N) space


def branchSums(root):
    sums = []
    # the recursive function doesnt return anything, it just appends values to a list
    calculateBranchSums(root, 0, sums)
    return sums

# this is the actual recursive function


def calculateBranchSums(node, runningSum, sums):

    newRunningSum = runningSum + node.value  # at each node re-calculate runningSum by add node's value
    if node.left == None and node.right == None:  # if at a leaf node, append running Sum
        sums.append(newRunningSum)
        return  # end the particular recursive call when base case is reached

    # recursive case
    children = []
    # check that left child isnt None. Need to add the left first since the question wants the branch sums to be
    # left to right
    if node.left is not None:
        children.append(node.left)

    if node.right is not None:
        children.append(node.right)

    for child in children:
        calculateBranchSums(child, newRunningSum, sums)

# because this is a binary tree we know that only every node has two children except leaf nodes that have None for both
# in otherwords, if the question tells us this is a binary tree, we dont have to worry about non-leaf nodes having None
# for one descendant and a node for the other descendant. However, we can simplify the recursive case and handle this edge
# case


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = runningSum + node.value  # at each node re-calculate runningSum by add node's value
    if node.left == None and node.right == None:  # if at a leaf node, append running Sum
        sums.append(newRunningSum)
        return  # end the particular recursive call when base case is reached
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
