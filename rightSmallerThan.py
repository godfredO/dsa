"""This question gives an input list and asks to return an array where each index's value represent the number of element in the input array 
that are to the right of and strictly smaller than the array's element at that index. The naive obvious solution is to use a double for loop 
to iterate through the loop and fill the output array. This leads to a O(n^2) time complexity. This solution is optimized by iterating once 
through the array from right to left and inserting the elements a BST and at the point of insertion counting the number of elements in the BST 
that are strictly less than the element being inserted, realizing that the BST property helps us to determine the number of elements that are 
strictly less than. This is due to the fact that values that are to the right to and less than will be in a node's left subtree but how do
we count the number of nodes in a left subtree and how do we update this count as we insert new values? That is what the second
solution effectively addresses. And how do we use the BST property to avoid traversing the loop twice in a double for loop?

Since the question asks to only consider the values to the right of an index we know that the last index will always have 0 as the number of 
values strictly less than since there are no values to the right of the last index. Not only that but we also iterate through the array from 
right to left to ensure that by the time we get to any index we would have already encountered all the elements that need be considered for its 
number of right smaller than value. This means that the first BST node and thus the root node of the BST tree will be the last value of 
the array and we know that the count for this node will always be 0. With that said this solution comes down to clever modification of the 
standard BST node to include an attribute leftSubtreeSize and a modification of the standard insert method of a BST class. 

We also initialize an output array by making a copy of the original array and as we iterate from right to left and insert BST nodes, we 
simultaneously update the value at index i of the output array. My first initial thought was, why not return the count was we insert the node
at a value, and I realized that unless this solution is done recursively so that would have the effect of returning the count in each call as
we climb up the recursive tree. So by, passing the output array, with the same size as the array, we ensure that we can always just update 
count at the appropriate index, meaning we also need to pass in the array index of the value we are inserting. 

Each BinaryTreeNode has the usual value, left, right attributes in addition to a leftSubtreeSize attribute. The reason for this is that the
in a binary search tree, for the subtree rooted at any node, all the nodes in its left subtree are of lesser value and as such the size of
the left subtree indicates the number of nodes in a tree, that are less than any nodes value. By iterating from right to left we ensure that
all the at any index, all the values to its right would have already been inserted and so if after the BST comparison we gp left, we know
that the will be increasing the size of the left subtree of the current node so we increment its leftSubtreeSize before calling the insert
method on it's left child, if the left child of the current node is not None. If it is, then we create a node with the insert value and set
it as the current node's left child followed by updating the output array value at the insert index with the rightSmallerThan value 
(which is initialized at 0 at first call, and only updated if we ever go right on a current node). 

If on the other hand if we are going right, then it could be because the insert value is equal to or greater than the current node's value. 
If the insert value is equal to the current node's value, then all the values in the current node's left subtree are also less than the insert 
value and since those values are to the right of the insert value's index, we know that that the insert value at this point will also have the
same right smaller than value as the current node, so we increment this count (which is initialized at 0 at first call) with the current node's 
leftSubtreeSize attribute value, before recursively calling this insert method on the right child of the of the current node ie moving right. 
If on the other hand, the insert value is greater than the current node, then the current node should also be counted towards the insert value's 
rightSmallerThan value, and so after incrementing this value with the left subtree size of the current node, we increment by 1 again for the 
current node, before going right by recursively calling the right child of the current node, if the right child is not None. If the right child
is None, then we create a node for the insert value (our modified BST class with the leftSubtreeSize attribute), and set this node as the right
child of the current Node followed by updating the output array at the insert index with the rightSmallerThan value.  Thus we have a modified
BST node that has a leftSubtreeSize attribute and we increment this attribute by 1 for a current node, whenever our insert value is less than
the current node's value. However if we have to go right, we increment the rightSmallerThan parameter with the value of the leftSubtreeSize
attribute of the current node (and an additional increment of 1 if the insert value is greater than current node value). The outer loop in 
the main function, is simple too, we can initialize an output of 0's the same size as the array, create a root modified bst node with last
element in the input array, loop backwards from the penultimate value to the first, and call the insert method on the root node, passing in
the current index, the output array, and an initial rightSmallerThan count value of 0.


So we create the root node with the last value in the array and loop through the array backwards and call the insert method on the 
root node. This modified insert method takes in the current value, the current index and the output array, in addition to a count value which is
set to a default of 0 whenever the insert method is called. The rational is that if the current value is greater than the root value and thus
belongs in the root's right subtree, its the same as saying that the root which is to the right of the current value in the array is less than
the current array and by extension the current value is greater than all values in the left subtree of the root node. So we update the count
with the left subtree size of the root plus one for the root node itself. If however a value is less than the root node and thus belongs in the
left subtree, then as we insert we increase the leftSubtreeSize parameter of the root node before we move left. This ensures that the next 
number that goes right will have the updated leftSubtreeSize. What about the case where the value is equal to the root node? In that case we
go right increment the count with the root's leftSubtreeSize value but we don't add one for the root itself since the question requires strictly
less than and to the right. Anyway whenever we reach the insert point itself, we have the final count for a node's value and we use the passed
index to update the value stored in the output array. Since we have to return an output array, the recursive stack doesnt worsen our
space complexity, so we use recursion instead of inserting iteratively. It is also important to realize that by root i mean the root of the
current subtree and not just the root of the entire tree. Finally we have to handle the edge case of an empty array at the start of the code,
by simply returning an empty output array, to avoid trying the create a BST node with a non-existent last value."""


	

