"""Optimal approach in this case is basically running mergesort on the array and whenever we find that the current iterator value in the right 
half is less than the current iterator value in the left half, since the left half indices are all less than the right half indices and because 
each half is sorted, the number of inversions is equal to the remaining elements in the left half ie len(leftHalf)- current iterator index in the 
leftHalf. By computing the inversions at the merge step, we can calculate the total inversions in the array. Because inversions are a measure of 
how unsorted an array is, the total measure of the unsortedness of an array is the unsortedness of the leftsubarray, the unsortedness of the right 
subarray and the unsortedness of merging the left and right subarraxy of the modified merge sort helper function. """
#O(nlog(n)) time | O(n) space
def countInversions(array):
    if len(array) == 0:
        return 0
    return countSubArrayInversions(array,0,len(array)) #len(array) is endIdx exclusive in this mergeSort implementation 

def countSubArrayInversions(array,start,end):
    if end - start <= 1: #in a single element or empty subarray, 
        return 0    #number of inversions is 0 for len(array) = 1 or 0

    #otherwise, sort and count inversions of left / right subarrays then sort and count inversions of both subarrays
    middle = start + (end -start) // 2 #same as (start + end) // 2, index of middle element
    leftInversions = countSubArrayInversions(array,start,middle) #inversions in left subarray, start <= i < middle
    rightInversions = countSubArrayInversions(array,middle,end) #inversions in right subarray, middle <= i < end
    mergedArrayInversions = mergeSortAndCountInversions(array,start,middle,end) #inversions when left / right merged
    return leftInversions + rightInversions + mergedArrayInversions

def mergeSortAndCountInversions(array,start,middle,end):
    sortedArray = []
    left = start #the left subarray pointer initialized at start
    right = middle #right subarray pointer initialized at middle
    inversions = 0 #initialize inversions

    while left < middle and right < end:
        if array[left] <= array[right]: #current value in left subarray is lesser value so no inversions
            sortedArray.append(array[left]) #add in sorted order
            left += 1 #increment left pointer
        else: #whenever the current element in the right subarray is the lesser value, inversions = middle - left
            inversions += middle - left #increment inversions by number of remaining elements in left subarray
            sortedArray.append(array[right])
            right += 1
    #add remaining elements in right and left subarray when one of the conditions terminates loop above before other
    sortedArray += array[left:middle] + array[right:end] #terminating element will have empty list
    #use sortedArray to modify input array in-place
    for idx,num in enumerate(sortedArray): #sortedArray is sorted from start to end so read values from start 
        array[start+idx] = num #read values from start and modify input array in place
    return inversions
        



"""The code below is the mergesort algorithm modified to measure inversions or unsortedness. Since the base case of mergesort is a single 
element array, which is sorted as is, the base case of the inversions helper method is 0 because a single element array is sorted so has no 
degree of unsortedness and thus 0 inversions.Also since we are only interested in inversions, we declare a sorted array in the merge step, 
merge the two halves into this array and use this array to modify the input array in each step. It is essential that you don't count 
inversions when the current left half number is equal to the current right half number so make sure to use left <= right  instead of 
left < right, which would work for ordinary merge sort but not in this modified merge sort for counting inversions. Since we will be counting 
inversions one sub-array at a time, whenever the current value in the right subarray is less than the current value in the left subarray, we 
count all the inversions that are being caused by the current subarray value. So since the right index starts from middle, we count 
middle - left , meaning the current right subarray will cause inversions for the current left subarray value and all the remaining left 
subarray values. We do this before we increment the right index to count the number of inversions caused by the next right subarray value. 
We also append to the sorted array. After this we add any remaining values from either subarray and modify the input array using the sorted 
array and starting from the startIdx that was the passed as the start of the left subarray. The python enumerate function allows us the numbers 
in the sorted array and their in-array indices to add to the startIdx so that we update the right values on each run. Since we are only 
interested in counting inversions, we only need to ensure that the array always reflects the remaining inversions after the last merge step. 
This solution re-purposes the auxilliary array method of mergesort but instead of passing around an additional array and swapping it with the 
main array and later using it as a reference / modify array, we create the auxilliary array inside the merge helper function, starting with an 
empty array and appending to it . Finally at the end, we use this sorted (auxilliary) array for the modification starting from startIdx. 
Remember that since we are returning the number of inversions, we need to store pointers, leftInversions, rightInversions, mergeInversions 
and add these up as the total number of inversions at each stage. Also although handle the edge case anyway"""

def countInversions(array):
    if len(array) == 0:
        return 0
    return countInversionsHelper(array, 0, len(array) - 1)

def countInversionsHelper(array, startIdx, endIdx):
	if startIdx == endIdx:
		return 0
	middleIdx = (startIdx + endIdx) // 2
	leftInversions   = countInversionsHelper(array, startIdx, middleIdx)
	rightInversions  = countInversionsHelper(array, middleIdx + 1, endIdx)
	mergeInversions  = domergeInversions(array, startIdx, middleIdx, endIdx)
	return leftInversions + rightInversions + mergeInversions

def domergeInversions(array, startIdx, middleIdx, endIdx):
	sorted = []
	leftIdx = startIdx
	rightIdx = middleIdx + 1
	inversions = 0
	
	while leftIdx <= middleIdx and rightIdx <= endIdx:
		if array[leftIdx] <= array[rightIdx]:
			sorted.append(array[leftIdx])
			leftIdx += 1
		else:
			sorted.append(array[rightIdx])
			rightIdx += 1 #inversions = remaining left subarray elements = start of righ subarray - current leftIdx 
			inversions += middleIdx + 1 - leftIdx #num inversions due to current right subarray element = left remainder

	sorted += array[leftIdx:middleIdx+1] + array[rightIdx:endIdx+1]
	
	for idx,num in enumerate(sorted):
		currentIdx = startIdx + idx
		array[currentIdx] = num

	return inversions

array = [2, 3, 3, 1, 9, 5, 6]
print(countInversions(array))