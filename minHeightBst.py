"""The question gives an array of sorted and distinct integers and asks to construct a BST of minimal height. The two properties, sorted
and distinct are essential for this algorithm. Basically to construct a bst of minimal height, there must be as many or nearly as many
nodes in the root's left subtree as there are in the right subtree, in otherwords, the tree needs to be  balanced. If one side is much
longer than the other side the tree will not have minimal height. Another way of putting it is that there there has to be as many values
that are less than the root as there are greater than the root. Usually the right subtree contains values that are greater than or equal
to the root node but because we know our array only contains distinct values, we know in this case all the nodes in the right subtree
will be greater in value than the root. In addition, because we need the root to have as many values less than it as greater than it,
it means that the root node has to be the middle value of this sorted distinct integer array. In fact, as with most binary (search) tree
problems, the problem has to be reformulated to work for the subtree rooted at each node, meaning the subtree rooted at each node must
have as many nodes in the left subtree as there are in the right subtree. This means as each stage we choose the middle value. In other
words, the subtree rooted at each node must be height balanced for the entire tree to be balanced and of minimal height. So to start
we choose the middle value of array to be the root node and since the array is already sorted we know that every integer to the right of the
middle value is in the root's right subtree and every integer to the left of the root subtree has to be in the left subtree. So when its
time to choose the right child of the root we look at all the integers that come after the middle value and choose their middle value. We
do the same for the left subtree. Thus the solution to this question is to always choose the middle value of any sub-array until the start
and end indices used to calculate the middle index cross each other, in which case we set the requesting node's child to None. Note that
if the indices passed are the same eg 0,0 their mid value is 0 and so we create a node with the singular value in the array, and then make
a call with crossed indices on either end 0,-1 and 1,0 either way endIdx < startIdx so we return None to be the child nodes. Thus the
optimal solution here uses a binary search approach."""

class BST:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

"""First implementation where we call insert on root node each time we need to add a node"""
# O(nlog(n)) time | O(n) space 
def minHeightBst(array):
    return constuctMinHeightBst(array,None, 0, len(array)-1)

def constuctMinHeightBst(array,bst,startIdx,endIdx):
    #base case, when there are no more values to insert
    if endIdx < startIdx:
        return    
    midIdx = (startIdx + endIdx) // 2
    valueToAdd = array[midIdx]
    #Create root node first time, otherwise insert new node
    if bst is None:
        bst = BST(valueToAdd)
    else:
        bst.insert(valueToAdd)
    #then recursively re-call the function on either side of valueToAdd
    constuctMinHeightBst(array,bst, startIdx, midIdx -1) #left side of subarray
    constuctMinHeightBst(array,bst,midIdx+1,endIdx)      #right side of subarray
    return bst


"""Second implementation where we manually create and manually insert nodes """
#O(n) time | O(n) space
def minHeightBst(array):
    return constuctMinHeightBst(array,None, 0, len(array)-1)

def constuctMinHeightBst(array,bst,startIdx,endIdx):
    #base case, when there are no more values to insert
    if endIdx < startIdx:
        return    
    midIdx = (startIdx + endIdx) // 2
    newBstNode = BST(array[midIdx]) #manually create bst node with the chose value
    if bst is None:
        bst = newBstNode #create root node
    else:
        if array[midIdx] < bst.value:
            bst.left = newBstNode #manually insert newly created bst node
            bst = bst.left #call recursive function with the newly inserted bst node
        else:
            bst.right = newBstNode #manually insert newly created bst node
            bst = bst.right #call recursive function with the newly inserted bst node
    #then recursively re-call the function on either side of valueToAdd
    constuctMinHeightBst(array,bst, startIdx, midIdx -1) #left side of subarray
    constuctMinHeightBst(array,bst,midIdx+1,endIdx)      #right side of subarray
    return bst


"""Third implementation where we clean up the second implementation Here we dont supply a node to the recursive function call, 
the recursive function already returns a node so we use that node to set its right and left children"""
#O(n) time | O(n) space
def minHeightBst(array):
    return constuctMinHeightBst(array, 0, len(array)-1)

def constuctMinHeightBst(array,startIdx,endIdx):
    #base case, when there are no more values to insert
    if endIdx < startIdx: #crossed indices
        return  None  # return None when algorithm ends
    midIdx = (startIdx + endIdx) // 2  #if start== end then mid == start == end and left right calls will be crossed so None child
    bst = BST(array[midIdx]) #create a node
    #then recursively re-call the function on either side of valueToAdd
    bst.left = constuctMinHeightBst(array,startIdx, midIdx -1) #left child of node comes from left side of subarray
    bst.right = constuctMinHeightBst(array,midIdx+1,endIdx)    #right child of node comes from side of subarray
    return bst
