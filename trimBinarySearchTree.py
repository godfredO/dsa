"""Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements 
lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any 
node's descendant should remain a descendant). It can be proven that there is a unique answer. The value of each node in the tree is unique.
root is guaranteed to be a valid binary search tree. Return the root of the trimmed binary search tree. Note that the root may change 
depending on the given bounds.

Example 1:
Input: root = [1,0,2], low = 1, high = 2
Output: [1,null,2]

Example 2:
Input: root = [3,0,4,null,2,null,null,1], low = 1, high = 3
Output: [3,2,null,1]


So right off, we will need to re-formulate the question for the (sub)tree rooted at each node. If the root value is less than the low value
then the entire left subtree is less than the low value. If the root value is greater than the high value then the entire right subtree is
greater than the high value. Note that the binary search tree is guaranteed to have unique values. Otherwise if the root doesnt fall out of 
bounds, we need to go through each subtree and find some subtree whose root falls out of bounds, on the right, we might find some value which 
is greater than high value; on the left, we might find some value which is less than low value. Whenver we find a root which falls out bounds, 
one of its subtrees will also be out of bounds, depending if falling out of the lower bound of the higher bounds. In any case, we will need 
to remove it and the subtree that falls out of bounds. The subtree that falls out of bounds is easier removed by setting it to None. So if the 
root node is less than low value, then its left child is set to None. If the root is greater than high value, then its right child is set to 
None.

Removing the root of a (sub)tree will depend on a couple of factors namely is it the root of the tree, and how many non-Null children does it 
have. This process is actually discussed in bstConstruction.py and bstConstructionII.py, remove method. If the node is not the root of the
entire tree, and has two None children ie is a leaf node, then we just set the node to None. So how do we code this out in the cleanest 
way possible. We can say that if a node is not out of bounds, the we call the trim function on its left/right subtree and assign the result of 
the returned node as its new left/right subtree .  This means that if the left/right child is in bounds, then it will return itself. If on the
otherhand the node is out of bounds then we will replace it with the returned value of calling on the subtree that isnt negated by the test
the root failed. That is if the root of a subtree, is less than low, then we replace it with the returned node of calling on its right subtree.
Similarly if the root of a subtree is greater than high, then we replace it with the returned node of calling on its left subtree.
The way we replace a node value is simply to return the result of calling on the non-negated subtree. Now we cant trim None values so in that 
case we return None to its parent just like it was anyway. Thus in this solution, we are recreating the tree again as we go. 

"""
def trimBST(root, low, high):
    if not root:
        return None
    
    if root.val > high:
        return trimBST(root.left, low, high)
    
    if root.val < low:
        return trimBST(root.right, low, high)
    
    root.left = trimBST(root.left, low, high)
    root.right = trimBST(root.right, low, high)

    return root
