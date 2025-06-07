"""This question is effectively the same as the KthLargestInBst.py question just the reverse. First thing to realize is that an inorder
traversal of a bst yields a sorted array. Second thing is that since Python is 0-indexed the first smallest value will be at index 0 of
the inorder array, so after grabbing all node values into the inorder array we return inorder[k-1]. So that is the inoptimal solution 
right there. Do an inorder traversal, grab all node values into an inorder array and return inorder[k-1].

The optimal solution like in KthLargestInBst.py is based on the fact that we dont really need to grab all nodes, we only need to visit
up to k nodes. So we create a class data structure that stores the number of nodes we have visited and stores the value of the last node
we visited. So when we go all the way to the leftmost leaf node, in the visit step, we check the number of nodes visited is less than k.
If it is we increment this value in the class data structure and 'visit' by storing the node's value in the data structure then we go
right. Our base case is to return if node is None or if we visited k or more nodes ie node is None or Tree.nodeVisited >=k. At the end 
we return the node value stored in this data structure. So the main difference between this question kthSmallestInBst.py, and the other 
is question, kthLargestInBst.py is that here we do a regular inorder dfs, in the other question we do a reverse inorder dfs. Another 
question that uses a reverse dfs is binaryTreeRightSideView.py , where we do a reverse preorder dfs, visit, right , left like the 
reverse inorder dfs of kth largest right, visit, left."""




"""Inoptimal solution of visiting every node and storing all node values"""
# O(n) time | O(n) space
def kthSmallest(root, k):
    inOrder = []
    getInOrder(root, inOrder)
    return inOrder[k-1]
    
def getInOrder(self, node, inOrder):
    if node is not None:
        getInOrder(node.left, inOrder)
        inOrder.append(node.val)
        getInOrder(node.right, inOrder)
    


"""Optimal solution of visiting only k nodes and storing a single node value at a time"""
class TreeInfo:
    def __init__(self, nodesVisited, lastVisitedNodeValue):
        self.nodesVisited = nodesVisited
        self.lastVisitedNodeValue = lastVisitedNodeValue
        

def kthSmallest(root, k):
    treeInfo = TreeInfo(0,-1)
    getModifiedInOrder(root, treeInfo, k)
    return treeInfo.lastVisitedNodeValue
    
def getModifiedInOrder(self, node, treeInfo, k):
    if node is None or treeInfo.nodesVisited >= k:
        return
        
    getModifiedInOrder(node.left, treeInfo, k)
        
    if treeInfo.nodesVisited < k:
        treeInfo.nodesVisited += 1
        treeInfo.lastVisitedNodeValue = node.val
        getModifiedInOrder(node.right, treeInfo, k)
    