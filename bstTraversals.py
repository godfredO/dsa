"""The question asks to write three functions that take in a binary search tree root node and an empty array, traverses the BST, and adds 
its nodes to the input array, and returns the array. The three functions should traverse the BST using in-order, pre-order, and post-order 
tree traversal techniques, respectively.
In in-order traversal, the pattern is left, visit, right. In pre-order traversal the pattern is visit, left, right. In post-order traversal 
the pattern is left, right, visit. The three patterns differ in the placement of the visit step. In between left and right for in-order, 
before left and right in pre-order and after left and right in post order. Visiting in this context means adding the node's value to the 
input array. Left means we call the traversal function on the left child of the current node. Right means we call the traversal function on 
the right child of the current node. 
Thus in in-order traversal, the first thing we do is to call the function recursively on the left child of the current node. And when we get 
to that left child the first thing we do is call on its left child and the left child and over and over until we get to the leftmost node in 
the tree. In the code, all three functions are wrapped in if node is not None. That is because when the leftmost node calls on its left child 
ie None node, the function will immediately return. Then we visit the leftmost node by adding its value to the input array, followed by a call
to its right child, which is None node and so the function will return immediately. Thus the entire algorithm will be finished on the leftmost
node, so execution returns to its parent node which will add its value to the input array before calling on its right child (a leaf node) and 
which will call on its left None child, a call which will immediately return, then this right leaf node child add its value to the array, 
followed by a call it its right None child which returns immediately, execution returns to its parent, where all calls are finished so 
execution returns to the parent's parent and so on and so forth.
The significance of in-order traversal for BST is that an in-order traversal will yield a sorted array of the nodes values in ascending order.
The siginificance of pre-order traversal is that the first value will be a tree's root node's value followed by values in the left subtree 
of the root node (and these values start with the left child of the root node), then the values in the right subtree of the root node (and 
these values start with the right child of the root node). The significance of post-order traversal is that triplets of values are added
in left child, right child, parent node. """


#O(n) time | O(n) space due to array | O(d) space if printing node values
def inOrderTraverse(tree,array):
    if tree is not None:
        inOrderTraverse(tree.left,array)
        array.append(tree.value)
        inOrderTraverse(tree.right,array)
    return array #base case, where are at the child of a leaf node. Also return array after completing all calls on current node

def preOrderTraverse(tree,array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree,array):
    if tree is not None:
        postOrderTraverse(tree.left,array)
        postOrderTraverse(tree.right,array)
        array.append(tree.value)
    return array



