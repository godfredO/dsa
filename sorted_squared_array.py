"""The question gives a non-empty array of integers that are sorted in ascending order and asks to return a new array of the same
length with the squares of the original integers also sorted in ascending order. Now we are told a non-empty array of integers,
so without further information we know that the integers can be negative, 0, positive. Now if the numbers were only positive and 
zero, then we could iterate through the array square each element and append to some array because we know that if positive numbers 
are sorted in ascending order then their squares will also be in the same order. However, if we add negative negative numbers then
the sorted order of the array and the sorted order of the squared array will differ. This is because the it is possible for example
that the most minimum negative number eg -100 will have a bigger square than the largest positive number eg 99. Thus we need to
compare the absolute values of the elements in order to make the correct sorted order for their squares. This is exactly what the
first solution does where we use a left and right pointer to iterate through the array from either end. If there are negative numbers
in the sorted array, the left pointer will start from the most minimum negative number and the right pointer will srtart from the 
largest positive number. We compare their absolute values and append the larger value to our output array and increment/ decrement the
chosen pointer for left/right pointer. In this question if there are odd number of elements the pointers will meet but should not cross, 
so using a while loop the condition is while left <= right. Since we append the square of the largest absolute number first, we will need 
to reverse the squared array at the end before returning. The other solutions avoid the reverse step by initializing a full-size squared 
array and filling it from the back, but the time complexities are all the same. """

#O(n) time | O(n) space
def sortedSquaredArray(array):
    l, r = 0, len(array) - 1
    squared = []

    while l <= r: #O(n)
        if abs(array[l]) > abs(array[r]):
            squared.append(array[l]**2)
            l +=1
        else:
            squared.append(array[r]**2)
            r -= 1
    return squared[::-1] #O(n)




def sortedSquaredArrayI(array):
    newArray = [0 for _ in array]

    l ,r = 0, len(array)- 1
    i= len(newArray) - 1

    while l <= r:
        if abs(array[l]) > abs(array[r]):
            newArray[i] = array[l] * array[l]
            l += 1
        else:
            newArray[i] = array[r] * array[r]
            r -= 1
        i -= 1
    return newArray



"""
The negative number with the largest squared value will be on the right most end. The positive number
with the largest squared value will be on the left end. Thus if you compare for which one is larger, between
the leftmost and rightmost then you are assured of never meeting a larger number. Thus it is neccessary for the
solution to test for the largest value as it moves both pointers.
"""


def sortedSquaredArrayII(array):
    newArray = [0 for _ in array]

    l, r= 0, len(array) - 1

    for i in reversed(range(len(newArray))):
        if abs(array[l]) > abs(array[r]):
            newArray[i] = array[l] * array[l]
            l +=1
        else:
            newArray[i] = array[r] * array[r]
            r -= 1

    return newArray



array = [-2,-1,0,4,4,5,6,8,9]
print(sortedSquaredArrayII(array))