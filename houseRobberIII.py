"""The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root. Besides the root, 
each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It 
will automatically contact the police if two directly-linked houses were broken into on the same night. Given the root of the binary tree, 
return the maximum amount of money the thief can rob without alerting the police. 0 <= Node.val <= 10^4 ie non-negative money values.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


When it comes to tree problems, the traversal options are level-order bfs, pre-order dfs, in-order dfs, and post-order dfs. This question
is a tree problem with a dynamic programming twist like triangle.py. The question at the heart of either problem is that the choice to
choose a node over its adjacent nodes is being done in the blind if done top-down. For any node we choose we can only choose any of its 
grand children next, we can't choose it children due to the constraint of non-adjacency. Since we have no way of no knowing if choosing 
the root and limiting ourselves its granchildren next will yield a better overall sum compared to choosing one of its children and limiting 
ourselves to its children's grandchildren next, a better way of approaching this problem is with a bottom up approach ie post-order dfs.

Now at each point we have two decisions to make, do we include the root of the current subtree or do we not. So in a bottom-top postorder
dfs way, we will be returning these two values. That from a leaf node, we return cases: [withRoot, withoutRoot] ie the max sum we obtained
by choosing the root of the leaf node's subtree and the max sum we obtained without the choosing the leaf node (the root of its subtree).
When we work our way up to the root of the binary tree ie whatever our original call returns, we return max(origninalCall[withRoot, without]).

But what does our visit step actually look like? What logic do we use? One further complication of this solution is that we can skip
successive levels. For example, we can choose the root, skip its child, skip the next child and choose the leaf node if that is the maximum 
sum since that's the only way we can choose the root and leaf by not choosing any of their adjacents. Well we know that for every leaf node, 
withRoot = leafnode.val, withoutRoot = 0. So we send this value up to its parent. The parent can add its value only to the withouRoot value 
of its child and that becomes the parent's own withRoot value parent.withRoot = parent.val + leftInfo.withoutRoot + rightInfo.withoutRoot. 

The parent's without root value parent.withoutRoot = max(leftInfo.withRoot, leftInfo.without) + max(leftInfo.withRoot, leftInfo.withoutRoot) 
Now why isnt it just parent.withoutRoot = leftInfo.withRoot + rightInfo.withRoot?. One way of saying this is that the maximum sum in a node's 
subtree not including its value may or may not include its children. It may be more advantageous to skip the current node and the current 
node's children etc in order to get access to some greater non-adjacent sum. Another way of saying it is, the max sum without a node, need 
not include its child node so we take the maximum of the sum with and without its child node and bubble it up, ie we don't necessarily have 
to choose a value from each level like in triangle.py, we can skip levels to maximize the sum. So if we have 1-> 2 -> 3 -> 100, node 3 will 
bubble up [3,100] and the without of 2 is max([3,100]) ie doesnt include 3. And that is why at the end we return the max of the withRoot and 
withoutRoot values returned by the original call.
 
"""
#O(n) time | O(d) space
class TreeInfo:
    def __init__(self, withRoot, withoutRoot):
        self.withRoot = withRoot
        self.withoutRoot = withoutRoot
        
def rob(root) -> int:
    treeInfo = postOrderDfs(root)
    withRoot, withoutRoot = treeInfo.withRoot , treeInfo.withoutRoot
    return max(withRoot, withoutRoot)

def postOrderDfs(node):
    if node is None:
        return TreeInfo(0,0)
    
    leftInfo = postOrderDfs(node.left)
    rightInfo = postOrderDfs(node.right)
    
    withRoot = node.val + leftInfo.withoutRoot + rightInfo.withoutRoot
    withoutRoot = max(leftInfo.withRoot, leftInfo.withoutRoot) + max(rightInfo.withRoot, rightInfo.withoutRoot)
    
    return TreeInfo(withRoot, withoutRoot)