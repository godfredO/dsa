"""You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has 
the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right 
node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of 
each level.

Example 2:
Input: root = []
Output: []

So if you go to leetcode and look at the figure A and figure B of this question, you realize that this is rightSiblingTree.py. However
in this question, the nodes have an additional next attribute and it is this attribute that we need to update to point to the right
sibling. We are also assured that this is a perfect binary tree in that all parents have two child nodes and all leaf nodes are on the
same level. So my first approach is to re-purpose bfs solution of rightSiblingTree.py, use depth information and if the next node on
the queue doesnt have the same depth as the current node, do nothing since the next pointer is already pointing to the None. 

In the dfs version, if isLeftChild, we update next to point to parent.right and else if parent is not None and parent.next is not None, 
(avoiding parents that are on the rightmost edge and the root node whose parent is None), we update the next pointer of node to point 
to parent.next.left. Note that since we are only updating next pointers herre, we can use the node.left and node.right in the recursive 
calls. The dfs pattern is inorder dfs.

Now to fully take advantage of the perfect binary tree structure, we can use a breadth-first search and actually obtain a O(1) solution.
Remember that breadth-first search for trees has another name, level-order traversal. So we will be traversing the tree level by level.
We will be using two pointers, current and next. currrent will traverse the nodes on the same level, and for each node on that level, it
will update that node's children's next pointers ie it will be updating the pointers of the nodes that are one level below. next pointer
will point to the leftmost node of the next level to be processed and will be used to move current pointer down. That is current pointer
will be updating the next attributes of the nodes on next pointers level. When current is at the root node, next will be at the root's 
left child, and when current has finished updating the next attributes of the root's two children(that are on next pointer's level),
the current pointer will move to next pointer and next pointer will move one level down, then current will start moving left to right,
updating each node's children's pointer.

So how does current update the pointers of the nodes below? We know that for each node on the current level, their left child will point
to their right child and their right child will point to their right sibling's left child , with the exception of the last node in the
tree, whose right child's next attribute doesnt need updating and should still point to None. That is current.left.next = current.right 
and current.right.next = current.next.left before advancing current to the next node on that level ie current.next. But if we are at the
last node in that level, we don't need to update its right child's pointer since its already pointing to None. So we actually surround it
with if current.next : current.right.next = current.next.left ie we only update a right child's next attribute if its parent has a non-None
next attribute node. Also when we are past the last node in that level, we know its time to advance current pointer. And how do we know this. 
At the last node, when we move the current pointer left, we actually move current to None. So after we move current pointer left (ie current
= current.next) we check if we just moved it to None ie if not current, and if that is the case then advance current a step below, we will 
only ever hit the advance step when we move left from the last node of the level we are at.. And advancing to the next level is done by 
current = next, next = current.next. 

The entire opertion goes on as long as both current and next are not None nodes ie we either advance to the None nodes of the leaf nodes 
(perfect tree so all leafs are on the same level) in which case current will also be None anyway. So from the root we will update 
root.left.next = root.right and since root.next is None, we move to the next level without updating its right child's next pointer. If you 
really look at the O(d) dfs you realize that is what we are actually doing. We also have to handle the edge case where the root node is None 
ie when initializing next, if root is None, next is not root.left but rather just None. At the end we return the root node.
"""


"""Bfs solution"""
from collections import deque
#O(n) time | O(n) space
def connect(root) :
    queue = deque()
    queue.append([root, 0])

    while queue:
        node, depth = queue.popleft()

        if node is None:
            continue
        
        queue.append([node.left, depth + 1])
        queue.append([node.right, depth + 1])
        
        nextNode = queue[0]
        if depth == nextNode[1]:
            node.next = nextNode[0]
    
    return root


"""Dfs solution"""
#O(n) time | O(d) space
def connect(root):
    mutate(root, None, None)
    return root

def mutate(node, parent, isLeftChild):
    if node is None:
        return
    
    mutate(node.left, node, True)

    if isLeftChild:
        node.next = parent.right
    elif parent is not None and parent.next is not None:
        node.next = parent.next.left
    
    mutate(node.right, node, False)


"""Optimized solution """
def connect(node):
    cur, next = node, node.left if node else None

    while cur and next:
        cur.left.next = cur.right
        if cur.next:
            cur.right.next = cur.next.left
        
        current = current.next
        if not current:
            current = next
            next = current.left
        
    return node