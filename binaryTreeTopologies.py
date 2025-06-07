"""A binary tree topology refers to the number of unique ways of arranging nodes irrespective of values. Thus the number of topologies of
0 nodes is 1 ie a null node. The number of topologies of 1 node is 1 ie the root node. When n > 1, we first have to choose the root node,
leaving n- 1 nodes. Then we know that each binary tree node can have a left subtree rooted at the left child and a right subtree rooted at
the right child. So if n = 3, then with 1 node for the root node, the left subtree can contain 0,1,2 nodes and the right subtree can also
contain 0,1,2 nodes. Particularly, if the left subtree contains 0 nodes, right subtree contains 2, if left subtree contains 1, right subtree
contains 1, if left subtree contains 2, right subtree contains 0. Thus by multiplying the left subtree / right subtree number of possible
topologies we get the number of topologies for that specific left / right subtree combo. Then sum up all the topology numbers to find the
solution.

In other words, we start with each subtree, and for each subtree we know that we will need a root node and there are n-1 total nodes in
the left and right subtrees. If all n-1 nodes go in the left subtree, then 0 go in the right subtree. So our recursive function takes in
number of nodes, n, and our base case is that if n == 0 or 1, return 1 way. Then we initialize a numTrees variable of 0. We use a for loop
to generate leftSubtreeSize up to n-1 ie range(n) and for each leftSubtreeSize, we generate the rightSubtreeSize as n-1 - leftSubtreeSize.
The we get the number of topologies for a subtree of leftSubtreeSize of nodes by calling the function again recursively with leftSubtreeSize
number of nodes, followed by the number of topologies for a subtree of rightSubtreeSize number of nodes and then the number of trees of that
combo is the product of the two since for each of the leftSubtreeSize topologies, we can have rightSubtreeSize topologies to go with. Then
after the multiplication we increment our number of tree variable.

Since we calculate the topology numbers repeatedly, ie leftsubtee = 2 and later rightsubtree=2, memoization or caching is essential to avoid
repeated work. This is because whether rightSubtreSize or leftSubtreeSize we are always asking for the number of ways of creating a (sub)tree
with a particular number of total nodes. Memoization drastically improves the time  complexity to O(n^2) and space of O(n).

With memoization comes a dyamic programming solution. The dynamic programming solutioin is based on the fact that we realize that the number
of topologies of 3 nodes depends on the number of topologies for 0,1,2 nodes because the subtrees could contain 0,1,2 nodes. Hence we can
declare an array of 0's size n+1 , update the base case at index 0 ie (tree with 0 nodes) updated to 1 ( or initialize the array with 1s).
Then in a for loop ,we generate the numberOfNodesInTree starting from 1 to n, and for each size, we initialize the number of trees variable
as 0, then inside we use another for loop to generate leftSubtreeSize, calculare rightSubtreeSize and access the values from the array, do
our multiplication and update the value in the array at index numberOfNodesInTree. At the end we return the value at array[n], and by array
here I'm refering to the dynamic programming array. The thing to realize is that in the recursion solution, we will have n calls on the call
stack and in each recursive call we have an O(n) for loop giving the time of O(n^2). So if we replace the recursive stack calls with a for
loop, and our memoization hashmap into an array, we are able to move from recursion to iteration and dynamic programming.

This question is similar to allPossibleFullBinaryTrees.py"""

"""Naive solution doesnt use caching leading to catalan number of repeated recursive calls and time complexity"""
# O((n*(2n)!)/(n!(n+1)!)) time | O(n) space


def numberOfBinaryTreeTopologies(n):
    if n == 0:  # if number of nodes is 0, base case
        return 1  # number of topologies with no nodes
    numberOfTrees = 0  # number of binary tree topologies, initialize to 0

    for leftTreeSize in range(n):  # 0 <= leftTreeSize <= n - 1
        rightTreeSize = n - 1 - leftTreeSize  # rightTreeSize + leftTreeSize = n -1, cos first node is root node
        numberOfLeftTrees = numberOfBinaryTreeTopologies(
            leftTreeSize)  # number of topologies of left subtree
        numberOfRightTrees = numberOfBinaryTreeTopologies(
            rightTreeSize)  # number of topologies of right subtree
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    return numberOfTrees


"""Optimal recursive solution using memoization or caching to avoid repeated work"""
# O(n^2) time | O(n) space


def numberOfBinaryTreeTopologies(n, cache={0: 1}):  # pass default value of cache
    if n in cache:  # base case since n=0 is already in cache and subsequent values will be added to cache
        return cache[n]
    numberOfTrees = 0  # number of binary tree topologies, initialize to 0
    for leftTreeSize in range(n):  # 0 <= leftTreeSize <= n - 1
        rightTreeSize = n - 1 - leftTreeSize  # rightTreeSize + leftTreeSize = n -1, cos first node is root node
        numberOfLeftTrees = numberOfBinaryTreeTopologies(
            leftTreeSize, cache)  # number of topologies of left subtree
        numberOfRightTrees = numberOfBinaryTreeTopologies(
            rightTreeSize, cache)  # number of topologies of right subtree
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    cache[n] = numberOfTrees  # add calculated topologies to cache
    return numberOfTrees


"""Optimal iterative solution that uses a sort-of dynamic programming approach. This solution simply makes the
observation that the number of binary tree topologies when n = 2 depends on the number of topologies when n = 0,1.
Thus since we know the base case of n = 0, we can find n = 1 and using n=0,1 we can find n=2 and so on."""
# O(n^2) time | O(n) space


def numberOfBinaryTreeTopologiesII(n):
    cache = [1]  # seed cache with topologies for n=0
    for m in range(1, n+1):  # loop to update the cache with number of topologies from  1<= m <= n, inclusive of n
        numberOfTrees = 0  # initialize the numbe of topologies for each number of nodes before calculating
        for leftTreeSize in range(m):  # this is exclusive range unlike the outer one
            rightTreeSize = m - 1 - leftTreeSize  # m is treeSize
            numberOfLeftTrees = cache[leftTreeSize]  # read the number of topologies from cache
            numberOfRightTrees = cache[rightTreeSize]  # read the number of topologies from cache
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        # append the numberOfTrees for n = m to the cache to be accessed later on
        cache.append(numberOfTrees)
    return cache[n]  # return the last value in the cache after all topology numbers have been appended


n = 3
print(numberOfBinaryTreeTopologiesII(n))
