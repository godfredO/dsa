"""Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest 
element in the matrix. Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
 

Constraints:
n == matrix.length == matrix[i].length ; 1 <= n <= 300 ; -109 <= matrix[i][j] <= 109 ;
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2

BRUTE FORCE: Here we literally take every element from matrix and sort them and then return k-1th element, as 
indexing starts from 0 in our Python. Time: O(n² * (log(n²)). Just like the brute force solution in 
kthSmallestNumberInMultiplicationTable.py. 

We could also implement a heap solution like in kthSmallestNumberInMultiplicationTable.py and store row and column
indices. We have that solution here too. The logic is similar to kthSmallestInMultiplicationTable.py.

BINARY SEARCH: Let's take advantage of that fact that each row is sorted. So one of the few things we know about 
this matrix is that top left right and the bottom right are going to be minimum and maximum respectively, so that 
is the search space of binary search. So we can take a guess mid value, and for that value we're going find the 
number of values in the array that are less than or greater to it. The kth smallest element has exactly k elements
that are less than or equal to it. To do this, we could go row by row and count the number of values that are less
than or equal to our guess mid value and this linear approach is simply a twist of the searchInsertPosition.py brute
force linear solution. If a row is [1,2,2,2,3], there are 4 values that are less than or equal to 2 meaning that we
modify the linear searchInsertPosition.py algorithm to return the minimum index whose value is greater than the mid
value (instead of minimum index whose value is greater or equal than mid ie here its index 4, val= 3). Let's call 
this function searchFinal(). Note that there is an inbuilt Python function bisect_right() which equals searchFinal() 
and another function bisect_left() which matches searchInsertPosition.py. Now, since each row is
actutally sorted, we can write searchFinal() itself as a binary search function instead of a linear function. Other 
than improving searchFinal() using binary search, there is no clever optimization that will allow us to find the 
number of elements in a row less than or equal to mid value in constant time, like we have seen in other kth smallest 
binary search questions. If we use the linear searchFinal() algorithm it means for each smallest element guess, we
do a O(n^2) operation, whiles if we use the binary search version, we do O(n*log(n)) operation ie we repeat binary
search (log(n)) for each row. 

.


"""

"""Brute force solution"""
#O(n^2*log(n^2)) time | O(n^2) space
def kthSmallest(matrix, k) :
    temp = []
        
    for row in matrix:
        temp.extend(row)
    temp.sort()
    return temp[k-1]


"""Merge-sort heap solution"""
#O(kn*log(n)) time | O(n) space
from collections import heapq
def kthSmallest(matrix, k) :
    rows , cols = len(matrix) , len(matrix[0])
    heap = [(matrix[rowIdx][0], rowIdx, 0) for rowIdx in range(rows)]   
    heapq.heapify(heap)                      

    for _ in range(k):
        val, rowIdx, colIdx = heapq.heappop(heap)     
        nxt = colIdx + 1                   
        if nxt < cols:                 
            heapq.heappush(heap, (matrix[rowIdx][nxt], rowIdx, nxt))    
    return val     
    

"""Binary-Search Solution"""
#O(nlog(n)*log(n^2))  time | O(1) space - searchFinal() using binary search
#O(n^2*log(n^2)) time | O(1) space - searchFinal() using linear search
def kthSmallest(matrix, k) :
    left, right, = matrix[0][0], matrix[-1][-1]   #min , max of search space
    
    while left < right :
        mid = (left+right) // 2
            
        if countLessOrEqual(matrix, mid) >= k:
            right = mid
        else:
            left= mid + 1
    return left

def countLessOrEqual(matrix, mid):
    count = 0
    for rowIdx in range(len(matrix)):
        count += searchFinal(rowIdx, matrix, mid)
    return count

#O(n) time | O(1) space - searchFinal() using binary search
def searchFinal(rowIdx, matrix, target):
    nums = matrix[rowIdx]
    idx = len(nums)
    for i,num in enumerate(nums):
        if num > target:
            idx = i
            break
    return idx 


#O(log(n)) time | O(1) space  - searchFinal() using binary search
def searchFinal(rowIdx, matrix, target):
    nums = matrix[rowIdx]
    left, right = 0, len(matrix[rowIdx])
        
    while left < right:
        mid = left + (right - left) // 2
        if condition(nums, mid, target):
            right = mid
        else:
            left = mid + 1
    return left
    
def condition(nums, mid, target):
    return nums[mid] > target