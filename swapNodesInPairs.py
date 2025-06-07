"""Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying 
the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
 

Constraints:
The number of nodes in the list is in the range [0, 100]. ; 0 <= Node.val <= 100 ;.

So this question is the same as algoexpert's nodeSwap.py. Basically, we can only swap a pair of nodes if we have well, a 
pair of nodes ie current node and current.next must both be non-None. So given 1->2->3->4, we swap 1,2 which means making 
2's next point to 1 and 1's next point to 2's next. The order of thes operations is important to get right. We also create
a dummy node and have its next pointer point to the head. The dummy node will be our initial previous node, and the head
node will be our first current node. Since we can only swap a pair of non-None nodes, our while loop is while current and
current.next are both non-None. First thing we do inside the while loop is to declare the second node of the pair, ie 
current.next and then its next node, current.next.next which will be the next current node of the next pair. Then we say
that the second node's next pointer should point to the current node, the current node should point to the next current
node. But this will leave the previous node pointing to the current node, so we update the previous node's pointer to 
point to the second node as this is the 'head' of the swapped pair. Then we update our pointers by moving previous pointer
to current node, and current node to the next current node. At the end, the dummy node's next attribute will be pointing 
to the new head of the list.

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head) :
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    curr = head
    while curr and curr.next:
        second = curr.next
        nextCurr = curr.next.next

        second.next = curr
        curr.next = nextCurr   
        prev.next = second

        prev= curr
        curr = nextCurr
    return dummy.next