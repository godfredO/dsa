"""You are given the root of a binary tree containing digits from 0 to 9 only. Each root-to-leaf path in the tree represents a number.
For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123. Return the total sum of all root-to-leaf numbers. 
A leaf node is a node with no children.

 

Example 1:


Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:


Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

So basically the question is asking to convert the numbers in every branch into a number and add up all the branch numbers. So if the 
leftmost branch from root to leftmos node is 4->9->5 then the number for that branch is 495 and after we have all the branch numbers we
sum them up. So, the this is going to be a preorder traversal and we are going to compute the sum as we go. Specifically if we go from
4->9, the number represented is 49 which is 40 + 9 = 49 and when we go to 5 the number represented is 495 which is equal to 490 + 5.
Thus at each point we multiply the running sum by 10 and add the current number's value (visit) and then feed this running sum to
both the left and right child of the current node. Meaning, if at 9, 5 is the left child and 1 is the right child, then we should get
495 and 491 ie 490 + 5 and 490 + 1. 

So that exactly what the preorder traversal dfs does, we pass in a node and a running sum, we multiply the running sum by 10 , then add 
the node's value before passing it to both the left and right child. Now after adding the node's value to the incremented sum, we check 
if the current node is a root node, in which case we just return the updated sum without making child calls. Of course we need to have a 
base case to handle going to the None child of a node with 1 bst and 1 None child. But any way, if we are not at a leaf node what do we 
return? We return the sum of the result of the recursive calls on the left and right child. Why? After we return the completed number 
from the leaf nodes we return the sum of the branches that end at those leaf nodes. So in order to handle the case of a node with 1 bst 
and 1 None child, we if we get to a None node we return 0, for this sum. 

This will have the effect of building the leftmost branch value, returning the value when we get to the leftmost leafnode up to its parent. 
It parent then makes the right child recursive call which may return another value or 0 (if the parent has 1 child), it sums it up and sends 
it up the tree, where the parent's parent will go down its right child, build up the values going down, and have the sum of all the branch 
values returned and so on and so forth until we get to the original call and return the sum of the root to leaf numbers.

Thus we have two base cases, one for if the node is None and one for if the node is a leaf node, however the second base case comes 
between the visit step of multiplyinng the sum by 10 and incrementing with node value and the go left, go right steps of preorder. It should
also be said that we initialize the sum as 0 so the first time, 0 * 10 + root.val = root.val.

"""
#O(n) time | O(d) space
def sumNumbers(root):
    return helper(root, 0)

def helper(node, sum):
    if node is None:
        return 0
    
    sum *= 10
    sum += node.val

    if node.right is None and node.left is None:
        return sum
    
    left = helper(node.left, sum)
    right = helper(node.right, sum)

    return left + right
