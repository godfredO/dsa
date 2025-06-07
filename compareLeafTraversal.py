class BinaryTree:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

"""This question gives the root nodes of two binary trees and asks to return if the two trees have the same leaf node values from
left to right, which is called a leaf traversal. In the naive solution we conduct a pre-order traversal, visit, left, right on 
both trees and at each stage we ask if the current node is a leaf node. If it is, we store the node value in array and if it is
not, we move on with the pre-order traversal. At the end we compare both arrays and check if the are identical. If they are, the
answer is True otherwise False. Now this is a very impressive application of preorder traversal, since we know that preorder
traversal visits the current node first before going left and right, by tweaking the preorder visit steps to only append when we
have verified that the current node is a leaf node, we are able to get all the leaf nodes in a tree. Now the only problem with 
this approach is that we store all the leaf nodes and in a binary tree that is potentially half all nodes ie O(n) space for each
tree. Since trees can have different node numbers this is O(n+m) for both trees. After we have all the leaf nodes if the lengths
of the filled arrays are not the same we return False, otherwise we go through the arrays. For each index, we compare the 
corresponding leaf nodes at those indices, if we find a pair that doesnt match, we return False. If we complete the for loop and
don't find a disparate pair, we return True

Now it is not necessary to store all the leaf nodes since a binary tree has half of its nodes as leaf nodes meaning that in very 
large trees, this is a significant space usage. And by the way, we only need to compare the first leaf node of both trees, then the 
second leaf nodes etc. The first solution (mid-optimal space complexity) uses a stack to process the nodes iteratively in a pre-order 
traversal. In a while loop we process tree one till we reach a leaf node and then process tree two till we reach a leaf node. 
Processing a tree, means checking if the current node is a leaf node. If it's not a leaf node we pop it off the stack and add its 
children to the stack. If it is a leaf node and we are on tree one we move to process tree two. How do we use a stack to process
the nodes in a preorder manner while checking for leaf nodes ? The key is adding the right child first before the left child. This
way when we pop from the stack, we pop the left child, and check if its a leaf node if it is we return that node otherwise we add
its right child first and then its left child. When we get to a leftmost leaf node, we pop and find that its a leaf node, and say
it has a right sibling will be on the stack and will be popped next. After that the only node on the stack will be the last parent
whose child nodes are et to be added aka the parent of the next leaf node that is in a different subtree. That is say we process 
the leaf node's in the left subtree of the root, the right child of the root will still be on the stack and when we find that this
node is not a leaf node we add its children right first then left. Before adding a child node we first check that its not None, and
at the end we pop the new current node for the while loop comparison at the top.

Once we have the leaf nodes for both trees we compare their values. If they are the same we go back to find the next next leaf nodes 
in both trees for comparison. At the end we check if both stacks are empty. This is because if both stacks are empty and if we never hit 
an inequal comparison then it means we found all leaf nodes and found them to be equal in value and in the same order for both trees. 
On the other hand if one of the stacks has elements on it and the other is empty, then it means that one tree has more leaf nodes than the 
other and thus they dont have the same leaf traversal. 

In the second solution (optimal space complexity) we observe that leaf nodes have both pointer going to None nodes 
and so if we are allowed to mutate the pointers, we can have the right pointer of each leaf node point to next leaf node, forming a linked 
list with the leftmost leaf node as the head node. In this solution, we have current, head, prev pointers to store the current node being 
processed, the head of the linked list aka leftmost leaf node, and the previous leaf node found so far for linkage to the linked list if 
the current node is found to be a leaf node. Since this approach finds all the leaf nodes in the root node's left subtree before finding 
the leaf nodes in the root node's right subtree, at the end of a tree traversal, the prev node of the left linked list will have to be 
joined to the head of the right linked list to form a single linked list for the tree. Once we have the linked lists for both trees and 
their head nodes, we iterate through the linked list, comparing node values until both iterators are None meaning we reached the end of 
both linked lists and found the leaf traversals to be the same. The first solution has a space of O(h1 + h2) due to both stacks. 

The second solution has a space of O(max(h1,h2)) since we traverse each tree separately and recursively to create linked lists of leaf 
nodes, so the only space used is the recursive stack."""

