"""A heap is a binary tree, is a binary tree that satisfies two addtional properties. The first one is completeness, that is a heap has
to have all of its levels filled up completely except the last level which iif it is partially filled , has to be filled from left to
right. The second property is the heap property. The heap property is where we distinguish a min heap from a max heap. The heap property
for a min heap is that every node's value has to be smaller than or equal to its children node's values. The heap property of a max heap
is that every node's value has to be greater than or equal to its children node's values. Its is essential to know that a heap is not 
sorted. Unlike other binary trees however, a heap can be represented as an array and this is due to the completeness property. To 
represent a heap as an array, we write the values of the valid heap trees by going level by level from top to bottom and at each level,
we go from left to right and add the values to the array. Because of the heap property the value at index 0 will be the minimum value
of a min heap or the maximum value of a max heap. In the array representation each node's index can be used to calculate its children 
node values ie childOneIdx = parentIdx * 2 + 1, childTwoIdx = parentIdx * 2 + 2. Similarly we can get the parent node index from a 
child node's index. parentIdx = (childNodeIdx - 1) // 2. In the min heap class below, we take in an array of numbers and build a heap
by swapping values around using these formulas and the heap property. To build a heap, we calculate the parentIdx of the last index in
the array, compare its value to its two children node and sift the parent node down the tree aka down the array until the parent node is
at the last position of the array. Sifting a parent node down involves swapping its position in the array with the smallest valued child
node (minHeap) and then repeating this comparison with the new child nodes based on the current index of the parent until we find the
correct position for it. So we start with the last parent, sift it down to its correct postion, then the second to last parent and over
and over again. In the code we choose the parents in the buildHeap method and call the siftDown method on each parent index. Sift down
runs in O(log(n)) but since sifting a parent down effectively sifts a child up, the build heap method actually runs in an amortized O(n) 
instead of the expected O(nlog(n)) if we have all the array elements at the beginning of the build heap method. Otherwise if we insert 
nodes one by one, then we will end up with the full O(nlog(n)) time complexity. T Removing in a minHeap refers to removing the root node 
or the minimum value, and to do this we simply swap the value at index 0 with the last node in the array, pop the last new last node, then
sift down the new index 0 element to its proper position which also has the effect of sifting up the actual new minimum value. Inserting
a node to a tree involves appending it to the heap, then sifting it up the tree to its correct position.
 """

class MinHeap:
    def __init__(self,array):
        self.heap = self.buildHeap(array)

    #O(n) time | O(1) space
    def buildHeap(self,array):
        firstParentIdx = (len(array)-2)//2  #the parent of the last value in array ie ((len(array) -1) -1)//2
        for currentIdx in reversed(range(firstParentIdx)):
            self.siftDown(currentIdx,len(array)-1,array)
        return array

    #O(log(n)) time | O(1) space
    def siftDown(self,currentIdx,endIdx,heap):
        childOneIdx = currentIdx*2 + 1
        while childOneIdx <= endIdx: #child node of a leaf node will be out of bounds, so we dont sift down
            childTwoIdx = currentIdx*2 + 2 if currentIdx*2 + 2 <= endIdx else -1 #in case 2nd child is out of bounds
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]: #choosing value to swap with parent
                idxToSwap = childTwoIdx #swap child 2 if lesser valued child and child 2 exists
            else: #if child 2 doesnt exist or child 1 is the lesser valued child
                idxToSwap = childOneIdx
            
            if heap[idxToSwap] < heap[currentIdx]: #if incorrectly positioned,
                self.swap(currentIdx,idxToSwap,heap) # swap currentIdx with the lesser valued child
                currentIdx = idxToSwap #after swap, update current position of swapped node
                childOneIdx = currentIdx *2 +1 #recalculate child
            else: #if no swap was done, then node is correctly positioned
                break

    #O(log(n)) time | O(1) space
    def siftUp(self,currentIdx,heap):
        parentIdx = (currentIdx - 1) // 2  #calcualate parentIdx for swap
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]: #while not at top of heap and incorrectly positioned
            self.swap(currentIdx,parentIdx,heap) #swap if incorrectly positioned
            currentIdx  = parentIdx #if swapped, currentIdx is now equal old parentIdx
            parentIdx = (currentIdx - 1) // 2 #new parentIdx

    #O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    #O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap) #swap the root with the last leaf node
        valueToRemove = self.heap.pop() #pop the new last value off the heap
        self.siftDown(0,len(self.heap)-1, self.heap) #sift down new root to its correct position
        return valueToRemove  #return the popped value

    #O(log(n)) time | O(1) space
    def insert(self,value):
        self.heap.append(value) #append to the heap returned after buildHeap
        self.siftUp(len(self.heap) -1, self.heap) #sift up appended value to correct position

    #Helper method
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i] #helper function to swap two values in an array
