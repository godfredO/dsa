"""This question gives an array of a sorted and shifted distinct integers and a target and asks to find the index at which the target occurs
and if the target is not in the array to return -1. Now because of the shift the array as a whole is not sorted but some parts of it will
be sorted. In vanilla binary search, because we know the whole array is sorted, only compare the target value to the middleIdx value. We 
still do that here, but if the middleIdx isnt the target, how do we move intelligently. After all, we know the array is both shifted and
sorted so some parts of if will the sorted up until the point of the shift. It turns out after calculating the middleIdx, one of the two 
subarrays will be sorted. To check if the left subarray is sorted we check if array[leftIdx] <= array[middleIdx]. If this is so ,
since leftIdx < middleIdx and the array of distinct integers is sorted and shifted, we can conclude that the left subarray is sorted. 
Similarly if array[middleIdx] <= array[rightIdx], we can conclude that the right subarray is sorted since middleIdx < rightIdx and we know 
the array of distinct integers is sorted and shifted.

Anyway because the input array is sorted but shifted one and only one of these subarrays will be sorted based on their pointers comparison 
with middleIdx. So let's say that the left subarray is sorted. If it is, we check if target falls within the left subarray bounds 
ie target >= array[leftIdx] and target <= array[middleIdx]. If the target value falls within the bounds of the left subarray, we explore 
that further, by moving the rightIdx to middleIdx -1. If on the other hand, target does not fall within the sorted left subarray, if it 
exists in the array, it must be in the right subarray so we move leftIdx to middleIdx + 1 and repeat the process till our left and right 
pointers cross. Thus we use middleIdx, leftIdx, rightIdx to find a sorted subarray, determine if the target falls within the sorted subarray 
and if it does, we explore that sorted subarray. If it doesnt we explore the other subarry. Thus we are able to intelligent movements based 
on the discovery of which subarray is sorted and use that sortedness to determine where target might lie."""


"""Recursive solution"""
#O(log(n)) time | O(log(n)) space
def shiftedBinarySearch(array,target):
     return shiftedBinarySearchHelper(array,target,0, len(array) - 1) #call helper with initial left, right pointers

def shiftedBinarySearchHelper(array,target,left,right):
    if left > right: #base case 1
        return -1
    
    middle = (left + right) // 2  #calculate middle pointer
    potentialMatch = array[middle] #value at middle pointer
    leftNum = array[left]          #value at left pointer
    rightNum = array[right]

    #base case 2
    if target == potentialMatch: #check if current middle value is our target
        return middle            #found target, return its index
    #recursive case, exploring subarray based on if subarray is in sorted order and if target is within subarray
    elif leftNum <= potentialMatch: #if left subarray is in sorted order, left could be the same as mid, index eg left=0,right=1, mid=0
        if target < potentialMatch and target >= leftNum: # check if target is within left subarray
            return shiftedBinarySearchHelper(array, target,left,middle -1)  #explore left subarray
        else: #if target is not in left subarray
            return shiftedBinarySearchHelper(array,target,middle + 1, right) #then explore right subarray
    else: #if left subarray is not in sorted order, right must be in sorted order 
        if target > potentialMatch and target <= rightNum: #check if target is within right subarray
            return shiftedBinarySearchHelper(array,target,middle + 1, right) #explore right subarray
        else: #if target is not within right subarray
            return shiftedBinarySearchHelper(array, target,left,middle -1)  #explore left subarray



"""Iterative Solution"""
#O(log(n)) time | O(1) space
def shiftedBinarySearchI(array,target):
    left = 0                 #initialize left pointer
    right = len(array) - 1   #initialize right pointer
    
    while left <= right:    #loop condition
        middle = (left + right) // 2  #calculate middle pointer
        potentialMatch = array[middle] #value at middle pointer
        leftNum = array[left]          #value at left pointer
        rightNum = array[right]        #value at right pointer

        if target == potentialMatch: #check if current middle value is our target
            return middle            #found target, return its index
        elif leftNum <= potentialMatch: #if left subarray is in sorted order
            if target < potentialMatch and target >= leftNum: # check if target is within left subarray
                right = middle -1  #explore left subarray 
            else: #if target is not in left subarray
                left = middle + 1 #then explore right subarray
        else: #if left subarray is not in sorted order, right must be in sorted order 
            if target > potentialMatch and target <= rightNum: #check if target is within right subarray
                left = middle + 1 #then explore right subarray
            else: #if target is not within right subarray
                right = middle -1  #explore left subarray 

    return - 1 #if we ever break out of loop without hitting return middle, then target is not in array





array = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
target = 33
print(shiftedBinarySearchI(array,target))