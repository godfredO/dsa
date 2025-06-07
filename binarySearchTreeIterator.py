"""
Tags: Binary Search Tre; Stack; Hard

Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor.
The pointer should be initialized to a non-existent number smaller than any element in the BST. boolean hasNext() Returns true if
there exists a number in the traversal to the right of the pointer, otherwise returns false. int next() Moves the pointer to the right,
then returns the number at the pointer. Notice that by initializing the pointer to a non-existent smallest number, the first call to
next() will return the smallest element in the BST. You may assume that next() calls will always be valid. That is, there will be at
least a next number in the in-order traversal when next() is called.

Example 1:
Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[null, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False

So the question is to implement a class binarySearchTreeIterator with methods next(), hasNext() and the purpose of object and its methods
is to iterate over a given binary search tree in an inorder traversal way. As a result, the initialization method is provided the root of
said binary search tree. The class has a pointer which is initialized at say -inf and when we call next() it is supposed move the pointer
to the next value in an inorder traversal, and return this value.

Now take a three node system, [root, left child, right child]. Because this is a binary search tree, after the class is initialized, the
first call of next() should return the leftmost leaf node value (the smallest value) and hasNext() should return True because the leftmost
node here isnt the last value in an inorder traversal, its parent is next. next() should now return the parent's value. hasNext() should
also return True because the next value after the parent is the right child. next() should now move the pointer to the right child and
return its value. hasNext() should now return False because the right child is the last value in the inorder traversal.

So the naive solution here would be to write the class in such a way that upon instantiation we actually do an inorder traversal of the
input binary tree and store the result array in the class (like a heap), initialize a current pointer at 0. Then next() just returns the
value at current pointer in the inorder array and increments it. hasNext() checks if the current pointer is not out of bounds. In this
approach, the initialization method will be O(n) time, next() and hasNext() will both be O(1) and the space complexity will be O(n) too.

Can we do better? Can we implement a solution, where the space complexity isn't O(n) but rather O(h), even if the time complexity of
next() and hasNext() becomes O(1) on average (ie most times its O(1) but not all the time, sometimes its worse). The solution here is
to use a modified version of the iterative inorder function discussed in iterativeInOrderII.py

So when we initialize the object we add the entire left branch of the current (sub)tree root to the stack until the current pointer is
pointing to None (inner while loop of iterativeInOrderII.py). Then when we call the next() method, we pop from the stack, move current
to the popped node's right child and if the right child is not None, add the entire left branch of the (sub)tree rooted at the right child
to the stack, before returning popped node's value. hasNext() should then return is stack is non-empty (basically the outer loop condition
from iterativeInOrderII.py). By only adding the leftmost branch of popped node's right child, we ensure that space complexity is O(h).
One thing to note is that we are assured that next() will only be called if its valid ie when we have elements on the stack, so its not
necessary to add a check for this.
"""


class BSTIterator:
    # O(h) time | O(h) space
    def __init__(self, root):
        self.stack = []             # stack to store root of current subtree and left branch
        self.addLeftBranch(root)    # stack contains root node and all left child

    # O(h) time Average(O(1)) time | O(h) space
    def next(self):
        res = self.stack.pop()  # pop last node in the left branch that was added
        self.addLeftBranch(res.right)  # add left branch in subtree rooted at right child
        return res.val  # value popped node (next in-order traversal node)

    # O(1) time | O(1) space
    def hasNext(self):
        return len(self.stack) != 0

    # helper method
    def addLeftBranch(self, node):
        current = node  # current node initialized at root; subtree rooted at node
        while current:
            self.stack.append(current)  # store current node on stack; starting from root node
            current = current.left      # go to left child
