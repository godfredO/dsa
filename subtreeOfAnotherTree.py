"""Given the roots of two binary trees, root and a subRoot, return True if there is a subtree of root with the same structure and node 
values of subroot and false otherwise. A subtree of a binary tree, tree, is a tree that consists of a node in tree and all of this node's 
descendants. The tree, tree, could also be considered a subtree of itself. 

This question in some ways is similar to sameTrees.py where we check that two trees have the same struture and we check if both subtrees 
are equal if the value of the root node is the same. Here we could do something similar, but since we are looking for a subtree, we might 
not match the root's value so we ask the same question to the left subtree and right subtree of the root. And here we are not asking if it 
is the same tree rather we are asking if it is a subtree, though when we eventually find the subtree as rooted at some node it will be the 
same tree. In otherwords, the subtree we are looking for could be rooted at the current root or at its left child or its right child.
So we if we check if the subroot is rooted at root and we find True, we return True otherwise we check if subroot is rooted at the current
root's right child or left child. And these checks are done by calling the function from isSameTree.

So the base cases, if subroot is None then we know that it is definitely a subtree of tree, since tree will contain a leaf node and the
children of leaf nodes are None values. So if the subroot is not None, the next thing we check is if tree is None. If it is then since
we didnt return True for subroot being None, it means subrrot is not None and a non-None node cannot be the subtree of a None node. So
we return False. So those are the base cases. However if tree is not None and subroot is not None, then we compare both of them, using
the sameTree function. This function will return True when a match is found but if it returns false, we need to check both subtrees of
tree in case subroot is a subtree in tree's left / right subtree. So we first call isSameTree on tree and subroot. If this returns true
we found subroot in tree so we return true . If not we compare subtroot to left subtree and right subtree by calling the recursive 
isSubtree function and we compare these with an or. ie If subroot is found in either of them or both subtrees we return True, but if its 
not found in either of them we return False. This is a preorder dfs because we verify the current root, before looking at its children."""


"""Solution  I"""
def isSubtree(root, subroot):
    if subroot is None: #if subroot is None, then its a subtree even if root is None or its a child of a leaf node in root tree
        return True
    
    if root is None :  #if subroot is not None then if root is None, then subroot cant be a subtree of None root tree
        return False
    
    if isSameTree(root, subroot): #check if root is itself the subtree that equals subroot, call isSameTree, if True, return True
        return True #if we subroot is the subtree rooted at root, return True 

    return isSubtree(root.left,subroot) or isSubtree(root.right, subroot) #if False, heck if subroot in root's left or right subtree

def isSameTree(p , q) :
    if not p or not q: #if either node is None then True if both are None, False if only one is None
        return not p and not q #so check if both are None
        
    if p.val != q.val: #at this point neither is None so if their values don't match return False
        return False
        
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right) #if values match, compare left subtrees and right subtrees



"""Same solution different coding of isSameTree.py"""
def isSubtree(root, subroot):
    if subroot is None: #if subroot is None, then its a subtree even if root is None or its a child of a leaf node in root tree
        return True
    
    if root is None :  #if subroot is not None then if root is None, then subroot cant be a subtree of None root tree
        return False
    
    if isSameTree(root, subroot): #check if root is itself the subtree that equals subroot, call isSameTree, if True, return True
        return True #if we subroot is the subtree rooted at root, return True 

    return isSubtree(root.left,subroot) or isSubtree(root.right, subroot) #if False, heck if subroot in root's left or right subtree

def isSameTree(headOne, headTwo):
    if headOne is None and headTwo is None: #if both nodes are None they are the same tree
        return True
    
    #if they are not the same nodes values or one is None and other is not return false
    if (headOne is None and headTwo is not None) or (headOne is not None and headTwo is None) or (headOne.value != headTwo.value):
        return False
    
    #if values are the same, cant conclude yet, check left subtree and right subtree
    return isSameTree(headOne.left, headTwo.left) and isSameTree(headOne.right, headTwo.right)