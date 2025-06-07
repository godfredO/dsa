"""The question asks to write a function that takes in a non-negative integer k and a k-sorted array of integers and returns the sorted
version of the array. Your function can either sort the array or create an entirely new array. A k-sorted array is a partiallyy sorted
array in which all elements are at most k positions away from their sorted position. eg [3,1,2,2] is k-sorted with k=3 because each 
element is at most 3 positions away from its sorted position. You are expected to come up with an algorithm that can sort the k-sorted
array faster than in O(nlogn) time.

Since the input array is k-sorted it means that each element is at most k jumps removed from its correct sorted position. This means 
that if we are looking for the value that should be at a particular index, we only have to look at k+1 elements, which will all be within k 
distance of the index and with all previously placed elements removed. That is the current element at the index could still be there in the
sorted array, or the elements up to k jumps away ie index +/- k. For k= 3, if  the index is 0, the possible candidates are the elements at 
index 0,1,2,3  ie k+1 elements, since all of these are at most k jumps away from index 0. And after we place the correct value at index 0 and
we move to index 1, we know that the element that belongs at 1 is at most k jumps to the left or to the right. But since we know the indices 
to the left ie index 0 has the correct value since we just placed it we still only have to look at k+1 element ie the values at indices 1,2,34. 
So this means that at any point in time, all we ever have to do is look at k+1  elements to the right, to figure out which element should be 
placed at a specific position in the sorted order since we go in sorted order from left to right effectively eliminating the k elements to the
left since these have already have the correct element and since we are choosing the minimum value of the k+1 elements. 

Now when we look at the k+1 elements, we are looking for the minimum value of the k+1 elements since we are sorting from index 0. Therefore 
at any index, we could use a minHeap to give us log(k) access to the minimum of k+1 elements and set that value at the index either in a new 
array or in place. So that's what this solution does. We start by inserting the first k+1 elements into the minHeap or the entire array if the 
length of the array is less than k. That is we initialize the minHeap with a slice of the array from index 0 to index k which is a total of
k+1 elements ie array[:min(k+1, len(array))]. So we start our loop from index k+1 till the end of the array.

Then, we start start a for loop from k+1 to the and end our sorted index at 0 ie the index to insert the next minimum number. The purpose of 
the loop is to continuously add the next element in the array to the minHeap each time we remove and insert a new value. Anyway inside the loop 
we call the remove method, insert it in the array at the current sorted index, increment the sorted index and insert the value at the current 
loop index into the minHeap. That when we remove the first root value from the minHeap, we insert it into the array at index 0 and insert the
value at the current loop index , ie at index k+1 into the heap, and increment the sorted (insert) index to index 1. The we remove the root 
again, insert at sorted (insert) index 1, our loop will be at index k+2 so we insert that value into the heap and increment the insert index
to 2. We keep going until the loop terminates at which point we would have inserted the last element of the array into the minHeap.

When the last array element is inserted into the loop, the for loop will terminate but we will have elements inside the minHeap, so we have a 
second while loop that insert at the current sorted index, increments the current sorted index until the entire array is empty. By inserting 
directly inside the original array, we don't use additional space and the entire algorithm takes O(nlog(k)), better than O(nlog(n)) from 
sorting blindly. Thus the main issue is to easily access the minimum value of k+1 elements and then insert in a the array.
A min-heap is used to provide easy access to the minimum of k+1 elements and to re-integrate the next value.

The pattern of using  secondary loop to insert remaining elements is common occurrence. Always check you dont need a second loop."""
class MinHeap:
    def __init__(self,array):
        self.heap = self.buildHeap(array)
    
    def isEmpty(self):
        return len(self.heap) == 0

    def buildHeap(self,array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx,len(array)-1, array) #array since self.heap doesnt exist yet
        return array #return the array which has been sifted in place
    
    def siftDown(self,currentIdx,endIdx,heap):
        childOneIdx = currentIdx * 2 + 1  #index of first child
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx *2 + 2 <= endIdx else -1 #second child index
            #if second child index is invalid and the value at second child index is less than first child
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]: #if both valid, swap smaller
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(idxToSwap,currentIdx,heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self,currentIdx,heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx,parentIdx,heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap)-1,self.heap)
        return valueToRemove

    def insert(self,value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    def swap(self, i, j, array):
        array[i], array[j] = array[j], array[i]       

#O(nlog(k)) time | O(k) space
def sortKSortedArray(array,k):
    #initialize minHeap with first k+1 elements of entire array. Since k could be larger than
    #the length of the array choose the first k+1 elements or the entire array if k is larger
    #Slicing is exclusive and arrays are 0 indexed so array[:k+1] first yields k+1 elements
    #slicing also yields arrays so we can feed it into the instantiation of MinHeap
    minHeapWithKElements = MinHeap(array[:min(k+1,len(array))]) #edge case k > len(array)
    
    nextIndexToInsertElement = 0 #start inserted sorted position here at 0
    for idx in range(k+1,len(array)): #loop through starting from k+1 
        minElement = minHeapWithKElements.remove() #remove smallest element in heap ie root
        array[nextIndexToInsertElement] = minElement #overwrite since first k+1 elements in heap
        nextIndexToInsertElement += 1 #increment sorted pointer after insertion

        currentElement = array[idx] #the current iterator value will be inserted in heap
        minHeapWithKElements.insert(currentElement) #add current iterator value to hap
    
    #handle elements still left on heap
    while not minHeapWithKElements.isEmpty(): #as long as we have elements on the minHeap
        minElement = minHeapWithKElements.remove() #remove root aka smallest element
        array[nextIndexToInsertElement] = minElement #insert heap removed value
        nextIndexToInsertElement += 1  #increment sorted pointer after insertion
    
    return array



array = [3, 2, 1, 5, 4, 7, 6, 5]
k = 3
print(sortKSortedArray(array,k))