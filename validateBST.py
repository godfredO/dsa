"""This question is basically asking if every node in a tree is a valid BST node which states that a BST node is valid if its value is
strictly greater than the value of every node in its left subtree and strictly equal to or less than the value of every node in its right
subtree. Another way of saying this is that if a node is the left child of its parent, then its value has to be strictly less than its
parent's value and if its the right child of its parent, then its value has to be strictly greater than or equal to its parent's value.
Thus as we go down a tree, a node's value has to fall within certain boundaries determined by its relationship to its parent and its 
parent's parent etc. So in this solution we give a lower bound of negative infinity and a positive bound of positive infinity to the root 
node and as we go down the tree we update the lowerbound with a node's value if we go right and the upper bound with a node's value if we 
go left and note that a node is valid if its value falls within its passed bounds and its children are within their own updated bounds. 

The key to coding out this solution is to have two base cases, one for True, and one for False. We add the True case to when a node is 
None and we explicitly state the False case. A node is not a valid BST node if it doesnt fall within its minValue and maxValue. A valid
BST node will have a  minValue <=  node.value  < maxValue and as stated before, when we go from a parent node to its right child, the
parent node's value becomes the  minimum value of its right child since the right child's value has to be equal to or greater than its
parent node's value. In the same way when we go from a parent node to its left child, the parent node's value becomes the maximum value
of its left child since the left child has to be strictly less than its parent node's value. Therefore if we find a left child node
whose value is greater than or equal to it parent node's value ie displaying right child behavior or if we find a right child node whose
value is less than its parent node's value ie displaying left child behavior, that node's value is violating the BST principle and 
we return False immediately. If the current node doesnt violate the BST principle, maybe its children do. So we don't return True just
yet, we return the result of checking its entire left subtree and right subtree. If we are able to reach None node without having hit
the False case then we can be satisfied that the subtree in question is indeed valid. That is why we return True if node is None.  It 
means we never hit a False in any of the nodes above it. If we had, we would have returned False immediately and not continued down. 
If we are able to go down both subtrees and reach leaf nodes without ever hitting False then the tree is valid. As such we return the
result of recursively calling the function with updated bounds on the left and right subtree if the current node is valid 
ie return rec(leftSubtree, lowerBound, node.value) and rec(rightSubtree, node.value, upperBound).

So that is the key to coding out this problem, if a node's value violates its passed minValue and maxValue ie node.value >= maxValue or
node.value < minValue, we stop there and return False. Otherwise we keep going down the tree by passing its value into the maxValue of
its left child and minValue of its right child and we return result of LeftSubtree And result of rightSubtree. If the node is None we 
return True, (and we need to check this first so that we are not trying to access a None node's value), because it means we got all the 
way down the tree without finding an invalid node. Thus if both subtrees return True we return True, if one or both return False, we 
return False.


This is a pre-order dfs since at the subtree rooted at each node,we validate the current root node. If the current node is invalid, we 
return False immediately. Otherwise we validate the entire left subtree (go left), then we validate the entire right subtree  (go right).  
Then return the result of validating the left and right subtrees and return the answer up the tree, where the current root's parent will 
be waiting for the answers in a pre-order dfs. 

We could also arrange the steps in a post-order way where we validate entire left subtree, entire right subtree, current node before
return the result of validating the entire subtree rooted at a node. However I believe that the spirit of the solution is pre-order
and I generally find that a lot of preorder question can be written in a postorder way also. To see the post-order dfs solution, check
validateBSTII.py.

With that said it is also important to verify the definition of a valid BST. On leetcode, the validate Binary Search Tree defines the
right subtree as only containing nodes with keys greater than the root node value and not the algoexpert way (greater than or equal to), 
so if a question says that, you have to add an equal sign when comparing a value to the lowerbound or minVal ie if a right child has
the same value as its parent, its invalid. Again all depends on the reading  of the question."""

def validateBst(tree):
    #the root node has neg inf and pos inf as its min and max values
    #helper function will recursively validate all subtrees and bubble value up to root
    return validateBstHelper(tree,float("-inf"), float("inf"))

def validateBstHelper(tree,minValue,maxValue):
    #first base case, the children of a leaf node (Null value) is a valid BST
    #if no subtree is False from root to leaf, then tree is valid and True bubbles up to root
    #a leaf's child will have either a number max or min or both 
    if tree is None:
        return True

    # minValue <= node.value < maxValue for a valid BST
    #second base case, when we prove a node isnt a valid BST
    if tree.value < minValue or tree.value >= maxValue:
        return False
    
    #recursive case, validate the left and right subtrees
    #a node's value is strictly greater than all nodes is its left subtree
    leftIsValid = validateBstHelper(tree.left,minValue,tree.value)
    #a node's value is less than or equal to all nodes is its right subtree
    rightIsValid = validateBstHelper(tree.right,tree.value,maxValue)
    return leftIsValid and rightIsValid


def validateBst(tree):
	return validateHelper(tree,float("-inf"), float("inf"))

def validateHelper(node,lowerBound,upperBound):
	if node is None:
		return True
	
	if node.value >= lowerBound and node.value < upperBound:
		return validateHelper(node.left, lowerBound, node.value) and validateHelper(node.right, node.value, upperBound)
	return False

#Same code as above, using default values instead of a helper function
def validateBst(tree, lowerBound=float("-inf"), upperBound=float("inf")):
	if tree is None:
		return True
	
	if tree.value < upperBound and tree.value >= lowerBound: 
		return validateBst(tree.left, lowerBound, tree.value) and validateBst(tree.right, tree.value, upperBound)
	return False