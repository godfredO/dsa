"""The question gives the root node of a binary search tree and an integer and asks to return the value of the bst node whose value
is closest to the integer, and we are assured that there will be only one closest value meaning if the integer is 12, the tree may
contain 11 or 13 but not both since these will both be a distance of 1 from 12. Anyway, this question leans heavily on the BST property
(no surprises there). So since we are expected to return the value of the closest node in terms of value, we initialize the closest value
to positive infinity, and since a BST node contains integer values, we know this closest value will be updated at some point. So first the 
base case, is that at each node we compute the absolute difference between the node and the target value and compares it to the absolute
difference between the target value and the current closest. If difference is lesser for the current node we update the closest value to
be the current node's value otherwise we mainitain the current closest value. After this comparison we take advantage of the BST property
by comparing the current node's value to the target to determine where to move next. If the target is less than the current node's value,
we know that every node to the right of the current node will be greater than or equal to the current node and as such as far from or
farther from the target value. So if the target value is less than the current value, we go left, by updating the current node pointer 
to point to the left child. If the target value is greater than the current node's value, we know that every node to the left of the
current node has a lower value than the current node and as such will be farther from the target so we move right. If the target is equal 
to the current node's value, we break out of the loop because there can't be a closer value. When the loop terminates we return the closest 
value. Due to the BST property we only visit half the nodes in the tree, giving a time complexit of O(log(n)). If this solution is implemented 
recursively, we use O(log(n)) space, which is the depth of a balanced, binary search tree. If implemented iteratively, we use O(1) space."""

"""Recursive approach"""
# Average : O(log(n)) time | O(log(n)) space
# Worst   : O(n) time | O(n) space
def findClosestValueInBST(tree,target):
    return findClosestValueInBSTHelper(tree,target ,float('inf'))

def findClosestValueInBSTHelper(tree,target,closest):
    if tree is None:
        return closest
    
    if abs(target -closest) > abs(target-tree.value):
        closest = tree.value

    #if current node's value is greater, go in the lesser direction ie left subtree to find a closer value to target
    if target < tree.value: 
        return findClosestValueInBSTHelper(tree.left,target,closest)
    #if current node's value is lesser, go in the greater direction ie right subtree to find a close value to target
    elif target > tree.value: 
        return findClosestValueInBSTHelper(tree.right,target,closest)
    #if current node's value equals target, return current node's value ie the updated closest variable
    else: 
        return closest


"""Iterative Solution"""
# Average: O(log(n)) time | O(1) space
# Worst  : O(n) time | O(1) space
def findClosestValueInBST(tree,target):
    return IterativeSolutionHelper(tree,target,float('inf'))

def IterativeSolutionHelper(tree,target,closest):
    currentNode = tree
    while currentNode is not None:

        if abs(target - closest) > abs(target-currentNode.value):
            closest = currentNode.value

        #if current node's value is greater, go in the lesser direction ie left subtree to find a closer value to target
        if target < currentNode.value: 
            currentNode = currentNode.left

        #if current node's value is lesser, go in the greater direction ie right subtree to find a close value to target
        elif target > currentNode.value: 
            currentNode = currentNode.right
        #if current node's value equals target, return current node's value ie the updated closest variable
        else:
            break

    return closest