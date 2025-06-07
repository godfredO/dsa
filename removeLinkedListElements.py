"""Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, 
and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
 

Constraints:
The number of nodes in the list is in the range [0, 104]. ; 1 <= Node.val <= 50 ;  0 <= val <= 50  .


So this solution uses, a variation of the standard three pointer system for overwriting node attributes. Inside the while loop, 
we first store a reference to the current node's next node and then check if the current node's value equals the target value. 
If the current node's value is not equal to the target value, then we update both pointers by moving previous to current, and 
current to the temporary pointer. If the current node's value equals the target value, then after storing a temporary reference
to the current node's next node, we remove the current node by setting the previous node's next pointer to the temporary
reference. This brings up the question, how we remove the head node if its value equals the target value, knowing that we will
need to return a new head node ie the current head's next node. To handle this case we create a dummy node, set its next node
as the head  and the dummy node becomes our initial previous node, and the head node becomes the initial current node. Now how
do we update the pointers in the case where the current node is removed. In that case, we keep previous right where it is, and
update current node to the temporary reference. At the end we know that the dummy node's next attribute will point to either
the original head or the new head, so we return dummy.next as the head of the linked list with removed nodes.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val) :
    dummy = ListNode(0,head)

    prev = dummy
    current = head
    while current:
        forward = current.next

        if current.val == val:
            prev.next = forward
        else:
            prev = current

        current  = forward

    return dummy.next