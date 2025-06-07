""" This question gives a non-empty array of integers, tells you that the array represents the pre-order traversal of a binary search tree.
Now because this is a pre-order traversal of a binary search tree we can use some key observations to re-create the binary search tree.
First off a pre-order traversal is visit, left, right, meaning the first value in the array is the first value we visited. Since the traversal
starts from the root node it means that the first value in a given array is the root of the (sub)tree it represents. The second observation is
that in a pre-order traversal we traverse the entire left subtree of the root before we visit the right child of the root and since the right
child has a value equal to or greater than its parent (root), it means that the right child of the root is the first value after the root value
that is greater than or equal to the root value. It also means that every value between the root value and the right child value must be in 
the left subtree of the root value and every value after the right child must be in the right subtree of the root value. So for example if the
second value in the array is greater than or equal to the first value then it means that the first value is the root value, the second would
be the right child meaning this particular root value has no left child, if we use list slicing, it means we would have been looking for a left
child between the first and second value ie a slice of length 0. This is essential because this becomes the base case of our algorithm when
we know to return None as the child of a node. Also since this binary search tree is valid, it means that these observations hold for the
subtree rooted at each node. So we start off by choosing the first value of the passed array to be the root, use a loop to find the right child
index, by looping from the second value and comparing every value to the root value. We cleverly initialize the rightChildIdx as the length
of the passed array, and in the for loop, the first time, we find a value that is greater or equal to the root, we update rightChildIdx to
that value's index and break out of the for loop. This means if the root has no right child, the rightChildIdx remains the length of the array.
Then we using the rightChildIdx we slice to create an array for the root's left / right child subtrees, do a left child subtree recursive call
with the appropriate sliced array, which will return either a BST node or None, which will be inserted as the root nodes left and right child.
The simplest way is to say root = bsT(array[0]) root.left = rec(leftSlice) root.right = rec(rightSlice) return root. However in the code we
go another route. We dont create the root node just yet, we wait to receive the left and right child nodes and when we have the right and left
child nodes then nodes we call the BST class to create a the root node and connect it to its right and left children nodes, by passing the 
right/ left child nodes into the instantiation method. This is the approach of the first solution where we conduct three O(n) operations, 
looping, slicing for left subtree and slicing for right subtree for O(3N) and the whole situation is repeated N times giving a time complexity
of O(n^2). 

The second solution takes advantage of another important interpretation of a valid BST property and what it means to be a valid BST tree, namely 
that a node's parent and grandparents all the way to the tree's root place a lower bound and an upper bound on the allowable values of a node in 
order for the tree to remain valid. Specifically if we go from a parent node to its left child then the parent node's value is an upper bound for 
the left child. Similarly if we go from a parent node to its right child then the parent node's value is a lower bound for the right child.  
So in solution two, we pass the root value of the current subtree as a lowerbound to its right child (subtree) and as an upper bound to its left 
child (subtree). But how do we avoid slicing and if we avoid slicing how do we choose the 'first' value as the root of the next subtree and how 
do we know to set None for a right / left child. Well for starters we use an object to store the index of the tree that we would be the 'first' 
value if we were slicing a passing a shorter array each time. Obviously, this object will start at 0 for the tree's root node but in each call 
it is incremented by 1. Because of this if we ever have this stored index go out of bounds we know to return None. We also know to return None 
if the current root value passed does not fit into the bounds that are passed. Thus if the current Node be created doesnt fit into the bounds of 
the parent that called for it then that parent has a None child . Also because we traverse and visit the entire left subtree before the right 
subtree  of a node in a pre-order we need to make sure that the call for the left subtree happens first before the right subtree call. This 
also ensures that by the time we create a node we have its left child and right child because by the time we get the node for the left child we 
will also be using the updated current node index to look for the right child from the correct place. And if the value being considered is 
out of bounds, we know to return None as well as when we go out of bounds. Solution two cleverly increments an index to consider to avoid 
slicing for O(n) time. The space is O(n) which happens in the case of a linked list type of tree since all calls will be pending until the l
ast node is done."""

class BST:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

"""Solution one where we pass for each position in the input array we loop through the remaining array
to find the position for the right child. if tree is like a linked list we have a lot of calls to do"""
#O(n^2) time | O(h) space
def reconstructBst(preOrderTraversalValues):
    if len(preOrderTraversalValues) == 0:
        return None #Set None node as child node if array is empty. such as when rightSubtree is from array[len(array):end]
    
    currentValue = preOrderTraversalValues[0] #we are trying to create a valid BST node with this value
    rightSubTreeRootIdx = len(preOrderTraversalValues) #assume right child may not exist

    #find value for the right child for node with value currentValue
    #by looping through call array for first value greater than the value of node we are trying to create
    for i in range(1,len(preOrderTraversalValues)): #exclude current value when finding the rightSubtreeRootIdx
        value = preOrderTraversalValues[i]
        if value >= currentValue: #>= because duplicate values go in the rightsubtree
            rightSubTreeRootIdx = i
            break
    
    #create left child node and tight
    leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubTreeRootIdx]) #from after current node value to rightSubtree index
    rightSubtree = reconstructBst(preOrderTraversalValues[rightSubTreeRootIdx:]) #if rightSubTreeRootIdx == len(array) this is []
    return BST(currentValue,leftSubtree,rightSubtree)





