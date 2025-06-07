"""Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST. According to the 
definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both 
p and q as descendants (where we allow a node to be a descendant of itself).” All Node.val are unique. p != q. p and q will exist in the 
BST. This question is the BST version of lowestCommonManager.py question.

Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:
Input: root = [2,1], p = 2, q = 1
Output: 2
 
"""


"""Solution One which repurposes the lowestCommonManager solution where we return a class instance that tracks the lowest common
ancestor found and the number of descendants found.  So we call the recursive helper function with the root , p, q where p,q are
the descendants we are looking for. So if we are at a None node we return TreeInfo(None, 0) meaning we havent found the lowest
common ancestor and we found 0 of the descendants in the subtree rooted at that None node of course. Then we initialize 
numDescendantsFound as 0, pack the left child and right child in that order in a list and in a for loop, call the recursive 
on the child nodes. Whatever instance of TreeInfo we receive from the child, we store as childInfo. Then we check if the lowest
common ancestor attribute of the childInfo class instance received is not None. If its not we return that class instance and in
the main function we return lowestCommonAncestor attribute of this received class. However we increment the numDescendantsFound
variable with whatever is stored in the childInfo attribute. Then outside this for loop we check if the current node is itself
one of the descendants. If it is, we increment the numDescendantsFound variable by 1. Then we check if numDescendantsFound is 
2. If it is, then lowestCommonAncestor variable is the current node else it is None. Then we return a TreeInfo() instance with
lowestCommonAncestor and numDescendantsFound. If this were an ordinary binary tree instead of a bst, this would be the solution."""

"""Solution Two recognizes that this is a BST problem, so we can move intelligently using the BST property. So we can also assume 
unique values. So first off the root node can be a descendant of itself so it can be equal to descendantOne or descendantTwo. Now 
lets say its not and the two descendants are in different subtrees. Lets say p (descendatOne) is less than the root node and q 
(descendantTwo) is greater than the root node, then they will be in different subtrees. Since the are in different subtrees, we 
split the direction where we go look for them and as such, the root node will be their lowest common ancestor. So if p is in the left 
subtree and q is in the right subtree, then the current node is the lowest common ancestor. If they are both less than or both greater 
than the loest common ancestor, then we go in one direction until this split occurs. If the current node is equal to one of them then 
the other must be in a subtree of the current node either left or right subtree so the current subtree since we start from the root 
node and go down the tree in one direction. This is the optimal solution because due to the use of the BST property we dont visit
every node so the time complexity is O(log(n)) and space complexity is also O(log(n)) if the tree is balanced but in general it is
tinme of O(h) and space of O(h) due to the recursive stack. If this is done iteratively, then the space is O(1). So the optimal 
solution is an iterative implementation of this solution. 
The code for this is actually quite clean. If both descendant node values greater the current node, then they are in the right subtree
of the current node so  we update current node to the right child, else if both values are less than the current node, then they are
in both in the left subtree of the current node so we update current node to the left child. Else the current node is the lowest
common ancestor either because the descendants node are in either subtree so we split directions at the current node or the current
node is one of the descendants and the other is in one of it subtrees, either way current node is the lowest common ancestor."""


#Naive solution, treating the BST as a generic graph without using the BST property.
class TreeInfo:
    def __init__(self,lowestCommonAncestor, numDescendantsFound):
        self.lowestCommonAncestor = lowestCommonAncestor
        self.numDescendantsFound = numDescendantsFound

#O(n) time | O(n) space
def lowestCommonAncestor(root, p, q):
    return getTreeInfo(root, p, q).lowestCommonAncestor


def getTreeInfo(node, descendantOne, descendantTwo):
    if node is None:
        return TreeInfo(None, 0)
    
    numDescendantsFound = 0
    for child in [node.left, node.right]:
        childInfo = getTreeInfo(child, descendantOne, descendantTwo)
        if childInfo.lowestCommonAncestor is not None:
            return childInfo
        numDescendantsFound += childInfo.numDescendantsFound
    
    if node == descendantOne or node == descendantTwo:
        numDescendantsFound += 1
    lowestCommonAncestor = node if numDescendantsFound == 2 else None
    return TreeInfo(lowestCommonAncestor, numDescendantsFound)



"Optimal solution "
#O(log(n)) time | O(d) space
def lowestCommonAncestor(root , p , q ) :
    current = root
    while True:
        if p.val > current.val and q.val > current.val:
            current = current.right
        elif p.val < current.val and q.val < current.val:
            current = current.left
        else:
            return current