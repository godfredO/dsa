"""A fundamental idea in sorting everywhere is that an array with a single element is sorted. And to add a new element to a sorted array, you
compare the element to the elements in the sorted array, back to front, until the new element is in its correct position (like three largest 
numbers question). These two ideas form the foundation of the insertion sort algorithm. We start with a tentatively sorted sub-array consisting 
of only the first element and we iterate through the rest of the array starting from the second element. The outer loop is going through the 
rest of the array, the inner loop is comparing the current element in the outer loop to the elements in the tentatively sorted sub-array and 
doing swaps until the current element in its correct sorted position in the tentatively sorted sub-array. Inside the inner loop as we swap the 
current element, we update its index in the tentatively sorted sub-array, making sure it doesnt go out of bounds on the left ie index 0. We do
a swap whenever the value we are placing is less than the value in the tentatively sorted sub-array we are comparing with. So the current index
in the outer loop is i, so we initialize an 'compare index', j as i, and we say that as long as j > 0 and array[j] < array[j-1], we swap the
values at j and j-1. The first comparison will thus be between the current value in the outer loop and the last value in the tentatively sorted
sub-array. Then we decreement the 'compare index', j to reflect the new position of the outer loop value in the sorted sub-array and we repeat
the comparison, shifting the current value left in the sorted sub-array each time we find that it is less than the value before it. When the
while loop breaks either because j == 0 or array[j] >= array[j-1], the current value would be in its sorted position inside the sorted subarray.
After the conclusion of the outer loop, we would have compared each element to the values in the tentatively sorted sub-array and moved each 
element to its final sorted position. Since both loops, the outer loop for choosing the current value, and the inner loop for inserting the 
current value into the tentatively sorted sub-array, run in O(n), the total time complexity is O(n^2) and since we are swapping in-place inside 
the inner loop, we don't use auxilliary space, so O(1) constant space complexity. """

#O(n^2) time - Worst , O(n) time - if sorted | O(1) space
def insertionSort(array):
    for i in range(1,len(array)): #start at index 1, second element so that we can compare
        j = i #index of number we are trying to insert
        while j > 0 and array[j] < array[j-1]: #after while loop index 0 to i is sorted
            swap(j,j-1,array) #swap into correct order
            j -= 1 #each swap decreases the index by one until number is in sorted order
    return array


def swap(i,j,array):
    array[j], array[i] = array[i], array[j]


array = [2,58,3,89.3,533,3,6,8,0,3]
print(insertionSort(array))