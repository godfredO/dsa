"""So in this question we have a sorted array and a target,(surprise surprise for a binary search problem),only that unlike other binary 
search problems the integers are not distinct and we are asked to return a list of two elements where the first element is the first index
at which the target number is located and the second element is the last index at which the target number is located. That is to say, the
target number occurs once in the input array, the output array will have the same value for first and second element. If the target is 
repeated multiple times, the output array will have different values for the first and second elements. If the target doesnt occur in the
input array, we are to return [-1 -1]. This question is the same as findFirstAndLastPositionOfElementInSortedArray.py name on leetcode.

The brute / naive force approach is to use binary search to find the target and then use the left boundary/ right boundary technique to find 
the left and right extremities. The binary search step is log(n) but the left boundary / right boundary step is O(n) giving the overall 
algorithm a time complexity of O(n). With that said since we know that the array is sorted (hence the binary search), can we use that
observation to find the left and right extremities in log(n)?

In the optimal solution we apply an altered version of binary search twice; first to find the left extremity and then to find the right 
extremity. Now in a normal binary search algorithm, once we find the target at middleIdx, we are done. But in this altered method, we need 
to check if middleIdx is the left extremity or right extrmeity. If checking for the left extremity, once we find our target at middleIdx, 
we first check if middleIdx is 0. If it is index 0, we know there are no numbers before index 0 so we know we have found the left extremity. 
If middleIdx is not 0, we then check if the preceding number, at middleIdx -1 is also equal to the target. If its not, then again, we know we 
have found our left extremity. If however, the number at middleIdx -1 is also equal to the target, then we know that there could be more 
instances of the target in the left subarray, so we move the rightIdx to middleIdx -1 and repeat binary search again and again until we find 
a middleIdx which contains the target value but whose middleIdx - 1 is not the target. When that happens we know that this new middleIdx is 
the earliest instance of the target and thus the left extremity. So we effectively alter binary search to return the left extremity not just
any index at which the target occurs (this explains why the vanilla binary search question the elements are distinct) . And this alteration
is simply adding a second check whenever we find an instance of the target. And this second check includes checking if middleIdx = 0, t
return middleIdx, if not we check if we have found the left extremity, the left extremity being that index at which the target occurs where
array[middleIdx-1] does not equal the target. So as long as we havent found the left extemeity(middleIdx or middleIdx - 1 != target) we keep 
binary search going by moving middleIdx decidedly left which is done by setting rightIdx = middleIdx - 1.

To find the right extremity, we do something similar but in the other direction. Once we find the target value at middleIdx, we ask if 
middleIdx is equal to len(array) - 1. If it is we know that there are no more numbers after the last index and so this middleIdx must be
the right extremity. If middleIdx is not len(array) - 1, we ask if the next value, the value at middleIdx + 1 is also equal to the target.
If its not, we know we have found the right extremity. If it is we know there could be more instances of the target value to the right of
middleIdx so we explore the right subarray by moving leftIdx to middleIdx + 1 and repeat binary search again till we find a new middleIdx
that contains our target value but whose middleIdx +1 isnt the target value.
In the code we use a boolean to signify if we are looking for the left / right extremity and thus the direction to search in after finding
our target. Also the checks need to be considered sequentially to avod throwing an error, since checking middleIdx + 1 would throw an error
if middleIdx is len(array) -1 same for checking middleIdx -1 if middleIdx is 0. So always check the absolute left/right extremities, 0 and
len(array) - 1 first before checking for the previous or next numbers value. Also we initialize the finalRange at [-1, -1] so that if
the target is not in the input array, we just return that like the question asks. Finally, the modification of binary search here, is
reminiscent of the modification for shifted binary search question. In that question, we make additional checks once we find a sorted 
subarray, in this question we make additional checks once we find the target value. Again intelligent movement based on sorted order.
 """

# def searchForRange(array,target):
#     finalRange = [-1,-1 ] #initial finalRange, return -1,-1 if never found
#     alteredBinarySearch(array,target,0, len(array) - 1, finalRange, True) #call to find left extremity
#     alteredBinarySearch(array,target,0, len(array) - 1, finalRange, False) #call to find right extremity
#     return finalRange

# """Recursive Implementation"""
# #O(log(n)) time | O(log(n)) space
# def alteredBinarySearch(array,target,left,right,finalRange,goLeft):
#     if left > right: #base case
#         return
#     mid = (left + right) // 2
#     if array[mid] < target: #if target is greater than middle value
#         alteredBinarySearch(array,target,mid + 1, right,finalRange,goLeft) #explore right subarray
#     elif array[mid] > target: #if target is less than middle value
#         alteredBinarySearch(array,target,left,mid - 1, finalRange,goLeft) #explore left subarray
#     else: #if the middle value is the target
#         if goLeft: #check if we are going left, if we 
#             if mid == 0 or array[mid - 1] != target: #if we are currently at the start of array or if we found the left most instance of target
#                 finalRange[0] = mid #update left extremity
#             else: #if not at start of array and previous number is another instance of target
#                 alteredBinarySearch(array,target,left,mid-1, finalRange,goLeft) #further explore left subarray
#         else: #if going right instead
#             if mid == len(array) - 1 or array[mid + 1] != target:#check if at the end of array or next number is not equal to target
#                 finalRange[1] = mid #update right extremity
#             else: #if not at end of array and next numbe is another instance of target
#                 alteredBinarySearch(array,target,mid+1,right,finalRange,goLeft) #further explore right subarray

def searchForRange(array,target):
    finalRange = [-1,-1 ] #initial finalRange, return -1,-1 if never found
    alteredBinarySearch(array,target,0, len(array) - 1, finalRange, True) #call to find left extremity
    alteredBinarySearch(array,target,0, len(array) - 1, finalRange, False) #call to find right extremity
    return finalRange

"""Iterative Implementation"""
#O(log(n)) time | O(1) space
def alteredBinarySearch(array,target,left,right,finalRange,goLeft):
    while left <= right: #base case
        mid = (left + right) // 2
        if array[mid] < target: #if target is greater than middle value
            left = mid + 1   #explore right subarray
        elif array[mid] > target: #if target is less than middle value
            right = mid - 1 #explore left subarray
        else: #if the middle value is the target
            if goLeft: #check if we are going left, if we 
                if mid == 0 or array[mid - 1] != target: #if we are currently at the start of array or if we found the left most instance of target
                    finalRange[0] = mid #update left extremity
                    return #we've found left extremity, so return 
                else: #if not at start of array and previous number is another instance of target
                    right = mid - 1 #further explore left subarray
            else: #if going right instead
                if mid == len(array) - 1 or array[mid + 1] != target:#check if at the end of array or next number is not equal to target
                    finalRange[1] = mid #update right extremity
                    return  #we've found the right extremity so return
                else: #if not at end of array and next numbe is another instance of target
                    left = mid + 1   #further explore right subarray

array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
target = 45
print(searchForRange(array,target))