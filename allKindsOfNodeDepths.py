"""
Tags: Binary Tree, Dfs, Bfs, Objects; Hard

This question builds on the node depths question where we are asked to return the sum of the node depths in a binary tree.
In this question we are asked to return the sum of the node depths of all the subtrees in the binary tree. By this it means
consider each subtree as its own tree and so for that subtree's consideration, its own root will have depth of 0 and its
children will have a depth of 1. However when we consider the parent's tree, then the previous root becaomes a child and the
previous children become grandchildren with new depths of 1, 2.

The naive approach uses the solution for determining the sum of node depths of the tree rooted at a node. The mid-optimal
approach realizes that if we add the number of nodes in a particular subtree to the sum of the node depths in the subtree
we will be able to solve the question in linear time instead of repeating the sum of node depths n times which would lead to
a worse time complexity."""

# Iterative approach of Naive solution where we repeat the sum of node depths for the subtree rooted at each node in the binary tree
# Average(nlog(n)) time | O(n) space
"""Naive approach, we use a stack to process the nodes one by 1. We add the root node, pop it, then call nodeDepths() on it to
sum all the node depths of the tree rooted at the root, increment the sumOfAllDepths variable with the return value, then we add
its left child and right child to the queue so that we can pop them, call the nodeDepths() on either when popped to sum up the
node depths rooted at that node and increment the sumOfAllDepths over and over. We are using the stack here, the way we would
use a for loop for an array, but this solution, is essentially breadth-first search in nature, since we determine node depths
for each subtree on level at a time. Since the order left,right, or  right,left doesnt affect the sum, we can use a stack. We
could still use a queue to properly demonstrate that it is breadth-first search. Since the nodeDepths() call is roughly going
through up to half the nodes each call and is called n times, the time complexity is O(nlogn) and the queue could contain up
to half of all nodes so O(n).


"""


def allKindsOfNodeDepths(root):  # we are provided the root node of the tree
    sumOfAllDepths = 0  # initialize
    stack = [root]  # stack for iterative processing of nodes, initialize with root node in it
    while len(stack) > 0:  # as long as we have nodes in the stack
        node = stack.pop()  # pop from the stack since the order of processing doesnt matter so we don't need a queue here
        if node is None:  # if the child nodes of a lead node is added skip
            continue
        # otherwise get and add the sum of all node depths for the subtree rooted at current node
        sumOfAllDepths += nodeDepths(node)  # for subtree rooted at current node
        stack.append(node.left)  # then append the left node to the stack
        stack.append(node.right)  # then append the right node to the stack
    return sumOfAllDepths  # return the sum of node depths of all subtrees in given


# the depth of every root node is 0 and this function is called on the subtree rooted at node initially
def nodeDepths(node, depth=0):  # depth=0 for node in subtree rooted at node
    if node is None:  # if node is the child of a leaf node, node is None
        return 0  # base case, would return 0 to leaf node so that leaf node get depth + 0
    # sum of node depths
    return depth + nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth+1)  # increment


# Recursive approach of Naive solution where we repeat the sum of node depths for the subtree rooted at each node in the binary tree
# Average O(nlog(n)) time | O(h) space
# this solution uses the call stack instead of implementing a stack/queue solution
"""
Instead of a stack / queue, we could also use a second recursive function allKindsOfNodeDepths(). What
this function does it that when called on a node, it assumes the node as the root ie depth=0 and calls
the nodeDepths() function to return the sum of depths rooted at the passed node. Just like the stack /
queue solution, the allKindsOfNodeDepths() function calls nodeDepths() n times. This is because, the
allKindsOfNodeDepths() function is calls nodeDepths() on the passed node before recursively calling on
every child node of the passed node. The difference between allKindsOfNodeDepths() and the stack /
queue solution is that allKindsOfNodeDepths() integrates the stack solution by using the call stack
when recursive calls are made to the child nodes. It does still take same time and space space complexity
as the stack and queue solution which is O(nlogn) time, O(n) space. In addition, allKindsOfNodeDepths
also demonstrates an important relationship:

allKindsOfNodeDepths(root) = nodeDepths(root) + allKindsOfNodeDepths(leftChild) + allKindsOfNodeDepths(rightChild)
"""


