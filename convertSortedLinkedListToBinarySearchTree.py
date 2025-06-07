"""Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST. For this problem, 
a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
 


This question is an extension of minHeightBst.py to a linked list as well as heightBalanced.py. The main idea is that a minimum height bst is 
height balanced. So basically, we iterate the linked list to get a sorted array and then create a minimum height binary search tree from it,
using preorder traversal.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedListToBST(self, head) :
    array = []
    currentNode = head
        
    while currentNode is not None:
        array.append(currentNode.val)
        currentNode = currentNode.next
        
    return helper(array, 0, len(array) - 1)

def helper(nums, startIdx, endIdx):
    if startIdx > endIdx:
        return None
    
    midIdx = (startIdx + endIdx) // 2
    midVal = nums[midIdx]
    
    root = TreeNode(midVal)
    
    root.left = helper(nums, startIdx, midIdx - 1)
    root.right = helper(nums, midIdx + 1, endIdx)
    
    return root
        