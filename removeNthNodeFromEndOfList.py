"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]


So this question is the same as algoexpert's remove_nth_node_from_end.py. The intutition is the same. If we have the
linked list 1->2->3->4, node 4 is the 1st from the end, 3 is the 2nd from the end, 2 is the 3rd from the end, 1 is 
the 4th from the end. What does it mean to remove a node say to remove the 2nd from the end ie node 3. Simply said, 
it means updating the next pointer of the previous node, node 2 to point to the removal node's next node ie node 4.
So really, the question is asking how can we obtain a reference to the node before the removal node in order to 
overwrite its next pointer. So say we are asked to remove the 4th from the end, in a list with 4 nodes (n <= number 
of nodes in list) ie the head node, node 1. This is where this solution is cleaner than the algoexpert solution. 
Basically, we use another technique common in linked list questions ie using a dummy node. So we create a dummy node
and make the head node its next pointer. So how do we get acess to the node before the removal node. We use a 
variation of the fast/slow pointer technique though in this case the two pointers vary, not by speed, by displacement.
So we initalize the fast pointer at the head node and jump exactly n times. If the head node is the removal nodes after
n jumps, the fast pointer will be at the None value of the tail node. We also initialize the slow pointer at the dummy
node. This means that after n jumps of the fast pointer (initialized at the head), the slow pointer (initialized) at
the dummy node will be pointing to the node before the removal node so we overwrite the dummy's next to point to the
head's next node, and return the dummy's next node as the new head. If the head node is not the removal node, then
after n jumps of the fast pointer, we advance both the fast and slow pointer until the fast pointer is None. Then 
whatever our slow pointer is pointing at, it will be the node before the removal node, so we update the node before 
the removal node's next attribute to point to the removal node's next node, hence skipping over the removal node. 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n) :
    dummy = ListNode(0)
    dummy.next = head

    fast = head
    count = 0
    while count < n : 
        count += 1
        fast = fast.next

    slow = dummy
    while fast:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next

    return dummy.next