""" The question gives two arrays and asks if the same binary search tree will be created from the arrays if we created a root node with 
the value at index 0 for both arrays and subsequently called the insert method for the remaining values to insert them in the tree starting 
from root. Since each node must be valid, our observations must hold for the subtree rooted at each node. The algorithm starts with a few 
checks. If the two arrays dont have the same length, then they would form BSTs with different number of nodes and thus cant form the same 
BSTs. Then if the two arrays dont have the same first elements then they would form BSTs with different root nodes and thus cant form the 
same BSTs. With those checks done, we construct arrays representing the right and left subtrees for the tree rooted at the first elements 
and feed these into the recursive algorithm,comparing rightsubtrees and leftsubtrees. At each call we know the first value is the root
of the next subtree and we know that it will be greater than value in its subtree and less than or equal to values in its right subtree so
we re-construct a new subarray for the left and right subtree and compare their lengths and the value of the root node. If we are able to 
keep calling the recursive function with increasingly shorter subarrays and reach the base case of empty arrays then the arrays represent 
the same BST. If we hit unequal root values or unequal subtree value lengths then we know the original arrays dont produce the same BST and
so we return False and bubble it up to the recursive call stack. Due to the slicing this solution is O(n^2) time.

But is it necessary to create a sliced array for comparison every time? Can we use the lowerBound upperBound interpretretation of the bst 
properties and indices to find the left child and rightchild and the root of the next subtree? Well yes. It is instrumental to realize when
we go from a root node of a subtree (parent) to its left child, the root node's value becomes the updated upper bound for its left child
but they both share the same lower bound. In the same way when we go from the root of a subtree, to its right child, the root node's value
becomes the updated lower bound of its right child but the share the same upper bound. By utilizing this fact, we can predict where a new
node will end up when the insert method is called on the root node. If the new value is less than the root node (upperBound) and greater 
than the root node's lowerBound then it will be in the left subtree of the root node of the subtree in question. Similarly if the new value
is greater than or equal to the root node (lowerBound) and less than the root node's upperBound, then it will be in the right subtree of the 
root node of the subtree in question. So with these insights, we have a function that returns the left child or right child for the current
subtree root and if none of the remaining values meet the requirement we need to check that it is the same for the second array. In this 
function we recognize that the starting index passed is the root of the current sub tree and if loking for the left child we return the
first index whose value satisfies the condition of being less than the value at the starting index but greater than or equal to the minValue. 
Similary if looking for the right child we return the first index satisifies the condition of being greater than or equal to the value at
the starting index and less than the maxValue. We return the first satisfying index so that we dont choose just any subtree node but the 
left/right child node index. Since this function is always going to recursively try to build out the subtree rooted at a left/right child, 
we use some value say -1 to indicate that that subtree doesnt actually exist and if this is the same for both arrays we continue on. 
That would equate to having a None child. So in that case we are asking if one node is None, return both are None. We still check if the 
root passed has the same value for each array, get the next right / left child , update the bounds for these with the current root value 
and keep comparing that both the left subtree and right subtree is the same for both arrays. In the previous solution where we would get an 
empty sliced array, here we get a -1 as the next root index to be considered and if arrays have this same value for the current root we know 
the subtrees are the same so True. We thus roll in both the empty array and length of sub-arrays conditions for the first solution into one 
and still separately check that the current root values of both arrays are the same. As always, the sequencing of these checks is crucial in 
the code. If the bsts formed by the two arrays are the same, then the the child node values as well as lowerbounds and upperbounds will be 
the same. So just like the reconstruct Bst question we replace slicing an entire subtree array with just finding the left/right child. 

Check sameTree.py for the general binary tree version."""


#O(n^2) time | O(n^2) space
def sameBsts(arrayOne,arrayTwo):
    #initial check if the two arrays cant form a tree with the same number of nodes
    if len(arrayOne) != len(arrayTwo):
        return False
    
    #base case when we call the recursive function on empty arrays it must mean we have gone t
    # through all subtrees and each succesive pair of subtrees was the same
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True

    #to avoid errors, check the empty array True case first before root value check to ensure since both arrays contain at least 1 element 
    #check if the two arrays represent trees rooted at the same value, ie same first element
    if arrayOne[0] != arrayTwo[0]: #this holds because getSmaller and getBiggerOrEqual loops in order from left to right
        return False

    #with checks done, create right and left subtrees for tree rooted at the first elements
    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBiggerOrEqual(arrayOne)
    rightTwo = getBiggerOrEqual(arrayTwo)

    #call recursive function on the pair of subtrees and return the outpuut
    return sameBsts(leftOne,leftTwo) and sameBsts(rightOne,rightTwo)

