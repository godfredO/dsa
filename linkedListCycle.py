"""Given head, the head of a linked list, determine if the linked list has a cycle in it, and return a boolean. There is a cycle in the linked 
list if there is some node in the list that can be reached again by continously following the next pointer. 

This question is sort of the foundational question for the findLoop.py linked list question. The first idea is that we can traverse the linked
list with a while loop and if there is a cycle or loop, we will eventually get back to a node we already traversed. So how do we know we have
seen a node before? We use a single pointer to traverse the linked list and while currentNode is not None, we go to currentNode.next, but 
before we check if currentNode is in the hashset if its not, we add it to it and advance the pointer. If currentNode is in the hashset we
return True. If currentNode becomes None, the while loop terminates and we return False. So this is inoptimal space complexity of O(n) and a
optimal time complexity of O(n). Clearly we will have to traverse the loop somehow, so we will not be able to improve on the time complexity.
But how can we improve the space complexity? Do we need to store a hashset of all the nodes? No we can repurpose the findLoop.py solution.

So in findLoop.py, we use two pointers, fast and slow and move them at 1x and 2x speed respectively until they meet, then we move slow to the
head node node and then advance both pointers at 1x speed each to find the start of the loop. In this question we dont need to return the 
start of the loop, we only need to return True if a loop exists and False otherwise. So we will use the fast and slow pointers and if they
meet, we know we have a loop, if however fast ends up at None, we know we dont have a loop. So the main complication is handling edge cases
and making sure the code can handle a loop and a non-loop linked list. So the first edge case is that if head is None or head.next is None we
have an empty linked list or a single node linked list so we return False, no loop. This also means we have at least 2 nodes in the linked list
at this point, so we advance slow= head.next and fast = head.next.next. Then the while loop condition is to break if fast ever meets second
or if fast is ever None. So we advance slow = slow.next but in case we are dealing with a non-loop then when we get to tail node 
fast= fast.next.next will throw an error because we would be calling next on None value. So we check if fast.next is not None, we advance fast
otherwise we know we dont have a loop so we return True. If fast.next is None, ie non loop it also means the linked list is odd-length. So when 
the loop terminates we need to check which condition terminated it. So if fast == slow, return True for a loop, but if fast == None ie for an
even-length linked list, then we return False. This application of the fast/slow findLoop algorithm ensures O(1) space.

Now even though this more verbose explanation and the attendant code works, there is a cleaner solution. This solution just changes the order
of things. We initialize both fast and slow at the head node. Then the while loop condition is while fast node is not None and fast.next node
is not None ie for even-length and odd-length linked list as well as for an empty linked list and a single node linked list. Then we advance
slow = slow.next and advance fast = fast.next.next. Then we check if they are equal. If they are, we return True. Otherwise outside the loop,
we return False. Cleaner and better. Comparing the two optimal solution it is clear that we only ever return False when node is None or 
node.next is None so why not cleverly combine it all. The reason is that if there is a loop, neither the fast nor slow pointer will ever 
hit a None node, instead they will equal each other at the tip of the cycle. If there is no loop, then the fast pointer will hit None if 
the linked list length is or the tail node ie fast.next is None. If we break because of either situation, we dont have a cycle. So after
advancing the pointers, we check for equality and the monment they are equal we found our cycle, otherwise if we break out of the fast/slow
pointer while loop conditions (even/odd) we know there is no cyle so we return False. In otherwise if you compare this solution to 
middleOfTheLinkedList.py the only additons are the check for pointer equality which yields True and or False if we break out of the loop.
In otherwords, this is another application of the fast/slow pointer linked list technique.
"""



#O(n) time | O(n) space
def hasCycle(head) -> bool:
        hashset = set()
        currentNode = head
        
        while currentNode is not None:
            if currentNode in hashset:
                return True
            hashset.add(currentNode)
            currentNode = currentNode.next
        return False


#O(n) time | O(1) space
def hasCycle(head):
        if head is None or head.next is None:
            return False
        
       
        first = head.next
        second = head.next.next
        
        while first != second and second is not None:
            first = first.next
            if second.next is None:
                return False
            else:
                second = second.next.next
            
        if second is None:
            return False
        else:
            return True


def hasCycle(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


def hasCycle(head):
    fast = head
    slow = head
    if not fast or not fast.next: #edge case None node or single node linked list
        return False
        
    fast = fast.next.next   #can advance since we checked for single node linked list
    slow  = slow.next       #need to advance before while loop

    while fast != slow and fast is not None and fast.next is not None: #add True and False conditions
        fast = fast.next.next
        slow = slow.next
        
    if fast is None or fast.next is None:   #False conditions
        return False
    return True                             #otherwise True conditions fast == slow