"""The question is to write a function that takes in the head of a singly linked list and an integer k, shifts the list in place by 
k positions, and returns the new head. Shifting a linked list means moving its nodes forward or backward and wrapping them around the 
list where appropriate. For example, shifting a linked list forward by one position makes its tail the new head. Whether nodes are
moved forward or backward is determined by whether k is positive or negative respectively.

This question in my opinion is based on the Remove Kth Node From the End. If head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 and k is two, the answer
is 4 -> 5 -> 0 -> 1 -> 2 -> 3. That is the new head of the linked list is the kth node from the end, the original tail now points to 
the original head and the new tail is the node before the kth Node from the end. In the Remove Kth Node From The End, we actually
realized that to remove the kth node we need to grab a reference to the node before  the kth node from the end and overwrite that
node's next pointer to the kth node's next pointer value in order to remove the kth node from the end from the list. So we can say that
if k == 0, we leave the list as it is otherwise in the general case, the kth node from the end becomes the new head, the original tail
points to the  original head and the node before the kth node from the end becomes the new tail. 

What about if k=-2 ie k is negative. The answer will be 2 -> 3 -> 4 -> 5 -> 0 -> 1. Here, the original tail still points to the original 
head, the kth node from the front becomes the new tail and the node after it becomes the new head. What about if k = 6? Here the linked 
list is 0 -> 1 -> 2 -> 3 -> 4 -> 5 ie if k is equal to the length of the linked list (total number of nodes), then it is the same as k=0. 
What about k = 7? That will be 5 -> 0 -> 1 -> 2-> 3 -> 4 ie equal to k=1. That means we need to modulo divide the input k, by the length 
of the linked list in order to get the true shift integer. So we now need the grab a reference to the original tail of the list, calculate 
the length of the linked list and grab a reference to the new tail (the new head will be the next of this node). 

So we know that the new tail and the new head are related by newTail.next = newHead, but if k is positive, the new tail is the (k+1)th 
node from the end, the new head is the kth node from the end. If k is negative, the new tail is the kth node from the front and the 
new head is the (k+1)th from the front. So how do we cleverly resolve this to write clean code? We do it by realizing that we can resolve
the position of the new tail to the position from the front of the linked list using the length of the linked list. Since we need to 
calculate the length anyway we can say that if k is positive, the position of the new tail is (length - k)th position from the front,
and if k is negative the new tail is kth node from the front and in either case the new head is newTail.next. 

So in the coded solution we calculate the length and grab a reference to the original tail of the linked list at the same time with a
while loop. We initialize the tail pointer to the head and initialize length to 1 (for the head node) and inside the while loop we
advance the pointer and increment the length varialbe until tail.next is None ie the while loop condition is while tail.next is not None.
And this is because if the next attribute on a node is None, we know we are at the  tail node. Then we calculate the offset ie the shift
distance by modulo division of the length by the absolute value of k. Then we check if the calculated offset is 0, ie no shift distance
in which case we return head. If not, we calculate the newTailPosition = length - offset if k > 0 else offset. Then its time to grab
a reference to the new tail using a for loop. We initialize the newTail variable at the head and loop from 1 to the newTailPosition and
when this for loop terminates the newTail variable will be pointing to the new tail node. We grab a reference to the newHead ie
newHead = newTail.next. Then we update the original tail's next pointer to point to the original head, we set the next pointer of the
newTail to None and we return the newHead."""


class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

#O(n) time | O(1) space
def shiftedLinkedList(head,k):
    #iterate the length of the linked list to grab tail and calculate length
    listLength = 1
    listTail = head
    while listTail.next is not None: #loop to grab current tail and calculate list length
        listTail = listTail.next
        listLength += 1
    
    offset = abs(k) % listLength  #offset from head or tail for position of new tail

    if offset == 0: #if offset is 0 then we do nothing and re
        return head #return the input head

    #otherwise if offset is not zero, then we need access to the new tail
    newTailPosition = listLength - offset if k > 0 else offset #calculate new tail position
    newTail = head  #then use a loop to grab the new tail, starting from the input head
    for i in range(1,newTailPosition):#we use a for loop because we know where we stopping
        newTail = newTail.next
    
    newHead = newTail.next #grab a reference to the new head

    #with the four important nodes grabbed, we do the four required operations in correct order
    newTail.next = None #set the next pointer to None since we already grabbed newHead
    listTail.next = head #set
    return newHead #return new head of shifted linked list



