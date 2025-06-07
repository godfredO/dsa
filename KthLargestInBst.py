"""The question asks to return the kth largest value in a binary search tree and we are assured that k will be less than or equal to
the number of nodes in the tree. This means if k is equal to the number of nodes we are to return the least value and if k is 1 we 
will be returning the largest value. Now since we are dealing with a bst, we know that an inorder traversal will yield a sorted array.
This is because an inorder traversal will go the way to the leftmost node which has the smallest value, visit it and then visit its
parent which will have the second smallest value followed by its right sibling which has the third smallest node. So this is exactly 
what the first solution does, by conducting an inorder traversal of the binary search tree and storing all of the node values in an 
array, after which we return array[len(array) - k], since the largest value will be len(array) -1 so the kth largest will be 
len(array) - k. 

The second solution is also based on the fact that an inorder traversal yields a sorted array, but instead of going left,visit,right 
and filling up an array from start to end, it reverses the inorder traversal and goes right, visit,left and also keeps track of the 
last value visited and the number of nodes visited. The reasoning being instead of visiting nodes from the smallest to the largest,
why don't we visit them from largest to smallest. Also, instead of storing all values, why not store a single value and keep a count
of the number of nodes visited so far so that if we visit k nodes, the stored value will be our answer. So in this optimal solution the 
only space used is the space for the recursive stack, and since we go all the way to the largest value and back up, k times, we improve
the recursive stack use from O(n) in the previous solution to O(h+k). 

In this solution the base case is if we are at a leaf node's None child or if we have visited k or more nodes, we just return. 
Also in the visit step, we check that the number of nodes visited is less than k, before increasing this tally by 1 and then storing 
the current node's value before going left. The call to go left is inside the if statement that checks we visited less than k nodes,
since there is no need making a call which will terminate at the base case anyway. The call to the right is outside because we first
need to go all the way to the right anyway. That is to say we only visit and go left if we have the current tally is less than k. 
So if k=4 and the current tally of visited nodes is say three, when we do this check, it will yield true, we increment the tally to 4, 
store the current node's value as the value of last node visited, and make a call to its left child and in that call we will realize that 
k == 4 and just return. By nesting, the call to the left child inside the check of tally counts we dont ensure that we really make O(h+k) 
calls only. Otherwise, if we had the call to the left child outside of the if statement, then we we visit k nodes, we wont visit the current 
node but would call on the left child and that call will immediately return because the first thing we check is that if the tally of nodes 
visited is greater than or equal to k, just return. Thus without nesting the left child call inside the if statement that check that 
nodesVisited < k, we would end up with an O(n) time because we would make a bunch of unnecessary calls that we immediately return from and 
even though we never go as far as visiting the nodes in those calls we miss the opportunity to fully optimize the code to O(h+k) ie go all 
the way down the rightmost branch, then visit up to k more nodes. With this optimal coding structure the recursive calls will thus stop when 
k nodes are visited. It is useful to realise that, the largest value in a binary search tree is the rightmost node in the tree, so the 
recursive algorithm will go all the way to this node before the first visit step occurs, which in this case involves storing the current 
node's value and incrementing the counter for number of node's visited as long as number of nodes visited is less than k.

Thus the key idea is reverse in-order traversal, we optimize our space complexity by tracking the last node visited, and we optimize
the time complexity by cleverly nesting the left child call inside the visit step's tally check."""

class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right



"""Inoptimal Solution store array from in-order traversal"""
#O(n) time | O(n) space
def findKthLargestValueInBst(tree,k):
    sortedNodeValues = []
    inOrderTraverse(tree,sortedNodeValues) #this function will populate sortedNodeValues list
    return sortedNodeValues[len(sortedNodeValues)-k]

def inOrderTraverse(node,array):
    #the base case of an inorder traverse is when we reach a None leaf node
    if node == None:
        return
    
    inOrderTraverse(node.left,array)
    array.append(node.value)
    inOrderTraverse(node.right, array)


"""Inoptimal Solution where we get the reversed in-order traversal array. Just to demonstrate, the idea."""


class TreeInfo:
    def __init__(self,numberOfNodesVisited,latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue  = latestVisitedNodeValue

"""Optimal Solution Reverse Inorder Traversal keeping track of number of nodes visited and value of last node"""
#O(h+k) time | O(h) space
def findKthLargestValueInBst(tree,k):
    treeInfo = TreeInfo(0,-1) #-1  here to signify that we havent visited any nodes, any placeholder will do
    reverseInOrderTraverse(tree,k,treeInfo)
    return treeInfo.latestVisitedNodeValue

def reverseInOrderTraverse(node,k,treeInfo):
    if node == None or treeInfo.numberOfNodesVisited >= k:
        return
    reverseInOrderTraverse(node.right,k,treeInfo) #call on right
    if treeInfo.numberOfNodesVisited < k : #after we reach a None leaf child we check how many nodes visited
        treeInfo.numberOfNodesVisited += 1 #increase number visited
        treeInfo.latestVisitedNodeValue = node.value #this is where we actually visit the node
        reverseInOrderTraverse(node.left, k,treeInfo) #then go left

