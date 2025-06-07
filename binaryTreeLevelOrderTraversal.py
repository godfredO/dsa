"""
Tags: Binary Tree; Medium

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

So this is THE foundational question of binary tree bfs aka level order traversing. And this is where I prefer NeetCode youtube channel's
coding technique to algoexpert's. This is simply because, it is simpler, cleaner, and more widely applicable. So anyway, we start with a
queue, initialize with the root node. Inside the bfs while loop, we take the size of the queue. This is the number of elements that belong
on the same level bfs style. We also initialize an empty temp array. Then using a for loop, we pop exactly size number of nodes. If the
popped node is None we skip. Otherwise we add its value to temp and add its child nodes to the queue, left child first, then right. With
all the nodes of a level appended we append to the output array, if the temp array is non-empty, since we don't want to append empty arrays
to the output. This can happen when the root node itself is None, which will yield [[]] instead of [] if we didnt have this check. Another
situation is if we dont have this check, we will add an empty array at the end for the leaf node's None children.
"""
# O(n) time | O(n) space
from collections import deque


def levelOrder(root):
    queue = deque()             # could also use a list and pop(0)
    queue.append(root)
    output = []
    while queue:
        # to ensure we only process existing nodes, since we add their children below
        size = len(queue)       # number of nodes in current level
        temp = []               # to hold values of nodes from the current level.
        for _ in range(size):
            node = queue.popleft()      # if a regular list is used, pop(0)
            if node:  # skip None nodes
                temp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if temp:                # if current level was just None nodes, their level list is empty, dont add
            output.append(temp)  # append non-empty traversal of current level
    return output
