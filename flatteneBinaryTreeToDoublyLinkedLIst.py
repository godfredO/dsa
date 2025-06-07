"""The question gives a binary tree and asks to flatten it by updating the pointers of the nodes to resemble the result of an
inorder travesal of the tree. The first solution does exactly this; it conducts an inorder traversal of the nodes and stores
the node objects in a list and then iterates through the list and updates the left,right pointers to point not to the left/ right
child but to the node object to its left and right in the inorder traversal array. In the code after the inorder traversal we
loop through the inorder array up to the penultimate position. At each index, we say the leftNode is the node at array[i] and the
right node is the node at array[i+1], then we update leftNode.right = rightNode, rightNode.left = leftNode. So index i is choosing
the index of the left node that is why we loop to the penultimate position so that the rightNode i+1 will be the last node. At the
end we return the first node in the array, inorder[0].

The second solution doesn't use an auxilliary array but instead makes use of another important realization. If the binary tree were a 
binary search tree, after an inorder traversal the result will be sorted. In other words, the new left pointer of a node in a flattened 
binary search tree will point to a node whose value is smaller and in particular the largest value node whose value is still smaller than 
the node in question. In the same way the right node will point to the smallest value node whose value is still greater or equal than the 
node in question. In other words the left pointer will point to the rightmost node in the left subtree and the right pointer will point to 
the leftmost node in the right subtree. 

So in the second solution, we write a recursive function, that returns the leftmost node and rightmost node in the subtree, rooted at 
each node. So a node will receive from both its left and right subtree, a left.leftmost, left.rightmost, right.leftmost, right.rightmost.
Now this is a common dfs pattern in binary trees (check the height-based or path questions like binary tree diameter) where we ask child
to return the same information and we do something with it ie postorder dfs since the base case is the leafnode's subtree. So here once a 
node receives this information from the child nodes, it will connect by saying node.left = left.rightmost, node.right = right.leftmost ie 
the are two return nodes that are used by the current node each time and return left.leftmost and right.rightmost as the leftmost and
rightmost nodes in its subtree. 

So the recursive function, as written here, takes in a node is supposed to return the leftmost and right most nodes in its subtree. If the
node.left is None then the leftmost node in its subtree is itself (ie if at a leafnode or node with a right child but no left child then 
that node is the leftmost node in its subtree). If node.right is None, rightmost = node (a leaf node or a node with a left child
but no right child is the rightmost node in its subtree). This means that if we are at a leafnode, the leafnode is both its leftmost and 
rightmost nodes. If we are at a node with one child, the node is one of either the leftmost or rightmost nodes of its subtree. 

If node.left is not None, then we recursively call the function on the left child and that call should return left.leftmost, left.rightmost 
nodes. We connect the node to left.rightmost (ie current.left = left.rightmost) before setting the leftmost variable to the left.leftmost as 
one of the node to the returned. We do the same with the rightmost variable. If node.right is not None, then we ask the right child to return 
its right.leftmost and right.rightmost, we connect the current node to the right.leftmost node (ie current.right = right.leftmost) and set the 
rightmost variable equal to right.rightmost, as one of the nodes to be returned. At the end of the recursive function we return the leftmost
variable and rightmost variable nodes. This means that the original call from the main function, will return [leftmost, rightmost] as the
leftmost node and rightmost node in the tree so we return leftmost as the 'head' of the flattened binary tree (remember lefmost here is
coming from the left.leftmost after root.left = left.rightmost and rightmost here is right.rightmost after root.right = right.leftmost).
  
The connect helper function is written here to take (left, right) and say left.right = right, right.left = left , replicating what the for
loop index was used to do in the first solution. To make this function work for connecting the returned values from a subtree, when 
connecting a node to its left.rightmost, we pass in (left.rightmost, node) and to connect a node to its right.leftmost, we pass in
(node, right.leftmost). 

"""
class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
#O(n) time | O(n) space
def flattenBinaryTree(root):
    inOrderNodes = getNodesInOrder(root,[]) #traverse the tree inorder style and store nodes in an array in order
    for i in range(0,len(inOrderNodes)-1): #from first to penultimate node in array of inorder nodes, update current and next
        leftNode = inOrderNodes[i] #access current node in list which will be on the left
        rightNode = inOrderNodes[i+1] #access the next node in list which will be on the right
        leftNode.right = rightNode #update the current node's right pointer to point to next node in inorder list
        rightNode.left = leftNode  #update the next node's left pointer to point to the current node in inorder list
    return inOrderNodes[0] #return the first node in the array

def getNodesInOrder(tree,array):
    if tree is not None: #if the current node is None do nothing at all, otherwise if current node is not None
        getNodesInOrder(tree.left,array) #go left recursively
        array.append(tree)  #when done with the left subtree, go right
        getNodesInOrder(tree.right,array)  #then go right recursively
    return array #return array of nodes


"""Optimal solution that improves space complexity where we recursively call on the left child of a node to return the rightmost node 
in the left subtree and we recursively call on the right child of a node to return the leftmost node in the right subtree and updating
pointer of node with the return nodes"""
#O(n) time | O(d) space
def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root) #recursive function
    return leftMost

def flattenTree(node):
    if node.left is None:   #base case if no left child exists at current node
        leftMost = node      #then current node is the leftmost node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left) # recursive call on the left child
        connectNodes(leftSubtreeRightMost,node) #update node's left pointer to point to left subtree rightmost node, and vice versa
        leftMost = leftSubtreeLeftMost #set the leftmost node in this subtree to be returned to parent

    if node.right is None:  #base case if no right child exists at current node
        rightMost = node    #then current node is the rightmost node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right) #recursive call on the right child
        connectNodes(node,rightSubtreeLeftMost) #update node's right pointer to point to right subtree leftmost node, and vice versa
        rightMost = rightSubtreeRightMost
    return [leftMost,rightMost] #base case return leftmost node and rightmost node to parent


def connectNodes(left,right): #update pointers
    left.right = right
    right.left = left