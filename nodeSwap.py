class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

"""Swapping two nodes consists of setting the first node's next attribute to the second node's next attribute and then setting 
the second node's next attribute to point to the first node. However when the next pair in the linked list is swapped, the tail 
of the previous pair is left pointing to the incorrect node instead of the new head of the current pair. To remedy this, the 
first solution uses recursion to swap two nodes and set the next point of the pair's new tail to the head node of swapping the 
next pair. Since that last part is only executed when the next recursive call returns, all node's will point to the correct next 
node. And since the recursive calls returns the new head of a swapped pair when the recursive calls return all the way to the 
original call, it also returns the new head of the linked list.In the iterative solution, three nodes are used; a previous node 
which starts at a temporary node which points to the head node; a first node and a second. Thus after swapping the first and 
second nodes (first.next = second.next, second.next=first), the previousNode node's incorrect pointer is corrected by setting 
previous.next = second. At the end we return tempNode.next as the new head of the linked list because we always keep a reference
to the temporary node. """
#O(n) time | O(n) space - recursive approach
def nodeSwap(head):
    if head is None or head.next is None: #if out of bounds (even-length) or no nodes to swap with (odd-length)
        return head #return the passed node 
    nextNode = head.next #referece to the node to swap passed node (head) with
    head.next = nodeSwap(head.next.next) #set next pointer of passed node (head) to the result of next recursive call
    nextNode.next = head #actual swap
    return nextNode #return the new head node of pair, head and head.next, after swap

"""Iterative approach of using three pointers"""
#O(n) time | O(1) space
def nodeSwap(head):
    tempNode = LinkedList(0) #create a temporary linked list node
    tempNode.next = head     #update the next attribute of temporary node to the head of linked list

    prevNode = tempNode #initialize previous node pointer to point to temporary node
    while prevNode.next is not None and prevNode.next.next is not None: #at least two nodes remaining, even,odd length conditions
        firstNode = prevNode.next          #initialize first swap pointer inside of loop
        secondNode = prevNode.next.next    #initialize second swap pointer inside of loop

        firstNode.next = secondNode.next  #first swap step
        secondNode.next = firstNode       #second swap step
        prevNode.next = secondNode        #fix incorrect pointer from previous pair's tail to current pair's head

        prevNode = firstNode              #advance previous node pointer

    return tempNode.next #temporary reference will be pointing to the new head node

