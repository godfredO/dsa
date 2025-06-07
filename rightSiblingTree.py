"""The question asks to convert a binary tree to a right sibling tree, and there is bfs solution which is more intuitive and should be
studied first and then a dfs solution which is the most optimal solution space-wise and should be studied second."""

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
"""The question gives a binary tree (its root node) and asks to convert it to a binary sibling tree. One main realization is that if 
a node is the left child of its parent then in the right sibling tree, its right pointer will point to its parent's right child whether
this right child is a None value or a bst node. If a node is the right child of its parent then its right pointer will point to its 
parent's right sibling's left child whether the parent's right sibling's left child is None or a bst node. 

With these two realizations and correct sequencing of the operations, this question is solved by making the recursive call on the left 
child, then updating the parent's right pointer to point to its right sibling before making the recursive call on the right child. This
recursive call thus takes a node, its parent node, and an isLeftChild boolean. We also need to store the left and right child somewhere 
in the code since we lose a pointer to the right child once a parent right pointer is updated to its right sibling. So after handling
the base case of returning if the node is None, the next thing we do is store these references ie left, right = node.left, node.right.
Then we make the recurisve call on the left child, passing  in the current node as parent and a True for the isLeftChild boolean
ie mutate(left,node, True). 

Then we right the main logic of the solution. We first handle the case of the root node whose parent is None ( and was originally called
with an isLeftChild boolean of None not False just None), by updating its right pointer to None. Next, we handle the case of left children
ie if isLeftChild:, where we update the right pointer to its parent's right child, whatever it is. Then we handle the case of the right
child which in general will have its right pointer point to its parent's right sibling's left child, if the parents right sibling isnt
None in which case we point to None.  After the main logic of the program we make a recursive call on the right child with the reference
that was stored ie mutate(right, node, False). The parent's pointers will be updated by the isLeftChild if its a left child of its own
parent otherwise by the else statement. And of course, this question is handled recursively so the recursive calls reach the leaf nodes 
before coming back up so that the right pointers are updated from bottom to top , from left to right. 

This is an inorder traversal dfs. Basically with binary tree questions that are solved with depth-first search, we have some logic step(s), 
go left step and go right step. The order of these steps determine if the depth-first search is inorder, postorder or preorder. In this
solution, we go left, them do our logic (visit), then go right, so the depth-first search used here is inorder."""


#O(n) time | O(d) space
def rightSiblingTree(root):
    mutate(root,None,None) #parent of root initialized as None, isLeftChild of root initialized as None
    return root

def mutate(node,parent,isLeftChild):
    if node is None:
        return
    left,right = node.left, node.right #grab left/right child and store references to them before pointers are updated

    mutate(left,node,True) #first call recursive function on left subtree to update the left child's right pointer

    #For each node updatingdepends on if it is the left child / right child , if parent is None , or parent.right is None
    #after the left child call uses this logic to update its pointers, we go up to parent call and update parents right pointer
    if parent is None: #if node has no parent because root has None parent. For each node update left child, itself, right child
        node.right = None #then make the right pointer point to None
    elif isLeftChild: #if node is the left child of its parent (then parent is not None) 
        node.right = parent.right #then update the right pointer to point to parent's right child aka right sibling
    #from the left child, we go up to the parent to update its right sibling before calling on the right child so parent.right will be 
    #parent's right sibling when we get here, parent and left will both be updated in elif isLeftChild or the parent in the else statement
    else: #if right child update pointer to parent's right sibling's left child if parent's right sibling isnt None else None (last on level)
        if parent.right is None:  #if the parent has no right sibling ie parent's right pointer is updated to None
            node.right = None     #then the node has no right sibling either so None since its the last on its level
        else: #else if the parent has a right sibling ie parent.right is not None after updating parent pointer
            node.right = parent.right.left #then update the node's pointer to left child of parent's right sibling 

    mutate(right,node,False) #lastly call recursive function on right subtree


"""The more intuitive solution with a less optimal space complexity is to use breadth first search. The question is essentially asking to
update each node's right pointer to point to the node to its right on the same level. Thus each node on the same level will point to some 
other node if it is not the last node on that level in which case it will point to None. The root node's right pointer will point to None 
since it is the only and therefore last node on its level. Another thing to also realize is that nodes on a level need to be processed from 
left to right and if the node immediately to the right on the same level is None then the updated right pointer will still point to it. 

So in this implementation we use a queue and we add to it the nodes with their level information left first then right and we can know if 
it is the last node on the level or not by comparing the level information on the node being processed with the next node to be processed. 
The next node to be processed will be the peek value of the queue. So after popping and unpacking into node, level we can compare the level
of the current node to the level of the object that is the peek value of the queue.

If the next node is on the same level we update the current node's right pointer to point to it otherwise it points to None. Before updating 
the pointers however we add the node's left child then right child in that order to the queue. This is essential because if we don't add 
them before overwriting pointers, we will lose references. Also, when we add the children node, we add even the None children nodes. This way 
if the tree isn't completely filled up, say the current node has a left child but a None right child, we still want the None value to be the
next node on the queue, to be the None value when the current node is the left child. And since they will have the same level information and
we added left before right, we will update the leftChild.right = None. However when we pop the None child node, we just skip. 

So we popleft() form the queue for the currentNode, skip if we pop a None node, add child nodes as is with depth information, then we compare 
the popped level information with the level information of the peek value level information. If the levels match, we update the right pointer
of the current Node to point to the peek value node else, we update the right pointer to None. At the end of the bfs while loop, we return
the root node of the tree.

The space complexity is the width of the tree which will have a worst-case value of n/2 because the bottom of a tree can house up to half of 
all nodes in the tree which can be significantly worse than the depth-first search solution because depth of a tree can be log(n) at best and 
O(n) at worse leading to a better or same space complexity as this breadth-first search solution. With that said the bfs solution is more 
intuitive."""

#O(n) time | O(n) space
def rightSiblingTree(root):
    queue = [(root,0)] #initialize queue with root node , level 0
    while queue:
        node,level = queue.pop(0) #fifo of queue, could use deque popleft
        if node is None: #if the current node is None, do nothing, it has no right child, left child to add or right pointer to update
            continue
        queue.append((node.left,level+1)) #if node is not None,fist add the left child first to queue, increment level information
        queue.append((node.right,level+1)) #then add right child second to the queue, increment level information
        nextNode = queue[0] #set a pointer to the next node and its level information, current first in queue
        if level == nextNode[1]: #if the current node is on the same level as the next node, then its not the last on the level
            node.right = nextNode[0] #so update its right pointer to point to the next node which is on its level and to its right
        else: #if the next node is on the next level, then current node is the last on its level
            node.right = None
    return root #return root node of tree at end when queue is empty