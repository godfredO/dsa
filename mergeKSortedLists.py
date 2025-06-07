"""You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists 
into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 

Constraints:
k == lists.length ; 0 <= k <= 104 ; 0 <= lists[i].length <= 500 ; -104 <= lists[i][j] <= 104 ; lists[i] is sorted in ascending 
order. The sum of lists[i].length will not exceed 104.



So this question is an extension of mergeTwoSortedLists.py and is also the linked list version of mergeSortedArrays.py. In 
mergeSortedArrays.py, we stored the current value of each array inside a minHeap (along with the array identifier), chose the
minimum value, added to our output list, and advance the current pointer by adding the next value in that array to the minHeap.
How do we adapt this to a merging k sorted linked lists. Well we use the same idea. The tricky part comes from implementating
the solution using Python's heapq module for the minHeap. Basically, when given a tuple of values, heapq will compare the first
values and if there is a tie, it compares the second values and so on. However heapq can only compare numbers, no node objects.
The way we go about this is to store current values, list index, current node in linked list, for each of the individual linked
list in the minHeap. Since the linked list index is unique, if two linked lists have the same current node value, the one with
the lower index will be chosen. This way, heapq will never have to compare the current node object we store. Also, we create
a dummy node which we use to build the merged linked list.

How do we initialize the minHeap? We go through the list of linked list, generate indices, and if the head node is not None
we add, the head node value, the list index and the head node. We also update the node at that list index to the head's next
node, so that at every moment, the list of linked lists, stores at each index, the next node to be compared for the linked list
at that index. With the minHeap initialized, we declare the current node in the merged linked list to equal the dummy node we
created. Then while the linked list is non-empty, we pop, the current minimum, which will be in the form, value (for the minimum
comparison), the list index (for settling ties and access the next node object for that linked list), and the current node for
that linked list, which we set as the next node of the current node in the merged linked list. Then we update the current node
for the merged list as the next node, which we just added. Then with the list index, we check if the next node in that linked
list is non-None. If so, we append the value, list index, and that node, before updating the next node for that linked list to
be the next of the node object whose value we just added to the minHeap. At the end we know that the head of the merged linked
list will be the next node of the dummy node we created, since that was our first current node, so we return dummy.next.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import heapq
def mergeKLists(lists):
    dummy = ListNode(0)
    currentHeads = []
    minHeap = []
    for i, head in enumerate(lists): #lists is a list of head nodes
        if head:
            heapq.heappush(minHeap,(head.val, i, head))
            lists[i] = lists[i].next
        
        heapq.heapify(minHeap)
        cur = dummy
        while minHeap:
            _ , i, node = heapq.heappop(minHeap)  #value, list index, node object
            cur.next = node
            cur = cur.next
            if lists[i]:
                heapq.heappush(minHeap,(lists[i].val, i,lists[i]))
                lists[i] = lists[i].next
        return dummy.next