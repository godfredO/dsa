"""Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or 
memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization 
algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the 
original tree structure.
Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

Example 1:


Input: root = [1,2,3,null,null,4,5]

Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory 
buffer, or transmitted across a network connection link to be reconstructed later, a process known as deserialization. The question is to
design an algorithm to serialize and deserialize a binary tree. You need to ensure that a binary tree can be serialized into a string and this
string can be deserialized into the original tree structure. eg a serialized tree is something like "1,2,3,Null,Null,4,5" where 1 is the root
node, 2 is its left child, 3 its right child, 2 has two None children and 3's left child is 4 and 3's right child is 5.

So there are two ways to go. We could do a breadth first search and serialize the node values that way. We could also use depth first search
using pre-order traversal. It is important to note that there arent any restrictions on the format of the serialized string, we just have to
be able to deserialize it later. So using depth first search with pre-order traversal can help us both serialize and deserialize. How would
we serialize a preOrder traversal string of a binary tree? It is the standard pre-order traversal, only difference is that when we visit a
node we store a string of its value ie '2' for value 2 and when we reach a None child, we store the string 'None' in the preorder array. This
choice of storing 'None' helps us in the deserialization step. This is because in a binary tree,  we don't have the mathematical BST property 
of binary search trees which we can use to help deserialization of binary search trees ie check the question reconstructBst.py, where we only
use a preorder traversal and this mathematical property to reconstruct a bst from a preorder traversal only. So the tree above, serialized 
with preorder traversal depth-first search will be  "1,2,Null,Null,3,4,Null,Null,5,Null,Null" ie we join the strings of node values and None
values with a ',' delimiter ie serializedString = ','.join(preorderStrings).

To deserialize we use a post order traversal depth-first search. We first split the serialized string along the delimiter ','. Now the rest
of the algorithm is based on a technique found in reconstructBst.py too. First we know that the first value in a preorder array is the root
node's value. The next value is either the left child or the right child. So we need a data structure that tracks the index of the current 
value in the array and starts of as 0. So we are going to recreate the tree, one (sub)tree at a time. So we choose create the root node, as 
the value stored at the current index value, increment the value of the pointer and then proceed to create its entire left and right subtrees, 
passing in the pointer object, which will be updated to the current index by the time we finish the left subtree and recursively come back up 
the tree to build the right subtree. Before choosing the root of the current subtree however, we first check if we have a 'None' at the current 
index value in which case we increment the  pointer and then return None value as the child in question, as the base case. At the end of the 
recursive case we return the current root value after connected with its left and right subtrees.

So for the (sub)tree rooted at any node how do we know that its entire left subtree is done and as such the next value is the right child. 
First if we encounter a 'Null' value then we know it cant have a child so if the Null value is a left child, then the next value is its 
parent's right child. If the Null value is a right child, then the next value is its parent's right child. And if a node has two null 
children, then that subtree is done and  the next value is its parent's right child. That is, for every leaf node in the tree, we specified 
what their children node is going to be, Null,Null, and when we are done with the leaf nodes, we recursively go back up the tree. And this 
point is why storing 'None' or 'Null' strings in the serialization method helps us deserialize it. And pre-order traversal is O(n) to 
serialize and post-order dfs deserialization will also be O(n).
Note that ReconstructBST.py and binaryTreeFromPreOrderAndInorder.py are effectively the deserialization step only that None values were not
stored. For ReconstructBst.py, we use the bst property to help us recreate the bst in linear time. For binaryTreeFromPreOrderAndInorder.py,
because None values are not stored, we need the inorder array in addition to the preorder array.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Index:
    def __init__(self, value):
        self.value = value

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        self.modifiedPreorder(root, preorder)
        return ','.join(preorder)
    
    def modifiedPreorder(self, node, array):
        if not node:
            array.append('None')
            return
        
        array.append(str(node.val))
        self.modifiedPreorder(node.left, array)
        self.modifiedPreorder(node.right, array)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder = data.split(',')
        index = Index(0)
        return self.modifiedPostorder(preorder, index)
    
    def modifiedPostorder(self, preorder, index):
        if preorder[index.value] == 'None':
            index.value += 1
            return None
        
        rootVal = int(preorder[index.value])
        index.value += 1
        
        leftSubtree = self.modifiedPostorder(preorder, index)
        rightSubtree = self.modifiedPostorder(preorder, index)
        
        return TreeNode(rootVal, leftSubtree, rightSubtree)
        


class BinaryTreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

"""Serialize tree with pre-order traversal"""
def serialize(root):
    result = []
    serializeHelper(root, result)
    return ",".join(result)

def serializeHelper(node,result):
    if node is None:
        result.append("None")
        return
    result.append(str(node.value))
    serializeHelper(node.left, result)
    serializeHelper(node.right, result)

class deserializePointer:
    def __init__(self, index):
        self.index = index

def deserialize(data):
    values = data.split(",")
    pointer = deserializePointer(0)
    return deserializeHelper(values, pointer)

def deserializeHelper(values, pointer):
    if values[pointer.index] == "None":
        pointer.index += 1
        return None
    
    node = BinaryTreeNode(int(values[pointer.index])) #create root node of subtree
    pointer.index += 1
    node.left = deserializeHelper(values, pointer)
    node.right = deserializeHelper(values, pointer)
    return node