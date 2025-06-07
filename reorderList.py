"""You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 
Constraints:
The number of nodes in the list is in the range [1, 5 * 104]. ; 1 <= Node.val <= 1000



This is the same question as algoexpert's zipLinkedList.py. Basically the steps combines solutions to other questions. First 
find the middle of the linked list and reverse that sublist, then reorder the reversed sub-list and the sublist from the head 
to the node before the middle. So if we have 1->2->3->4, we first use the slow and fast pointer techiniqe to find the middle 
node 3 ie middleOfTheLinkedList.py. Now the only addition to this question is realizing that the middle node will always be 
the tail node of the reordered list. Thus to avoid having a cycle in the final reordered list, we need to set its next 
attribute to None. Hence, we reverse the sublist starting from the current next node of the middle node. So first we store a 
reference to the slow node's next node, as the head of the sublist to be reversed and then we set the next attribute of the 
slow node as None as its going to be the new tail. Then we reverse the half the original linked list starting from (previous) 
middle node's next node to the current tail. This first step is the same as reverseLinkedList.py just that instead of starting 
from the middle node we are starting from its (previous) next node to the current tail. With half the linked list reversed, we 
reorder the list using a variation of the 3 pointer method. In this method we need a two pointers for the two sublists, and 
inside the while loop, we store temporary references to the next nodes of the two sublists, so its actually a 4 pointer 
variation. Anyway, reordering the sublists step is similar to reverseLinkedList.py, and as such its loop condition is while the 
second sublist is not None. Hence this question combines middleOfTheLinkedList.py and reverseLinkedList.py with the only additon 
being that the middle node becomes the reordered list's tail and as such the second sublist starts from its next node, and after 
storing a reference to that node, we set the middle node's next attribute to None to make it the new tail and to avoid having
a loop in our reordered list (which occurs for even-length liked list). So slow/fast pointer and 3 pointers with tail info.

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reorderList(head) :
    """
    Do not return anything, modify head in-place instead.
    """
    
    slow = head
    fast = head
    while fast  and fast.next :
        slow = slow.next
        fast = fast.next.next
        
    
    prev = None
    current = slow.next
    slow.next = None
    while current :
        forward = current.next

        current.next = prev

        prev = current
        current = forward
        

    first = head
    second = prev
    while second is not None:
        forward1 = first.next
        forward2 = second.next

        first.next = second
        second.next = forward1

        first = forward1
        second = forward2
        
        
