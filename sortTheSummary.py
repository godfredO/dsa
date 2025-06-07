"""Given an array of integers, create a 2-dimensional array where the first element is a distinct value from the array and the second element
is that value's frequency within the array. Sort the resulting array descending by frequency. If multiple values have the same frequency, 
they should be sorted ascending. 
-Eg arr = [3,3,1,2,1].  Answer = [[1,2],[3,2],[2,1]]"""

def groupSort(arr):
    freq = {}

    for num in arr:
        if num not in freq:
            freq[num] = [num,0]
        freq[num][1] += 1
    
    array = list(freq.values())
    
    buildHeap(array)
    print(array)
    for lastIdx in reversed(range(1,len(array))): #final value to second value due swap with idx 0
        
        swap(array,0,lastIdx)#swap the root of heap, max value, with final value in array
        print(array)
        siftDown(0, lastIdx - 1,array) #sift down the swapped value to its correnct position in shorter heap
        print(array)
    return array
    

def buildHeap(array):
    firstParentIdx = (len(array) - 2)// 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(array) - 1, array)
    
def siftDown(currentIdx, endIdx, heap):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx != -1: #if childTwoIdx is valid
            if heap[childTwoIdx][1] < heap[childOneIdx][1]: #if childTwoIdx has lower frequency
                idxToSwap = childTwoIdx #choose lower frequency
            elif heap[childTwoIdx][1] == heap[childOneIdx][1]: #if frequencies equal
                if heap[childTwoIdx][0] > heap[childOneIdx][0]: #if childTwoIdx has the higher distinct value
                    idxToSwap = childTwoIdx   #choose childTwo
                else: #if childOneIdx has the higher distinct value
                    idxToSwap = childOneIdx #choose childOneIdx
        else: #if childTwoIdx is invalid
            idxToSwap = childOneIdx #choose childOneIdx
        
        if heap[idxToSwap][1] < heap[currentIdx][1]:
            swap(heap, idxToSwap, currentIdx)
            currentIdx = idxToSwap
            childOneIdx = currentIdx *2 + 1
        elif heap[idxToSwap][1] == heap[currentIdx][1]:
            if heap[idxToSwap][0] > heap[currentIdx][0]:
                swap(heap, idxToSwap, currentIdx)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return
        else:
            return
        
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]




arr = [3,2,1]
print(groupSort(arr))