def getSmaller(array):  #loop through array and collect all values that will go in the left subtree of first value
    smaller = []
    for i in range(1,len(array)): #start iteration at second value. First value is root node
        if array[i] < array[0]: #compare to root node for values in the left subtree
            smaller.append(array[i]) #append in order
    return smaller #return left subtree array for tree rooted at first element

def getBiggerOrEqual(array): #loop through array and collect all values that will go in the right subtree of first value
    biggerOrEqual = []
    for i in range(1,len(array)): #start iteration at second value. First value is root node
        if array[i] >= array[0]: #compare to root node for values in the right subtree
            biggerOrEqual.append(array[i]) #append in order
    return biggerOrEqual #return right subtree array for tree rooted at first element


"""Optimal solution which uses the same idea as the first solution but instead of
creating new subarrays representing the right and left subtrees rooted at the current
first element, we pass in pointers and values representing the current root node, and its
ancestors to avoid creating new subarrays. The ancestors will be represented by minVal
and maxVal (validate bsts solution) since the max and min values in any subtree are
bounded by the ancestor values. This improves the space complexity to O(d)
where d is the depth of the binary search tree, as is typical of recursive solutions"""

def sameBsts(arrayOne,arrayTwo):
    #since the original root nodes have no ancestors the bounds of their values are
    #negative inifinity and positive inifinity. Check "validate bsts" solution idea
    return areSameBsts(arrayOne,arrayTwo,0,0,float("-inf"), float("inf"))


def areSameBsts(arrayOne,arrayTwo,rootIdxOne,rootIdxTwo,minVal,maxVal):

    #when we reach a base case of empty arrays, there will be no root node indices
    #and helper function will return -1 for root indices. We can also mix in the
    #length of array check by verifying that if one array is empty hence a root
    #index of -1 then the other is also empty and has a root index of -1
    if rootIdxOne == -1 or rootIdxTwo == -1: #if either array is empty
        return rootIdxOne == rootIdxTwo #verify they are both empty, since both will be -1

    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]: #compare root node values
        return False
    
    leftRootIdxOne = getIdxOfFirstSmallerValue(arrayOne,rootIdxOne,minVal)
    leftRootIdxTwo = getIdxOfFirstSmallerValue(arrayTwo,rootIdxTwo,minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqualValue(arrayOne,rootIdxOne,maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqualValue(arrayTwo,rootIdxTwo,maxVal)

    #array values at rootIdxOne and rootIdxTwo should same due to check above
    currentValue = arrayOne[rootIdxOne] #root is same for both trees, so choose one, and use updated indices
    leftAreSame = areSameBsts(arrayOne,arrayTwo, leftRootIdxOne,leftRootIdxTwo,minVal, currentValue)
    rightAreSame = areSameBsts(arrayOne,arrayTwo,rightRootIdxOne,rightRootIdxTwo, currentValue,maxVal)

    return leftAreSame and rightAreSame

def getIdxOfFirstSmallerValue(array,startingIdx,minVal):
    #to find the first value (idx) in the left subtree rooted at root idx
    #we know that root idx is the max value of the left subtree and its
    #ancestor is the min value of the left subtree
    for i in range(startingIdx + 1, len(array)):
        if array[i] < array[startingIdx] and array[i] >= minVal:#note >= minVal, minVal is right ancestor
            return i #return the first element that satisfies the condition of left child, ie first value in roots left subtree 
    return -1 #return -1 if there is no left child ie no first smaller value idx

def getIdxOfFirstBiggerOrEqualValue(array,startingIdx,maxVal):
    #to find the first value (idx) in the right subtree rooted at root idx
    #we know that root idx is the min value of the right subtree and its
    #ancestor is the max value of the right subtree
    for i in range(startingIdx + 1, len(array)): #startingIdx 
        if array[i] >= array[startingIdx] and array[i] < maxVal:#note >= array[startingIdx] for right subtree
            return i #return the first element that satisfies the condition of right child, ie first value in roots right subtree 
    return -1 #return -2 if there is no right child ie no first bigger of equal value

arrayOne = [10, 15, 8, 12, 94, 81, 5, 2, 11]
arrayTwo = [10, 8, 5, 15, 2, 12, 11, 94, 81]
print(sameBsts(arrayOne,arrayTwo))