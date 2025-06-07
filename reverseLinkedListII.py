"""Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the 
list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:
The number of nodes in the list is n. ;  1 <= n <= 500  ;  -500 <= Node.val <= 500  ;  1 <= left <= right <= n


So the first thing to note about this question is what is meant by position. The head node is the 1st node, its next node 
is the 2nd node and so on. So we need to find the left-st node and the right-st node and reverse the sub-list between them
so at the end the node initially at the left-st becomes the right-st and the node initially at the right-st becomes the
left-st node, and the nodes in between are also reversed. Another way of saying this is that, the left-st node should point
to whatever node the right-st node originally pointed to, and whatever node originally pointed to the left-st node should
point to the right-st node and in addition, all nodes between the original left-st and right-st positions should be reversed.
So if given list head = [1,2,3,4,5], left = 2, right = 4, the 2nd node is node 2, the 4th node is node 4 and the sublist 
betweenm them is 2,3,4 and after reversing this sublist is 4,3,2; node 2 should now point to whatever node 4 previously 
pointed to ie node 5 ; and whatever node originally pointed to node 2 should now point to node 4 ie node 1 shoul point to 
node 4; this yields [1,4,3,2,5]. 

So the first thing is to grab references to the node before the left node and the left node itself. Suppose left is 1, then 
it means we have to grab a reference to the node before it, which obviously doesnt exist. So we use a dummy node, which 
points to the head. The we initialize the prev pointer at this dummy node, and the current pointer at the head node. Then we 
iterate a total of range(left - 1) times. If left is 1, then this is range(1-1) = range(0) which doesnt run at all so prev
will remain at the dummy node and current at the head node as this is the first node. Similarly if left is 3, range(left- 1)
is range(2) ie 0,1, hence we iterate two times, at which point prev points at the 2nd node and left points at the 3rd node.
Alternatively we could initialize a count at 0 then iterate and increment the count in a while loop until count equals left. 

Then its time to reverse the list between left and right, which is basically a reverseLinkedList.py. Since we have a reference 
to the left node, we initialize a prev node at None (treating left as the head of its sublist), and run reverseLinkedList.py
a total of range(right - left + 1) times, to reverse the sublist from left to right. That is if left is 2 and right is 4 then
we need to reverse three nodes ie 2nd,3rd,4th, and this can be done with range(4-2+1) = range(3) = 0,1,2. Alternatively we
could initialize a count at left -1 then iterate and increment count in a while loop until count equals right. One thing you
notice is that when this for loop terminates, current will be pointing to the node/None after the node intially at right, and
we know that the next pointer of the node initially at left should be pointing to this node. Since we saved a reference to
the node before the original left node we know that the original left node, is this node's next. So leftPrev.next.next = cur.
Also, after reversing the sublist, the new head of the reversed sublist will be at the prev node, and this is the node that
was originally at right. So after using leftPrev to access the original left and updating the original left's next pointer
to current, we can then overwrite leftPrev's next pointer to point to the head of the sublist prev. At the end we know that
the dummy node will always point to the new head of the linked list as a whole so we return that.






"""
#Definition for singly linked list
class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    dummy = ListNode(0,head)

    leftPrev, cur = dummy, head
    for _ in range(left-1):
        leftPrev = leftPrev.next
        cur = cur.next
        
    prev = None
    for _ in range(right - left + 1):
        tmpNext = cur.next
        cur.next = prev
        prev, cur = cur, tmpNext
        
    leftPrev.next.next = cur
    leftPrev.next = prev

    return dummy.next