"""The input to this question is the root node of a binary tree and a node object which is in the binary tree and we are asked to return the
node object that comes after the input node object in an inorder traversal. We are also told the nodes in this binary tree contain a parent
pointer that points to each node's parent object. The naive solution is to actually conduct an in-order traversal where we append the node 
object to a list in the visit step. After that, we iterate through this list and compare each current node to the node of interest, while
also keeping track of the index. When we find the node and we are not the last position, we return the next node. If the node is the last 
position, we return None. 

The optimal solution uses the fact that we have a parent pointer which allows us to move up the tree.The first observation is that after
visiting a node, we go right to its right child if it has one and then keep going left from its right child. So if the node of interest has
a right subtree, then its successor is the leftmost node in the left subtree of its right child, meaning if the right child doesnt have a
left subtree, then the successor is the right child as its the node that will be visited next otherwise, we would keep going left until
we get to node that doesnt have a left child. So in the code, if we verify that node.right is not None, then we go to its right child, 
node.right and then in a while loop when keep going left ie node.left as long as node.left is not None. This will give us the leftmost 
leafnode of the right child's left subtree.

If the node of interest has no right subtree, then in the inorder traversal, execution would return to its parent and its parent will be
visited next if the node in question is the left child of its parent. Otherwise if the node in question is the right child of its parent, 
the call on its parent would have been completed so execution will go up and the next node we visit will be the first parent for which we 
are coming from its left subtree. That is as long as the current node is the right node of its parent we keep use the parent attribute to 
keep going up, until the current node is the in the left subtree of the parent. Of course the root node has None for parent, so if we are
ever coming from the right subtree of the root, there is no where to go, meaning we just completed all the calls for our root node and as
such our target Node is the last node in the inorder traversal, hence will have a successor of None (which incidentally happens to also
be the root's parent). So if we are not in the left subtree of a parent or at the root, we break out of the while loop and return 
currentNode.parent which will evaluate to None if we are at the root, because the target node is actually the last value in the inorder 
traversal otherwise an actual  node.

So a few things, if you use the inoptimal solution, you only use the passed node object for a check. However if you go to the optimal 
solution, you don't actually use the root node, it becomes unnecessary."""

class BinaryTree:
    def __init__(self,value,left=None,right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

#O(n) time | O(n) space
# def findSuccessor(tree,node):
#     inOrderTraversalOrder = getInOrderTraversalOrder(tree) #returns a list containing node objects from in-order traversal, left,visit, right
#     for idx, currentNode in enumerate(inOrderTraversalOrder):
#         if currentNode != node:
#             continue
#         if idx == len(inOrderTraversalOrder) -1 : #the case where the given node is the last object from in-order traversal of binary tree
#             return None
#         return inOrderTraversalOrder[idx + 1] #return successor object


# def getInOrderTraversalOrder(node,order=[]):
#     #this function is called witht the root node of the tree
#     if node is None: #base case when we get to the child node of a leaf node which should be none
#         return order #at the base case return list for eaf node to append its value and pass the list to its parent

#     getInOrderTraversalOrder(node.left,order) #go left
#     order.append(node)                        #visit, append the object itself
#     getInOrderTraversalOrder(node.right,order)  #go right
#     return order


"""Optimal Solution - more direct coding"""
def findSuccessor(tree, node):
    if node.right is not None:
        currentNode = node.right
        while currentNode.left is not None:
            currentNode = currentNode.left
            return currentNode

    currentNode = node
    while currentNode.parent is not None and currentNode == currentNode.parent.right:
        currentNode = currentNode.parent
        return currentNode.parent

"""Optimal solution"""
#O(h) time | O(1) space
def findSuccessor(tree, node):
    #if the given node has a right subtree its successor is the leftmost descendant in the right subtree or the direct right descendant
    if node.right is not None: #if it has a right subtree
        return getLeftmostChild(node) #the successor is the leftmost descendant in node's right subtree
    
    #if the node doesnt have a right subtree, the successor is an ancestor,from which the given node is in its left subtree
    return getRightmostParent(node) 

def getLeftmostChild(node): #this is the getMinValue() helper used in the remove() method of BST construction
    currentNode = node.right #go into right subtree
    while currentNode.left is not None: # as long as we can go left
        currentNode = currentNode.left #keep going left
    return currentNode #return left most descendant in right subtree

def getRightmostParent(node):
    currentNode = node
    #while currentNode is not the root node and currentnode is the right descendant, 
    # keep moving until an ancestor whose left child yields the given node
    #thus loop terminates when at the root node( currentNode.parent is None) or the successor currentNode.parent.left == currentNode
    while currentNode.parent is not None and currentNode.parent.right ==  currentNode:
        currentNode = currentNode.parent
    
    #will return None if the loop breaks on the root node . will return successor if the ancestor whose left child yielded current node is found
    return currentNode.parent