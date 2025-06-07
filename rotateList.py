"""Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:
The number of nodes in the list is in the range [0, 500]. ; -100 <= Node.val <= 100 ; 0 <= k <= 2 * 109


So the question is actually the same as algoexpert's shiftedLinkedList.py.  One difference is that in the
algoexpert version, k could be negative, but in this leetcode version, we are assured in the constraints
that k is non-negative. So the first thing to realize is that the solution hinges on finding the new tail
of the rotated linked list. If k=2 for example, it will be the node before the kth node from the end. We 
also know that the kth node from the end will be the new head of the linked list and the original tail of
the linked list will point to the original head of the linked list. We also need to calculate the length
of the linked list in such a way that we stop at the original tail node so as to store a reference to the
tail node. Then with the length information, we can calculate the new tail position, and use that value
to iterate exactly new tail length to grab access to the node before the kth node from the end. Now here
we calculate this position exactly as length - k - 1 before iterating, although in shiftedLinkedList.py,
we used a range() function with new tail position as the end value and thus is excluded hence the -1. In 
otherwords, lets say length - k = 4. Then we can use range(4-1) = range(3) = 0,1,2 or range(1,4) = 1,2,3. 
Either way, we make exactly 3 jumps from the head of the linked list. The point to jump the correct number 
of times from the head node so that we land on the new tail of the rotated linked list. And realize that 
when calculating the length  we start from the head which is a length of 1. In the algoexpert solution we 
do the same when iterating to find the new tail position, look above. Once we have the new tail, we store 
a pointer to the new head ie newTail.next, set the new tail's next pointer to the None, and set the original 
tail's next pointer to the head node. Finally, to handle the case where k is bigger than the length of the 
linked list, we modulo divide the input k by the length to get the k we use in our code. Also if the input 
k equals the length of the linked list, we dont need to do any rotations, so we just return the original 
head. This is because if we do exactly length number of rotations, we will end up with the original linked 
list. Also if the input head is None, we just return it as is, to avoid trying to calculate the length.
"""
def rotateRight(head, k) :
    if not head:
        return head
        
    length , tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1
        
    k = k % length
    if not k:
        return head
        
    newTail = head
    for  _ in range(1,length - k):
        newTail = newTail.next
        
    newHead = newTail.next
    newTail.next = None
    tail.next = head
    return newHead