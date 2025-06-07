class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

"""So this question gives us a binary tree where the nodes have a parent attribute in additon to the customary left and right attributes
and we are asked to do an inorder traversal iteratively. Now if we didnt have the parent attribute, then we an iterative inorder 
traversal simply means using our own stack to implement the inorder depth-first search, and that is iterativeInOrderII.py.

So we treat the binary tree like a linked list and use two pointers, a prev and current pointer. When we start at the root, the prev
pointer is at None and the current is at the root. And inside a while loop, we keep going as long as the current is not None. So in
an inorder traversal we keep going left until we reach the leftmost leaf node. How do we keep going left? We say that if the prev node
is None (ie the parent of the root) or the prev node is the current's parent then, if the current node's left child is not None, we declare 
a temporary pointer next, which will point to the current node's left child. Then we advance the pointers by moving prev to current and
moving current to next. This means that when we first start, if the root node has a left child, we will declare next to point to that left
child and advance the pointers. When we get back to the while loop condition, prev will be pointing to the root node and current to the left
child.

So we keep advancing until we get to the leftmost leafnode ie prev is the current's parent but current.left is None. In that case we visit
the current node and declare the next pointer. Now here is the interesting bit, we say that next should point to current node's right child
if the right child is not None else the parent. Now if the current node were a node without a left child but a right child, this will mean
we update next to point to that right child, then when we update the pointers prev will move to the current node and current will move to
next. Now suppose that the current node is indeed a leaf node, then we update next to point to its parent after visiting the current node.
So when we update prev to current and current to next, the prev node will actually be the left child and the next node the parent.  So our
second check is that if the prev node is the left child of the current node, then we just came from a leaf node on the left so we visit the
current node, parent, and again declare a next node as the right child or the parent. Then when we update our pointers current will move to
next and prev to current ie current becomes the right child and prev the parent.  That is whever we visit we use our next pointer to go right
or to go up the tree. Now the next time around in the while loop, the prev node will be the current's parent albeit this time its the right 
child and if this right child isnt a leaf node, we keep going left by declaring next to point to its own right child else, we visit the
current node before declaring the next pointer. Now say this right child is also a leaf node, then we will declare next to go its parent
and when we advance the pointers, current will point to next ie the right childs parent and prev will point to current ie the right child.
So now we are in a situation where prev is the right child of currrent and that is different from the previous cases where previous was
either the left child of the current node or the parent node. This present situation means we need to go up, and there is nothing to visit
now, so we declare next to be the current's parent. Now take a simple system of three nodes. At this point we will be declaring next to
point to the root's parent which is None so when we update our pointers by moving current to next and prev to current, current will be
pointing to None and prev to the root, so we break out our while loop."""

#O(n) time | O(1) space
def iterativeInOrderTraversal(tree,callback):
    previousNode = None #initialize the previousNode pointer at None, the parent of the root node
    currentNode = tree #initialize the currentNode pointer at the root node
    while currentNode is not None: #we end the algorithm, if we ever try to access the parent node of the root node
        if previousNode == None or previousNode == currentNode.parent: #when coming from top, we need to explore left subtree
            if currentNode.left is not None: #if a left subtree exists
                nextNode = currentNode.left #set the nextNode pointer inside the loop to the left subtree
            else: #if the left subtree doesn't exist
                callback(currentNode) #then visit the current node by calling the callback function on it
                #explore right subtree if right child exists otherwise go back up to parent
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent #leafnode or one child
        elif previousNode == currentNode.left: #if coming back from the left subtree, then we just finished exploring left subtree
            callback(currentNode) #so we visit current node by calling the callback function on it
            #explore right subtree if right child exists otherwise go back up to parent
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else: #if coming from the right subtree ie previousNode == currentNode.right then we just finished exploring the right subtree
            nextNode = currentNode.parent #go back up to the parent

        previousNode = currentNode  #update previous node pointer after the logic above
        currentNode = nextNode      #update current  node pointer after the logic above


"""This question is about conducting in-order traversal iteratively instead of recursively. To do this, the node structure has to have 
a parent attribute so that we can go up the tree. We are also given a callback() function, that is what we use to visit a node. In a 
recurisve approach, we would return up the recursive tree so we wouldnt need a node attribute that stores the parent. This also means 
that the only node which will have None parent node is the root node. To conduct the iteration we need a previous pointer and a current 
pointer, and inside the while loop we declare a next pointer as a temporary reference to the next node, whether the left child, right
child or ones parent. Thus this iterative inorder traversal treats the binary tree like a linked list. And the whole thing is wrapped
inside a while loop whose loop condition is while currentNode is not None. The direction we move in depends on the relationship of the
currentNode and the prevNode, after we make a decision on where to move, we advance the pointers with the help of the nextNode temporary
pointer. 

If the previous pointer is equal to the current node's parent node or the parent node pointer is None, then it means we need to 
explore the left subtree, by declaring the next node pointer to point to the currentNode.left . This corresponds to the situation of going 
left in the recursive version, ie we go left at the very start where parent is None and if we are just coming from a parent node, we keep 
going left until we hit the leftmost leafnode. We keep going left as long as the left child exists otherwise we need to visit the current 
node and then go right if the right node exists by declaring the next node pointer to be currentNode.right otherwise the next node will be 
the parent node ie currentNode.parent. In otherwords, if we are at a leaf node, we visit and go to parent. If we are at a node with a None
left child and a BST node right child, we visit and go to the right node next. Then we update the pointers by moving previous pointer to
current and moving current to next node.

If the previous pointer is equal to the left child of the current node then it means we have just finished exploring the left subtree and 
so we have to visit the current node followed by exploring the right subtree , if the right subtree exists otherwise we go up to the parent
by decalaring the next node pointer to be the currentNode.right if it exist else currentNode.parent. In otherwords if we are dealing with a
node with a BST left child a None right child we go to the parent next otherwise, we go to the right child. Then we update the pointers by 
moving previous to current and current to next node. If we moved to the right child, the next iteration will trigger the first if clause
because the current will be at the right child and the previous will be at the parent and if that right child is a leaf node, that if
statement will visit it before going up the tree, if the right child has a left subtree, we will move left or if the righ child has a
None left child but a BST right child we will move further right.

If the previous pointer is not the currentNode's parent or the currentNode's left child it is because previous is pointing to the right
child and current is pointing to the parent. Thus we simply don't have a node to visit, we just update next node to be the current node's 
parent since we have finished all calls involving the current node and this corresponds to going up the recurisive stack. Then we update 
the pointers. This is essential because this step is what does the last update that terminates the while loop ie when we get back up to the 
root node, we will update to next node to its parent aka None. So when we update the pointers and move current to next Node, and previous
to current, previous will be pointing to the root node and current will be pointing to None.

In any of these cases, before we explore a particular subtree, we need to check if that subtree exists at all. That is 
before we explore the left subtree we first check if the current node has a left child, if it does we explore, if it doesnt we visit current 
node by calling the callback function on the current node followed by exploration of the right subtree. Before we explore the right subtree we 
first check if the current node has a right child, if it does we explore, it it doesnt we go up to the parent node and visit the parent node 
by calling the callback function on it. If we ever get to the point where the current node is None therefore, it means we have reached 
the end of the algorithm since at the start of the process, the current node is the root node and the previous node is its parent, None. 
Once again, it is essential for the node class to include an attribute to the parent for in order traversal to work iteratively."""