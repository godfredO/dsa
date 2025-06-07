"""
Tags: Sorting, Two Pointer, Medium

Bubblesort is traverse and swap which keeps bubbling largest numbers to the end of the array. You need to keep track of the swaps, here
using isSorted , because if no swaps occur, the array is sorted. If swaps do occur, the array is not sorted yet and you need to traverse and
swap another time. When do swaps occur? Swaps occur when the current element is greater than the next element. Thus we choose our currrent
element index ,i, in a for loop and compare it to the next element at i+1. As such the first time we go through the array, i varies from 0 to
len(array) - 2 (last but one index due to Python zero-indexing) ie for i in range(len(array) - 1), which after end exclusivity ends at the
penultimate array element. Bubble sort thus moves in a rightward direction which is the opposite to insertion sort, which moves leftward. If
the input array is already sorted, we will still do one pass so O(n) time which is the best time for bubble sort, and at the end because no
swap would have been done we break out of the while loop. In the code, the way we handle this is to initialize isSorted to False, then in the
outer while loop, the loop condition is while not isSorted which will evaluate to True whenever isSorted is False. Then inside the outer
while loop, we flip isSorted to True in case the array is sorted as is. Then insde an inner for loop, we check if the current value is greater
than the next value using an if statement. If this if statement evaluates to True, we do a swap and then set isSorted to False. This means we
set isSorted to False every time we swap to values.

Now the reason why bubble sort is so called is because it bubbles the largest value in the array to the end after the first iteration, then
bubbles the second largest value to its correct position after the second position. Thus on the second iteration there is no need to include
the element in the last position because we know the value there is in its correct sorted position after the first iteration. Thus in bubble
sort we can add a small optimization that keeps track of the number of iteration already done and uses that to increasingly reduce the number
of elements we look at on each iteration. On the first iteration, we look at len(array) elements. After the first iteration we only need look
at len(array) - 1 elements. Then len(array) - 2 elements after that and so on and so forth. In the code the way we handle this is to initialize
a counter variable which counts the number of passes done to 0. Then in the inner for loop, we choose our current value as range(len(array) - 1
- counter). The -1 is because the first time counter is 0 and we go up to the penultimate value and then compare with i+1. Upon termination of
the inner for loop, we increment the counter variable, so that the next time we do not go up to the last value we placed. Each iteration compares
up to n values so O(n) times and this iteration is repeated n times for each index till every element has been bubbled to its correct sorted
position for a total of O(n^2) time. Bubble sort happens in-place so constant space. It is important to note that since we compare the current
index value to the next value, the current index should go up to the penultimate position len(array) -1 before optimizing to len(array) - 1 -
counter.
"""


# O(n^2) time | O(1) space  || Unoptimized bubble sort
def bubbleSort(arr):                            # unoptimzed bubble sort; O(n^2) even on pre-sorted arrays

    for passes in range(len(arr)):              # repeat two-pointer correctly place all values
        for left in range(len(arr)-1):          # left pointer of adjacent pairs check of relative positions
            if arr[left] > arr[left + 1]:       # right pointer = left + 1 ; relative position check
                arr[left], arr[left + 1] = arr[left + 1], arr[left]  # swap to bubble larger value
    return arr


# O(n^2) time | O(1) space  || Optimized for O(N) on pre-sorted arrays
def bubbleSort(arr):

    preSorted = True                            # optimization flag for O(n) on pre-sorted array
    for bubbleSwaps in range(len(arr)-1):       # repeat two-pointer for last n-1 positions
        # additional optimization for left in range(len(arr)-1 -bubbleSwaps / bubbleSwaps + 1)
        for left in range(len(arr)-1 - bubbleSwaps):          # left pointer; goes up to penultimate index
            if arr[left] > arr[left + 1]:       # right pointer = left + 1; up to last index
                arr[left], arr[left + 1] = arr[left + 1], arr[left]  # swap to bubble larger value
                preSorted = False
        if preSorted:       # check after bubble swap pass if pre sorted
            break           # if pre sorted, no bubble passes needed
    return preSorted, arr


# O(n^2) time | O(1) space  || Optimized for O(N) on most partially-sorted arrays
def bubbleSort(arr):

    for passes in range(len(arr)-1):       # repeat two-pointer for last n-1 positions
        # re-initialize optimization flag on each pass allows for O(n) on most partially sorted arrays
        swapped = False
        # optimization for left in range(len(arr)-1 -passes); dont include prev bubbled values
        for left in range(len(arr)-1 - passes):  # left pointer; goes up to prev placed idx
            if arr[left] > arr[left + 1]:       # right pointer = left + 1; up to last index
                arr[left], arr[left + 1] = arr[left + 1], arr[left]  # swap to bubble larger value
                swapped = True
        if not swapped:         # if no swap was made during current pass
            break               # break ; array was sorted during current pass
    return arr


# O(n^2) time | O(1) space. Best case time O(n)(sorted input array) since a sorted array is still traversed once
def bubbleSort(array):      # further optimizations; O(N) single pass on already sorted array
    isSorted = False        # this flag is an integral part of
    counter = 0  # counts the number of iterations to exclude the final number in every iteration

    while not isSorted:  # O(n) for each index in the array
        isSorted = True  # a sorted array will still have one iteration, if no swaps are made, will be changed in for loop if
        for i in range(len(array)-1-counter):  # we only need to go to penultimate value , up to O(n)
            if array[i] > array[i+1]:  # compare current value with next value, thus go only to penultimate
                array[i], array[i+1] = array[i+1], array[i]  # swap
                isSorted = False  # if a swap occurs then array wasnt sorted for this iteration
        counter += 1  # after nth iteration, nth number from the end is in its correct position
    return array


# O(n^2) time | O(1) space. Best case time O(n)(partially sorted input array) since a sorted array is still traversed
def bubbleSort(arr):    # improved implementation of optimizations; O(N) on most partially sorted arrays

    for n in range(len(arr)-1, 0, -1):   # n is current index to correctly position (last to first)
        # re-initialize flag on each pass to False to track swaps for improvement on partially sorted arrays
        swapped = False  # flag to check if we bubble anything or not to correctly place current index n
        for i in range(n):  # left index to consider for current index n ; span under consideration
            if arr[i] > arr[i+1]:  # goes to len(arr)-1
                swapped = True      # set flag to True when swap occurs ie additional passes needed
                arr[i], arr[i+1] = arr[i+1], arr[i]  # this is bubbling the largest up to index n
        if not swapped:  # if no bubbling was done for current index n, then everything is sorted
            break
    return arr


array = [1, 3, 6, 2, 2, 7, 9, 1, 77, 4, 234, 0, 2]
array = [3, 9, 77, 234]
print(bubbleSort(array))
