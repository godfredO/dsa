"""Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false
 

Constraints:
The number of nodes in the list is in the range [1, 105]. ; 0 <= Node.val <= 9 ;



This question is the same as the algoexpert linkedListPalindrome.py, I just want to save the leetcode name also. Basically the 
steps for determining if a palindrome is a linked list is an combination of middleOfTheLinkedList.py, reverseLinkedList.py with 
palindrome_check.py. We grab the middle node, reverse the list from the middle to the tail, and then starting from the reversed 
linked list portion and the head of the linked list, we compare values. If the values are not the same we know we dont have a 
palindrome so we return False. Otherwise, if the reversed portion becomes None (even/odd length), we return True. I just feel 
like not using helper functions so enjoy. So the first sublist starts from the head to the node before the middle node, the 
second sublist starts from the middle node to the end of the linked list. The reason I mention this is, just like the reverse 
step, the loop condition is while the second sublist is not None (in reverse step, while the second node, current is not None).
 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isPalindrome(head) :
    slow = head
    fast = head

    #grab middle of linked list
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
    prev = None
    current = slow

    #reverse middle to end of linked list
    while current is not None:
        forward = current.next

        current.next = prev
            
        prev = current
        current = forward
        
    first = head
    second = prev   #head of reversed portion 

    while second is not None:
        if first.val != second.val:
            return False
            
        first = first.next
        second = second.next
    return True