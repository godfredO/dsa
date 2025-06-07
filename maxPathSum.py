"""The input is the head of a binary tree and the question asks to return its max path sum. A path is a collection of connected nodes 
in a tree, where no node is connected to more than two other nodes; a path sum is the sum of the values of the nodes in a particular 
path. This question extends the Binary Tree Diameter question and height balanced binary tree question. However instead of height info, 
the left and right subtrees will be returning a branch sum and a maxPathSum . The branch sum is the sum that includes a node's value 
with or without one of the left/right child branchSum. Note here that the branch sum may not include either child branch sum due to 
negative numbers unlike the height info which always went to one of the deepest leaf nodes in either child subtree. Instead of diameter, 
each node also returns a maxPathSum for comparison and bubbling up to the original call. At each node instead of the node root path we 
calculate a currentTreeSum which may include a triangular sum rooted at a node and both both ist left/ right child sums or its value only 
or the sum of its value and one of the returned branch sums. Then we compare the currentTreeSum, left.maxPathSum, right.maxPathSum as a 
way of updating the maxPathSum seen. We then return an object includding the maxPathSum and the branchSum up the tree. The branch sum here 
is the value that will be used by a node's parent to determine its own currentTreeSum, and the  currentTreeSum will be used for the comparison 
that bubbles the maxPathSum seen so far up the tree to the original function call. Thus this is a post-order depth-first search solution.

Thus for every node in a binary tree, there are three options for the max path sum that includes its value; the node's value alone, the node's 
value plus the greater child branch sum ie left/right subtree,  or the node's value plus the branch sum of both its subtrees. Now it is 
important to recognize that any of these options is a candidate for the current max sum but as for the branch sum returned to a node's parent 
we cant consider the triangle max sum ie node.value + leftSubtre max sum + rightSubtree max sum because of the definition of a path. Thus at 
each node we get the left subtree, right subtree max subsums and branch sums, choose the max child branch sum and calculate the max sum of the 
node as a branch by choosing the maximum of the node's value alone and the sum of the node's value plus the max child branch sum. This is what 
we return to the parent as the current node's branch sum. That is the branch sum of a node is either the node's value or its sum with the max 
child branch sum. Then we calculate the triangle path sum where we sum the node's value and both subtree sums. Then we compare the running max 
sum to the triangle sum and the branch sum and choose the maximum of these as new running max sum. Now it is essential to realize that we will 
actually be getting a running max sum from both children so when updating the running max sum we actually include both left running max sum and 
right running max sum. Because we make recursive calls to the children nodes before visiting the current node (determining branch, triangular
and updating maxPathSum), this dfs solution is post-order. If the base case is at the leafnode, we have a post-order dfs. If base case is at 
the root, we have a pre-order dfs (like nodeDepths.py)

"""

"""Solution version - post order dfs"""
class TreeInfo:
	def __init__(self, branchSum, maxPathSum):
		self.branchSum = branchSum
		self.maxPathSum = maxPathSum

def maxPathSum(tree):
	return helper(tree).maxPathSum

def helper(node):
	if node is None:
		return TreeInfo(float("-inf"), float("-inf"))
	
	leftInfo = helper(node.left)   #go left
	rightInfo = helper(node.right) #go right
	
	#unlike the height which is always 1+max(left,right), due to negative numbers we cant say node.value + max(lef,right)
    #but rather we do max(node.value + node.value + max(left,right)), visit step in post-order dfs
	currentBranchSum = max(node.value , node.value + leftInfo.branchSum, node.value + rightInfo.branchSum)
	triangularSum = node.value + leftInfo.branchSum +  rightInfo.branchSum
	
	currentPathSum = max(triangularSum, currentBranchSum)
	
	maxPathSum = max(currentPathSum, leftInfo.maxPathSum, rightInfo.maxPathSum)
	
	return TreeInfo(currentBranchSum, maxPathSum)


"""Same solution but i only store the maxPathSum in an object otherwise returning the branch sum as an integer"""
class PathSum:
    def __init__(self, value):
        self.value = value
        

def maxPathSum(root) :
    maxSum = PathSum(float("-inf")) #initialize maxPathSum at -inf, could also be root value in this solution technique
    postOrderDfs(root, maxSum)
    return maxSum.value
    
