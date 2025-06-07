"""Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, 
return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:
The number of nodes in the list is in the range [1, 100]. ;  1 <= Node.val <= 100 ;

This question is the foundational question to the fast and slow pointer technique used in linked list questions. Basically,
this technique is used to pick out the middle node of the linked list. The idea is that we initialize both pointers at the
head node, and inside a while loop, we advance the slow pointer 1X times , and we advance the fast pointer 2X times. If the
length of the linked list is odd, then the loop condition is that we keep advancing as long as the fast pointer is not on 
the tail node ie while fast.next is not None. Similarly, if the length of the linked list is even, the loop condition is 
that we keep advancing as long as the fast pointer is not on a None node. Hence the overall loop condition is while fast 
is not None and fast.next is not None. When the while loop terminates, the slow pointer wil be pointing to the middle node
in the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(head) :
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow