""" Binary Trees, Memoization, DP, Hard

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have
Node.val == 0. Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example 1:

Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],
[0,0,0,0,0,null,null,0,0]]

Example 2:
Input: n = 3
Output: [[0,0,0]]

This is another dynamic programming / recursion memoization tree question like binaryTreeTopologies.py , houseRobberIII.py, maxPathSum.py.
Now this question is a closely related to binaryTreeTopologies.py (aka uniqueBSTs.py) but instead of returning the number of different
trees we can create with n nodes, we are told that we can only consider full binary trees and we are to return an array of the structures
of all full binary trees with n nodes (the value version is written from top to bottom, left to right (like heaps which are binary trees
that follow the principle of completeness)). Anyway, what is a full binary tree? A full binary tree is a binary tree where each node has
exactly 0 or 2 children. So for n=0 we just have a None node, so [[Null]], for a n= 1, we have just the rootNode so [[0]] (we are told that
all tree values should have value of 0). Can we have a full binary tree with size 2? The topologies for n=2 [[0,Null,0], [0,0,Null]]
(extending from uniqueBSTs.py), neither tree is full, so we return []. In fact we can look back at n=0 and realize that it doesnt meet our
definition of a every node in a full tree having exactly 0 or 2 children. In other words if n % 2 == 0, we can't have a full tree because
some node will have only 1 child. What about n=3? Of the 5 topologies for n=3, only 1 is full ie [[0,0,0]], the remaining topologies
[[0,Null,0,Null,0], [0,0,Null,0,Null], [0,0, Null, Null, 0], [0,Null, 0, 0, Null]] all have some nodes with 1 child.

So to build the full tree, we start with the root node, so that is 1 node, after which we have n-1 nodes. Can we put all these n-1 nodes
in one subtree only eg if n=7 after choosing the root node, can we have 6 in the left/right subtree and 0 in the other? No, because then
the root will have 1 child and that isnt a full binary tree. So we have to put 1 node as the right child and 1 node as the left child of
the root node. So we have 7 - 3 = 4 nodes remaining. Now this is where it gets interesting. We can put choose to split the remaining nodes
into the right child's tree or the left child's tree or we can put all four in on child tree. If we split, then either child has 2 children
nodes. If we don't split the other child has 0 children nodes. So if we split, the right/left child of the root has to have 1 right child
and left child after which it has 0 nodes remaining. If we put it all in one child subtree, then it has to have a left and right child and
we will have reduced the number of remaining nodes by 2 and we can choose again to put it all in either child's tree, or split.

Another of saying this is that if n = 9, we choose the root nodes and of the remaining 8 nodes, the left subtree can have 1 node(left child)
and the right subtree can have 7 nodes total (including right child) or left subtree can have 3 nodes and right subtre can have 5 nodes or
left subtree can have 5 nodes and right subtree can have 3 nodes or left subtree can have 7 nodes and right subtree can have 1 node. So we
can use this to develop a dynamic programming solution. We know that our base case is that if n%2 == 0 we return [], otherwise we declare
our dynamic programming data structure of size n+1 and at each index, we store a empyty array. Then we know that we have another base case.
If n == 1, we have a rootNode, so in our array, at index 1, we append a binary treeNode of value 0 ie dp[1].append(TreeNode(0)). Then we
start an outer loop of treeSizes from n=3 to n, taking increments of 2 ie range(3, n+1, 2). Then inside this loop, initialize the left
and right subtree sizes as left = 1 and right = treeSize - 1 - left. Then with a while loop, we will be creating the full trees as we
increment left subtree size and decrementing right subtree size, so our loop condition is while right >= 1 to have a full binary tree.
Now we loop over the trees stored at dp[left] and for each tree, we loop over all the trees stored at dp[right], create a rootNode with
value 0 and update the left and right attributes of this root node with the current left tree as right tree. With this tree complete, we
append it to the array at dp[treeSize], the inside the while loop we increment left by 2 and decrement right by 2. This while loop may
be replaced with a for loop generating either leftSubtreeSize or rightSubtreeSize. At the end we return dp[n].

Now even though I have the dynamic programming solution, won't it be fun to explore the memoization recursion approach that yields the
dynamic programming solution? Welp, if you understand the dynamic programming solution, you can read and understand the memoization
recursion approach.

In summary this solution is based on some realizations about treeSize, leftSubtreeSize, rightSubtreeSize of the tree node, and
the relationships between these values for a full binary tree. Basically, if the treeSize is even, we know we cannot have a full
binary tree. If its odd, we form the root node and to form the left and right subtrees, we realize these are also bound by the
same size restrictions (no even sizes) and also are related to one another rightSubSize = treeSize - rootNode - leftSubSize.
So in this solution, we create configurations until we reach the treeSize in the question and then return that configuration.
There is a DP solution and its corresponding memoization solution since smaller tree size configurations are used to build
larger size configurations until configurations of the final tree size asked in the question is reached and returned. if __name__ == '__main__':
each step we use the dp/memoization/backtracking to obtain the subtrees, and attached to a newly created root node.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""Dynamic programming solution"""
# O(n^4) time | O(n) space


