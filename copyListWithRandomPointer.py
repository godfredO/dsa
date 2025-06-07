"""A linked list of length n is given such that each node contains an additional random pointer, which could point to any 
node in the list, or null. Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of 
the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list 
represent the same list state. None of the pointers in the new list should point to nodes in the original list. For example, 
if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in 
the copied list, x.random --> y. Return the head of the copied linked list. The linked list is represented in the 
input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:
val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point 
to any node. Your code will only be given the head of the original linked list.

Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 
Constraints:
0 <= n <= 1000  ; -104 <= Node.val <= 104  ; Node.random is null or is pointing to some node in the linked list.


So this question reminds me of cloneGraph.py. Basically we have some sort of modified linked list where each node, in 
addition to the next attribute for iterating the linked list, has a random attribute which can point to another node in
the list or Null. In otherwords, the next pointer works just like a regular linked list; if we move down the next pointer
whenever we get to None, we know we have gone past the tail of the list. And we are being told to do a deep copy of the 
linked list, making sure to preserve node values, their next and random attribute values and order ie fully copy the list 
into another list. In otherwords, the main sticking point is in the copying of the random pointer. If the original node's
random attribute points to None, in the copy of the current node we can just set its random attribute to None. However,
if the random attribute points to another node, several steps down the linked list or even pointing to a node that comes 
earlier in the linked list, how would we ensure that we copy the linked list in such a way that we get the same node 
structure and order, since the random pointer isnt linear in nature like the next pointer. 

The solution is that we are going to use two passes, through the linked list. In the first pass, we create copies of the
original linked list nodes, and in addition, we create a hashmap that maps the original nodes to their copies, just like
the hashmap in cloneGraph.py . Then in the second pass, we actually connect the nodes, their next pointers and their
random pointers using the hashmap we created in the first pass. That is for any original node, we access its copy from 
the hashmap, and then update the next pointer of the copy to the hashmap value of the original's next pointer, and we 
update the random pointer of the copy to the hashmap value of the original's next pointer. Since the next pointer of the
linked list's tail points to None and some random pointers also point to None, we initialize our hashmap with a None key 
and a corresponding None value so that if a pointer goes to None, we can still use the hashmap as intended.  At the end
we return the mapped value of the head node which will be the head of the deep copy. 

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head):
    oldToCopy = {None:None}

    cur = head
    while cur:
        copy = Node(cur.val)
        oldToCopy[cur] = copy
        cur = cur.next
        

    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
        
    return oldToCopy[head]