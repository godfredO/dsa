"""You are given two binary trees root1 and root2. Imagine that when you put one of them to cover the other, some nodes of the two trees 
are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, 
then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.Return the 
merged tree. Note: The merging process must start from the root nodes of both trees.

 

Example 1:


Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

To merge overlapping nodes in the two trees, we have to check the overlapping nodes. The root nodes of both trees overlap, the root's right
child overlap, the left child overlap etc. So if the overlapping nodes are non-Null, the resulting node will have a value that is the sum
of the two nodes. If one of the overlapping node, the resulting node will have a value of the non-null tree so its like conducting a sum
by assuming 0 for the null value. If both overlapping nodes are None, then the resulting 'node' will simply be a None value.

So this is a type of question that requires that we traverse two trees at the same time like leaftraversal.py and actually a linked list
question sum_of_linked_lists.py. In fact there is a lot of similarities between binary trees and linked lists. Anyway as we traverse both 
trees, we will be creating the resulting tree. If both of the trees are None, the resulting node will also be None and that is our base
case . Otherwise we add up the values to get the value of the resulting node, assuming 0 as the value for a node if its None otherwise the
node's actual value. As such we access the value's separately so that we can access the node's value or 0, then we add it together, create
a new node with the value and then proceed to merge the left subtree and right subtree.
 
Now how suppose that root1 has no right child but root2 has an entire right subtree, we can assume 0 for root1's right child in the addition 
with root2's right child but how do we write our recursive function such that we still keep traversing both trees when in fact, we can't 
traverse down tree1 again but still need to traverse tree2. Well since accessing the left or right attribute on a None value will throw an 
error, when making the call to merge subtrees, we only pass in tree1.left if its not None else we pass in None and the same for tree2. This 
way we are able for avoid an error, but still ensure that the logic of our program works since in the next recursive call, we will assume 0
as value and None as its child and so on and so forth until we reach a point where both trees are None values and which point we return None
and proceed no further. At the end of the recursive case we return the new node we just created. So the crux of this simple question is 
checking if a node is None before trying to access its right or left child and if it is, assigining a default of None. 

Since we have to traverse both trees, the total time complexity is O(n+m) n= nodes in tree1, m= nodes in tree2. And the space complexity
is on the same order of O(n+m) although you can actually also say O(max(n,m)) time and space. That said this question is the binary tree
equivalent of sum_of_linked_lists.py. 

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
        return helper(root1, root2)
    

    
def helper(node1, node2):
    if node1 is None and node2 is None:
        return None
    
    val1 = node1.val if node1 is not None else 0
    val2 = node2.val if node2 is not None else 0
    
    val = val1 + val2
    
    root = TreeNode(val)
    
    tree1Left = node1.left if node1 is not None else None       #check that node1 is not None
    tree2Left = node2.left if node2 is not None else None       #check that node2 is not None
    
    root.left = helper(tree1Left, tree2Left)
    
    tree1Right = node1.right if node1 is not None else None     #check that node1 is not None
    tree2Right = node2.right if node2 is not None else None     #check that node2 is not None
    
    root.right = helper(tree1Right, tree2Right)
    
    return root
        