"""The question wants you to implement a continuous median class that can receive a stream of numbers and at any point in time, is 
able to give constant time access to the median of the inserted numbers thus far. The median of a set of numbers is the 'middle' number 
the numbers are ordered from smallest to greatest. If there's an odd number of numbers in the set as in {1,3,7}, the median is the 
middle ie 3 in this case. If there's an even number of numbers in the set as in {1,3,7,8}, the median is the average ofthe two middle
numbers ie (3+7)/2 = 5.

The naive approach will be to constantly sort the numbers after each insertion and calculate the index of the middle number if the number 
of inserted numbers is odd or the indices of the middle two numbers if the number of inserted numbers is even. Then the median in that case 
will be the middle number or the average of the middle two numbers. This would not provide the constant time access to the median since that 
would require a sorting step each time.

The optimal solution depends on realising that we don't actually need the numbers to be sorted per se. We just need a lower half of numbers
and an upper half of numbers where the smallest value in the upper half is greater than all the values in the lower half and the greatest
value in the lower half is less than all the values in the upper half. Thus the LOWER half will be a MAXHeap and the UPPER Half will be a
MINHeap, that have are effectively height-balanced between the two of them meaning their size are the same or differs by 1. If their sizes
ever differ by 2 we rebalance the heap by removing the root of the heap with the greater size and inserting it in the other heap. In the 
implementation, because min and max heaps differ from one another only in terms of their comparison function, we have created a single heap
class that takes in a comparison function and uses it in the siftDown and siftUp methods to generate either a minHeap or a maxHeap. Also,
to provide constant time access to the median is as simple as accessing the lengths of the minHeap and maxHeap and if their lengths are
equal, accessing the peek values and dividing by 2 since the peek values are the middle two values in this situation. This corresponds to
calculating the median of an even-length set of numbers. If their lengths differ by 1, which is allowed, the median is simply the peek value 
of the heap that has the greater length. This corresponds to calculating the median of an odd-length set of numbers.
THE KEY TO THIS SOLUTION IS THAT THE LOWER HALF IS A MAXHEAP AND THE UPPER HALF IS A MINHEAP.

The Continuous median class has three attributes; the self.lowers which points to a MAXHeap initially created by instantiating a Heap class
with the MAX_HEAP_FUNC ie greater than comparsion and an empty array; self.greaters which points to a MINHeap initially created by 
instantiating a Heap class with the MIN_HEAP_FUNC ie less than comparison and an empty array; and the self.median which stores the median 
at any point.

The heap class used has three attributes too; self.comparisonFunc which stores the name of the comparison function for a heap ie MIN_HEAP_FUNC
for a minHeap, MAX_HEAP_FUNC for a max heap; self.heap which stores the array of numbers resulting from calling buildHeap, and self.length
which stores the length of the heap, which can be accessed from the minHeap instance and maxHeap instance stored on the class definition of
the Continuous median class ie self.lowers.length and self.greaters.length, so that the length info can be used to choose an appropriate
measure for calculating the median, as well decide when its time to rebalance the heap. When the Continuous Median super class initializes
either a maxHeap and minHeap, with an empty array, a length of 0 is stored. In the code we use len(self.heap) but storing 0 directly works too.
Then we we insert into a heap, ie from the continuous median class we call self.lowers.insert(value) or self.greaters.insert(value), the actual
insert method on the Heap class appends the value to the end of the array, increments the length attribute by 1 before calling the siftUp
method on the last index position. Similarly inside the remove() method of the Heap class, after swapping a root node with the last node and
popping from the heap, we decrement the stored length by 1 ie swap(), pop(), self.length -= 1. 

The Continuous Median class has three methods that utilize (super-class) the standard methods of a heap class; insert(), rebalanceHeaps(), and 
updateMedian() all super-class heap methods. These methods in the super class utilize the standard heap methods to achieve their aims. 
The Insert() method uses a heap's peek() and insert() methods as well as the stored length on the heap class ie self.lowers.peek(), 
self.lowers.insert(), self.greaters.insert(), self.lowers.length. 
The rebalanceHeaps() method uses a heap's remove()  and insert() methods as well as the stored length attribute ie self.lowers.length, 
self.greaters.length, self.greaters.insert(self.lowers.remove()), self.lowers.insert(self.greaters.remove()). 
The updateMedian() method uses the stored length attribute, the peek() methods of a standard heap class ie self.greaters.length, 
self.lowers.length, self.lowers.peek(), self.greaters.peek().
The getMedian method on Continuous Median class return the value stored in the median attribute of the Continuous Median class.

When we insert an number we check if the lowerHalf is empty or if the number is less than the peek value of the lowerHalf. If so we insert 
the number into the lowerHalf by calling the lowerHalf's insert method with the number. If not we call the upperHalf's insert method with 
the number. It is essential that the checking for a non-empty first to avoid comparing a number with the peek value of an empty list and 
throwing an IndexError in the process. After inserting the number in the appropriate heap, we call the rebalanceHeaps() method followed by 
the updateMedian() method.

The rebalance method checks if the lowerHalf's length exceeds the upperHalf's length by 2 ie self.lowers.length - self.greaters.length 
== 2. If it is, it removes the root node of the lowerHalf and inserts in the upperHalf. Othewise (elif) it checks if the upperHalf's length 
exceeds the lowerHalf's length by 2, in which case removes the root node of the upperHalf and inserts in the lowerHalf. Because the 
rebalanceHeaps() method is called each time after the insert() method inserts a number in a heap, the two heaps' length may differ by 1 
but never 2.

After inserting a number and calling the rebalanceHeaps() method, the insert() method calls the updateMedian() method. This method first
checks if the two heaps are of equal length ie even-length set of numbers, and if that the case the self.median attribute is updated to
be the the average of the peek values of the two heaps ie self.median = (self.lowers.peek() + self.greaters.peek())/2. If not even length
the the median is the root value of the longer heap. So (elif) self.lowers.length > self.greaters.length: self.median = self.lowers.peek(),
else (if self.greaters.length > self.lowers.length): self.median = self.greaters.peek().

How does the comparison functions, MIN_HEAP_FUNC and MAX_HEAP_FUNC, affect the writing of siftDown and siftUp. First whenever we use
compound checks, we remove the comparison check and make it its own if statement where we supply the comparison values to the function. 
Eg if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx], becomses if childTwoIdx != -1:(indent) 
if self.compFunc(heap[childOneIdx], heap[childTwoIdx]). This means compariosn is true, we set idxToSwap to childOneIdx and we also handle
the else case where childTwoIdx == -1 by setting idxToSwap = childOneIdx. Similarly if heap[idxToSwap] < heap[currentIdx] becomes
if self.compFunc(heap[idxToSwap], heap[currentIdx]). The same changes occur in siftUp where we decouple the boundary change ie currentIdx>0
from the comparison ie while currentIdx > 0 : if self.compFunc(heap[currentIdx], heap[parentIdx]). Finally the comparison functions
themselves are trivial ie MIN_HEAP_FUNC(a,b): returns a < b and MAX_HEAP_FUNC(a,b): returns a > b so order is important. Also it is
important to have an else: return on the siftUp method when the comparison returns false like we have on siftDown.

Thus as we insert the stream of numbers, we rebalance the heaps and store the new median (using peek values so constant time), as an 
attribute in the class , an attribute which is returned whenever we call for the median. Also the first time the maxHeap or minHeap is 
instantiated the length of the heap is stored in the length parameter after buildHeap runs. After that initial length is stored, we need to 
update this parameter inside the insert or remove method by incrementing or decrementing by 1. The ContinuousMedian class initially 
instantiates both heaps with an empty array, making it even more crucial to update length whenever a heaps insert method is called. Due to 
the fact that the comparison functions are implemented separately and their names passed in upon heap instantiation there are some minor 
tweaks to loop conditions or comparison lines inside siftDown and siftUp. The insert function call updates length after appending and the 
remove function after popping. Finally, the rebalance method of the ContinuousMedian class cleverly uses remove, insert methods. Because we 
instatiate the heaps with empty array, the real use of siftDown and siftUp is in the insert and remove method, and even though the 
ContinuousMedianClass never removes an element, we call on the heap's remove() and insert() methods when rebalancing the heaps. Note that
if the insert value is equal to the minHeap peek value, the equal to case goes to insert in the maxHeap but since we rebalance the heap 
each time if we inserted 2,2,2,2 the first one will go to the minHeap, rebalance, update median, the second to the maxHeap due to equality
case, rebalance and update median, the third will go to the maxheap due to the equality case,rebalance and update median, the fourth will 
go to the maxHeap due to the equality, rebalance will remove a 2 from the maxheap and insert in the minHeap, then update."""

