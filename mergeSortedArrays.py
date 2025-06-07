"""In this question, we are given a list of sorted arrays and asked to merge these sorted arrays into one sorted array. There will be
k sorted arrays and n total elements. So of the bat we know the space complexity will be at least O(n) due to the size of the return
array. This also means the time complexity will at least have an O(n) component. Now with that said, how do we actually merge k sorted
arrays. The first realization is that this is a generalization of an essential step of the merge sort algorithm which involves merging
2 sorted array. In merge sort, we use two pointers that start at the beginning of both sorted arrays and compare the values at those
indices, and which ever value is smaller, we add to our result array and move the pointer until all elements are in the result array in
sorted order. We can generalize this idea by comparing k elements, each element being the current iterator value in the k sorted arrays.
Thus we need to compare k values, n times leading to a time complexity of O(nk) when we use an array to to store the k values for 
comparison. The step of comparing k values and choosing the smallest value can be improved by using a min heap which will reduce that 
operation from an O(k) to O(log(k)) step and O(k) to build the heap the first time. Thus the first solution uses an array for a time
complexity of O(nk) and the second solution uses a min heap for a time complexity of O(nlog(k))"""

"""Just a description of the code. There is an array that stores the current iterator positions for the sorted arrays which is initalized
at 0 for all sub-arrays since we are assured that all sub-arrays are non-empty. Inside the while loop we initialize a new array of smallest 
items on each  loop run and we iterate through the arrays, store the arrayIdx and check thatthe iterator position for the current sub-array , 
which is at array Idx, is within bounds for the relevant array before adding the value at that iterator position. We then create a dictionary
object with arrayIdx and number as keys, so that we can append a value if its the minimum of the k elements and arrayIdx helps us know which
iterator position to increment. We append this object to the smallest items array (starts out empty on each run). After collecting the values
at the iterator positions for all the k sorted sub-arrays with the for loop, outside the for loop we check if the smallest items array of 
dictionary objects is empty. This would be the case if each iterator is out of bounds for their relevant arrays, meaning we have sorted all
the n values and thus break out of the while loop and return our final array. If the smallest items array is non-empty, we use a helper method
to find the object with the smallest value. This helper method works by initializing index 0 of smallest items as the index with the smallest
value and with a for loop starting from index 1, compares values of the dictionary objects, updating the minimum value index whenever a value
is lower. Anyway with the smallest value object returned, we increment the iterator position for the relevant array using the arrayIdx key and
append the value to our final array and go back to the top of the while loop, initailize a new empty smallest items array, collect values at
the iterator positions again and repeat. The while loop will run O(n) times, the for loop for collecting values will be O(k), the helper method
will be O(k), the smallest items array will be O(k) and the final array will be O(n). This gives a time complexity of O(n *(k + k)) ie O(2nk) or
O(nk) and the space complexity will be O(n+k)."""

#O(nk) time | O(n+k) space - this solution uses an array to store values from k sorted arrays for a minimum comparison
def mergeSortedArrays(arrays):
    sortedList = []  #initialize result array as empty list
    elementIdxs = [0 for array in arrays] #this stores the iterator positions in the sorted arrays; initialize at index 0 for k arrays

    while True: #O(n)

        smallestItems = [] #stores values at the iterator positions for min value comparison, starts out as empty on each loop run
        for arrayIdx in range(len(arrays)): #loop through the k sorted arrays, O(k), to choose array values for minimum comparison
            relevantArray = arrays[arrayIdx] #choose the current sorted array, 
            elementIdx = elementIdxs[arrayIdx] #current iterator position in current sorted array
            if elementIdx == len(relevantArray): #if the iterator for current sorted array is out of bounds for that array
                continue #then skip choosing an element for that array
            smallestItems.append({"arrayIdx":arrayIdx,"num":relevantArray[elementIdx]}) #add current element and its index in sorted array

        if len(smallestItems) == 0 : #if we hit the continue statement k times, we have placed all n elements
            break #break since we have added all n elements to list
        nextItem = getMinValue(smallestItems) #helper function to find the current minimum of all k iterator positions of sorted arrays
        sortedList.append(nextItem["num"]) #add the current smallest value to output list
        elementIdxs[nextItem["arrayIdx"]] += 1 #increment the element index for the arrayIdx sorted array in arrays

    return sortedList #at the end of while loop return merged list of sorted array with n elemens in sorted order

def getMinValue(items): #O(k)
    minValueIdx = 0  #initialize the index with the minimum value at index 0 ie first item
    for i in range(1,len(items)): #start looping from second item comparing all with the value at minValueIdx
        if items[i]["num"] < items[minValueIdx]["num"]: #if the number at iterator index is less that the number at minValueIdx
            minValueIdx = i #update minValueIdx to be the current iterator index
    return items[minValueIdx] #return the dictionary at minValueIdx