def postOrderDfs(node, maxSum):
    if not node: 
        return float("-inf")   #from a None node, return a branch sum of -inf to parent
    
    leftBranchSum = postOrderDfs(node.left, maxSum)
    rightBranchSum = postOrderDfs(node.right, maxSum)
    
    currentBranchSum = max(node.val, node.val + max(leftBranchSum, rightBranchSum))
    triangularSum = node.val + leftBranchSum + rightBranchSum
    
    currentPathSum = max(currentBranchSum, triangularSum)
    
    maxSum.value = max(maxSum.value, currentPathSum)
    
    return currentBranchSum
        


#O(n) time | O(d) space
def maxPathSum(tree):
    """Because the maxSum will be passed around in a recursive algorithm its important that
    it be stored in a mutable data structure instead of an immutable data type like an integer
    I am opting for storing it in a Python list. I could also have implemented a class."""
    maxSum = [float("-inf")] #initialize maxSum at -inf in case answer is a negative integer
    maxPathSumHelper(tree,maxSum) #helper method called on root node and initialized maxSum
    return maxSum[0] #since I chose to store my value in a list return the first element

def maxPathSumHelper(node,maxSum):
    if node is None:  #when recursive child reaches the None child of a leaf node
        return float("-inf") #should return -inf again in case answer is a negative value
    
    #if we are not at a leaf node's child
    left = maxPathSumHelper(node.left,maxSum) #recursive call on left subtree
    right = maxPathSumHelper(node.right,maxSum) #recursive call on right subtree

    value = node.value
    maxChild = max(left,right) #choose the child subtree that returns the max value
    #the max of tree rooted at current node, comparing node's value vs adding to max child value
    rooted = max(maxChild + value, value) #rooted value may or may not use child subtree values
    #compare if adding nodes value to both child subtree's values and the rooted value
    triangle = max(rooted,left + right+ value) #triangle value may not use the actual triangle sum 
    #update maxSum by comparing values returned by left, right child subtrees and triangle sum
    maxSum[0] = max(maxSum[0], left,right, triangle) #note triangle may rooted value or triangle sum

    #this is the value returned to left and right when called by ancestor, note that a valid path
    return rooted #through current node to ancestor cannot include a triangle


"""Same solution just implemented differently. In this solution we pass around the updated maxPath and
the node path value ie returns two values, tuple. First value is the maximum sum of current node as a 
branch and second value is the running max path sum"""
def maxPathSum(tree):
    _,maxSum = findMaxSum(tree)
    return maxSum

def findMaxSum(tree):
    if tree is None:
        return (0,float("-inf")) #max sum of current node as branch,  running max path sum
    
    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch,rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch+value,value) #in previous solution I call this rooted
    maxSumAsRootNode = max(leftMaxSumAsBranch+value+rightMaxSumAsBranch,maxSumAsBranch)#triangle
    maxPathSum = max(leftMaxPathSum,rightMaxPathSum,maxSumAsRootNode) #update running max path sum
    return (maxSumAsBranch, maxPathSum) #return tuple of max branch sum and updated max path sum


"""Same solution using a custom class instead and realizing that the branch sum of a None node can also
be -inf and we still get the right answer."""
class TreeInfo:
    def __init__(self, branchSum, maxTreeSum):
        self.branchSum = branchSum
        self.maxTreeSum = maxTreeSum
        
def maxPathSum(tree):
    return dfs(tree).maxTreeSum

def dfs(node):
    if node is None:
        return TreeInfo(float("-inf"),float("-inf"))

    leftSubtreeInfo = dfs(node.left)
    rightSubtreeInfo = dfs(node.right)

    leftBranchSum, leftTreeSum = leftSubtreeInfo.branchSum, leftSubtreeInfo.maxTreeSum
    rightBranchSum , rightTreeSum = rightSubtreeInfo.branchSum, rightSubtreeInfo.maxTreeSum

    childBranchSum = max(leftBranchSum, rightBranchSum)
    
    branchSum = max(childBranchSum + node.value, node.value) #for use by parent
    triangleSum = leftBranchSum + rightBranchSum + node.value
    currentTreeSum = max(branchSum, triangleSum)

    maxTreeSum = max(currentTreeSum, leftTreeSum, rightTreeSum) #bubble up the maxPathSum
    return TreeInfo(branchSum,maxTreeSum)
    