"""So for the optimal solution we start with a realization that all BST's have which is that a parent node's value is the maxValue for its 
left child (subtree) and the minValue for this right child (subtree). By this we mean that the left child is strictly less in value to the 
parent node, and the right child is greater than or equal to its parent node's value. The next observation has to do with pre-order traversal 
which is that in a pre-order traversal we actually visit the entire leftmost branch of the tree first ie we keep going left all the way to the 
leftmost leafnode, which has None node children, before we visit the right child of this leftmost leafnode's parent. In otherwords, if the 
leftmost branch has four nodes, these will be the four nodes in the pre-order traversal array after the root (first). Then after the leftmost 
leafnode's value, the next value will be the right child of its parent or if the leftmost leafnode's parent has a None right child, then the 
next value in the preorder traversal array after the leftmost leafnode will be the right child of its parents parent. Thus its leftmost branch, 
then parent's right child, grandparent's right child, great grand parent's right child all the way up till we get to the right child of the root 
node. 

Now as we go left down the tree, we update the next value's maxValue with a parent's value, as we go up the right children, we update the 
next value's minValue with the parent's value. So when we are at the leftmost leafnode's the next element in the array will fail the minValue, 
maxValue check when checked for leftchild ie leftmost leafnode's value is maxValue  or for rightChild ie leftmost leafnode's value is minValue.
So when a value fails its minValue, maxValue check, we know that left/right child of the node that made the call, is None. Also note that
as we go down and up the tree, we are still going from left to right in the preorder array. So we start at index zero, with a minValue of 
-inf and a maxValue of +inf and since any integer will pass this check, we update the current index to index 1, and check if the value
at index 1 is the left child of the root, if it is we ask if value at index 2 is the left child of the value at index 1 and so on.
Now if we ever get to the last index in the array, then the next index will be equal to the length of the array, meaning the last index value
must have a None child in the tree since child nodes are either Bst nodes or None. 

Anyway that what the optimal solution does, it takes an object which stores the current index we're at in the array, the preorder array, 
the minValue, and the maxValue. The first thing it checks is if the current index is equal to the length of the preorder array. If it is, 
then we are looking for a child of the last index value so we return None as the child. Next thing is we access the value at the current 
index and check if it violates the minValue, maxValue check. If it does, we return None to the parent that called it. If it doesnt, we 
increment the current index, update the maxValue and check if the value at the updated current index is the leftchild. If it turns out the 
next value is the left child, that will go on and create its  entire subtree so that when execution returns to the orginal call, the current 
index will have been updated to reflect the position of the right child in the preorder array, then we update the minValue and do the minValue, 
maxValue check at the now current index of the preorder array for the right child. If that fails, we receive a None as the right child. If the 
check doesnt fail, then that right child will go ahead and create its entire subtree and with the returned left child node and right child node, 
we create the current node and have its left attribute point to the left child and the right attribute point to the right child. So in summary, 
if current index equals length of preorder array, return None. If value at current index fails minvalue,maxvalue check, return None. Otherwise, 
increment current index and check if the value at the current index is the left child. If it is, create entire left subtree, return root of left 
subtree ie left child and an updated current index. Then check if the value at the updated current index is the right child. Just another 
observation of recursive solutions, if wondering about the base cases, look at the inputs. We pass in a current index, so we have a base case 
for that. We also pass in the minValue, maxValue, and we have a base case for those too.
 """

class TreeInfo:
    def __init__(self,rootIdx):
        self.rootIdx = rootIdx

#O(n) time | O(n) space
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)  #start at index 0
    return reconstructBstFromRange(float("-inf"), float("inf"), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound,upperBound,preOrderTraversalValues,currentSubtreeInfo):
    #base case 1, left or right child of a leaf node
    if currentSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None #when we call for left and right child of a leaf node, they will both be none valuesand we will have the rootIdx be len(array)
    
    rootValue = preOrderTraversalValues[currentSubtreeInfo.rootIdx]  #store a reference to the value of the root of the current subtreee


    #base case 2, if the value being considered is not within bounds then the child of the node that did the call is a None child
    if rootValue < lowerBound or rootValue >= upperBound:
        return None  
    
    #if value is within bounds then we move advance till we are done with the original array, otherwise rootidx counter will be updated
    currentSubtreeInfo.rootIdx += 1 #increment the index counter
    leftSubtree = reconstructBstFromRange(lowerBound,rootValue,preOrderTraversalValues, currentSubtreeInfo) #this is a node, pass counter
    #if next value is left child, entire left subtree will be completed, and currentSubtreeInfo will be updated before rightSubtree call
    rightSubtree = reconstructBstFromRange(rootValue,upperBound,preOrderTraversalValues,currentSubtreeInfo) #this is a node, pass counter
    return BST(rootValue,leftSubtree,rightSubtree) #finally create a BST node once left and right child nodes returned as BST nodes or None




