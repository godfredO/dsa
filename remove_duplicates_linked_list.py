"""The input is the head of a singly linked list whose nodes are in sorted order with respect to their values. The question asks that returns
a modified version of the linked list that doesnt contain any nodes with duplicate values, this modification should be done in-place,
and the modified linked list should still have its nodes sorted with respect to their values.

This question is an excellent example of the sorted proximity order pattern. The first observation that helps solve this question is that 
since all the nodes are sorted with respect to their values, all the duplicates will be next to one another. The second thing to realize is 
that removing a node from a linked list involves updating the next pointer that points to it to point to the node that the removal node's
next pointer points to, phew!!! a mouth full. In this question specifically since any duplicates will be back to back, we need the next 
pointer of the first instance of a duplicate value to point to the node pointed to by the next pointer of the last duplicate. Thus we use
two pointers, the first pointer will be iterating through the linked list and will be pointing to the first instance of a possible duplicate.
In linked list we only use while loops so the first pointer here, will be initialized outside the while loop and since it will be iterating 
through the entire linked list, we keep advancing it until we get to the end of the linked list ie while first pointer node is not None. 
The second pointer will be initialized inside the while loop to point to the current first pointer node's next paramenter. The purpose of this 
second pointer is to find all the duplicates of the first pointer node's value. So while this second pointer is not None and the current 
second pointer node's value is equal to the first pointer node's value we keep advancing the second pointer by updating it to the node in its
next pointer. Thus we use an inner while loop to advance the second pointer. When this inner while loop breaks the secoond pointer will be 
pointing to the next pointer node of the last duplicate ie the first node that is not a duplicate of first pointer's current node. Then to
remove the intervening duplicates, we update the first pointer's next node to point to the current second pointer node which at this point
holds a non-duplicate value of the first pointer node. Then we advance the first pointer by updating it to this current second pointer. Then
back to the top of the outer while loop to find its duplicates until all  duplicates are removed. At the end we return the original head of
the linked list. Since the second pointer is initialized afresh inside the loop whenever the first pointer is advanced and the inner while
loop only traverses intervening duplicates, and the first pointer only moves to non-duplicate values, the total traversal here is exactly
n jumps for all pointers eg 1-1-1-2-2-2-3-3, the first pointer will be at the first 1, the first 2 and the first 3. The second pointer will
go through all the intervening duplicates ie two 1's, two 2's, and one 3 ie 3 jumps of first pointer, 5 jumps of second pointer for a total
of 8 jumps which is the total number of nodes.

Alternatively we could combine a lot of these steps. We know that we need to check if the next node is non-None and if its not, check if its
value equals the current node. If these are true, we update the current node's next pointe to be its next node's next node ie cur.next =
cur.next.next. This form of the inner loop will break if cur.next is None or cur.next doesnt have the same value as cur node so outside the
inner while loop,  we advance cur pointer to cur.next which will either be the next distinct node or None."""


class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None
    
# O(n) time | O(1) space
# the input to the function is the head node
def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList

    #checking if end of linked list is reached 
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        
        #skip through duplicates until distinct valued node is found
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        
        # update the current node's pointer to be the next object with a non-duplicate value
        currentNode.next = nextDistinctNode
        # move current node to the distinct value found and repeat outer while
        currentNode = nextDistinctNode

    return linkedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head) :
    cur = head

    while cur :
        while cur.next and cur.next.val == cur.val:
            cur.next= cur.next.next
        cur = cur.next     
    return head