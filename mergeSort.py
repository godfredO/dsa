"""The idea behind merge sort is rather intuitive; an aray of length one is sorted. Then if given two arrays of length one we can use 
pointers to compare their values and write their values in sorted order in some other array. This is what merge sort does. Its a divide 
and conquer algorithm in that it divides the input array into subarrays until it reaches an array of length one. Then pointers are used to 
merge the sorted subarrays into a result array. The two solutions here differ in that in the first solution, we slice the input array to 
divide it, thus making copies at each recursive stage. This leads to log(n) copies of the array giving a space of nlog(n) for the copies and 
log(n) for the recursive stack. O(Nlog(n) + log(n)) > O(Nlog(n)). One difference between mergeSort and quickSort algorithm is that in
mergeSort we calculate a middle index to divide the array and the middle value belongs to one of the resulting halvees, the right half in
this case. In quicksort after finding the correct sorted position of the pivot the pivot idx is used to divide the input array but the 
input value itself is not part of either half, we just sort the preceding values and the proceding values.
The reason we have log(n) calls is because we sort the entire left subarray before sorting the entire right subarray. And at each stage we
do an O(n) slice followed by an O(n) merge giving a total complexity of O(nlog(n)). The new copies of the arrays we make during each log(n) 
call also leads to the space complexity of O(nlog(n)). In the optimal solution we dont do this, we only create a single O(n) copy either as 
a reference (first optimal solution) or as a tentative sorted subarray(in the second solution) so we have a total space complexity of O(n).
The time complexity is still O(nlog(n)) in the optimal solution because even though we don't make O(n) slice operation, in each log(n) call,
we still do a O(n) merge step in each log(n) call."""

#o(nlog(n)) time | O(nlog(n)) space
# def mergeSort(array):
#     if len(array) == 1: #base case
#         return array
#     #divide input array into left and right half
#     middleIdx = len(array) // 2 #calculate the middle index for dividing array
#     leftHalf = array[:middleIdx] #left half after dividing input array
#     rightHalf = array[middleIdx:] #right half after dividing input array

#     #call mergeSort on both halves and merge the returned values from calling mergeSort on both halves
#     return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

# def mergeSortedArrays(leftHalf,rightHalf): #this approach declares the right size array and updates values
#     #could also have started off with an an empty array, appended to this array the smaller value based
#     #on comparison making sure to add the remaining values of the array that didnt terminate the while loop
#     sortedArray = [None] * (len(leftHalf) + len(rightHalf)) #initialize
#     k = i = j = 0   #sortedArray current index, leftHalf current index, rightHalf current index

#     while i < len(leftHalf) and j < len(rightHalf): #we could have avoided index k by using a for loop
#         if leftHalf[i] <= rightHalf[j]: #smaller or equal value based on
#             sortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             sortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1
    
#     #after above loop terminates, dump the remaining values in the non-terminating half ,left or right
#     while i < len(leftHalf):
#         sortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1
#     while j < len(rightHalf):
#         sortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1
#     return sortedArray

"""Optimal solution. The solution above makes a slice copy of the array into leftHalf and rightHalf at each stage leading to a space complexity 
of nlogn for the log(n) copies of the up to n-length slice copy. In the optimal solution we make a single auxilliary copy of the input array. 
This auxilliary is passed together with the main input array into the mergeSort function. In this case the input array is the modify array and 
the auxilliary is the reference array. The algorithm overwrites the value at specifc index of the modify array by reading values stored at 
certain passed indices of the reference array. So when we start, the input array is the modify and the auxilliary is the reference. At each stage 
of the array we swqp the modify and reference array of the previous level. This ensures that the algorithm can read values in sorted order from 
the reference array to overwrite values in the modify array since the current reference was modified into sorted order from the previous round. 
This  way we improve the space complexity"""

#O(nlog(n)) time | O(n) space
def mergeSort(array):
    if len(array) <= 1: #if passed an empty array or array of length 1
        return array  #return the same array
    auxiliaryArray = array[:]
    mergeSortHelper(array,0, len(array) - 1 , auxiliaryArray) #pass main and aux array, pointers for dividing
    return array #sorted in-place

def mergeSortHelper(mainArray,startIdx,endIdx,auxiliaryArray):
    if startIdx == endIdx: #if pass an empty array by splitting a single element array
        return #return, base case reached
    middleIdx = (startIdx + endIdx) // 2 #middle index for array diving
    mergeSortHelper(auxiliaryArray,startIdx,middleIdx,mainArray) #swap main and aux and divide middleIdx inclusive
    mergeSortHelper(auxiliaryArray,middleIdx + 1,endIdx,mainArray) #swap main and aux and divide endIdx inclusive
    doMerge(mainArray,startIdx,middleIdx,endIdx,auxiliaryArray) #helper to overwrite modify array values 