def allKindsOfNodeDepths(root):  # this is a very elegant way of writing the sum of all node depths
    if root is None:
        return 0
    # get node depth and add node depths
    return nodeDepths(root) + allKindsOfNodeDepths(root.left) + allKindsOfNodeDepths(root.right)


# the depth of every root node is 0 and this function is called on the subtree rooted at node initially
def nodeDepths(node, depth=0):
    if node is None:  # if node is the child of a leaf node, node is None
        return 0  # base case, would return 0 to leaf node so that leaf node get depth + 0
    # sum of node depths
    return depth + nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth+1)


"""

Solution II asks the question, how do we avoid, repeating the nodeDepths() function call n times. Is there any thing we can use?
Take a tree with a root , one left child and one right child. When considering the subtree rooted at a leaf node, the leaf node is
only one node in that subtree, and since its the root of that subtree, its depth in that subtree is 0. So the depths of
the subtree rooted at the leaf node is 0, and there is only one node in that subtree. When we consider the subtree rooted at the
the root, the leaf nodes now have a depth of 1. The same leaf node is now depth 1 with respect to the entire tree. The root node
has a depth of 0 in the entire subtree. This gives a nodeDepths of 0 + 1 + 1= 2. How does the nodeDepths of the root, relate to
the nodeDepths of the leaf child nodes? It is by realising that at each node, the nodeDepths = leftNodeDepths + leftSubtreeNumNodes
+ rightNodeDepths + rightSubtreeNumNodes ie 0 + 1 + 0 + 1 = 2. So if we calculate the nodeDepths from the leaf nodes and work our
way up the tree, we are able to use the nodeDepths we have calculated and the number of nodes to calcualate the nodeDepths of each
parent. Now that we have the nodeDepths of the parent, we can calculate the sumOfNodeDepths = parent.nodeDepths +
leftChild.sumOfnodeDepths + rightChild.sumOfnodeDepths. Thus this solution extends on the previous solution by breaking down
nodeDepths = leftchild.nodeDepths + leftSubtree.NumNodes + rightchild.nodeDepths + rightSubtree.NumNodes. Also note that we have
to calculate the number of nodes for the parent node which is 1 + leftSubtree.NumNodes + rightSubtree.NumNodes. After Calculating
the parent nodes nodeDepths, sumOfnodeDepths, numNodes, these are packaged in a TreeInfo(numNodes, nodeDepths, sumOfNodeDepths)
custom object.

So in this solution, we go all the way down to the leaf nodes, and each node returns three values to its parent, nodeDepths of the
subtree rooted at the child node, the number of nodes in the subtree rooted at the child node , the sumOfAllDepths in the subtree
rooted at the childNode. The parent uses the nodeDepths and numNodes from both its left and right children to calculate its own
nodeDepths, ie nodeDepths = leftNodeDepths + leftSubtreeNumNodes + rightNodeDepths + rightSubtreeNumNodes, then adds this
calculated value to the sumOfAllDepths from its left and right children to calculate the sumOfAllDepths rooted at it, and finally
adds 1 to the number of nodes from its left and right children and returns this triplet of numbers to its parent. This approach is
better and more cleanly coded recursively. If tree is None we return TreeInfo(0,0,0). This is the height-based dfs approach as seen
in say the binaryTreeDiameter.py question or the dfs solution of nodesDistanceKAway.py  but instead of height or distance from
target, branch path etc we are returning up the tree, the number of nodes in a child subtree, nodeDepths and sumOfNodeDepths. That
is we recurse down the tree and solve the problem from the bottom up. At each node, we make a call to the child nodes, the child
node's return some value(s) and which is used in some logic or calculation before returning new value(s) up the tree. When the
original call gets its values from its ichild nodes, what it returns is the answer to the question.

"""


