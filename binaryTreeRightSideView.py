"""
Tags: Binary Tree; Breadth First Search
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []



So from my standpoint, the question is asking for the values of the rightmost nodes for each level from the root, to the deepest leaf node
level. So obviously the root being the only node on its level, it will also be the rightmost node. If the root has a right node, that will
be  rightmost node otherwise, the left child will be the rightmost node. The difficulty comes when you have a lopsided tree. That is if the
right child of the root is also  a leaf node, then the remaining nodes will be in the left subtree of the root. Modeled this way, this
question can be solved with breadth-first search, where we go level by level, find the rightmost node at each level. Bfs in trees is also
called level-order traversal.

To use breadth first search, we use a queue and initialize it with the root node and the depth/ level information ie [root,0]. Then inside
the bfs while loop, popleft() from the front of the queue, unpack into node, depth. If the node is None, skip. Then if the node.left is not
None append the left child with depth+1 as level information. Then if the node.right is not None append the right child with depth + 1 as
level information. It is important to append the left child first before the right child if the child node in question is not None. Then if
the queue is non-empty and the current node in the front of the queue has the same depth as the current node's depth, then the current node
is not the rightmost node on that level so we continue. Otherwise, either because the queue is empty or the node at the front of the queue has
a different level information ie one level below, then we have the rightmost node on the current level so we go ahead and append the current
node's value to our result array. Three facts make this possible, one we append the left child before the right child, two we don't append a
child if its a None child and three, we compare the current node's depth to the front of queue node information.

There is a second coding of the same bfs solution without the use of depth information and in a similar manner to the way breadth-first
search for general graph problems like minimumNumberOfPasses.py. Anyway, we initialize our queue with our root node. Then inside the while
loop, we initialize rightmost variable to None and take the current size of the queue. We use a for loop to pop exactly size number of nodes.
If the node in question None, we continue. Otherwise, we set the rightMost variable as the current node and we add its left then right
child. Then outside the for loop, if the rightMost variable is still the None value initialized, we do nothing otherwise we append the
value of the rightMost variable node. By taking the size of the of the queue ie a snapshot and popping exactly that number of elements,
before even adding to the queue, we ensure that we only compare nodes of the same level. And when we add to the queue, we add left node
first, followed by right node so that the rightmost node variable will be set to the last non-None node on a level going from left to right.
Personally this way of coding it is easier once you understand why everything is being done.

Now obviously, the breadth-first search solution is very intuitive but the problem with bfs in trees in that since trees have about half of
all nodes at the bottom of the tree, so the space complexity of tree bfs O(n) can be huge. The depth first solution is a really clever one
indeed. Basically, we know that the depth of the root node is 0, and before we append the root node's value, the result array will be empty
ie len(result) = 0. The if root has child node(s), those will have a level or depth of 1 and before we add the rightmost node from that
level, the result array will have the root aka len(result) == 1 and that matches the level we are at. So in the depth first search solution
we use a preorder array where the visit step involves checking if the depth of the passed node equals the current length of the result
array. This kind of mimic taking a size snapshot of the in the bfs solution. Anyway, if it is we append the current node to the result array.
The reason we are able to do that is because, in the dfs solution we go right, then go left so we are doing a reverse preorder dfs. And of
course we have the base case of returning if the node is None. So we have a first base case , a visit step of checking if the node info
matches the length of the result array, and then we go right with incremented depth information before going left with incremented depth
information. This will have the effect of traversing the tree rightmost branch to leftmost branch and adding the rightmost nodes that way.
The obvious benefit of the dfs solution is that the space complexity is better.
"""

"""Bfs solution I"""
# O(n) time| O(n) space




from collections import deque
def rightSideView(root) :
    queue = deque()
    queue.append([root, 0])   # initialize queue with depth information

    output = []
    while queue:
        node, depth = queue.popleft()
        if node is None:                    # if popped node is None, go back to while loop
            continue

        if node.left is not None:            # left before right so last pop() is rightmost
            queue.append([node.left, depth + 1])    # append left child to queue with updated depth

        if node.right is not None:          # left before right so last pop() is rightmost
            queue.append([node.right, depth + 1])   # append right child to queue with updated depth

        if queue and queue[0][1] == depth:      # node at queue front at same level as current node
            continue                            # current level not finished, go back to while loop

        output.append([node, depth])

    return output


"""Bfs solution II"""
# O(n) time| O(n) space


def rightSideView(root):
    queue = deque()
    queue.append([root])

    output = []
    while queue:
        rightMost = None            # variable for rightMost node of current level
        size = len(queue)           # number of nodes at the current tree level

        for _ in range(size):       # pop only nodes in the same tree level
            node = queue.popleft()  # first in first out
            if node:                # if node is not None
                rightMost = node            # set rightMost variable to current node
                queue.append(node.left)     # left before right so last pop() is rightmost
                queue.append(node.right)    # left before right so last pop() is rightmost

        if rightMost:                       # if current level rightMost node was updated
            output.append(rightMost.val)

    return output


"""Dfs solution"""
# O(n) time | O(d) space


def rightSideView(root):
    result = []
    preorderDfs(root, 0, result)    # depth is used to guid choice of rightmost node
    return result


def preorderDfs(node, depth, result):
    if node is None:
        return

    if depth == len(result):    # one node per level, so current depth = len(result) before append
        result.append(node.val)

    preorderDfs(node.right, depth + 1, result)  # in dfs, right node first for depth=len(result)
    preorderDfs(node.left, depth + 1, result)   # in dfs, left node second for depth=len(result)