def doMerge(mainArray,startIdx,middleIdx,endIdx,auxiliaryArray):
    #this helper function takes in two pointers for two sorted subarrays in a reference array, compares their 
    # values and ovewrites a value in the modify array.  startIdx <= subarrayOne <= middleIdx of refernce
    # middle+1 <= subarrayTwo <= endIdx of reference. Modify array iterator starts at startIdx ie start of
    #subarrayOne. Modify array values from startIdx to endIdx are thus overwritten with reference array values
    #based on comparison using pointers of the values in the two sorted subarrays
    #No need to return a value because we overwrite and thus sort the modify array in place
    k = startIdx   #modify array iterator, starting at the first index of sorted subarrayOne of reference
    i = startIdx   # reference array iterator for first sorted subarray, startIdx <= i <= middleIdx
    j = middleIdx + 1  #reference array iterator for second sorted subarray, middleIdx + 1 <=j <= endIdx

    while i <= middleIdx and j <= endIdx: #iterators can go up to the bounds
        if auxiliaryArray[i] <= auxiliaryArray[j]: #compare values in the reference array
            mainArray[k] = auxiliaryArray[i] #overwrite the value at index k of modify array
            i += 1 #increment first sorted subarray pointer
        else: #if value pointed to in the second subarray is less
            mainArray[k] = auxiliaryArray[j]  #overwrite
            j += 1
        k += 1
    while i <= middleIdx:
        mainArray[k] = auxiliaryArray[i]
        i += 1
        k += 1
    while j <= endIdx:
        mainArray[k] = auxiliaryArray[j]
        j += 1
        k += 1


"""Optimal solution but instead of passing around an auxilliary we use the indices more cleverly and we only declare an auxilliary array
for temporary use inside of the merge method, like we did in the radix sort question."""
#O(nlog(n)) time | O(n) space
def mergeSort(array):
	if len(array) <= 1:
		return array
	mergeSortHelper(array, 0, len(array) - 1)
	return array


def mergeSortHelper(array, startIdx, endIdx ):
	if startIdx == endIdx: #a single element array will have start equal 0 and end = len(array) - 1 ie 1-1=0
		return
	middleIdx = (startIdx + endIdx ) // 2
	mergeSortHelper(array, startIdx, middleIdx) #left subarray is startIdx to middleIdx, sort entire left subarray first before
	mergeSortHelper(array, middleIdx + 1, endIdx) #right subarray is middleIdx + 1 to endIdx
	doMerge(array, startIdx, middleIdx, endIdx)   #once both left and right calls return, merge array with startIdx, middleIdx, endIdx

def doMerge(array, startIdx, middleIdx, endIdx):
	sorted = []  #sorted array, like the first solution, but empty
	i = startIdx #iterator for left sub-array initialized at leftIdx
	j = middleIdx + 1 #iterator for right sub-array initialized at middleIdx + 1 like in mergeSortHelper()
	
	while i <= middleIdx and j <= endIdx: # startIdx<= left-subarray <=middleIdx, middleIdx + 1 <= right-subarray <= endIdx
		if array[i] <= array[j]: # the equal to in <= is essential here, the next value is the lesser or equal value
			sorted.append(array[i]) #if left subarray element is less than or equal to right subarray element, append left subaray element
			i += 1 #increment left subarray index
		else: #else if left subarray element is greater then right subarray element is less, so choose right subarray element as next value
			sorted.append(array[j]) #so append right subarray element to sorted array
			j += 1  #increment right subarray index

    #when loop breaks one subarray will have elements pending and one will be empty,so concatenate sorted with an empty and a pending array
    # from current index to end of either sub-arrays, startIdx<= left-subarray <=middleIdx, middleIdx + 1 <= right-subarray <= endIdx
    #so add from currentLeft to middle + 1 and currentRight to endIdx + 1. +1 here is for slice exclusivity
	sorted += array[i:middleIdx+1] + array[j:endIdx+1] #add remaining elements from one sub-array and empty sub-array

	for idx in range(len(sorted)): #then modify, input array from startIdx to endIdx by copying from sorted temporary array
		currentIdx = startIdx + idx   #calculate the current value's index in input array, ie startIdx + currentSortedIndex
		array[currentIdx] = sorted[idx] #copy the value from sorted into input array

    

array = [8, 5, 2, 9, 5, 6, 3]
print(mergeSort(array))