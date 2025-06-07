"""The question gives an array of distinct integers as well as an integer k and asks to return the kth smallest integer in that array. Now 
from k we can deduce the index at which the kth smallest integer will be located if the array wee sorted. We know the 1st smallest integer
in a sorted array will occur at index 0, the 2nd smallest integer would be at index 1 etc. That is to say the kth smallest integer would 
be at index k-1 in a sorted array. Similarly this question can be asked as the kth largest integer in an array. We know that in a sorted
array the 1st largest integer would be located at index len(array) - 1 if the array were sorted, the 2nd largest integer would be located
at index len(array) - 2, meaning that the kth largest integer would be located at len(array) - k in the sorted array. Thus the first
step in this solution is to find the index of the kth smallest/greatest integer if the array were sorted. 

Next thing is to ask if we have to sort our array, which would take O(nlog(n)) at best instead of the O(n) that the question is asking for. 
We are able to achieve the linear time complexity by using our knowledge of how quick sort works and intelligently moving through our array. 
Now in quicksort we choose the first element in a (sub)array as the pivot, and we position it in its correct sorted position so that at the 
end, the pivot's final position is at the rightIdx, and after we swap the pivot into the current rightIdx, we know that it divides the array 
into a left subarray, right subarray and even though the subarrays are not sorted in themselves, they are as a whole, sorted with respect to 
the pivot. Meaning after each run of quicksort, we know the final index of the pivot number, and we know that all the values before this index 
are less than or equal to the piviot number and all the values after this index are greater than or equal to this pivot number and we repeat 
quicksort again on each subarray starting with the smaller subarray until all the whole array is sorted. Now we don't want to sort the whole 
array, so we first check if rightIdx, which is the final index of the pivot, is in fact equal to the kth index we calculated earlier. If it
is, we return the recently placed pivot number. 
However if its not , we can intelligently move in one direction based on how the kth index compares to the rightIdx. If kth index < rightIdx 
then we know that the kth index value will be in the left subarray so we call quicksort on only the left subarray, by updating endIdx = 
rightIdx - 1 (iteratively speaking). If the kth index > rightIdx then we know that the kth index value will be in the right subarray of the 
current pivot so we repeat quicksort only on the right subarray by updating startIdx = rightIdx + 1. 

Now quicksort requires the use of space, either the recursive stack, a stack or a queue so that we can sort the left and right subarrays but 
since we are only interested in finding the kth index element and we only move in one direction based on the comparison of the kth index to 
rightIdx, we are able to implement quickselect in constant space and because we only move in one direction we will visit at most n pivots 
before we find the pivotIdx (rightIdx) which equals kth index and we retun that pivot number after swapping it to rightIdx. We do this by 
wrapping the typical quicksort algorithm in while startIdx <= endIdx so that we solve the question iteratively instead of the recursive nature 
of quicksort which is designed to solve both subarrays starting with the smallest sized subarray."""

#O(n) time | O(1) space
# def quickselect(array, k):
#     position = k- 1 #because of Python's zero-index, kth smallest will be at k+1 index
#     return quickselectHelper(array,0,len(array)-1, position)

# def quickselectHelper(array,startIdx,endIdx,position):
#     while True:
#         if startIdx > endIdx:
#             raise Exception("Your algorithm should never arrive here") #it means we skipped kth smallest number
#         pivotIdx = startIdx
#         leftIdx = startIdx + 1
#         rightIdx = endIdx
#         while leftIdx <= rightIdx: #this while loop and the last swap is quicksort
#             if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
#                 swap(leftIdx,rightIdx,array)
#             if array[leftIdx] <= array[pivotIdx]:
#                 leftIdx += 1
#             if array[rightIdx] >= array[pivotIdx]:
#                 rightIdx -= 1

#         swap(pivotIdx,rightIdx,array) #swap pivot number with number at rightIdx

#         if rightIdx == position: #swapped pivot is now at rightIdx, so compare that to position,kth smallest value index
#             return array[rightIdx] #if final sorted positon of pivot is the positon we are looking for, return in
#         elif rightIdx < position: #else,if final sorted position of pivot is lower than kth position, ignore left subarray
#             startIdx = rightIdx + 1 #quicksort the right subarray
#         else: #if rightIdx > position, disregard the right subarray
#             endIdx = rightIdx - 1

# def swap(i,j,array):
#     array[i], array[j] = array[j] , array[i]


def quickselect(array, k):
    if len(array) < k:
        raise Exception("You skipped the kth smallest number")   
    kthIndex = k - 1
    return helper(array, kthIndex, 0, len(array) - 1)

def helper(array, kthIndex, startIdx, endIdx):
	
	#<= so that if equal we will skip over the inner while loop and hit the return statement, if < we return null since return statement is passed
	while startIdx <= endIdx: #when equal we skip inner while loop and go straight to return since rightIdx == startIdx == kthIndex
		pivotIdx = startIdx
		leftIdx = startIdx + 1
		rightIdx = endIdx

		while leftIdx <= rightIdx:
			if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
				swap(leftIdx, rightIdx, array)
			elif array[leftIdx] <= array[pivotIdx]:
				leftIdx += 1
			elif array[rightIdx] >= array[pivotIdx]:
				rightIdx -= 1
		swap(pivotIdx, rightIdx, array)
		
		if rightIdx == kthIndex:
			return array[rightIdx]
		elif kthIndex < rightIdx:
			endIdx = rightIdx - 1
		else:
			startIdx = rightIdx + 1

def swap(i,j,array):
	array[i], array[j] = array[j], array[i]

"""Same idea, assuming input is always valid, so no need to raise exception"""
#O(n) time | O(1) space
def quickselect(array,k):
	kthIdx = k - 1
	startIdx, endIdx = 0, len(array) - 1
	
	while startIdx <= endIdx:
		pivotIdx = startIdx 
		leftIdx = startIdx + 1
		rightIdx = endIdx
		
		while leftIdx <= rightIdx:
			if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
				swap(array, leftIdx, rightIdx)
			if array[leftIdx] <= array[pivotIdx] :
				leftIdx += 1
			if array[rightIdx] >= array[pivotIdx]:
				rightIdx -= 1

		swap(array, pivotIdx, rightIdx)
		
		if kthIdx == rightIdx:
			return array[rightIdx]
		elif kthIdx < rightIdx:
			endIdx = rightIdx - 1
		else:
			startIdx = rightIdx + 1
	

def swap(array, i, j):
	array[i] , array[j] = array[j] , array[i]

array = [8, 5, 2, 9, 7, 6, 3]
k = 3
print(quickselect(array,k))