class TreeInfo:
    def __init__(self, numNodes, nodeDepths, sumOfNodeDepths):
        self.numNodes = numNodes
        self.nodeDepths = nodeDepths
        self.sumOfNodeDepths = sumOfNodeDepths


def allKindsOfNodeDepths(root):
    return helper(root).sumOfNodeDepths


def helper(node):
    if node is None:
        return TreeInfo(0, 0, 0)

    leftInfo = helper(node.left)        # dfs to child node
    rightInfo = helper(node.right)      # dfs to child node

    numNodes = 1 + leftInfo.numNodes + rightInfo.numNodes  # add one to the root node
    nodeDepths = leftInfo.nodeDepths + leftInfo.numNodes + rightInfo.nodeDepths + rightInfo.numNodes
    sumOfNodeDepths = nodeDepths + leftInfo.sumOfNodeDepths + rightInfo.sumOfNodeDepths

    return TreeInfo(numNodes, nodeDepths, sumOfNodeDepths)


"""#Optimal time complexity solution with non-optimal space complexity, where we store node depth and number of nodes in subtree values
#and sum these at the end . In this solution we use a different formula to derive the sum of the node depths of each subtree, with is
# sumOfNodeDepths[node] = sumOfNodeDepths[node.left] + nodeCount[node.left] + sumOfNodeDepths[node.right] + nodeCount[node.right] that
# is it is important to realize that each node adds an addend to the sumOfNodeDepths of its parent, parent's parent, parent's parent's
# parent etc and this addend increases by 1 each time since its depth with respect to the subtree rooted at parent, parent's parent
# also increases by 1 each time for each successive subtree being considered. That is the node depth that each node contributes to the
# sum of node depths formula with respective to a subtree ,rooted at some root node for that subtree, depends on the number of edges
# between the node and the root of the subtree. So when the root of the subtree is a node's parent, a node contributes 1 to that subtree
# but contributes 2 to the sum of node depths for the subtree rooted at its parent's parent reflecting its edge distance from the root
# node in question and as a result the same node contributes several times and each time with an increment of the node depth to the sum
# of node depths for all the subtree to which it belongs. This solution thus calculates the node count of each subtree then uses the
# node counts to calculate the sum of node depths of each subtree and finally for all the subtrees , adds up the sum of node depths"""
# O(n) time | O(n) space


def allKindsOfNodeDepths(root):
    nodeCounts = {}  # initialize hashtable for storing the number of nodes in each subtree
    addNodeCounts(root, nodeCounts)
    nodeDepths = {}  # initialize hashtable for storing the sum of node depths in each subtree
    addNodeDepths(root, nodeDepths, nodeCounts)
    return sumAllNodeDepths(root, nodeDepths)


def addNodeCounts(node, nodeCounts):
    # initialize hashmap node key entry for node count in subtree rooted at passed node at 1 for the node itself
    nodeCounts[node] = 1
    if node.left is not None:  # if there is a left child
        # then get the node count of subtree rooted at left child node
        addNodeCounts(node.left, nodeCounts)
        # add the nodeCounts of left subtree to the 1 initialize for current node
        nodeCounts[node] += nodeCounts[node.left]
    if node.right is not None:  # if there is a right child
        # then get the node count of subtree rooted at right child node
        addNodeCounts(node.right, nodeCounts)
        # add the nodeCounts of right subtree to the 1 initialized for current node
        nodeCounts[node] += nodeCounts[node.right]


