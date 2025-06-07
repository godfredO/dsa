""" The question is to write a function that takes in the heads of two singly linked lists that are in sorted order, respectively. The 
function should mutate the lists in place (ie it shouldnt create a brand new list) and return the head of the merged list; the merged
list should be in sorted order.

The first solution here, generalizes merge sort, that is we have pointers for each linked list, compare the values of the current list
one node and the current list two node, choose the minimum value and append to the last node in the running merged sorted list. In the
general case, if p1.value < p2.value, this would involve prev.next = p1, prev = p1, p1 = p1.next. However if p2.value <= p1 (the else
statement takes care of when the two values are equal), prev.next = p2, prev = p2, p2 = p2.next. In anycase we mutate the previous node's
next pointer to whichever linked list has a lower value, move prev to that node and then advance the linked list pointer for the next
lower number in the linked list to compare. In this version of the solution, when we compare the last nodes of both linked list, one
linked list pointer will move to the None after a tail node. If we choose the current p1 value as the lower valued node, then after
appending it to the previous node of the merged sorted list, we would advance prev to point to the last node in linked list one and then
we would advance p1 to None. Simlarly if the current p2 node is the lower valued node, we would append p2 to the end of the merged sorted
list, advance prev to point to the last node of the linked list two and then we would advance p2 to None. The point here is that if
p1 is None, the we need to connect the last node of list one to the current node of list two. Simlarly if p2 is  None, then we need to 
connect the last node of list two to the current node of list one. 



The second version of the solution, is a generalization of insertion sort. We recognize that both linked lists are already sorted so 
instead of thinking of the question as merging sorted linkied lists, we can instead rephrase it as inserting nodes from list two into
the sorted linked list one. We still use prev pointer here, but it is more appropriately called p1Prev because we are saying that at
all times list one is already sorted and we just need to find a node to insert between p1Prev and p1. So when we do the minimum , if
p1.value < p2.value, it means that p2.value will come after the current p1.value in the merged sorted list; hence we dont need to 
insert p2 into list one yet, we just advance p1Prev and p2 ie p1Prev = p1, p1 = p1.next. If however p2.value <= p1.value, then the 
current p2 value will come before the current p1 value in the sorted merged list, so we have to insert the current p2 value between
p1Prev and p1. So p1Prev.next = p2, p1Prev = p2, p2 = p2.next, p1Prev.next = p1. Inserting p2 between p1Prev and p1 involves updating
the next pointer of p1Prev to point to p2, moving p1Prev to p2, advancing p2 and then updating the next pointer of the current p1Prev,
which was p2, which completes the insert . In this way, we keep moving down list one if there is no need to insert the current p2 node.
As such suppose we needed to insert the last p2 node between p1Prev and p1, then after inserting it, the current p1 would be the tail
node anyway so there would be no edge cases to handle. However suppose the we dont need to insert the last p2 node between p1prev and 
p1, then when we advance p1Prev to point to the last node in list One, and then advance p1, p1 will be pointing to None, but we would
still need to add the last node in p2 to the list. Thus in this solutiion, we only check if p1 is None in which case we connect p1Prev
to the current p2 node to add it to the list. 

At the end of either method, we return headOne if headOne.value < headTwo.value else headTwo, since the head node of the merged linked
list is going to be the  lower valued head node of the two. Also in both solution, we have the option of initializing p1Prev or prev
with None or with a dummy node. If we use None, value we need to first check if prev or p1Prev is not None before attempting to update
its next pointer. If it is None, we essentially skip this step.
"""
class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None


"""  """

def mergeLinkedLists(headOne, headTwo):
    prev = None
    p1 = headOne
    p2 = headTwo
    
    
    while p1 is not None and p2 is not None:
      
        if p1.value < p2.value:
            if prev is not None:
                prev.next = p1
            prev = p1
            p1 = p1.next
        else:
            if prev is not None:
                prev.next = p2
            prev = p2
            p2 = p2.next

    if p1 is None:
        prev.next = p2

    if p2 is None:
        prev.next = p1

    return headOne if headOne.value < headTwo.value else headTwo



"""Iterative solution. If the first linked list current value, p1.value is less then we need to move forward in list one. 
To do this we move the prev pointer to point to the same node as p1 before settingp1 to refer to p1.next (leaving p1prev at previous p1). 
If the p1.value >= p2.value, we need to have the current p1 point to the current p2, have p2 point to the next node in list One and then move 
forward in list two. To do this we set p1Prev.next to be p2 (skip this step at the beginning when p1Prev is None), then set p1Prev to p2 
before advancing p2 ie p2 = p2.next. Finally set p1Prev.next to be p1, which would have been advanced previously """
#O(n+m) time | O(1) space 
def mergeLinkedLists(headOne,headTwo):
    p1 = headOne    #current node in first linked list
    p1Prev = None   #previous node in first linked list
    p2 = headTwo    #current node in two linked list

    while p1 is not None and p2 is not None:
        if p1.value < p2.value:  #in this case, there is nothing to mutate
            p1Prev = p1   #move p1Prev reference to p1
            p1 = p1.next  #move p1 reference to the next value
        else: #p1.value >= p2.value, we need to have p1 point to p2, p2 point to next node in list One, then advance p2
            if p1Prev is not None: # if not at start, p1Prev = p1 , otherwise skip this step
                p1Prev.next = p2   #so mutate a p1Prev pointer to point to p2
            p1Prev = p2  #move p1Prev reference to p2
            p2 = p2.next #move p2 reference to the next value
            p1Prev.next = p1 #mutate the p1Prev pointer to point to p1
    if p1 is None: #we run out of values in first linked list
        p1Prev.next = p2
    
    return headOne if headOne.value < headTwo.value else headTwo  #the head of the merged lists is the smaller value of headOne and headTwo

            
"""Recursive solution. This is the same logic as the iterative approach, except that we use auxilliary space in the form of frames on the
call stack"""
#O(n+m) time | O(n+m) space
def mergeLinkedLists(headOne,headTwo):
    recursiveMerge(headOne,headTwo,None)
    return headOne if headOne.value < headTwo.value else headTwo

def recursiveMerge(p1,p2,p1Prev):
    if p1 is None:
        p1Prev.next = p2
        return #we are done with recursive algorithm here
    
    if p2 is None: 
        return

    if p1.value < p2.value: #in this case we only need to advance p1 and p1Prev pointers
        recursiveMerge(p1.next,p2,p1) #so call recursive function with advanced values

    else:#in this case we need to have p1Prev point to p2, have p2 point to p1 then advance p2
        if p1Prev is not None:
            p1Prev.next = p2 #have p1Prev next pointer point to p2
        newP2 = p2.next #grab the next node in the second linked list, thus advancing p2 
        p2.next = p1    #then overwrite the next pointer of current p2 to have p2 point to p1
        recursiveMerge(p1,newP2,p2)  #now call the recursive function with newP2, and a moved p1Prev
        
    




