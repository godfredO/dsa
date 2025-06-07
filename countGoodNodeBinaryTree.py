"""Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater 
than X. Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.


A node X in a binary tree is called good, if in the path from root to X there are no nodes with a value greater than X. Another way of saying
this is that every value on the path from root to X is equal to or less than the value of X. Put yet another way, the value of X is greater
than or equal to the value of all nodes on the path from root to X. Now do we need to compare the value of node X to the value of every
other node that occurs on the path between it an the root? No, we simply need to compare it to the maximum value on the path between it and
root. We are asked to count all good nodes in a binary tree given the root. So the solution is straightforward, we keep a maxInPath variable
which is initialized at -inf, since we are doing a maximum comparison, then at each node we compare if the node's value is greater than or
equal to the maxInPath. If it is, we increment the number of good nodes variable. Now there are two solutions discussed below, the breadth
first search solution, and the depth first search solution and they have the same time complexity but the depth-first search solution has
a better space complexity.

In the breadth-first search, we initialiae our queue with a the root node and the intialized maxInPath ie -inf. Inside the bfs while loop,
we pop, check if the node is None in which case we skip and the first thing we check is if the node is greater or equal to the maxInPath 
value packed with it. If it is, we increment our numGoodNodes variable by 1. Next we update the maxInPath variable by doing a max comparison 
with the current node's value. The reason being that if the current node has a greater value, it will become the new maxInPath for its child
nodes. After the update, we add its child nodes to the queue with the updated maxInPath values. Because half of all nodes in a binary tree 
can be in its leaf nodes, the queue can hold up to n/2 nodes giving a space complexity of O(n).

The dfs solution uses the bottom down method of dfs employed for binary trees where after checking the base case(s), the first thing we do
is to make a call to the child nodes, before carrying out some logic, sometimes with values returned by the child node calls. In the main 
function we initialize an object goodNodes which will be updated in the recursive calls whenever we find a good node. Then we make the 
recursive call on the root, with the initial maxInPath of -inf , and the goodNodes object. Inside the recursive call the base case is that 
if the node is None, we return. The we make the recursive call to the left child and the right child but in these calls, we pass in for
the maxInPath, the maximum of the current node's value and the passed maxInPath ie rec(node.left, max(maxInPath,node.value), goodNodes),
rec(node.right, max(maxInPath, node.value), goodNodes). This ensures that the child nodes get the updated maxInPath value. Then after the
child calls, we check if the node value is greater than or equal to the passed maxInPath, and if it is, we increment the value stord in
the goodNodes object by 1. Thus we will go all the way down to the leftmost leafnode, arrive there with the most updated maxInPath for the
path from root to it, do the comparison, updating the good nodes object value if found to be a good node, then execution is returned to
its parent who then calls on its right child (say a leaf node too), after that call is resolved, execution returns to the parent to do
its own comparison. Doing the max comparison of the parent value with the passed maxInPath value inside the child recursive calls ensure
that the when execution returns to the parent its technically comparing itself to the right maxInPath for its own path to root. At the
end, in the main function call, we return the value stored in goodNodes object.

The dfs soluton here can actually be re-written in a pre-order manner ie, we can check if the current node is a good node by comparing 
it with the passed maxInPath. The after we make the child node calls. We can still pass in the max comparison of the current node with
the maxInPath or since we have already compard the current node, we can actually just update the maxInPath before doing the child node
calls. So solution III is a preorder dfs and closely aligns with the bfs solution. 

Finally, the last solution is just about coding style we can avoid implementing a custom object for a single value. In this coded 
solution, the base case is that if we are at a None node we return 0. The we  initialise a result variable as 1 if the current node is 
greater or equal to maxInPath else 0. We then update the maxInPath by doing a max comparison with the current node's value . Finally we
increment the result variable with the value returned by the recursive call on the left subtree and then increment it again with the value 
returned by the  recursive call on the right subtree. At the end we return the result variable. This approach has the effect of finding
the number of good nodes in the left and right subtree and then add it to the result variable before the result variable is sent up the
tree.

One final word, since the root will be in every path and the root node always counts as a good node, we can techically initialize maxInPath 
as the root node's value instead of -inf but I like consistency so I prefer to always use -inf if I will be doing max comparisons.

"""
"""Bfs solution - inoptimal space complexity"""
#O(n) time | O(n) space
from collections import deque
def goodNodes(root) :
        numGood = 0
        queue  = deque()
        queue.append([root, float("-inf")])
        while queue:
            node, maxInPath = queue.popleft()
            if node is None:
                continue
            
            if node.val >= maxInPath:
                numGood += 1
            
            maxInPath = max(node.val, maxInPath)
            
            queue.append([node.left, maxInPath])
            queue.append([node.right, maxInPath])
        return numGood


"""Dfs solution, just do the max comparison inside the child recursive calls"""
#O(n) time | O(d) space - Optimal solution
class GoodNodes:
    def __init__(self,value):
        self.value = value

def goodNodes(root):
    goodNodes = GoodNodes(0)
    return helper(root, float("-inf"), goodNodes)

def helper(node, maxInPath, goodNodes):
    if node is None:
        return
    
    helper(node.left, max(maxInPath, node.val), goodNodes)
    helper(node.right, max(maxInPath, node.val), goodNodes)

    if node.val >= maxInPath:
        goodNodes.value += 1
    

"""Preorder dfs solution"""
#O(n) time | O(d) space - Optimal solution
class GoodNodes:
    def __init__(self,value):
        self.value = value

def goodNodes(root):
    goodNodes = GoodNodes(0)
    return helper(root, float("-inf"), goodNodes)

def helper(node, maxInPath, goodNodes):
    if node is None:
        return
    
    if node.val >= maxInPath:
        goodNodes.value += 1
    
    maxInPath = max(maxInPath, node.val)
    
    helper(node.left, maxInPath  , goodNodes)
    helper(node.right, maxInPath , goodNodes)


"""Preorder dfs solution without the use of objects"""
def goodNodes(root):
    return helper(root, float("-inf"))

def helper(node, maxInPath):
    if node is None:
        return 0 
    
    result = 1 if node.val >= maxInPath else 0
    maxInPath = max(maxInPath, node.val)
    result += helper(node.left, maxInPath)
    result += helper(node.right, maxInPath)
    return result

    

"""Preorder dfs solution without the use of objects and initializing maxPath as root node value"""
def goodNodes(root):
    return helper(root, root.val)

def helper(node, maxInPath):
    if node is None:
        return 0 
    
    result = 1 if node.val >= maxInPath else 0
    maxInPath = max(maxInPath, node.val)
    result += helper(node.left, maxInPath)
    result += helper(node.right, maxInPath)
    return result