"""This next solution is exactly the same time and space complexity as above and is essentially the same idea. The difference is
instead of generalizing knowledge of merging 2 sorted arrays to merging k sorted arrays, we can realize that since the k sub-arrays
are all sorted we can first merge the first sorted array with the secod sorted array and merge the result of with the third sorted array.
Thus we can still use the same knowledge of merging 2 sorted arrays without generalizing it to k sorted arrays; we just get to
repeat it k times for the exact same result."""
#O(nk) time | O(n) space
# def mergeSortedArrays(arrays):
#     result = arrays[0] #initialize the output array as the first array of the k sorted arrays to be merged with next sorted array
#     for i in range(1,len(arrays)) : #start looping from second array, and merge  with the resulting array of merging preceding arrays,O(k)
#         nextArray = arrays[i] #choose the next array to be merged with result of merging previous sorted arrayys
#         result = mergeTwoSortedArrays(result,nextArray) #merge previous with current array and make output the new result array
#     return result #return the result of merging all sorted arrays, one at a time

# def mergeTwoSortedArrays(arrayOne,arrayTwo): #standard merge sort step of merging two sorted arrays, O(n)
#     output = []  #initialize output of merge as empty array
#     pt1,pt2= 0,0 #initialize the iterators for both sorted arrays
#     while pt1 < len(arrayOne) and pt2 < len(arrayTwo): #loop condition as long as both pointers are in bounds of the respective arrays
#         if arrayOne[pt1] < arrayTwo[pt2]: #if current iterator value of array one is the smaller value
#             output.append(arrayOne[pt1]) #then append the current iterator value of array one
#             pt1 += 1  #increment pointer for array one
#         else: #else if both iterator values are equal or the current iterator value of array two is the smaller value
#             output.append(arrayTwo[pt2]) #then append the current iterator value of array two
#             pt2 += 1 #increment pointer for array two
#     #while loop above terminates if one pointer goes out of bounds, so need to add the remaining elements from non-terminating array
#     #the following lines can all be replaced by output += arrayOne[pt:] + arrayTwo[pt2:]
#     if pt1 < len(arrayOne): #add the remaining array one values if pt2 was the terminating pointer
#         while pt1 < len(arrayOne): #as long as iterator for array one is in bounds
#             output.append(arrayOne[pt1]) #add the current iterator value for array one
#             pt1 += 1 #increment pointer for array one
    
#     if pt2 < len(arrayTwo): #add the remaining array two values if pt1 was the terminatin pointer
#         while pt2 < len(arrayTwo): #as long as iterator for array two is in bounds
#             output.append(arrayTwo[pt2]) #add the current iterator value for array two
#             pt2 += 1 #increment pointer for array
    
#     return output #return the output list from merging the two sorted arrays
        

"""Optimal solution of using a min heap to avoid either comparing k values in an array like the first solution or merging two sorted arrays
k times, like the second solution. Instead the min heap will hold up to k values and will provide constant time access to the minimum value
and log(k) insertions thus improving the time complexity. Check out the Sorted K-Sorted Arrays question, and even laptop rentals question."""
class MinHeap:
    def __init__(self,array):
        self.heap = self.buildHeap(array)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def buildHeap(self,array):
        firstParentIdx = (len(array)-2) // 2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(currentIdx,len(array)-1,array)
        return array
    
    def siftDown(self,currentIdx,endIdx,heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx]["num"] < heap[childOneIdx]["num"]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap]["num"] < heap[currentIdx]["num"]:
                self.swap(currentIdx,idxToSwap,heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
    
    def siftUp(self,currentIdx,heap):
        parentIdx = (currentIdx -1) // 2
        while currentIdx > 0 and heap[currentIdx]["num"] < heap[parentIdx]["num"]:
            self.swap(currentIdx,parentIdx,heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
    
    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap)-1, self.heap)
        return valueToRemove
    
    def insert(self,value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
    
    def swap(self,i,j,heap):
        heap[i], heap[j] = heap[j], heap[i]

#O(nlog(k)) time | O(n+k) space
def mergeSortedArrays(arrays):
    sortedList = [] #initialize empty output array
    smallestItems = [] #initialize empty array to hold first elements from all k sorted arrays
    for arrayIdx in range(len(arrays)): #loop through input array
        smallestItems.append({"arrayIdx":arrayIdx, "elementIdx":0, "num":arrays[arrayIdx][0]}) #add first elements to array
    minHeap  = MinHeap(smallestItems) #use list of first elements from k sorted list to create min heap
    while not minHeap.isEmpty(): #as long as the heap is not empty
        smallestItem = minHeap.remove() #remove the dict object with the smallest num value
        arrayIdx, elementIdx, num = smallestItem["arrayIdx"], smallestItem["elementIdx"], smallestItem["num"] #unpack dict
        sortedList.append(num) #append smallest number to 
        if elementIdx == len(arrays[arrayIdx])-1: #if we reached the end of the sorted array at arrayIdx
            continue #continue, don't add next element since there is no next element
        minHeap.insert({"arrayIdx":arrayIdx, "elementIdx": elementIdx + 1, "num": arrays[arrayIdx][elementIdx + 1]}) #add next element
    return sortedList #return sorted list 








arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150]
  ]
print(mergeSortedArrays(arrays))
