"""Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []
 
Constraints:
The number of nodes in the list is in the range [0, 5 * 104].  ; -105 <= Node.val <= 105


So this question is about applying sorting algorithms to a linked list. Particularly, we are going to use merge sort
recursively to sort the linked list, so first read mergeSort.py to understand the steps involved in merge sort. So
basically, merge sort, splits the array into two halves, and calls merge sort on either half until an array of size 
1 is obtained which is sorted as is, which is returned as the sorted halves, then the next step is to use pointers to 
merge the sorted halves into one sorted subarray, and the sorted subarray is returned. So split, call merge sort on
both halves, merge result of calling merge sort on both halves into one sorted (sub)array, return merged (sub)array. 

So how do we split a linked list. We cant just use indices like in mergeSort.py. Well we already have a question that
deals with just that. We find the middle node of the linked list, as done in the question middleOfTheLinkedList.py and 
this involves using a fast/slow pointer system. Since we need the middle node to split the list into two halves of 
roughly equal size, and then break the link between them. This means that if the list is of even-length eg 1->2->3->4, 
we want the middle node to be the greater of the two middle nodes ie node 3 in this case, and we want to break the link 
by setting the next of node 2 to None. Since this is a linked list, we can only do this by getting access to node 2, 
storing its next node ie node 3 as the middle node, before updating the next node of node 2 to None. In other to store
a reference to the 2 and not the 3, we need a slight modification on the algorithm in middleOfTheLinkedList.py, which
is set up to get the second of the two middle indices instead of the first. We achieve this by effectively not moving
the slow pointer on the first jump of the fast pointer. We can do this by initializing the slow pointer at null, and
the first time, we set it to head, while moving the fast pointer at its normal 2x speed. Then subsequently we move the
slow pointer 1x speed and the fast pointer 2x speed until the fast pointer or fast.next is None. I suppose we could
also use a dummy node, and initialize the slow pointer at that dummy node, while initializing the fast pointer at the
head node so that when we move the first time, we move the slow pointer to head while the fast pointer jumps 2x speed
from the head node, a techique used in removeNthNodeFromEnd.py. Another way used in the code below, is to initialize
slow at head node, and fast at head.next. Whichever technique you use, the aim is to get the first of two middle nodes.

With the two halves split, we call merge sort on the left half with head node and on the right half with mid node, and 
we keep doing this until we reach the base case of calling the main merge sort function with a None head node or a 
single node list in which head.next is None, and if that is the case, we return the head node as is. With the sorted 
halves obtained we use a merge function to merge the two halves. How do we do this?. This is mergeLinkedLists.py. We 
create a dummy node which will be our initial prev node, then if the current node value in the left half is less than 
the current node value in the right half, we set it as the next of the prev node, before advancing the prev node to the 
current left half node and advance the left half current node to is next node. Otherwise, the right half current node 
is the lesser value so it becomes prev's next, before advancing prev to the current right half node, and advancing the
current right half node to its next node. Since this while loop keeps going as long as both halves are non-None, when
we break, we check if either half's current node is non-None and if it is, we set it as the next node of prev. Then we
know that the dummy node's next node will be the head node of the merged lists, so we return dummy.next. When we get 
the merged lists head, we return that from the main merge sort function. 
    
There are log(n) calls of the sortList() before the base case is reached, at which point we merge which takes linear 
time. So the time complexity is O(nlog(n)) and the space complexity is O(log(n))
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head) :
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left,right)

    def getMid(self,head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge(self,left,right):
        dummy = ListNode(0)
        prev = dummy
        while left and right:
            if left.val < right.val:
                prev.next = left
                prev = left
                left = left.next
            else:
                prev.next = right
                prev = right
                right = right.next
        if left:
            prev.next = left
        elif right:
            prev.next = right
        return dummy.next