# this maps each node to the sum of the node depths of subtree rooted at node
def addNodeDepths(node, nodeDepths, nodeCounts):
    # initialize hashmap node key entry for sum of node depths in subtree rooted at passed node at 0
    nodeDepths[node] = 0
    if node.left is not None:  # if there is a left child
        # then get the node count of subtree rooted at left child node
        addNodeDepths(node.left, nodeDepths, nodeCounts)
        # add the sum of the node depths of left subtree
        nodeDepths[node] += nodeDepths[node.left] + nodeCounts[node.left]
    if node.right is not None:  # if there is a right child
        # then get the node count of subtree rooted at right child node
        addNodeDepths(node.right, nodeDepths, nodeCounts)
        # add the sum of the node depths of left subtree
        nodeDepths[node] += nodeDepths[node.right] + nodeCounts[node.right]


def sumAllNodeDepths(node, nodeDepths):  # add up the sumofNodeDepths for each subtree in original tree
    if node is None:
        return 0
    return sumAllNodeDepths(node.left, nodeDepths) + sumAllNodeDepths(node.right, nodeDepths) + nodeDepths[node]


""""#

Recursive approach for optimal solution which improves space complexity with same linear time complexity. In the code implementation
at each node of the tree, we update the nodeCount of the subtree rooted at that node, the sum of node depths of the subtree rooted at
that node and the final output value the sum of all subtree nodedepth sums. The three pieces of information will be carried in a defined
class.

This solution effectively, factorizes the left subtree and right subtree contribution to the parent node depths calculation.
"""
# O(n) time | O(d) space


class TreeInfo:
    def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
        self.numNodesInTree = numNodesInTree            # numNodes
        self.sumOfDepths = sumOfDepths                  # nodeDepths
        self.sumOfAllDepths = sumOfAllDepths            # sumOfNodeDepths


def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths


def getTreeInfo(tree):  # returns
    if tree is None:
        return TreeInfo(0, 0, 0)
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
    sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree

    numNodesInTree = 1 + leftTreeInfo.numNodesInTree + rightTreeInfo.numNodesInTree
    sumOfDepths = sumOfLeftDepths + sumOfRightDepths
    sumOfAllDepths = sumOfDepths + leftTreeInfo.sumOfAllDepths + rightTreeInfo.sumOfAllDepths

    return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)


"""Optimal approach uses the same bottom-top approach here. So lets say the leaf node has depth of 3 with respect to the root node,
depth of 2 with respect to the roots child, a depth of 1 with respect to its parent and a depth of 0 with respect to itself, then
its total depthSum contribution is 3 + 2 + 1 + 0 = 6. Now realize how these depth sum contributors are reflected in the depth of
the tree itself. Thus if we go down the tree, supplying depth information to each node and at the same time updating the depthSum
with the depth information we would arrive at a leaf node with its depthSum calculated. That is we initialize the depthSum = 0,
and the depth of the root node at 0. In the recursive call, we increment depthSum with the passed node and pass the updated
depthSum to the children nodes. This way at each node, to get its total depthSum contribution, is to add the passed depth to
the running depthSum. So at the root , depthSum += 0 = 0, at its child depthSum += 1 =1, at the leaf node's parent depthSum += 2
= 3 and at the leaf node depthSum += 3 = 6, which is the same as 3+2+1+0=6. Now the sum of all node depths means that we return
up the tree, the updated depthSum and the result of calling on the child nodes.So the leaf node's None children will return 0
each so we return 6 + 0 + 0 = 6 . At the leaf's parent we return 3 + 6 + 6 (assuming a fully filled tree at each stage) = 15. And
so on and so forth, till we reach the root and return the sum of all node depths.

"""

