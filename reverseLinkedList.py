"""The question asks to write a function that takes in the head of a singly linked list, reverses the list in-place and returns its new
head. So lets say the linked list is 0 -> 1 -> 2 , the reversed linked list is 2 - > 1 - > 0. So at its core, when iterating through the
linked list, what does reversing it mean?. It entails making the next attribute on a node point to the previous node ie node.next = prev.
So we definitely need a currentNode pointer and a prev pointer. However, if we overwrite node.next say for node 1, we would loose any
reference to the original next node ie for node 1 we will lose the next attribute reference to node 2. So it means that before we update
a node's next pointer we have to store a reference to the original next node. So obviously the currentNode pointer will start at node 0,
ie initialized at the original head node , currentNode = head. And what will the prev pointer be initialized as? We know that after 
reversing the linked list, the original head node will become the new tail node and the tail of a linked list points to None value. So
we initialize prev pointer at None. So we initialize prev=None and currentNode = head, then we use a while loop to iterate and reverse
the linked list one next pointer at a time. Inside the while loop, the first thing we do is store a temporaray pointer to the original
pointer ie next = currentNode.next, then we reverse currentNode's next pointer ie currentNode.next = prev, then we advance the pointers
ie prev = currentNode, currentNode= next. We keep going until currentNode is None, at which point we terminate the loop and return
the prev pointer which will be pointing to the original tail which is the new head node.
"""



class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

#O(n) time | O(1) space
def reverseLinkedList(head):
    #we only declare p1 and p2 outside of the while loop, we declare p3 inside each iteration of the while loop
    #p1 is None because we reverse the middle pointer's node, and to reverse the head node ( ie make it the new tail)
    #we need p1 to be None so that we can overwrite the current head's next pointer to point to None, p1,
    p1,p2 = None,head  #previous node pointer, current node pointer

    while p2 is not None:
        p3 = p2.next #declare next node pointer to store a reference to the currentNode.next node before we overwrite the currentNode.next
        p2.next = p1 #reversal step by overwriting currentNode.next to point to the previous node
        p1 = p2 #advance the previous node pointer to point to current node
        p2 = p3 #advance the current node pointer to point to next node
    return p1 #return the new head of the linked list