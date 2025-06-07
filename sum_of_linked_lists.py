"""The question gives the head nodes to two linked lists of potentially unequal lengths. Each linked list represents a non-negative number,
where each node in the linked list is a digit of that integer but in reverse order. eg 8,125 will be 5->2->1->8. Thus the head node in 
each linked list is the least significant digit of that integer. The question asks to write a function that returns the head of a new linked
list that represents the sum of the integers and ordered in the same way from least significant to most significant digit of the sum.

So by reversing the order of the nodes, ie the least significant digit of integer is the head node, we know that we can add corresponding node
in the linked list, even though the lengths may be unequal. Specifically, we can add and carry over just we will do with actual integers from 
least significant to most significant. eg 17 + 19 is 7+9= 6 carry 1, then carry + 1+1 = 3, to give 36. Thus to start we add up the current 
carry plus the current node values if the current nodes are not None else we assume 0 (2 + 19, we assume 0 for first integer when adding 
carry 1 + 0 + 1), carry starts off as 0, addendOne starts as head of linkedListOne, addendTwo starts as linkedListTwo. Then with the sum, we 
get the value that goes into the node itself and the new carry using modulo of 10 and floor division by 10  respectively. With the modulo 
result we create a new LinkedList node. 

Now in order to return the create a linked list as we go, we initialize a dummy node, and this dummy node will be the starting point of our 
iteration ie currentNode. In otherwords, we create a node, and store two references to it, called dummy node and currentNode. The dummy node 
reference will always point to this node, the currentNode reference will be updated as we create the resulting linked list. So whenever we 
create a new node with the modulo result, we set the next attribute of currentNode to the new node and then advance the currentNode reference 
to point to the new Node. Also since the Node class has the next attribute pointing to None, upon instantiation, we don't have to worry about 
what the last node in the resulting linked list will point to. Then finally we advance addendOne and addendTwo using the next pointer if
they are not None otherwise we set them to None. The None value will be our indicator at the beginning of the algorithm to assume a value of
0 for the value of a particular addend due to the unequal lengths of the linked lists. Finally the while loop's is while addendOne is not
None or addedTwo is not None or carry is not 0, meaning if one of the addends is None and the other isn't the we still have additions with 
carry left. If both addend node's are None and carry is 0, we have finished our algorithm. At the end we return dummy.next because it will be 
pointing to the head node.
"""

#Input class
class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

#O(max(n,m)) time | O(max(n,m))
def sumOfLinkedLists(linkedListOne,linkedListTwo):
    dummyHead = LinkedList(0)  #dummy node whose next pointer will point to our actual head node
    currentNode = dummyHead   #initialize pointer as our dummy node
    carry = 0                 # initialize carry 

    nodeOne = linkedListOne  # linkedListOne head as pointer
    nodeTwo = linkedListTwo  # linkedListTwo head as pointer

    while nodeOne is not None or nodeTwo is not None or carry !=0: #if one node is not None or we have a carry value
        valueOne = nodeOne.value if nodeOne is not None else 0
        valueTwo = nodeOne.value if nodeTwo is not None else 0

        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10    #modulo yield the remainder which will be node value
        newNode = LinkedList(newValue)  #use our input class to create a node
        currentNode.next = newNode     #add newNode to output linkedlist
        currentNode = newNode         # advance pointer

        carry = sumOfValues // 10    # update carry variable

        nodeOne = nodeOne.next if nodeOne is not None else None   # advance addednd one
        nodeTwo = nodeTwo.next if nodeTwo is not None else None  # advance addend two

    return dummyHead.next
