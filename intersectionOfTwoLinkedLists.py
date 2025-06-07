"""Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two 
linked lists have no intersection at all, return null.
For example, the following two linked lists begin to intersect at node c1:
a1->a2->c1->c2->c3 ; b1->b2->b3->c1->c2->c3

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. 
If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:
4->1->8->4->5 ; 5->6->1->8->4->5
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected 
node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are 
different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B 
(3rd node in A and 4th node in B) point to the same location in memory.

Example 2:
1->9->1->2->4 ; 3->2->4
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node 
in A; There are 1 node before the intersected node in B.

Example 3:
2->6->4 ; 1->5
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, 
intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.



The solution to this rather complex looking problem is rather simple, clever and clean. So we know that the total length of the
linked list is fixed, whether the individual linked list lengths are equal or different. So if one list is length 4 and the other
is length 3 the total length is fixed at 7. If one list is 4 and the other is length 4 the total length is fixed at 8. So we use
a two pointer method, to traverse all nodes. The first pointer will start on headA, the second pointer will start on headB. Both
pointers will traverse both linked lists. So we advance first pointer down linked list A and get to the None value after the tail,
we move it to the head of linked list B, and the same is done for the second pointer. This means that if the two linked lists dont
intersect, after traversing both linked lists, both pointers will point to None. The interesting thing is that if the two linked
lists infact do intersect, then they will meet at the point of intersection. Meaning the while loop condition is while first !=
second. At the end we return either first or second which will either be None or the point of intersection.
"""


def getIntersectionNode(headA, headB):
    first = headA
    second = headB

    while first != second:
        if first is not None:
            first = first.next
        else:
            first = headB
            
        if second is not None:
            second = second.next
        else:
            second = headA
            
    return second


def getIntersectionNode(headA, headB):
    l1,l2 = headA, headB
    while l1 != l2:
        l1 = l1.next if l1 else headB
        l2 = l2.next if l2 else headA
    return l1