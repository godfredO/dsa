"""This question gives an array and asks to find and return indices representing the smallest subarray that needs to be sorted in the input
array in order for the entire input array to be sorted in ascending order. The question can also be rephrased as compared to the sorted array 
which indices in the input array represents the subarray (adjacent numbers), that needs to be sorted in order to have the input array match 
the sorted version . If the array is [1,2,4,3,5,1,5], then the subarray from index 1 to index 5 needs to be sorted when compared to the 
sorted array [1,1,2,3,4,5,5]. We are also asked to return [-1, -1] if the array is sorted. When the corresponding indices of the input array
and its sorted counterpart are compared, the answer contains the minimum and maximum index in input array that dont match the sorted version.
Thus this subarray contains both the minimum and maximum values that are out of place in the input array, which in this case will be the second 
1 and the second 5. 

Thus to solve this problem, we find all the numbers that are out of place. Of these, we track the smallest and the largest numbers that are 
out of place. With the smallest number, iterate from the beginning of the array to find what its final position i in a sorted array would be. 
For the largest number iterate from the end of the array to find what its final position j will be in a sorted array. Return [i,j], which 
represents the final sorted indices of the minimum and maximum values that are out of place when compared with the sorted array. Thus this
final sweep to find final sorted indices is an application of the proximity uncentered patter ie decouple and repeat. 

To determine if a number is out of place we compare its value to its neighbors using a variation of the left/right boundary technique which 
itself is a variation of getNeighbors() function often used in graph problems. We also employ clever comparison with +/- inf, and when we
find a value is out of order, we determine if its the max / min out of order. The out of place helper function handles the edge cases of 
index 0 and index len(array) - 1, since these only have a single neighbor, before the general case of a middle value which has two 
neighbors. A number is out of place if it is less than the preceding value in the array or greater than the next value in the array.
This is because for sorted order, the middle value can be equal to or greater than the preceding value and equal to or less than the next
value. Once we have the min/max out of order values, its time to find their final sorted indices and return that as the answer.

To determine the final sorted indices for min/max out of place values, looping from front/back, we check if the value at the current index 
will still be at that index in the sorted array. Thus for the min value out of place, we start at index 0 and as long as the current value 
is less than or equal to min out of place, min out of place's sorted index is to the current value's right so we increment the index until 
we break out of the loop. Similarly for max out of place, we start from the end of the array and ask if the value at the current index will 
still be in this position in the sorted array ie is the value at the current index greater than or equal to max out of place. If it is, we 
know that max out of place's final sorted position is somewhere to the left so we decrement the current index. 
Thus if we come to a value that is greater than min out of place, then we know that index is the final sorted position of min out of place
value. Similarly if we come to a value that is less than max out of place, we know that index is the final sorted position of max out of 
place. To check if the array is sorted, we check if min out of order is still at +inf (or max out of order is still at -inf). If it is, we 
return [-1, -1] and we do this check before we start trying to find the left/right boundary of the unsorted subarray. The reason is that we 
go from sorted to unsorted by swapping at least a pair of values so there will always be min and max out of place values if array is not 
sorted. """

#O(n) time | O(1) space
def subarraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")

    #loop through the entire array to find out-of-order numbers
    #we only store the minOutOfOrder and maxOutOfOrder at the end of the loop
    for i in range(len(array)): #use range indices since out of order-ness depends on index too
        num = array[i]
        if isOutOfOrder(i,num,array): #if current number is out of order, depends on index, num, neighbors
            minOutOfOrder = min(minOutOfOrder,num)
            maxOutOfOrder = max(maxOutOfOrder,num)
            
    #edge case, where input array is already sorted, we never update initial minOutOfOrder        
    #only one check needed since we know if one number is found out of order, another number will be too
    #thus if we didnt update one initial valuee, we didnt update the other initial value either
    if minOutOfOrder == float("inf"):
        return [-1.-1]
    
    #find the final positions of minOutOfOrder and maxOutOfOrder, can use for loop and break statement too 
    subarrayLeftIdx = 0 #to find final position of minOutOfOrder, start looping from beginning of array
    while minOutOfOrder >= array[subarrayLeftIdx]: #if current number will still be here in sorted version
        subarrayLeftIdx += 1 #advance

    subbarrayRightIdx = len(array) - 1 #to find final position of maxOutOfOrder, start looping from end of array
    while maxOutOfOrder <= array[subbarrayRightIdx]: #if current number will still be here in sorted version
        subbarrayRightIdx -= 1 #advance
    
    return [subarrayLeftIdx,subbarrayRightIdx]


def isOutOfOrder(i,num,array):
    #we want to compare the number to its adjacent numbers in the list, if it has two neighbors
    if i== 0: #first number has one neighbor, number after it
        return num > array[i+1] #array[index 0] can be equal or less than array[index 1] but if its greater than index 0 is out of place
    if i == len(array) - 1: #last number has one neighbor, number before it
        return num < array[i-1] #last index value can be equal or greater than penultimate value. If last index value is less its out of place
    return num> array[i+1] or num < array[i-1] #otherwise, compare to both neighbors. Out of place is greater than preceding or less than next


array = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
print(subarraySort(array))