"""The question is to write a function that takes in a sorted array of distinct integers and returns the first index in the array that
is equal to the value at that index. In other words, the function should return the minimum index where index == array[index]. If there
is no such index, the function should return -1."""

"""Naive solution where we check if each value is equal to its index in a sorted array of distinct integers. If values are
neither distinct nor sorted, this is the only solution that is guaranteed to work because this solution doesnt use any of these
pieces of information hence its naivete."""
#O(n) time | O(1) space
# def indexEqualsValue(array):
#     for i in range(len(array)):
#         if array[i] == i:
#             return i
#     return - 1


"""Optimal solution based on the fact that the input is a sorted array of distinct integers. As a result if the value at an index is less than 
its index, then all the sorted distinct integers to its left are also less than their index, so explore the right subarray. For example if the 
value at index 3 is 2, then due to distinctedness and sortedness, index 2 can be at most 1 and if index 2 is 1, index 1 can be at most 0. Thus 
there is no point in checking the left subarray if after binary search array[midIdx] < midIdx so look right. Similarly if a value at an index 
is greater than its index, then all the sorted distinct integers to its right are also greater than their indices, so explore the left subarray. 
For example, if the value at index 3 is 4, then due to the distinctedness and sortedness, the value at index 4 will at least be 5 and if the 
value at index 4 is 5, the value at index 5 is at least 6. Thus there is no point in checking the right subarray if after binary search, 
array[midIdx] > midIdx so look left. Lastly if a value is equal to its index, then it might not be the first such value  so check if the 
previous value (to its left) is also equal to its index in which case, explore the left subarray to find the first value that is equal to its
index, otherwise return the current index (since its the mimimum index where index == array[index]). For example, if the value at index 3 is 3, 
then the value at index 2 could be 2 and still maintain the distinctedness and sortedness. So if after binary search array[midIdx] == midIdx, 
then look in the left subarray if array[midIdx-1] == midIdx - 1. If it is, move rightIdx to midIdx-1 and keep checking. If its not, return the 
current midIdx. If no value in the array is equal to its index return -1. 

So the solution to this question hinges on altering binary search to return the minimum index in the array that is equal to the value at that 
index. The first alteration to compare array[middleIdx] to middleIdx (no target value in a bs question, wow) and move based what sortedness 
and distinctedness tell us about the left subarray elements and the right subarray elements. If array[middleIdx] is less than middleIdx, we know 
our answer cannot be in the left subarray so we explore the right subarray by moving leftIdx to middleIdx + 1. If array[middleIdx] is greater 
than middleIdx, we know our answer cannot be in the right subarray so we explore the left subarray by moving rightIdx to middleIdx - 1. 
If array[middleIdx] == middleIdx, middleIdx may not be the minimum such index, so we check if closest left subarray value to middleIdx also 
satisifies our search criteria ie array[middleIdx - 1] == middleIdx -1, and if true, we explore the left subarray (ie continue binary search), 
if not, we know that the current middleIdx must be the minimum such index because if more such indices exist, they would be in the right subarray 
and hence those indices will be greater than the current middleIdx. 

Search For Range is another such question that hinges on clever alteration of binary search in order to get a log(n) time complexity instead of 
linear time complexity. And like that question, an important alteration happens in the step where middleIdx equals our search criteria."""

#O(log(n)) time | O(1) space
def indexEqualsValue(array):
    left = 0                    #initialize left pointer at the beginning of array
    right = len(array) - 1      #initialize right pointer at the end of array

    while left <= right:            #if the left pointer ever passes the right pointer, we're done
        mid =(left + right) // 2    #middle pointer for  binary search technique
        value = array[mid]          #current value (value at middle pointer)

        if value < mid:   #if the current value is less than its index, then all values to its left are also less than their indices
            left = mid + 1   #so explore the right subarray by moving the left pointer
        elif value > mid: #if the current value is greater than its index, then all values to its right are also greater than indices
            right = mid - 1  #so explore the left subarray by moving the right pointer
        else: #if the current value is equal to its index
            if array[mid - 1] == mid - 1: #current value might not be the first, so check the previous value
                right = mid - 1           #if previous value is also equal to its index, explore the left subarray for other such values
            else:                         #if the previous value is not equal to its index, the current value must be the first such value
                return mid          #so return current index
    return - 1    #if no value in the array is equal to its index, then return - 1


"""Same time complexity as optimal iterative solution but a worse space complexity because of the recursive stack. Requires
sorted array of distinct integers"""
#O(log(n)) time | O(log(n)) space
def indexEqualsValue(array):
    left = 0
    right = len(array) - 1
    return indexEqualsValueHelper(array,left,right)

def indexEqualsValueHelper(array, left, right):
    if left > right: #base case
        return - 1

    mid = (left + right) // 2
    value = array[mid]

    if value < mid:
        return indexEqualsValueHelper(array,mid+1, right)
    elif value > mid:
        return indexEqualsValueHelper(array, left, mid - 1)
    else:
        if array[mid - 1] == mid - 1:
            return indexEqualsValueHelper(array,left, mid - 1)
        else:
            return mid


array = [0,1,2,3,4,5,6,7]
print(indexEqualsValue(array))