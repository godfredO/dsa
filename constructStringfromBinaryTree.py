""" Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder 
traversal way, and return it. Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the 
string and the original binary tree.

Example 1:
Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it 
will be "1(2(4))(3)"

Example 2:
Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping 
relationship between the input and the output.


So the question is asking us to do a preorder traversal of the tree, so we start with the root node's value. Next will be the root's
left subtree, but we want to put the entire left subtree in parenthesis, before going to the right subtree which will also be put in
parenthesis, if the right subtree is not empty. In the code, we initialize an array and make a recursive call on the root node.
The base case is to return if we call on a None node, otherwise, we append an opening parenthesis, then a string of the node's value.
Before going left and right we check if the current node has a None left subtree but a non-None right subtree in which case we append a 
set of closed parenthesis before making the left and right recursive calls. For a leaf node, both of the child calls will immedaitely 
return. Otherwise we will go to the left child, repeat, then the right child, repeat. After the right child call ends we append a 
closing parenthesis.

The main thing is that the check for a node that doesnt have a left subtree but has a right subtree and append a set of parenthesis for 
the empty left subtree in order to ensure a non-ambiguous string representation for that tree. This is because of the question's 
specification to omit all empty parenthesis that do not affect the one-to-one mapping relationship between the string and the original 
binary tree, as demonstrated in Example 2. In other words, if a node has a left subtree but no right subtree, we can just return from
the right child call, if its a leaf node we can also just return from both child calls. But if it has a right subtree but no left 
subtree then we need the empty array to un-ambigously say that there is no left subtree lest the right subtree be mistaken for the
left subtree in that case. At the end we slice our array to remove the first paenthesis we append for the root of the  tree and then 
join the array's contents with "",join(array) before returning the resulting string.
"""






# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root) -> str:
        result = []
        dfs(root, result)
        result = result[1:-1]
        return "".join(result)
    
    
def dfs(node, result):
    if node is None:
        return 
    result.append("(")
    result.append(str(node.val))
    if node.left is None and node.right is not None:
        result.append("()")
    dfs(node.left, result)
    dfs(node.right, result)
    result.append(")")
        