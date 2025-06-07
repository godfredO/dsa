"""This algorithm is that the question can be subdivided into three parts. Linking up nodes with values less than k, linking 
up nodes with values equal to k, and linking up nodes with values greater than k. Since all three sub-linked lists are 
constructed at the same time the relative ordering of nodes is maintained and while iterate we store variables to the head 
and tails of each of the sub-linked list so that at the end of the iteration we can link the sub-linked lists together and 
return the head of the new linked list"""

class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None
#O(n) time | O(1) space
def rearrangeLinkedList(head,k): 
    smallerListHead = None    #initialize at None in case some of the sub-lists don't have nodes eg if no nodes.value < k
    smallerListTail = None
    equalListHead = None      #initialize at None in case some of the sub-lists don't have nodes eg if no nodes.value = k
    equalListTail = None
    greaterListHead = None    #initialize at None in case some of the sub-lists don't have nodes eg if no nodes.value > k
    greaterListTail = None

    node = head     #current node for iterating through the linked list, initialize at head node
    while node is not None:     #iterate to the end of the linked list, where the tail points to None
        if node.value < k:      #if current node belongs in the smaller than k sub-list
            smallerListHead,smallerListTail = growLinkedList(smallerListHead,smallerListTail,node) #update smaller sub-list             
        elif node.value > k:    #if current node belongs in the greater than k sub-list
            greaterListHead,greaterListTail = growLinkedList(greaterListHead,greaterListTail,node) #update greater sub-list               
        else:                   #if current node belongs in the equal to k sub-list
            equalListHead,equalListTail = growLinkedList(equalListHead,equalListTail,node) #update equal sub-list     

        prevNode = node         #prevNode to access current node which will be new previous node, when iterator advances
        node = node.next        #advance to next node in linked list, thus new current node
        prevNode.next = None    #overwrite next pointer of prevNode, which is now in a sublist and could be a tail node

    #link smaller,equal sub-lists and return the head and tail since possible no node.value < k and smallerHead = None
    firstHead,firstTail = connectLinkedLists(smallerListHead,smallerListTail,equalListHead,equalListTail)
    #connect the resulting list from above (smaller,equal) to greater sub-list, only finalHead is needed after
    finalHead,_ = connectLinkedLists(firstHead,firstTail,greaterListHead,greaterListTail)
    return finalHead #return finalHead resulting from connecting all three sub-list

def growLinkedList(currentHead,currentTail,currentNode): #helper method to update sub-lists and return their head and tail
    #the passed node will always be the newTail so we only need to update the prev tail's next to point to it
    #by setting newHead to passed head we correctly update newHead once, the first time. 
    #thus we only update newHead once, always current tail's next pointer to point to passed node, which is always new tail
    newHead = currentHead  #initialize newHead to the passed head, head changes from None to final head and that's it
    newTail = currentNode  #initialize newTail to the passed node and not the passed tail, thus newTail won't be None
    
    if newHead is None: #the only time we update to the final head node of sub-list is when the passed head is None 
        newHead = currentNode  #this update is done only once when newHead= head=None. afterwards newHead != None
    
    if currentTail is not None: #on first call tail will be passed as None and then updated to node when newTail=node
        currentTail.next = currentNode #thus second time tail will be prevNode in sublist and we just update the next pointer
    return (newHead,newTail) #return a tuple or list of newHead and newTail, which was updated in first two lines

def connectLinkedLists(headOne,tailOne,headTwo,tailTwo):
    #to connect in general, make tailOne point to headOne but also checking if any of the passed is None ie empty sub-lists
    #and in general, we expect headOne to be new joint head and tailTwo to be new joint tail except if either is None
    newHead = headTwo if headOne is None else headOne #if headOne is None, then tailOne is None and headTwo is new Head
    newTail = tailOne if tailTwo is None else tailTwo #if tailTwo is None, then headOne is None and tailOne is new Head

    if tailOne is not None: #check that tailOne is not None before having next point to headTwo ie connecting tail to head
        tailOne.next = headTwo #actual connect step
    return (newHead,newTail)