"""Selection sort uses the fact that an empty array is considered sorted as-is and that if we have a list 
of numbers and we select the minimum number and append to an initially empty array (this sorted subarray 
will obviously keep growing in size as we append), we will eventually end up with a sorted list. 

The idea could be done in O(n^2) time and O(n) space if you start with an empty array but because the 
standard algorithm is done in place, so we build the sorted subarray O(n) and choose minimum value O(n) 
all in-place to give a time complexity of O(n^2) and O(1) space. We are able to build the sorted subarray
by swapping values in place instead of appending to a different sorted subarray (which initially started 
out as empty).

We initialize our append idx, at 0, meaning when we select the next minimum element we will 'append' here 
by swapping with the the value at index 0. Then each time we 'append' (by swapping the minimum value with 
the value at append idx) we increment this append idx by 1. And we keep doing this until the 'append idx' 
is at the last position in the array, len(array) - 1. If the 'append idx' is ever equal to the last position, 
we know that there are no more values after that position from which to search for the minimum value, so
we are at the end of our algorithm. As such our outer while loop's condition is while currentIdx < 
len(array) - 1.

In the code implementation we use two pointers, a currentIdx or appendIdx and a smallest Idx. currentIdx 
starts is initialized as 0 outside the outer while loop and  inside that while loop we initialize smallest 
idx at currentIdx. Then we use a for loop to find the minimum value in the subarray from currentIdx + 1 
to the end of the array. To find the minimum value in this sub-array with the loop, we compare the value at 
smallestIdx to the current value in the for loop. If the value at smallestIdx is greater than the 
currentValue in the for loop, it means that the smallest value in the sub-array ending for the subarray 
ending at the currentIdx, is actually the currentValue, so we update smallestIdx to the current index. So 
so the if statement updates smallestIdx by comparing the value at the current smallestIdx to the current 
value in the inner for loop. Upon termination of the inner for loop, smallestIdx would be pointing to the 
smallest value in the sub-array that goes from currentIdx + 1 to len(array), so we swap the values at 
currentIdx and smallestIdx, then we increment currentIdx, and go up to the outer while loop. Thus after 
we found the minimum value using the for loop we swap it with the currentIdx aka appendIdx before 
incrementing currentIdx. The reasonwhy currentIdx goes up to len(array) -1 is because this algorithm is 
saying find the minimum value in the rest of the array after currentIdx, and swap this minimum value 
with the value at currentIdx, but if currentIdx is at the last position, there is no remaining rest of 
the array to search through for miniumum element because there is nothing after the last position, 
meaning the array must be sorted and the value at currentIdx, at the last position, is the larges 
value in the array. """

#O(n^2) time (best,average,worst) | O(1) space
def selectionSort(array):
    currentIdx = 0  #index of first number of unsorted sublist, initialize at index 0


    while currentIdx < len(array)-1: #if currentIdx moves to the end of the array, we have finished sorting
        smallestIdx = currentIdx #start the rightward expansion from currentIdx

        for i in range(currentIdx+1,len(array)): #loop through remaining array for smallest value
            if array[smallestIdx] > array[i]: #simple if statement with for loop to find the index of remaining smallest value
                smallestIdx = i               #update smallestIdx each time
        swap(currentIdx,smallestIdx,array)   #swap currentIdx with smallestIdx value when for loop finds the smallest in rest of array
        currentIdx +=1 #unsorted sublist now starts at currentIdx +1
    return array

def swap(i,j,array):
    array[i], array[j] = array[j], array[i]



def selectionSort(array):
	unsortedIdx = 0 # this points to the first number of our unsorted sub array, initialized at start of array
	
	while unsortedIdx < len(array) -1:
		smallestIdx = unsortedIdx #pointer for smallest number in unsorted sub-array, initialized at current start of unsorted subarray
		
		#for loop to find the smallest number in unsorted sublist
		for i in range(unsortedIdx+1,len(array)): #from second number in unsorted subarray to end of list
			if array[smallestIdx] > array[i]:
				smallestIdx = i
		
		#swap smallest number in unsorted subarray with first number		
		array[smallestIdx], array[unsortedIdx] = array[unsortedIdx], array[smallestIdx]
		#no move the beginning of unsorted subarray 
		unsortedIdx += 1
	return array

