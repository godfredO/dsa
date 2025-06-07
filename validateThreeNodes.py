"""Given three nodes which belong to a BST, nodeOne, nodeTwo, nodeThree, we are to write a function that returns a boolean representing
whether one of nodeOne, nodeThree is an ancestor of nodeTwo and the other is a descendant of nodeTwo. That is True means either nodeOne is]
an ancestor and nodeThree is a descendant of nodeTwo or nodeThree is an ancestor and nodeOne is a descendant of nodeTwo, otherwise False."""
class BST:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right


"""A valid bst node has a left and right attribute, for children nodes, but no attribute that points to the parent node. Thus we can only 
verify if one node is a descendant of another node but we can't directly verify if one node is the ancestor of another node without a parent
node attribute unless we iterate and create a dictionary mapping but thats overkill. Here we are going to go with checking if one node is the
descendant of another by applying the bst property and choosing a child node, left or right until we find the descendant node or we reach a 
leaf node's child node ie None, at which point we can say the two nodes are not descendant and ancestor nodes. 
Solution one first treats node one as the ancestor of node two ie it verifies if node two is the descendant of node one. If it turns out that 
node one is the ancestor ie node two is the descendant of, then to verify that node three is the descendant of node two aka verify that node 
two is the ancestor of node three. In otherwords we verify that node two is the descendant of node one and if this is true we verify that
node three is the descendant of node two and we return the result. Similarly if it turns out that node one is not the ancestor of node two 
ie node two is not a descendant of node one, then we check if node three is the ancestor of node two, which if true will be 
followed by verifying if node two is the ancestor of node one ( ie making node one a descendant of node two). Also, the space complexity is
the height / depth of the tree is the descendant check is done recursively but it is constant space if done iteratively. Doing it iteratively
simply means using a while loop whose condition is while node is not None and node is not target. Inside this while loop we update node to
be left if the target.value < node.value else node.right and when the loop breaks either because node is None or target, we check if node is
target. The interesting thing about this solution is that be using complement thinking, we are able to use the same helper function four times
knowing that it will be called at least two times or at most three times. In the case where nodeTwo is the descendant of nodeOne or the 
the descendant of nodeThree, both if statements return False, meaning we never hit the either inner return statements so we return False at the 
end. This situation can mean, nodeTwo is in a diffrent subtree from both nodeOne and nodeThree, this quirky situation is actually the 
inspiration for the optimal solution."""

#O(h) time | O(h) space - where h is the height of the binary tree
def validateThreeNodes(nodeOne,nodeTwo,nodeThree):
    #(possibleAncestor, possibleDescendant),to verify ancestor, switch ancestor and desc nodes
    if isDescendant(nodeTwo,nodeOne): #if nodeTwo is nodeOne's ancestor,    ie if nodeOne is nodeTwo's descendant 
        return isDescendant(nodeThree, nodeTwo) #check if nodeThree is nodeTwo's ancestor ie if nodeTwo is nodeThree's descendant
    
    if isDescendant(nodeTwo,nodeThree):#if nodeTwo is an ancestor of nodeThree
        return isDescendant(nodeOne,nodeTwo) #check if nodeOne is nodeTwo's ancestor
        
    return False #if nodeTwo is below both, nodeThree and nodeOne in the tree, both if statements will return False


def isDescendant(node,target): #check if target is a descendant of node
    if node is None: #if called from a leaf node, target wasnt found in node's descendant subtree
        return False

    if node is target: #checking the equality of  objects themselves, not just their values
        return True 
    
    #if the target value is less than current node value then check current node's left subtree else check right subtree
    return isDescendant(node.left,target) if target.value < node.value else isDescendant(node.right,target)


"""Iterative version of solution one. Improves space complexity by rewritting isDescendant() helper funtion to use
iteration vs recursion"""
#O(h) time | O(1) space
def validateThreeNodes(nodeOne,nodeTwo,nodeThree):
    #(possibleAncestor, possibleDescendant),to verify ancestor, switch ancestor and desc nodes
    if isDescendant(nodeTwo,nodeOne): #if nodeTwo is nodeOne's ancestor,    ie if nodeOne is nodeTwo's descendant 
        return isDescendant(nodeThree, nodeTwo) #check if nodeThree is nodeTwo's ancestor ie if nodeTwo is nodeThree's descendant
    
    if isDescendant(nodeTwo,nodeThree):#if nodeTwo is an ancestor of nodeThree
        return isDescendant(nodeOne,nodeTwo) #check if nodeOne is nodeTwo's ancestor
        
    return False