"""Optimal approach less less lines of code stems from observation that the depth that a node contributes to a subtree's sum of
all node depths depends on the distance or relation of the node to the root of the subtree being considered. Thus a leaf node
contributes a depth of 1 to its parent node, 2 to its parent's parent node, 3 to its paren'ts parent's node. Thus a node contributes
a depth of d to the root of the binary tree, d-1 to the root's child, all the way up to a depth of 0 when considering the subtree
rooted at the said node. Thus at each node we need to add 0 + 1 + 2 +...+d to a running sum of all node depths as its singular
depth contribution to all the subtrees of which it is a part. Instead of using a O(d) for loop to contribute the sum of a node's
depth contribution to the overall sum of all depth node's we can realize that these numbers are reflected in the depth of the
node with respect to the root of the binary tree (d), its parent's depth with respect to the root of the binary tree (d-1) and on
and on. So in this algorithm, we keep a running sum, and at each node we add the node's passed depth to this running sum and also
pass this running sum to the node's child so that when the node's child itself add its depth to the running sum it would also be
adding the (d-1), (d-2), contributions. Thus a leaf node receives a running sum that contains 0 + 1 + 2 + ... + (d-1), adds d to
this sum as its total contribution, 0 + 1 + 2 + ... + (d-1) + d, and returns this value to its parent who will add it to a depth
as its total contribution.

Thus each node receives a depthSum that contains all of its contributions to all subtrees from the subtree rooted at it to the
subtree rooted at the child of the root node of the binary tree and adds to this running depth sum the its depth contribution
to the tree rooted at the root of the binary tree and returns to its parent this updated total depth contribution and the total
depth contributions of its children nodes. This solution is an exact replica of the nodeDepths function itself, just that we
update the depthSum with the passed depth value and we return the sum of the depthSum and the returned value of calling on the
child nodes.

This elegant solution relies on realizing that each node contributes depths of d,d-1,...,0 to all the subtrees it belongs to.


"""

# O(n) time | O(d) space


def allKindsOfNodeDepthes(root, depthSum=0, depth=0):
    if root is None:
        return 0
    depthSum += depth  # depthSum depth dependent contributions 0+1+..+d-1 so add d
    return depthSum + allKindsOfNodeDepths(root.left, depthSum, depth+1) + allKindsOfNodeDepths(root.right, depthSum, depth+1)


"""

The final optimal solution builds on the previous solution's observation that each node contributes 0 to sum of all node depths
of the tree rooted at it, 1 to the tree rooted at its parent and all the way to d to the tree rooted at the root of the binary tree
In the previous solution we realized that these values are also reflected in the depth of the node to the root of the binary tree,
its parent's depth to the root of the binary tree etc and so kept a running depthSum which increased by d at each node and was also
passed to the node's children nodes. This solution simplifies this further by realising that the sum d + (d-1) + (d-2) + .. + 1 + 0
can be calculated at each node with the formula (d*(d+1))/2, realising that after removing 0 which doesnt really change the sum,
d + (d-1) + (d-2) + ... + 3 + 2 + 1  can be arranged as d + 1 + (d-1) + 2 + (d-2) + 3 and realizing that d-1+2=d+1, d-2+3=d+1, each
adjacent sum pairs adds to the same (d + 1) and if d is odd there will be a lone (d + 1) / 2 term. Thus if we express each (d+1)
term as (d+1)/2 + (d+1) / 2, we realise that there are d terms of (d+1)/2 giving  d*(d+1)/2. So by using this mathematical formula
we can directly calculate a node's depth contribution to all subtrees to which it belongs at the node in one step instead of passing
the depth sum.

5 odd depth
5+4+3+2+1 = (5+1)+(4+2)+3 = 6+6+3 = 3+3+3+3+3 = (d*(d+1)/2) = (5*6/2) = 15
4 even depth
4+3+2+1 = (4+1)+(3+2) = 5+5 = (d*(d+1)/2) = (4*5/2) = 10
"""

# O(n) time | O(d) space


def allKindsOfNodeDepths(root, depth=0):
    if root is None:
        return 0
    depthSum = (depth*(depth+1)) / 2  # using Gauss Summation instead of passing around depthSum
    return depthSum + allKindsOfNodeDepths(root.left, depth+1) + allKindsOfNodeDepths(root.right, depth+1)
