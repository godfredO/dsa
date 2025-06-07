"""The question gives the head of a singly linked list and asks to remove the kth node from the end of the list. The operation should 
mutate the original linked list ie done in-place and the input head object should remain the same object after removal is done even 
if the head node is the node that's supposed to be removed, in which case the function should simply mutate its value and next pointer.
The function doesnt need to return anything. Finally we can assume that the input linked list will always have at least k nodes.

The first observation here, is that the last node in a linked list is the 1st node from the end, the penultimate the 2nd node from the
end etc. The second observation here is that to remove a node we simply have to update the bindings of the node before it to point to
the node after it. The third observation is that to do this, we have to grab the node before the removal node by somehow iterating 
through the linkd list and storing a reference to the node before the removal node. The final observation is actually in the question,
which is if the node to be removed is the head of the linked list we simply mutate the head's value and next pointer.

To solve this problem, we initialize two pointers at the head node, firstPointer and secondPointer. We will be moving one of these pointer 
exactly k times, so we also need a counter for the number of jumps which we initialize at 1. Then in a while loop, we say while 
secondPointer is not None and jumps <= k, we advance second pointer to second.next. Alternatively we could initialize the counter as 0
and the condition will be while secondPointer is not None and jumps < k. Either way we take exactly k jumps. If the removal node is the head, 
after exactly k jumps, the secondPointer will be at None. Thus this will be our indicator that head node is the node to be removed. So we 
handle that edge case next. If secondPointer is None, we mutate the head node object, value to head.next and its next attribute to 
head.next.next so that the head node has the same value as the second node and points to the third node. In the general case, we advance 
both secondPointer and firstPointer until secondPointer is at the last node in the linked list ie while secondPointer.next is not None. 
When this happens, firstPointer will be referencing the node before the removal node. So at this point we simply update the next attribute
of firstPointer node and we are done."""

class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

#O(N) time | O(1) space where N is number of nodes in linked list
def removeNthNodeFromEnd(head,n):
    counter = 1   #count number of nodes traversed
    first = head  #traverse linked list using exposed head
    second = head #traverse linked list using exposed head

    # when loop ends, counter = n+1 and second is on n+1th node 
    # as such second pointer is n nodes of first counter
    while counter <= n:
        second = second.next #traverse linked list using second
        counter += 1
    
    """
    second pointer is on the n+1th node while our first pointer is on the head node. 
    If the second node is the null value, then it means our first pointer, is already pointing to 
    the node to remove, which happens to be the head node. We overwrite the head node since
    we have access to it. overwrite head node if that is the object to be removed
    this ensures that we can still use the same object to access linked list
    return to end the function executing
    """
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return



    """
    # when loop ends second pointer will be on the end node
    # and first pointer will be on the node BEFORE the one to be removed
    # this is because a singly linked list has next attribute but no prev attribute
    # therefore if we moved first pointer to the node to be removed we will have no
    # way of accessing the previous node in order to update its next attribute
    """
    while second.next is not None:
        first = first.next
        second = second.next

    """ 
    # updating the next attribute of node before the node to be removed is how we actually
    # remove the node from the linked list.
    first.next = NODE_TO_REMOVE
    remove NODE_TO_REMOVE by setting first.next = first.next.next
    """
    first.next = first.next.next
    