"""A heap class that takes a comparison function to create a min heap and a max heap"""
class Heap:
    def __init__(self,comparisonFunc,array):
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self,array):
        firstParentIdx = (len(array) - 2)// 2 #parent of last value
        for currentIdx in reversed(range(firstParentIdx + 1)): #+1 to include firstParentIdx
            self.siftDown(currentIdx,len(array) - 1, array)
        return array
    
    def siftDown(self,currentIdx,endIdx,heap):
        childOneIdx = currentIdx * 2 + 1 #calculate first child
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1:#if child two index is valid
                if self.comparisonFunc(heap[childTwoIdx], heap[childOneIdx]):#use comp
                    idxToSwap = childTwoIdx #if childTwo is True for comparison, swap 2
                else:
                    idxToSwap = childOneIdx #if childTwo is False for comparison, swap 1
            else:
                idxToSwap = childOneIdx #if childTwoIdx is invalid, swap 1
            if self.comparisonFunc(heap[idxToSwap], heap[currentIdx]): #min/max comparison
                self.swap(currentIdx,idxToSwap,heap) #if comparison True, swap child/parent
                currentIdx = idxToSwap #update the new index of the old parent
                childOneIdx = currentIdx * 2 + 1 #calculate new child index from parent index
            else:
                return #if chosem child/ parent comparsion is False, end
    
    def siftUp(self,currentIdx,heap):
        parentIdx = (currentIdx - 1) // 2 #calculate the parent index 
        while currentIdx > 0: #while within bounds, go up till reach the first value index
            if self.comparisonFunc(heap[currentIdx],heap[parentIdx]):#use min/max heap func
                self.swap(currentIdx,parentIdx,heap) #if comparison True, swap with parent
                currentIdx = parentIdx #swapped value is now at parentIdx
                parentIdx = (currentIdx - 1) // 2 #calculate new parentIdx
            else:
                return
    
    def peek(self):
        return self.heap[0] #constant time indexed-access of first value
    
    def remove(self):
        self.swap(0,self.length - 1, self.heap) #swap root ie first and last values
        valueToRemove = self.heap.pop() #pop (the old root) from the end of heap
        self.length -= 1 #update length
        self.siftDown(0,self.length -1, self.heap) #then sift down the swapped value
        return valueToRemove #return popped value
    
    def insert(self,value):
        self.heap.append(value)  #append value
        self.length += 1 #update length  
        self.siftUp(self.length - 1, self.heap) #then siftUp to final position
    
    def swap(self,i,j,array):
        array[i], array[j] = array[j], array[i] #one line Python swapping

