"""Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:
Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the 
sorted list and inserts it there.
It repeats until no input elements remain.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:
The number of nodes in the list is in the range [1, 5000]. ;  -5000 <= Node.val <= 5000 ; 

This question is asking to apply insertion sort to sort a singly linked list. For insertion sort in an array, we
iterate forward, and for the value at each index, we iterate backwards, to insert the current value in the sorted
subarray, which starts with the first value. However for a singly linked list, we don't have a prev atrribute, just 
a next attribute, so we cant repeat the array step that iterates backwards. Instead, we need use the next attribute 
and a couple of pointers to sort the linked list. 

First off, since we may have a new head node after sorting, we use a dummy node such that dummy.next always points
to the head. So like the array version of insertion sort, we start off saying that the subarray containing the first 
node only is sorted, so we will make that first node the next of the prev node (prev starts from the dummy) and we
advance the current node pointer to the head node's next pointer. But before we do this, we move the prev pointer
until we are at the insertion point of the current node. We say that if prev.next is not None and prev.next is less
than or equal to the current node's value we advance prev pointer to prev.next. This is because to insert the current
node, we insert it between prev node, and prev.next. This means by the time we break out of of this inner while loop, 
prev.next will be greater than the current node. So we store a temporary pointer to current.next. Then we insert the
current node as follows: tmp = current.next; current.next = prev.next; prev.next.next = tmp; prev.next = current ; 
then we update prev node ie prev =  prev.next; current = tmp. In otherwords, we have a prev node, and a current node,
but we compare prev.next to see if we need to insert current node between prev and prev.next, but we before we do that
we advance / update prev pointer until prev is pointing at the insertion point of the current node and we do that by
advancing prev if prev.next exists and prev.next is less than or equal to the current node's value. So instead of
iterating backwards to find the insertion point, we use the prev node to iterate forward to find the insertion point. 

Now we know that in the worst case, insertion sort is O(n^2) because for an input in descending order, then for each
array element we need to iterate backwards all the way to front of the array, however in an array sorted in ascending
order, we will never have to iterate backwards, giving insertion sort a best case complexity of O(n). Here, since we 
don't always know where the current node is going to be inserted, we re-instantiate the prev node at the dummy node 
for each current node and iterate until we find the insertion point of the current node. In othewords, unlike the 
array version of insertion sort where we compare the current node to the end of the sorted subarray and keep going
back until we find the insertion point, here we start from the start of the sorted sublist and keep going until we
find the insertion point. This means for each node, we potentially have to move the prev pointer to find the 
appropriate insertion point leading to a O(n^2) time complexity. In otherwords, we have a while loop that updates 
the prev pointer, and after inserting current node, we update the current pointer. In some ways you can say this is
a variation of the 3 pointer method since we need a prev and current pointer, but we also need to declare a temporary
reference to current.next, which will be our next current node before we insert current node between prev and prev.next
which happens by comparing the values of prev.next (if it exists) and current node. The main thing to note about this
question is that prev pointer is always declared starting from the dummy node unlike other 3 pointer methods where
we initialize prev pointer once and continue from where we last left prev pointer. 

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortList(head):
    dummy = ListNode(0)
        
    current = head

    while current:
        prev = dummy

        while prev.next and prev.next.val <= current.val:
            prev = prev.next
            
        tmp = current.next
        current.next = prev.next
        prev.next = current

        current = tmp
    return dummy.next