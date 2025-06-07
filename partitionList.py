"""Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater 
than or equal to x. You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
 
Constraints:
The number of nodes in the list is in the range [0, 200].  ; -100 <= Node.val <= 100 ; -200 <= x <= 200

So this question is the same as algoexpert's rearrangeLinkedList.py, but of course using dummy nodes completely simplifies
the solution and intuition. The question is asking to move all nodes with values less than the target to the front of the
linked list and move all nodes with values equal to and greater than the target to the back of the linked list while 
maintaining relative order of the nodes. Another way of thinking about it is that, we have to form two separate linked lists
; one linked list will contain nodes whose values that are less than the target, the other linked list will contain nodes
whose values are equal or greater than the target. Once we have these two separate (sub) lists, we can reconnect them to
form the re-arranged list.

So what we do is to create two dummy nodes, and initialize a before pointer and a after pointer and we iterate the linked
list from left to right. We compare the value of the current node in the linked list to the target. If its less, it becomes
the next node in the before (sub) list otherwise its the next node in the after (sub) list, then we update the chosen list's
pointer and the current node. At the end of the iteration, we join the before tail to the after head's next as after head's
next is the first after node that is in the linked list; we also set the after tail to None, since its the tail of the 
rearranged linked list and return the before head's next node as its the real head of the rearranged linked list. Since we 
are not creating new nodes, this solution is O(n) time, O(1) space. In essence this question is an unmerging of a linked 
list, and uses the 2 pointer technique.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    beforeHead = ListNode(0)
    afterHead = ListNode(0)

    before = beforeHead
    after = afterHead
    current = head
    while current:
        if current.val < x:
            before.next = current
            current = current.next
            before = before.next
        else:
            after.next = current
            current = current.next
            after = after.next
        
    before.next = afterHead.next
    after.next = None
    return beforeHead.next