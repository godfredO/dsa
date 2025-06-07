"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. 
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is 
not a multiple of k then left-out nodes, in the end, should remain as it is. You may not alter the values in 
the list's nodes, only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
Constraints:
The number of nodes in the list is n.  ;  1 <= k <= n <= 5000  ; 0 <= Node.val <= 1000  . 


So this question is a generalization of swapNodesInPairs.py or nodeSwap.py where we are reversing nodes 2 at a time,
kinda like the relationship between mergeLinkedLists.py and mergeKSortedLists.py. So each group has to have k nodes,
then we find the first k nodes, reverse them, the second k nodes reverse them and if we get to the end and the last
group has less than k nodes, we dont do anything. This is kind of realizing that in the swapNodesInPairs.py, we could
only swap nodes if there were a pair of non-None nodes, just that here, we replace pair with group of k non-None nodes.

Now like most linked list questions, we use a dummy node, since we could modify the original head node. So when you
think about reversing the first k-group, we apply reverseLinkedList.py and swapNodesInPairs.py. This is because we 
know that after reversing the k-group we need to set the previous node to the k-group, to the new head of the reversec
k-group. We also know from swapNodesInPairs that after reversing the k-group, the node that is originally first in the
k-group will become last in the k-group and as such its next pointer will need to be update to the next node of the
original last node in the k-group. So after creating a dummy node and setting its next attribute as the head node, we
start from the use a while loop to make exactly k jumps from the dummy node to grab the kth node from the dummy which
will be the last node of the first k group. Now since we are told that the linked list length will not necessarily be
a multiple of k, we need to ensure that if there is no first k-group (or any other subsequent k-group for that matter),
we know to stop immediately. So the while loop for grabbing the kth node of the next k group will stop when we have
made k jumps or the current node is None. If the kth node is None, we break out of our main while loop, otherwise we
reverse the k-group, starting from the first node in the k-group. For any k-group, there are two other nodes we need
the groupPrevious and the groupNext. The groupPrev is the node before the first node in the k-group, the groupNext
the next node after the kth node in the k-group. The groupPrev will be initialized at the dummy node for the first
k-group, and the groupNext will the kth.next node. An observation from swapNodesInPairs.py, is that after reversing 
the k-group, the original first node will point to the groupNext. So we apply reverseLinkedList.py, initializing the
prev node as groupNext, and current as groupPrev.next ie the first node in the k-group. Then we do the standard steps
for reversing the k-group. We stop whenever the current group equals groupNext, since that indicates that we have 
finished the entire k-group. Reversing steps involve storing a temporary variable to current.next, updating current's
next attribute to prev and then shifting prev to current and current to the temporary variable we stored. When we
finish reversing the k-group, its time to set groupPrev's next pointer to the new 'head' of the k-group. So we first
store a temporary to the current next attribute of groupPrev which is now the last node of the reversed k-group and
thus the next groupPrev for the next k-group. Then we update groupPrev.next to kth which, is now the first node in 
the reversed k-group, before updating groupPrev to the temporary variable we stoed. At the end, we return the next
node of the dummy variable reference which will be pointing to the new head of the linked list after reversing all
nodes in k-group.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head

    groupPrev = dummy
    while True:
        #grab kth node of current k-group
        kth = groupPrev
        count = 0
        while kth and count < k:
            count += 1
            kth = kth.next

        if not kth:
            break
            
        groupNext = kth.next

        #reverse step
        prev , cur = groupNext, groupPrev.next
        while cur != groupNext:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            
        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next
            