def MAX_HEAP_FUNC(a,b): #the maximum of a, b for sifting in a maxHeap
    return a > b 

def MIN_HEAP_FUNC(a,b): #the minimum of a, b for sifting in a minHeap
    return a < b

#O(log(n)) time | O(n) space
class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC,[]) #initialize a max heap for the lower half 
        self.greaters = Heap(MIN_HEAP_FUNC, []) #initialize a min heap for the greater half 
        self.median = None
    
    #O(log(n)) time | O(n) space
    def insert(self,number):
        #num less than lower half max heap peek  value or lower half max heap is empty
        if not self.lowers.length or number < self.lowers.peek(): #if lowers empty, num < lowers peek
            self.lowers.insert(number) #insert num in lower half max heap 
        else: #if the number is greater than lower half max heap peek value
            self.greaters.insert(number) #insert in greater half min heap
        self.rebalanceHeaps() #re-balance heaps if necessary, lengths differ by more than 1
        self.updateMedian() #after every insertion, re-calculate median   

    def rebalanceHeaps(self):
        if self.lowers.length - self.greaters.length == 2:#if lower length is two more than greater
            self.greaters.insert(self.lowers.remove()) #remove from lower and insert in greater
        elif self.greaters.length - self.lowers.length == 2:#if greater length is two more than lower
            self.lowers.insert(self.greaters.remove())

    def updateMedian(self): #update running median after every insertion
        if self.lowers.length == self.greaters.length: #if lower and greater heaps same length
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2 #median is avg of peeks
        elif self.lowers.length > self.greaters.length: #if lower half max heap is longer
            self.median = self.lowers.peek() #median is peek valuue of lower half max heap
        else: #if greater half min heap is longer
            self.median = self.greaters.peek() #median is peek value of greater half min heap
    
    def getMedian(self):
        return self.median