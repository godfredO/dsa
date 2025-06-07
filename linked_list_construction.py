"""This question asks to write a construction method for a doubly linked list which is a linked list with a head and a tail and each node
has a prev and a next attribute pointing to another node or None/null. The methods are setHead(), setTail(), insertBefore(), insertAfter(),
insertAtPosition(), remove(), removeNodesWithValue(), containsNodeWithValue(). If we are smart about how we implement these methods, we
can re-use some methods to  implement other methods. All of these methods take in a node object as an input parameter, insertAtPosition(),
containsNodeWithValue() and removeNodesWithValue() also take an integer representing position or value. insertBefore() and insertAfter()
take two node objects, the insert Node, and the before/After Node.

The order of implementation based on simplicity and reusablilty is, containsNodeWithValue(), removeNodeBindings() a helper method, remove(),
removeNodesWithValue(), insertBefore(), insertAfter(), setHead(), setTail(), insertAtPosition(). If we start from the head, we iterate using
the next attribute; if we start from the tail we iterate using the prev attribute. The head node's prev attribute should always point to 
None; a tail node's next attribute should always point to None.  The DoublyLinkedList class always stores references to the current head and 
tail. Finally, A collapsed binary tree yields a doubly linked list. 
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # O(1) time | O(1) space
    def setHead(self,node):
        if self.head is None: #if this is a new doubly linked list, head and tail will be None
            self.head = node #so update head reference to node
            self.tail = node #and update tail reference to node
            return #return because that's finished
        
        self.insertBefore(self.head,node) #otherwise if there is an existing head node, just insert node before the current head
        
    # O(1) time | O(1) space
    def setTail(self,node):
        if self.tail is None: #if this is a new doubly linked list, head and tail will be None
            self.setHead(node) #so update head reference to node and update tail reference to node, same as in setHead()
            return #the return, operation is concluded

        self.insertAfter(self.tail,node) #otherwise if there is an existing tail node, insert after current tail
            
    # O(1) time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail: #edge case of one-node list where nodeToInsert is head and tail
            return #in this case just return, nodeToInsert is head and tail

        self.remove(nodeToInsert) #if not edge case, we will remove nodeToInsert from its current position and re-insert it before  node
        #so now we removed nodeToInsert updated it and its previous neighbor's bindings, now set it before node
        nodeToInsert.prev = node.prev #set nodeToInsert before node by updating its prev pointer to node's prev
        nodeToInsert.next = node      #set nodeToInsert's next pointer to node

        if node.prev is None: #edge case, if node's prev is None then node is the head, so nodeToInsert is the new head
            self.head = nodeToInsert #if true that node is head, set nodeToInsert as doubly linked list head, update class head reference
        else: #othewise if node.prev is another node then node.prev's next attribute should now point to nodeToInsert
            node.prev.next = nodeToInsert #update node.prev.next to be nodeToInsert
        
        node.prev = nodeToInsert #finally, update node's prev pointer to nodeToInsert

    # O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert): #this method is similar to insertBefore()
        if nodeToInsert == self.head and nodeToInsert == self.tail: #edge case of one-node list where nodeToInsert is head and tail
            return #in this case just return, nodeToInsert is head and tail, and we cant lose these references


        self.remove(nodeToInsert) #if not edge case, we will remove nodeToInsert from its current position and re-insert it after node
        #so now we removed nodeToInsert updated it and its previous neighbor's bindings, now set it after node
        nodeToInsert.prev = node #set nodeToInsert after node by updating its prev pointer to node
        nodeToInsert.next = node.next #set nodeToInsert's next pointer to node's next

        if node.next is None: #edge case, if node's next is None then node is the tail, so nodeToInsert is the new tail
            self.tail = nodeToInsert #if true that node is head, set nodeToInsert as doubly linked list head, update class tail reference
        else: #othewise if node.next is another node then node.next's prev attribute should now point to nodeToInsert
            node.next.prev = nodeToInsert   #update node.next.prev to be nodeToInsert

        node.next = nodeToInsert #finally, update node's next pointer to nodeToInsert

    # O(p) time | O(1) space #the time complexity depends on position since we have to find the position first
    def insertAtPostion(self, position, nodeToInsert): #we have to find the position first
        if position == 1: #if position is 1, 
            self.setHead(nodeToInsert) #just call setHead on node 
            return #then return

        node = self.head  #for all other positions, we have to find the position first, so initialize pointer at head
        currentPosition = 1 #position of head is 1, this is one method we should always start from head since we know its position

        while node is not None and currentPosition != position: #not at position or either end of doubly linked list
            node = node.next #advance node using next 
            currentPosition += 1 #increment postion 
        
        if node is not None: #if we didnt break out of while loop due to None condition,
            self.insertBefore(node,nodeToInsert) #insert nodeToInsert before current node at position
        else: #if we broke out of while loop due to None condition,
            self.setTail(nodeToInsert) #then set nodeToInsert as tail

    # O(n) time | O(1) space
    def removeNodesWithValue(self, value): #to remove nodes with value, find and remove 1st node with value, then second etc
        node = self.head #to find start iterating from head node and use next attribute or tail node and use prev attribute
        while node is not None: #while we are not at either end of the linked list, keep finding new nodes with value
            nodeToRemove = node #store additional reference to current node before updating current node reference
            node = node.next   #update current node reference to the next node, using next since we started from head
            if nodeToRemove.value == value: #check node's value if equal to value ie found node with value
                self.remove(nodeToRemove)  #call remove method on node with value,

    # O(1) time | O(1) space
    def remove(self, node):
        if (node == self.head): #edge case if node is head of doubly linked list
            self.head = self.head.next #then make its next node the new head, new head's prev will point to None in removeBindings()
        if (node == self.tail): #edge case if node is tail of doubly linked list
            self.tail = self.tail.prev #then make its prev node the new tail, new tail's next will point to None in removeBindings()
        self.removeNodeBindings(node) #after handling edge cases, remove node by removing its bindings, updating neighbor's bindings

    # O(n) time | O(1) space
    def containsNodeWithValue(self,value):
        node = self.head #start iterating from head node reference in DoublyLinkedList class. We can also use tail
        while node is not None and node.value != value: #if we are not at end or current node doesnt have the value
            node = node.next #go to the next, since we started from head. If tail is used go to prev.
        
        return node is not None #while loop breaks if we find value or None. so return if node is not None
    
    def removeNodeBindings(self,node): #updating a node's neighbors attributes to remove node's bindings
        if node.prev is not None:  #first update the prev neighbor's next attribute
            node.prev.next = node.next #update prev neighbor's next attribute to node's next neighbor
        if node.next is not None:  #then update the next neighbor's prev attribute
            node.next.prev = node.prev #update the next neighbor's prev attribute to node's prev neighbor
        node.prev = None #Then remove node's bindings, set node's prev to None
        node.next = None #set node's next to None




