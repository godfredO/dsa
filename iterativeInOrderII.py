"""So this is using a stack to do an iterative inorder traversal. We also use one pointer, current which is initialized at the root.
When we enter the outer while loop, the loop condition is while current isnt None or the stack isnt empty, we keep going. This means
if current is None and the stack is empty, we are done with our algorith. In the beginning, because current is the root, if the root
isnt None, we are able to start the algorithm even though the stack at this point is empty.

So in inorder traversal the pattern is we go left until we cant, then we visit the current node, then we go right. So we have an 
inner for loop, that goes left and that loop condition is to keep going while current is not None. So if current is not None, we
append current node to the stack and advance current pointer to the left child. This will keep running until we get to the None child 
of a current node, then its time to visit the current node and then go right.

To visit and then go right, we pop from the stack, the last node we appended, and add that value to the result array. Then we advance 
current pointer to the popped node's right child. Then we go up to the outer loop. So say the last popped node was a leaf node, and
so current is now None, its right child, then if the stack is non-empty we enter the outer while loop, but not the inner while loop
and we pop its parent node, append its value to the stack and advance current pointer to the parent's right child. Now I am going 
with a three node system here (root, left,right) , so now we would be at the right child of the root node which is not None. If this
right child is also a leaf node, when we go left, current will be pointing to its left None child so we will break out of the inner
while loop, pop the right child, append its value to the result array  and update current to now point to the right None child. At
this point, current is None and the stack is empty so we return the result array. This iterative function demonstrates what is 
happening under the hood of the recursive implementation of inorder traversal of a tree."""

def inorderTraversal(root):
    current = root
    stack = []
    result = []

    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result