"""Naive solution of double for loops"""
#O(n^2) time | O(n) space
def rightSmallerThan(array):
    rightSmallerCounts = []
    for i in range(len(array)):
        rightSmallerCount = 0
        for j in range(i+1,len(array)):
            if array[j] < array[i]:
                rightSmallerCount += 1
        rightSmallerCounts.append(rightSmallerCount)
    return rightSmallerCounts


"""Optimal Solution using the BST property and looping in reverse to insert into modified BST"""
#O(nlogn) time | O(n) space
class ModifiedBST:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.leftSubtreeSize = 0
	
	def insert(self, value, idx, output, rightSmallerCount):
		if value < self.value:
			self.leftSubtreeSize += 1
			if self.left is not None:
				self.left.insert(value, idx, output, rightSmallerCount)
			else:
				self.left = ModifiedBST(value)
				output[idx] = rightSmallerCount
		else:
			rightSmallerCount += self.leftSubtreeSize
			if value > self.value:
				rightSmallerCount += 1
			if self.right is not None:
				self.right.insert(value, idx, output, rightSmallerCount)
			else:
				self.right = ModifiedBST(value)
				output[idx] = rightSmallerCount
		
def rightSmallerThan(array):
	if not array:
		return []
	
	output = [0]*len(array)
	root = ModifiedBST(array[-1])
	for idx in reversed(range(len(array) - 1)):
		root.insert(array[idx], idx, output, 0)
	return output


# """Optimal solution using bst, first implementation"""
# #O(nlog(n)) time | O(n) space
# def rightSmallerThan(array):
#     if len(array) == 0: #edge case, if input array is empty
#         return [] #return empty array, wouldnt want to create a bst of empty list
#     lastIdx = len(array) - 1 #last index of input array, this is were we create bst root node, 
#     bst = SpecialBST(array[lastIdx],lastIdx,0) #create a bst with last value in array, which will be the root node
#     for i in reversed(range(len(array)-1)): #loop right to left starting from second to last, last already added above
#         bst.insert(array[i],i) #insert values in bst from right to left, traversing using root node from above
#     rightSmallerCounts = array[:]  #initialize output array of same length as input array, here, copied input array
#     getRightSmallerCounts(bst,rightSmallerCounts) #helper function to populate output array by traversing bst from root node
#     return rightSmallerCounts #return the populated output array




# def getRightSmallerCounts(bst,rightSmallerCounts): #recursive method to traverse bst and populate result array
#     if bst is None: #if this recursive method is called on the child of a leaf node
#         return      #do nothing, just return
#     rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime #read index and result from bst node and insert into result array
#     getRightSmallerCounts(bst.left,rightSmallerCounts) #call recursive method on left child
#     getRightSmallerCounts(bst.right,rightSmallerCounts) #call recursive method on right child