def allPossibleFBT(n):
    if n % 2 == 0:      # first base case, even treeSize has no full bst configurations
        return []

    # could also use list comprehension dp = {i:[] for i in range(n+1)}
    dp = [[] for i in range(n+1)]  # configuration of full binary trees, include 0 size trees
    dp[1].append(TreeNode(0))   # another base case, the configuration of treeSize = 1

    for treeSize in range(3, n+1, 2):  # +1 for end-exclusivity of Python's range, step = 2
        for leftSubtreeSize in range(1, treeSize, 2):
            rightSubtreeSize = treeSize - 1 - leftSubtreeSize  # -1 for the root node

            for leftSubtree in dp[leftSubtreeSize]:         # build on previous DP solutions
                for rightSubtree in dp[rightSubtreeSize]:   # build on previous DP solutions
                    root = TreeNode(0)                      # only need to create root node
                    root.left = leftSubtree                 # attach prev dp soln as subtree
                    root.right = rightSubtree               # attach prev dp soln as subtree
                    # dp[treeSize].append(TreeNode(0,leftSubtree,rightSubtree))
                    dp[treeSize].append(root)
    return dp[n]        # return the last dp solution as the correct configuration


"""Memoization recursive solution- backtracking"""


def allPossibleFBT(n):
    cache = {0: [], 1: [TreeNode(0)]}   # initialize configurations with known dp base cases
    return backTrack(n, cache)          # dfs backtracking function


def backTrack(treeSize, cache):
    if treeSize % 2 == 0:               # base case, treeSize cannot be even
        return []                       # no full bst tree configuration for even treeSize
    if treeSize in cache:               # prev dp solutions for use as left and right subtrees
        return cache[treeSize]          # save work by return from memoization

    fullTrees = []                      # all treeSize full bst configurations
    for leftSubtreeSize in range(1, treeSize, 2):           # leftSubSize from treeSize
        rightSubtreeSize = treeSize - 1 - leftSubtreeSize   # rightSubSize from leftSubSize, treeSize
        leftSubtrees = backTrack(leftSubtreeSize, cache)    # configurations treeSize=leftSubsize
        rightSubtrees = backTrack(rightSubtreeSize, cache)  # configurations treeSize=rightSubsize

        for leftTree in leftSubtrees:   # all full bst configurations of treeSize=leftSubSize
            for rightTree in rightSubtrees:     # all full bst configurations of treeSize=rightSubSize
                root = TreeNode(0)              # create root node
                root.left = leftTree            # attach leftSubtree
                root.right = rightTree          # attach leftSubtree
                fullTrees.append(root)  # result.append(TreeNode(0,leftSubtree,rightSubtree))

        cache[treeSize] = fullTrees     # memoization step to build larger (sub)trees
    return cache[treeSize]              # return after using memoization to build all subtrees


n = 5
print(allPossibleFBT(n))
