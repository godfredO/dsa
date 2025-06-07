"""The question asks to write a function that takes in the head of a single linked list that contains a loop (in other words, the list's
tail node points to some node in the list instead of None/Null. The function should return the actual node object fom which the loop 
origniates in constant space.

So the intuition behind this is not the simplest to explain even though its simpler to demonstrate. Lets say the linked list is 
1->2->3->4->5->3. Meaning the origin of the loop is 3 and nodes 3,4,5 are in the loop and the nodes 1,2 are not in the loop.
To find the origin of the loop, we first realize that there is some node in the loop that has a 'loop distance' equal to the distance 
from the head of the linked list to the origin of the loop. In the example here, the head of the loop, node 1, is a distance of 2 from the 
origin of the loop, node 3, distance being the number of 'edges' we traverse or jumps we make to get from node 1 to node 3. Node 3 has a 
'loop distance' of 0 from itself meaning from node 3 we take 0 jumps to get to itself (the origin of the loop). Node 4 is 2 jumps away from
the origin of the loop ie we would hop from 4 to 5 and from 5 to 3. Node 5 is a loop distance of 1 from the origin of the loop. So in this
solution, finding the origin of the loop lies in finding node 4, storing a pointer to it and the from there taking exactly 2 jumps to the
origin of the loop where 2 is the distance between the head of the linked list and the origin of the loop.

The technique used involves using two pointers moving at different rates. The first pointer jumps one node at a time, or 1x rate. The 
second pointer jumps two nodes at a time ie 2x rate. So first = first.next, second = second.next.next. So we advance these pointers 
until they meet. And where will they meet? They will meet at the node in the loop that has a 'loop' distance equal to the distance from
the head to the origin of the loop.  So first moves 1 -> 2 -> 3 -> 4 and second moves 1 -> 3 -> 5 -> 4. So after four single jumps from
the first pointer and four double jumps from second pointer, they meet. So we keep moving both pointers at their respective rates until
they meet and when they do, we move the first pointer back to the head of the linked list, leaving the second pointer on node 4. Then we
advance both pointers until they meet again, and since they are both a distance of 2 from the head of the loop, they will meet when they
both are at node 3 after first and second pointer take exactly 2 jumps each. So that's the algorithm, in the code we use two while loops.
The first while loop moves the two pointers at 1x speed and 2x speed until they meet, then we move the first pointer back to the head,
and use the while loop to move both pointers at 1x speed until they meet. When they meet, we return either pointer's current node.
The only quirk about the code is that, since the loop condition of the first while loop is to run until they point to the same node if 
we initialize both pointers at the head, the first while loop won't run at all. The way to go around that is to advance both pointers
one time by their respective rates before starting the first while loop. That way they point to different nodes at the start of the first
while loop and only cross paths when they both point to the node in the loop whose base distance equals the head to loop origin distance.
And we are able to do this because we are assured that the input linked list contains a cycle, hence we will never hit a None while
moving either pointers, and a such we now first.next and second.next.next will never be None. Contrast this with middleOfTheLinkedList.py
and linkedListCycle.py where we use the fast/slow pointer technique but have to handle the possibility (or certainity) of no loop existing.


So this solution works irrespective of the number of nodes in the loop or the number of nodes from the head of the linked list to the
origin of the loop. In the example, 1 -> 2 -> 3 -> 4 -> 5, there are 3 nodes in the loop so we can say that node 3 has a 'base loop
distance' of 0, 0+3, 0+3+3 etc. That is if we start from node 3 and take 3 jumps, we get back to node3, or 6 jumps ie 'base loop
distance' + numberOfNodesInLoop. Similarly node 4 has a 'base loop distance' of 2 but a general loop distance of 2 + 3= 5, 5+ 3 = 8
etc. Similarly node 5 with a 'base loop distance' of 1 has general loop distance of 1,4,7,10 etc.
That is since a loop will at least contain one node (eg 1 - > 2 -> 3 -> 3), there will always be some node in the loop whose
loop distance, either base or general, is equal to the distance from the head of the linked list to the loop origin. 

If D is the distance from head node to loop origin,
P is distance betwen the loop origin and the node in the loop whose loop distance equals D
R is the distance between the node in the loop whose loop distance equals D

The purpose of this section is to show that the technique of initially moving pointers at 1x and 2x speeds works
When the nodes meet first pointer has travelled D+P, second pointer has travelled T+P where T= total number of nodes or distance
T = D + P + R
So first = D + P, second = D + P + R + P
Since we know that  second moves at 2x, and first at 1x, the we know that if first = D+P, then second must be 2D + 2P
second = 2D + 2P = D + P + R + P
         2D + 2P - D - P - P = R
                           D = R
"""


class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None
        
#O(n) time | O(1) space
def findLoop(head):
    first = head.next #skip the head node, first moves 1 node at a time
    second = head.next.next #skip the head node, second moves two nodes at a time
    
    while first != second: #move first and second pointer till they overlap
        first = first.next #move first pointer one node at a time
        second = second.next.next #move second pointer two nodes at a time
    
    first = head  #once both pointers overlap, reset the first to the head

    while first!=second:
        first = first.next #now move both pointers one node at a time
        second = second.next #till they overlap again, now at the head of the loop
    
    return first

