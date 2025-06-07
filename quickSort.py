"""
Quicksort is an intelligent algorithm that sorts an array with respect to a chosen number which is called the 
pivot number. So when we start quicksort we have a startIdx and an endIdx (0, len(array) -1). Quicksort is 
implemented recursively. So when we call the recursive function on an unsorted array, with startIdx and endIdx, 
the first thing we do is to first check if the startIdx, endIdx is valid. We know that a single element array 
is sorted so if startIdx equals endIdx we just return to the main function and from there we return the single
element array as is. We also know that if startIdx is ever greater than endIdx, thats invalid so we either just 
finished sorting an array or we just called the recursive function with the wrong indices. So anyway, the first
thing we check is that if startIdx >= endIdx: return. If not we know we have valid startIdx, endIdx for an 
unsorted array. Then we choose the pivot number and pivotIdx and this is (usually) the very first element in the 
(sub)array passed ie pivotIdx = startIdx. Then we initialize rightIdx as startIdx + 1 and leftIdx as endIdx. This
technique is similar to how we use pointers / references in the threeNumberSum question where we center on a number
and use a rightIdx and leftIdx to find its complement pair. Thus in quicksort we center on pivotIdx, and use 
rightIdx and leftIdx to sort the rest of the array elements with respect to the pivotIdx number (pivotnumber), so 
that after each run of quicksort, the pivot number will be in its final sorted position, the left subarray will 
contain numbers that are less than or equal to the pivot number, the right subarray will contain number that are 
greater than or equal to the pivot number.

So inside the while loop ie while leftIdx <= rightIdx: the first check is that if the current leftIdx number is 
greater than the pivot number and the current rightIdx number is less than the pivot number, we swap them and 
position them in the correct subarrays. We then check if the leftIdx number is 'relatively sorted with respect 
to the pivot', ie is the current leftIdx number less than or equal to the pivotIdx, if it is we increment the 
leftIdx because the current positon of the number will put it in the correct subarray once we find the correct 
sorted position for the pivot number. Similarly if the rightIdx number is greater than or equal to the pivot 
number, we decrement rightIdx. So what these steps do is to swap the leftIdx and rightIdx values if they are 
both currently positioned in the wrong subarrays and also keep moving leftIdx and rightIdx pointers, until 
they are both pointing to values that are currently positioned in the wrong subarray. The sequencing is also 
important, we first check if the current left/right values need to be swapped before incrementing either pointer
separately. Thus we have a sequence of three if statements that need to follow a logical order in order to 
not miss out on any value.

So when the while loop terminates, we do a final swap of the value at pivotIdx (pivot number) and the value at the current rightIdx, because 
that is the final sorted positon of the pivot. Then we compute which sub-array is smaller in size, and call the recursive call on it. The 
left subarray will thus extend from startIdx to rightIdx - 1 and the right subarray will extend from rightIdx + 1 to endIdx. So if 
rightIdx - 1 - startIdx < endIdx - (rightIdx + 1) , then the left subarray is smaller so we call the recursive function on the subarray 
extending from startIdx to rightIdx - 1 before we call the recursive function on the subarray extending from rightIdx + 1 to endIdx. Because 
quicksort sorts the array in-place, the only spaced is the recursive stack and there will be log(n) calls on the stack at any one point for 
space complexity of log(n). Since each number will be the pivot at some point, the time complexity is O(nlogn). The logic underlying 
quicksort is used in a searching algorithm called quickselect, so check out the quickselect question."""

def quicksort(array):
    if len(array) < 2:      # if the array is empty or a single element, it is sorted as is
        return array 
    
    # 1. Pick a pivot 
    pivot = array[0]                                # first element is the simplest choice of pivot
    # Partition array into two subarrays (O(n))
    left = [i for i in array[1:] if i <= pivot]     # left subarray; elements less than or equal to pivot
    right = [i for i in array[1:] if i > pivot]     # right subarray of elments greater than pivot
    # Call quicksort recursively on the two sub-arrays (O(n) or O(log(n)))
    return quicksort(left) + [pivot] + quicksort(right) # return arranged and sorted subarrays with pivot 

#O(nlog(n)) time | O(log(n)) space
def quickSort(array):
    quickSortHelper(array,0,len(array)-1) #first call to quicksortHelper on entire array, to modify in-place
    return array

#we are gonna be calling this recursive function on the subarrays created by the pivot's position
def quickSortHelper(array, startIdx,endIdx):

    if startIdx >= endIdx:   #if dealing with an array of length 1, startIdx == endIdx (or if current quick sort is finished)
        return               #its sorted and we're done

    pivotIdx = startIdx     #pivotIdx is the first value in the subarray
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:#condition for swapping leftIdx and rightIdx
            swap(leftIdx,rightIdx,array)
        if array[leftIdx] <= array[pivotIdx]: #condition for advancing leftIdx
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]: #condition for advancing rightIdx
            rightIdx -= 1
    swap(pivotIdx,rightIdx,array)   #at the end of each quick sort application swap the pivot with the rightIdx num

    #after swap, the pivot number is at rightIdx, so length of left subarray is from startIdx to rightIdx -1
    #similarly, the right subarray is from rightIdx +1 to endIdx and the order is to ensure positive length
    leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)
    if leftSubarrayIsSmaller:#if left subarray is smaller
        quickSortHelper(array, startIdx,rightIdx -1) #first recursive call should be on the left subarray
        quickSortHelper(array, rightIdx + 1, endIdx) #followed
    else:                                           #else if right subarray is shorter
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx,rightIdx -1)

def swap(i,j,array):
    array[i],array[j] = array[j], array[i]

array = [8, 5, 2, 9, 5, 6, 3]
print(quickSort(array))