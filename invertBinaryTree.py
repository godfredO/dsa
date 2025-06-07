"""This question is better called mirror-image a binary or flip a binary tree sideways. This is because the inversion here, is actually 
flipping the binary tree sideways to yield a mirror image of the original. Also know that for a binary tree roughly half of all its
nodes are leaf nodes so the depth of a binary tree is log N. So since we have references to a node's left and right child, we simply
swap these and call the recursive function on the current (swapped) left child, then swapped right child. If we ever call from a
leaf node the swapped children will be None values and these don't have children to swap so to we just return. The recursive version,
will thus swap the left/right children of the root node, then go down the swapped left child's subtree, finish swapping a every pair
of left/right children before tackling the subtree of the swapped right child of the root. The iterative version uses breadth first
search and thus a queue. We first add the root node, then while the queue is non-empty we do the following operations. We popleft
for the currentNode. If the currentNode is None, we continue to the top of the loop, otherwise we swap the left/right children of
the currentNode, then add the swapped left/right children to the queue. In either the recursive (dfs) and iterative (bfs), after
swapping a node's children, it really doesnt matter which child we process first as long as we are. This means the bfs solution
can actually be written with a stack and the dfs solution can have the right child call come before the left child call. However keeping
the standard of using queues and calling the left child first is useful since there are some questions where the left to right order
actually matters. """


#Iterative solution , breadth-first search implemented with a queue
#O(N) time | O(N) space
def invertBinaryTree(tree):
    queue = [tree] #initialize the queue with the root node
    while len(queue): #same as while len(queue) > 0. In Python an len(empty list) is False, len(non-empty list) is True
        current = queue.pop(0) #first node, O(N) operation in Python but assuming constant time, could use deque
        if current is None:
            continue #if current node is None skip to next node in queue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left,tree.right = tree.right,tree.left


#Iterative solution , breadth-first search implemented with a stack, because we are not doing a short path question so order unimportant
# ie is to say we could as well go right before left and we will still get the same inverted binary tree
#O(N) time | O(N) space
def invertBinaryTree(tree):
	queue  = []
	queue.append(tree)
	
	while queue:
		currentNode = queue.pop()
		if currentNode is None:
			continue
		swap(currentNode)
		queue.append(currentNode.left)
		queue.append(currentNode.right)

def swap(node):
	node.left, node.right = node.right, node.left

"""Recursive Solution"""
#O(n) time | O(d) space
def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapLeftAndRight(tree):
    tree.left,tree.right = tree.right,tree.left