#O(n+m) time | O(n+m) space
def compareLeafTraversal(tree1, tree2):
	tree1LeafNodes = []
	tree2LeafNodes = []
	getLeafNodes(tree1, tree1LeafNodes)  #helper method uses pre-order traversal to grab leaf nodes for comparison
	getLeafNodes(tree2, tree2LeafNodes)
	if len(tree1LeafNodes) != len(tree2LeafNodes):
		return False
	for idx in range(len(tree1LeafNodes)):
		if tree1LeafNodes[idx] != tree2LeafNodes[idx]:
			return False
	return True

def getLeafNodes(node,array): #uses modified pre-order traversal to grab leaf nodes
	if node is None:
		return
	if node.right is None and node.left is None: #this is the visit step of the pre-order traversal, for only leaf nodes
		array.append(node.value)
	getLeafNodes(node.left, array)
	getLeafNodes(node.right, array)

#O(n+m) time | O(h1 + h2) space
def compareLeafTraversal(tree1,tree2):
    tree1TraversalStack = [tree1]   #intialize stack for tree 1 with the root node in it
    tree2TraversalStack = [tree2]  #initialize stack for tree 2 with the root node in it
    while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0: #stop if either stack is empty
        tree1Leaf = getNextLeafNode(tree1TraversalStack) #get the next leaf node in tree 1
        tree2Leaf = getNextLeafNode(tree2TraversalStack) #get the next leaf node in tree 2

        if tree1Leaf.value != tree2Leaf.value: #if the current leaf nodes differ in value
            return False 
    return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0 #if all leaf nodes are processed 

def getNextLeafNode(traversalStack):
    currentNode = traversalStack.pop() #pop current node from stack
    while not isLeafNode(currentNode): #if the current node is not a leaf keep pre-order traversal after popping for current node
        if currentNode.right is not None: #if the current node has a right child ,add it first to stack to achieve pre-order after pop
            traversalStack.append(currentNode.right) #add the right node first to acheive pre-order traversal after popping current node
        if currentNode.left is not None: #if the current node has a left child ,add it second to stack to achieve pre-order after pop
            traversalStack.append(currentNode.left) #add the left node second to acheive pre-order traversal after popping current node
        currentNode = traversalStack.pop() #pop current node from top of stack to achieve pre-order traversal after right, left appending
    return currentNode #if current node is a leaf node, loop will break and return current leaf node

def isLeafNode(node):
    return node.left is None and node.right is None

#Optimal space complexity solution where we mutate the right pointers of leaf nodes to create a linked list, join linked lists from
#the left and right subtree of root nodes to form a single linked list of leaf nodes for either tree and finally traverse linked lists
#starting from the leftmost leaf node (as head).
def compareLeafTraversal(tree1,tree2):
    tree1LeafNodesLinkedList,_ = connectLeafNodes(tree1) #return head node and previous node of leaf node's linked list
    tree2LeafNodesLinkedList,_ = connectLeafNodes(tree2) #return head node and previous node of leaf node's linked list

    list1CurrentNode = tree1LeafNodesLinkedList
    list2CurrentNode = tree2LeafNodesLinkedList
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value:
            return False
        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right
    return list1CurrentNode is None and list2CurrentNode is None
    
def connectLeafNodes(currentNode,head=None,previousNode=None): #initialize linked list head and previous nodes as None
    if currentNode is None: #if recursive call is called on a leaf node's child nodes
        return head,previousNode #just return the current head node and previous node of linked lists

    if isLeafNode(currentNode): #if current node is a leaf node, we add it to the linked list or set it as the head node of linked list
        if previousNode is None: #if previous node in linked list is the same as initialized, then we don't have a head node yet
            head = currentNode #set current leaf node as head if this is the first leaf node in in-order tree traversal
        else: #if there is a previous Node then it means we have a head and we need to mutate previous Node's right pointer
            previousNode.right = currentNode  #add current node to linked list by updating previous node's right pointer
        previousNode = currentNode #update previous node iterator to point to current node after adding current node to linked list

    leftHead,leftPreviousNode = connectLeafNodes(currentNode.left,head,previousNode) #go down the left subtree of current node
    return connectLeafNodes(currentNode.right,leftHead,leftPreviousNode) #go down right subtree, adding leaf nodes to left linked list

def isLeafNode(node):
    return node.left is None and node.right is None