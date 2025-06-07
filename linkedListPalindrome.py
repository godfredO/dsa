class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None


"""The first solution for this question uses recursion to compare a left node and a right node. At first call, both left node
and right node are the head node and at each successive call the right node is replaced by the next node in the linked list
until the base case where the right node is the None node after the tail at which point we return back up in the recursive tree.
At this point we check if the left node and right node are the same and return the answer True/ False as well as leftnode.next
which will be the new left node to compare against back up the recursive call stack constantly updating the left node and bubbling
up the answer to leftNode.value == rightNode.value until we get back up to the first recursive call. This approach allows us to 
effectively compare node values at the beginning of the linked list to the corresponding node values at the end of the linked list"""
class LinkedListInfo:
    def __init__(self,outerNodesAreEqual,leftNodeToCompare):
        self.outerNodesAreEqual = outerNodesAreEqual
        self.leftNodeToCompare = leftNodeToCompare

#O(n) time | O(n) space - space use is due to recursive stack
def linkedListPalindrome(head):
    isPalindromeResults = isPalindrome(head,head)
    return isPalindromeResults.outerNodesAreEqual

def isPalindrome(leftNode,rightNode):
    if rightNode is None: #base case, when right node is None ie rightNode has gone past the tail node
        return LinkedListInfo(True,leftNode)
    
    recursiveCallResults = isPalindrome(leftNode,rightNode.next) #this step will keep going until base case
    leftNodeToCompare = recursiveCallResults.leftNodeToCompare   #unpack the class object returned by recursive call
    outerNodesAreEqual = recursiveCallResults.outerNodesAreEqual #unpack the class object returned by recursive call

    recursiveIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value #compare right,left nodes, bubble up Boolean
    nextLeftNodeToCompare = leftNodeToCompare.next  #advance leftNode to leftNode.next
    return LinkedListInfo(recursiveIsEqual,nextLeftNodeToCompare) #return the result of comparison and next left node to compare


"""The second solution is iterative and starts by reversing half the linked list. To obtain the head node of the second half of the
linked list for reversing we use two pointers, first and second. We advance first pointer one step at a time and advance second pointer
two steps at a time. At the moment when second pointer reaches None node after the tail, the first pointer will be pointing to the 
middle node. This works whether the linked list is off even or odd length. Then with the head node of the second half of the linked list
we can reverse the second half using three pointers, two of these prev,current, outside the while loop and the third, next, inside the 
while loop and returning the head of the reversed second half. Now this solution is only viable if the interviewer says that we can 
mutate the input linked list due to the reversal step. Then we can step through the first half and reversed second half comparing the
values of the current nodes to check if the linked list is a palindrome."""
#O(n) time | O(1) space
def linkedListPalindrome(head):
    slowNode = head     #first pointer, which will store the head of the second half of the linked list when while loop terminates
    fastNode = head     #second pointer

    #grab the head of the second half of linked list using slowNode in while loop and using fastNode to know when to stop
    while fastNode is not None and fastNode.next is not None: #even-length condition and odd-length condition
        slowNode = slowNode.next #advance first pointer one jump at a time, stores second half head node at loop termination
        fastNode = fastNode.next.next #advance second pointer at 2x speed, hence the loop condition
    
    reversedSecondHalfNode = reverseLinkedList(slowNode) #reverse second half and return the head node of reversed second half
    firstHalfNode = head #pointer for first half

    while reversedSecondHalfNode is not None:
        if reversedSecondHalfNode.value != firstHalfNode.value:
            return False
        reversedSecondHalfNode = reversedSecondHalfNode.next
        firstHalfNode = firstHalfNode.next
    return True #if we make it out of  while loop above, then linked list is a palindrome

def reverseLinkedList(head):
    previousNode, currentNode = None,head
    while currentNode is not None:
        nextNode = currentNode.next  #create a pointer to store the node after currentNode
        currentNode.next = previousNode #first reverse the next attribute of currentNode
        previousNode = currentNode #then advance the previousNode pointer to currentNode
        currentNode = nextNode  #then advance currentNode pointer to nextNode
    return previousNode  #when loop breaks previous Node will be at head of reversed linked list

    
