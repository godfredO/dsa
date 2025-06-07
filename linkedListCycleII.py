"""Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null. There is 
a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next 
pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
It is -1 if there is no cycle. Note that pos is not passed as a parameter. Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

So this question is essentially the same as algoexpert's findLoop.py, only difference here is that we are not assured that
the input linked list contains a loop. Hence if the input linked list does not contain a loop, we are to return None, 
otherwise, we are to return the origin of the loop. So we still apply the fast/slow pointer technique, read findLoop.py to
understand. However to handle the possibility that there is no loop, we first have to check if fast is None or fast.next
is None, before we first advance our pointers before the first while loop. Then in the first while loop, we add to the loop
condition, while fast != second and fast is not None and fast.next is not None. To understand the reason for the additions,
read middleOfTheLinkedList.py of linkedListCycle.py. So we may break out of the first while loop because there is a loop,
ie if fast == slow and we found the node in the loop whose cycle distance equals the head nod's distance to the loop origin;
or we may break out of the loop because there is no loop and fast is None (even length) or fast.next is None (odd length).
So we first check if we broke out of the loop because there is no loop, if so we return None. Otherwise, we move slow to 
the head node and now advance both slow and fast at 1x speed until they meet at the origin of the loop. So you can say that
this quesion is basically findLoop.py mised with linkedListCycle.py.
"""

def detectCycle(head) :
    slow = head
    fast  = head
        
    if fast is None or fast.next is  None:
        return None

    slow = head.next
    fast = head.next.next

    while slow != fast and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    if fast is None or fast.next is  None:
        return None

    slow = head                     #move slow to head before moving
    while slow != fast:
        slow = slow.next
        fast  = fast.next
        
    return slow