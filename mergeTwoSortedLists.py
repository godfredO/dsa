"""You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The list 
should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].; -100 <= Node.val <= 100 ; 
Both list1 and list2 are sorted in non-decreasing order.

We are told both lists are in non-decreasing order aka ascending order ie the each node's value is either equal to or greater 
than the previous node's value. This uses a variation of the 3 pointer technique, and the variation is that 3 pointers become
5 pointers. So we have a previous pointer, 2 current pointers, and 2 forward pointers. The loop condition is usually while
the second/current pointer is not None, but since we have 2 current pointers, the condition is while current1 is not None and
current2 is not None. Also, our initial previous node is a dummy node we create since we dont know which head node will be 
first in the merged list. Anyway inside of the while loop, we declare our two forward pointers. Then if the current1 node's
value is less than current2 node's value, the update the previous node's pointer to current1, advance previous pointer to
current1, and advance current1 to forward1. Otherwise, we update the previous node's pointer to current2, advance previous
pointer to current2, and advance current2 to forward2. This demonstrates another important aspect of 3 pointer technique, we
don't advance all pointers each time (check removeLinkedListElements.py for another interesting example of this). Now what
happens if we break out of the while loop because one of the current nodes is None. In that case we set the previous node's
next attribute to the non-None node, so we have an if/elif statement checking if either current node is non-None in order to
updatie previous pointer's next attribute to that current node. This has the effect of adding all the remaining nodes in that
current node's linked list to the merged list. At the end since we know that the dummy node's next attribute points to the
head of the merged list, we return dummy.next. 

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2) :
    dummy = ListNode(0)

    prev = dummy
    current1 = list1
    current2 = list2

    while current1 and current2:
        forward1 = current1.next
        forward2 = current2.next

        if current1.val < current2.val:
            prev.next = current1
            prev = current1
            current1 = forward1
        else:
            prev.next = current2
            prev = current2
            current2 = forward2

    if current1:
        prev.next = current1
    elif current2:
        prev.next = current2
            
    return dummy.next