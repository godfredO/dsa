"""Given the root of a binary tree, flatten the tree into a "linked list": The "linked list" should use the same TreeNode class where 
the right child pointer points to the next node in the list and the left child pointer is always null. The "linked list" should be in 
the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
 

So you should review flattenBinaryTreeToDoublyLinkedList.py which is based on an inorder traversal and yields a doubly linked list.
This question is based on a pre-order traversal and we are told that the right child pointer should always point to the next node in
the list and the left child pointer to Null/None. So the obvious solution is to collect all the nodes in a preorder array and then
in a for loop that goes to the penultimate position, modify the left pointer to point to None and the right pointer to point to 
the next node ie array[i].right = array[idx+1]. The last value in the preorder array will be a leaf node pointing to None anyway.
Now of course the space complexity of this naive solution is O(n). Now do we need to store all the nodes.

Because preorder traversal is [rootNode, leftSubtree, rightSubtree], that is we have to flatten the entire left subtree before flattening 
the entire right subtree. In addition, the flattened left subtree of the rootNode will go between the rootNode and the right child of the 
rootNode, and this holds for the subtree rooted at any node. After flattening the left subtree, what does it mean to insert it between
the rootNode and the right child? It means the rootNode's right pointer will point to the head of the flattend left subttee and the tail
of the flattened left subtree will point to the root's right child. This means our recursive function should return the head and tail
of a flattened linked list representing the left subtree, then right = root.right, root.right = head, tail.right = right, before we call
the flattening recursive function on the right child. What about if the rootNode has no left child ie None value. Now the head of the
flattened left subtree is going to be the left child of the root node, so what we really need to return is the tail of the flattened
left subtree.If the left subtree is None, then we don't need to modify the rootNode's right pointer, we leave it pointing to the right 
child. Of course the sequence of the pointer is essential.

Now how do we determine the tail of the flattened linked list. If you look at the preorder traversal of three nodes, it becomes clear
that the tail of the flattened linked list is the tail of the right subtree if the right child is not None, if it is then the tail
is the tail of the flattened left subtree if that is not None. If both the tail of the flattened left and right subtrees are None, then
the tail to be returned is the root. We can do this simply using the way in which Python evaluates or statements whereby it stores the
first non-None value as the result. Because we have to first get the tail of the flattened left and right subtrees, the pattern used
here is postorder dfs in nature.

"""

"""Naive approach, storing all nodes in an array and iterating over the array"""
#O(n) time | O(n) space
def flatten(root):
    """
    Do not return anything, modify root in-place instead.
    """
    array = []
    getPreOrder(root, array)
    for i in range(len(array)-1):
        array[i].right = array[i+1]
        array[i].left = None
        
def getPreOrder(node, array):
    if node: 
        array.append(node)
        getPreOrder(node.left, array)
        getPreOrder(node.right, array)


"""Optimal approach"""
def flatten(root):
    getTail(root)

def getTail(node):
    if not node:
        return None
    
    leftTail = getTail(node.left)
    rightTail = getTail(node.right)

    if node.left: #if root.left is None, then leftTail is None
        leftTail.right = node.right #returned tail's right pointer points to root's right child
        node.right = node.left #the root points to its left child in the linked list, preorder next visited
        node.left = None #then update left pointer of root to None
    
    tail = rightTail or leftTail or node    #order of tail, rightTail, leftTail, node
    return tail