# class SpecialBST:
#     def __init__(self,value,idx,numSmallerAtInsertTime):
#         self.value = value                  #the value of node,
#         self.idx = idx                      #the index of node's value in the input array
#         self.numSmallerAtInsertTime = numSmallerAtInsertTime  #stores the value neeed for output array
#         self.leftSubtreeSize = 0    #number of nodes in left subtree of node, initalize at 0, the value for lastIdx in array
#         self.left = None            #left child of bst node
#         self.right = None           #right child of bst node
    
#     def insert(self,value,idx,numSmallerAtInsertTime=0): #initialize numSmallerAtInsertTime to 0
#         if value < self.value: #if the array element is less than the value of current node, ie left subtree
#             self.leftSubtreeSize += 1 #since array element is going into current node's left subtree
#             if self.left is None: #if the current node doesnt have a left child
#                 self.left = SpecialBST(value,idx,numSmallerAtInsertTime) #then create a node for value and insert as left child
#             else: #if self.left is not None
#                 self.left.insert(value,idx,numSmallerAtInsertTime) #then call the insert method on the left child of current node
#         else: #if value >= self.value , ie value's node goes into the right subtree of current node (self)
#             numSmallerAtInsertTime += self.leftSubtreeSize #value is also greater than all values in current node's left subtree
#             if value > self.value: #then only if it is also strictly greater than current node (since right subtree is >=)
#                 numSmallerAtInsertTime += 1 #then increment numSmallerAtInsertTime by 1 for current node
#             if self.right is None: #if the current node doesn't have a right child, make current value a node and right child
#                 self.right = SpecialBST(value,idx,numSmallerAtInsertTime) #create node and insert as right child of current node
#             else: #if current node has a right child, then call the insert method on right child
#                 self.right.insert(value,idx,numSmallerAtInsertTime) #call insert method on right child of current node


"""Optimal solution with same time and space complexity but we construct output array as we construct binary tree """
#O(nlog(n)) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0: #edge case, if input array is empty
        return [] #return empty array, wouldnt want to create a bst of empty list
    rightSmallerCounts = array[:]  #initialize output array of same length as input array, here, copied input array
    lastIdx = len(array) - 1 #last index of input array, this is were we create bst root node, 
    bst = SpecialBST(array[lastIdx]) #create a bst with last value in array, which will be the root node
    rightSmallerCounts[lastIdx] = 0 #we know the last element will have 0 elements to the right 
    for i in reversed(range(len(array)-1)): #loop right to left starting from second to last, last already added above
        bst.insert(array[i],i, rightSmallerCounts) #insert values in bst from right to left, traversing using root node 
    return rightSmallerCounts #return the populated output array

class SpecialBST:
    def __init__(self,value):
        self.value = value                  #the value of node,
        self.leftSubtreeSize = 0    #number of nodes in left subtree of node, initalize at 0, the value for lastIdx in array
        self.left = None            #left child of bst node
        self.right = None           #right child of bst node
    
    def insert(self,value,idx,rightSmallerCounts, numSmallerAtInsertTime=0): #initialize numSmallerAtInsertTime to 0
        if value < self.value: #if the array element is less than the value of current node, ie left subtree
            self.leftSubtreeSize += 1 #since array element is going into current node's left subtree
            if self.left is None: #if the current node doesnt have a left child
                self.left = SpecialBST(value) #then create a node for value and insert as left child
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else: #if self.left is not None
                self.left.insert(value,idx,rightSmallerCounts,numSmallerAtInsertTime) #then call the insert method on the left child of current node
        else: #if value >= self.value , ie value's node goes into the right subtree of current node (self)
            numSmallerAtInsertTime += self.leftSubtreeSize #value is also greater than all values in current node's left subtree
            if value > self.value: #then only if it is also strictly greater than current node (since right subtree is >=)
                numSmallerAtInsertTime += 1 #then increment numSmallerAtInsertTime by 1 for current node
            if self.right is None: #if the current node doesn't have a right child, make current value a node and right child
                self.right = SpecialBST(value) #create node and insert as right child of current node
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else: #if current node has a right child, then call the insert method on right child
                self.right.insert(value,idx,rightSmallerCounts,numSmallerAtInsertTime) #call insert method on right child of current node



array = [8, 5, 11, -1, 3, 4, 2]
print(rightSmallerThan(array))