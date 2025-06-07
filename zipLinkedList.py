class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

"""The solutuion to this problem is the sum of three basic steps; split the linked list, reverse the second half and
interweave the first half and the reversed second half. When the linked list is split using the slow and fast pointer
technique, the slow pointer actually lands on the node that will be the tail node of the interwoven linked list. So
to simplify the code we set the head of the second half to be the next node after the slow pointer and set the next
attribute of the slow pointer node to None since we know it will be final tail node. Also when it comes to splitting
linked lists using the two pointer system, for odd-length linked lists we move both pointer, slow at 1x speed, fast
at 2x speed, until fast pointer is on the last node where the next attribute will be pointing to None. For even-length
linked lists, we move both pointers at their respective speeds until the fast pointer goes out of bounde ie None node"""
#O(n) time | O(1) space
def zipLinkedList(linkedList):
    if linkedList.next is None  : #if the linked list head node is the only node in the linked list ie length = 1
        return linkedList #return do nothing, zipped as is

    firstHalfHead = linkedList  #head of first half is the head of the original linked list
    secondHalfHead = splitLinkedList(linkedList) #split the linked list and return the head of second half

    reversedSecondHalfHead = reverseLinkedList(secondHalfHead) #reverse the second half of linked list

    return interweaveLinkedLists(firstHalfHead,reversedSecondHalfHead) #interweave the split linked lists

def splitLinkedList(linkedList):
    slowIterator = linkedList
    fastIterator = linkedList
    while fastIterator is not None and fastIterator.next is not None: #even-length and odd-length loop conditions
        slowIterator = slowIterator.next
        fastIterator = fastIterator.next.next
    secondHalfHead = slowIterator.next #store the secondHalfHead before the next attribute of slow is overwritten
    slowIterator.next = None #overwrite the next pointer since this will be the tail after interweaving step
    return secondHalfHead #return the head of the second half of linked list for reversing step

def reverseLinkedList(linkedList):
    previousNode, currentNode = None, linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode

def interweaveLinkedLists(linkedList1,linkedList2):
    linkedList1Iterator = linkedList1  #pointer for list 1, initialize at head of list 1
    linkedList2Iterator = linkedList2  #pointer node for list 2, initialize at head of list 2
    while linkedList2Iterator is not None: #we know second list is going to be shorter thus tied to implementation
        linkedList1IteratorNext = linkedList1Iterator.next #store references to next node in split linked list
        linkedList2IteratorNext = linkedList2Iterator.next #store references to next node in reversed split linked list

        linkedList1Iterator.next = linkedList2Iterator #link current node in list 1 to current node in list 2
        linkedList2Iterator.next = linkedList1IteratorNext #link current node in list 2 to next node in lis 1

        linkedList1Iterator = linkedList1IteratorNext  #update pointer to next node in list 1
        linkedList2Iterator = linkedList2IteratorNext  #update pointer to next node in list 2
    return linkedList1 #return head node