def isDescendant(node,target): #check if target is a descendant of node
    while node is not None and node is not target: #keep updaating node until its is None or the target
        node = node.left if target.value < node.value else node.right #bst property
    
    return node is target #check if node stops at target


"""Approach Two which uses a slightly different logic to achieve an improved average time complexity and constant space complexity. The idea is 
that the question is asking to verify if nodeTwo is  on the path from nodeOne to nodeThree. This is because if nodeOne is nodeTwo's ancestor and 
nodeTwo is nodeThree's ancestor then all three nodes must be in the samesubtree. This is assuming the subtree in question is rooted at nodeOne, 
then by following the BST principle, and searching for nodeThree,we will encounter nodeTwo on this path. Similarly if nodeThree is the ancestor, 
then nodeTwo will be on the path from nodeThreeto nodeOne. Thus in this algorithm, we only ever go the distance from nodeOne to nodeThree and 
this distance is at most equalto the height of the binary search tree ie time complexity is O(d) where d is the distance between nodeOne and 
nodeThree. In the implementation, we assume that either nodeOne or nodeThree is the ancestor and iterate at the same time, from nodeThree to 
nodeOne and from nodeOne to nodeThree. Since either path can lead to a None value, nodeTwo or to the other of nodeOne / nodeThree, at each step 
of this algorithm, we check if nodeOne and nodeThree are both None, we break, if either path is at nodeTwo at which point we break the path that 
is at nodeTwo and check if the other node is the descendant of nodeTwo; if the two paths have converged, which will happen if nodeThree is a 
leaf node and thus is not updated and is also a descendant of nodeOne, in which case we return False since we didnt find nodeTwo. Another way of
saying this is that there are three break conditions; if we get to None on the search for nodeThree from nodeOne or on the search for nodeOne 
from nodeThree; if we get to nodeTwo in either searches; if we find nodeThree on the search from nodeOne; and if we find nodeOne on the search
from nodeThree. In three of these conditions we don't need to continue further ie if we are at None for both searches or if we find either 
nodeOne or nodeThree from the other's search. This is because in any of these cases we know nodeTwo is not on the path betwen the two other 
nodes. If however we break because on search found nodeTwo then we verify that the other node is a descendant of nodeTwo. It is important to 
also know that if only one of the searches is at a None, we just pause that search and continue with the other until it also reaches None, 
or finds nodeTwo. If you imagine a case where nodeThree is a child of nodeOne and we actually find nodeThree from nodeOne, we would have done 
only a single traversal step to break out of the loop and return the answer, thus giving a better average time complelxity than the previous 
solution. However once we find nodeTwo from either searches, and use iteration to find if the other node is a descendant of nodeTwo, both 
solutions will have the same complexities. The space complexity is the height / depth of the tree is the descendant check is done recursively 
but it is constant space if done iteratively"""

#O(d) time | O(1) space - where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne,nodeTwo,nodeThree):
    searchOne = nodeOne #start path one search at nodeOne
    searchTwo = nodeThree

    while True: #four break conditions
        foundThreeFromOne = searchOne is nodeThree
        foundOneFromThree = searchTwo is nodeOne
        foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        finishedSearching = searchOne is None and searchTwo is None
        if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishedSearching:
            break

        if searchOne is not None:
            searchOne = searchOne.left if searchOne.value > nodeTwo.value else searchOne.right

        if searchTwo is not None:
            searchTwo = searchTwo.left if searchTwo.value > nodeTwo.value else searchTwo.right
    
    #this is necessary because we dont have access to foundThreeFromOne, foundOneFromThree etc outside the while loop
    foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
    foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo #if finishedSearching, then foundNodeTwo is false for either search
    if not foundNodeTwo or foundNodeFromOther: #if instead of finding nodeTwo both searches found the other starting points, or finished searching
        return False  #then

    return searchFromTarget(nodeTwo,nodeThree if searchOne is nodeTwo else nodeOne) #since we foundNodeTwo,

def searchFromTarget(node,target): #check if target is a descendant of node
    while node is not None and node is not target: #keep updaating node until its is None or the target
        node = node.left if target.value < node.value else node.right #bst property
    
    return node is target #check if node stops at target