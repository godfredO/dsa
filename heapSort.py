"""Heap sort is such a beautiful application of a heap re-purposed to sort an array in constant space by cleverly utilizing the buildHeap()
and siftDown() methods of a typical MaxHeap class. Anyway the algorithm is as follows, we build a max heap in place using the buildHeap() 
method. Because this is going to be done in-place, we remove the return array statement that is typically at the end of buildHeap(). Then
we 'remove' the root of the maxHeap, by swapping it with the last element in the array. Now swapping the root node in a heap with the last
element in a heap is what you would typically do in a heap's remove() method and in this sorting algorithm it carries additional significance.
This is because the maximum element in the array belongs in the last position anyway, so after this swap operation, our maxHeap is shorter
by 1. After a removal in a heap we would then sift down the value at the root position to its correct position in the heap and re-establish
the max heap property ensuring that the updated root node is the maximum value remaining in the heap. Typically the siftDown method() takes
an endIdx and because we just put the largest value in the last position, the endIdx we supply to the siftDown method is the penultimate 
position to reflect the fact that the heap just got shorter ie endIdx - 1. 

So to repurpose a heap's methods to sort an array, we loop through the array in reversed manner from the last position to the second position 
ie endIdx = reversed(range(1,len(array))). Then we swap the current root node value (index 0) with the value at endIdx, siftDown the 'imposter' 
root node (index 0) to its correct position in the heap, remembering to supply endIdx -1 as the 'endIdx' for the siftDown method).
We also use the customary swap method to 'remove' our root node. By using a max heap this way, we move each value to its correct sorted 
order position starting with the largest, next largest all the way to the least value.
BuildHeap will take O(n), the for loop will take O(n), the siftDown() method takes a total O(nlog(n)) (ie log(n) called n-1 times) giving 
O(n) + O(nlog(n)) and the limiting complexity is thus O(nlog(n)) and constant space since the maxheap is built in-place. Also, going up to
the second value (index 0) is tiny optimization since the maxHeap at that point will only contain the first sorted value which we swap with 
itself. Also we only use buildHeap(), siftDown(), and swap() methods of a buildHeap and so define these as separate helper functions since we 
dont need a class definition to sort in-place. We call buildHeap() once at the start of the array, and then afterwards we keep calling swap()
and siftDown() n-1 times. """

#O(nlog(n)) time | O(1) space
def heapSort(array):
    buildMaxHeap(array) #convert the array into a max-heap
    for endIdx in reversed(range(1,len(array))): #final value to second value due swap with idx 0
        swap(0,endIdx,array)#swap the root of heap, max value, with final value in array
        siftDown(0,endIdx-1,array) #sift down the swapped value to its correnct position in shorter heap
    return array

def buildMaxHeap(array):
    firstParentIdx = (len(array) - 2) // 2 #parent of the last element in array, leaf node
    for currentIdx in reversed(range(firstParentIdx + 1)): #ranges in python are exclusive so + 1
        siftDown(currentIdx, len(array)-1,array)
        
def swap(i,j,array):
    array[i], array[j] = array[j], array[i]

def siftDown(currentIdx,endIdx,heap):
    childOneIdx = currentIdx * 2 +1
    while childOneIdx <= endIdx: #while first child node is still located in the heap, in bounds of array
        childTwoIdx = currentIdx *2 + 2 if currentIdx *2 + 2 <= endIdx else -1 #if second child node exists
        if childTwoIdx != -1 and heap[childTwoIdx] > heap[childOneIdx]: #if childtwo exists and is the greater child
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx,idxToSwap,heap)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return #if the current node is in the correct place

array = [5,9,0,3,5,7,-9,8]
print(heapSort(array))

