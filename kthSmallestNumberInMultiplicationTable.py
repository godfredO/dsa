"""Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat 
where mat[i][j] == i * j (1-indexed). Given three integers m, n, and k, return the kth smallest element in the m x n 
multiplication table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.

Example 2:
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.

Constraints:
1 <= m, n <= 3 * 104
1 <= k <= m * n

Take a 3x3 multiplication table, where the first row values are the multiples of 1 (1*1,1*2,1*3);the second row values
are the multiples of 2 (2*1,2*2,2*3); and the third row values are the multiples of 3 (3*1,2*2,3*3). The question asks
to return the kth smallest number in the mxn multiplication table. Now for the 3x3 table, a sorted list of all the 
elements in the table are [1,2,2,3,3,4,6,6,9] and if k=5, the 5th smallest value is value 3. Now how do we find this
answer. The brute force approach would be to create a list of the entire table elements, sort it and return the element
at index k-1. An example of a sorting algorithm that can be used is heap sort. I mention this because it bears some
significance when comparing to the other solutions. Specifically we have to generate all the elements of the 
multiplication table before feeding this list to the sorting algorithm. The loop to generate all table elements will be 
m*n, and the values will be stored in an m*n array,  followed by m*nlog(m*n) sorting step giving a total time complexity 
of O(m*nlog(m*n)) and a space complexity of O(m*n). The kth smallest number will be sortedArray[k-1].

Now, do we need to generate all m*n values, sort them before returning the value at iindex k-1? Well we dont have to, and
the intuition behind this actually comes another sorting algorithm, merge sort. You see, we have to realize that according
to the question, every row in the multiplication table contains the multiples of the row number. Row 1 contains [1,2,3] 
for a 3x3 matrix. Row 2 contains [2,4,6]. Row 3 contains [3,6,9]. In otherwords, each row is a sorted array and we can
merge th m sorted arrays using merge sort. If we want the first element of the merged sorted array, we would compare all
the values at index 0 of each row and choose the minimum value. To choose the minimum of m values, we can use a heap, but
unlike solution one (assuming heap sort is our chosen sorting algorithm), the heap only needs to hold one value from each
row ie m values instead of m*n values. Now we could store indices for the current values of each row that is in our heap,
but because this is a multiplication table, and we know that multiplication is simply repeated addition, we can generate
the next element by adding the row number to the current value from that row. So we initialize our heap with (1,1), (2,2)
(3,3) where the first element is the value we are comparing and the second value is the row number we use for adding the
next value from that row. So we will pop from our heap, exactly k times to find the kth smallest number. So we first pop
(1,1) and add 1+1=2 so (2,1) as the next value from row 1. This way our heap will contain (2,1),(2,2), (3,3). So the next
number we pop is (2,2) so we add (4,2) so that the heap contains (2,1),(3,3),(4,2). Then the 3rd smallest value is popped
so (2,1) and we add 2+1= 3 , (3,1) so that the heap now contains (3,3),(3,1),(4,2). So we pop exactly k times, and the kth
popped value is our kth smallest element. So we first take in m values, heapify them which is O(m), popping from the heap
is O(mlog(m)), pushing onto the heap is O(mlog(m)). So the overall space complexity is O(m) and the time complexity is 
O(k*mlog(m)) and both are improvements over sorting all the elements in the multiplication table, (idk why leetcode says 
pop and push are mlog(m) instead of O(log(m))).

The optimal solution uses binary search, specifically by posing the question in the form of the minimum value for which 
a condition function returns True. The first thing to realize is that the search space is [1,m*n] ie the lowest possible
multiplication value is 1*1 and for an m*n table, the maximum value is m*n. So we start with the left pointer at 1 and 
the right pointer at m*n, calculcate our mid, but what do we do with our mid. Well if we had our sorted array of table 
elements such as [1,2,2,3,3,4,6,6,9], we realize that the kth smallest element has exactly k values that are less than 
or equal to it. In fact all values greater than the kth smallest elements will have more than k values that are less 
than or equal. So we can say that the kth smallest element in the multiplication table is the minimum value for which 
the condition "number of elements smaller than or equal to is greater than or equal to k" is True. So that is what we 
do with our guess value, mid. We go through each row of the multiplication table and count how many elements are less 
than or equal to it. 

Now this poses two questions. First, what if our mid value is not in the mulitplication table. Second, won't it be 
inefficient to go through the entire multiplication table and count the number of elements that are less than or equal 
to the mid value? Let's address the second question first. You have to realize that for any row (1-indexed) the values 
are actually row*1 , row*2, row*3, ..., row*n. Secondly say our guess mid value is say 5, then we know that in a 3x3 
table, each row has only 3 values, so for each row the number of values that are less than or equal to our mid value is 
at most 3. So for row 1, we know that 1*1, 1*2, 1*3 are all less than 5. Now for any row, we dont actually have to do 
any counting, because we realize that we can get the number of values that are less than or equal to our mid value, by 
floor dividing with the row number. So for row 2, 5//2 is 2 ie 2*1, 2*2 are less than 5 but not 2*3. So for any guess
mid value, we can go through each row and take the minimum of the the number of columns, n and the floor division of 
the mid value by the row number to yield the number of values in that row that are less than or equal to mid. And if 
the total number of values in the table less than or equal to our mid value is greater than or equal to k, we move our 
right pointer to mid (find minimum True value) otherwise we move left pointer to mid + 1 (find a value big enough to 
yield True for our condition function). 

The second pertinent question is whether we can end up with a final value that is not in the multiplication table. And 
the answer is no. Say we start with left pointer of 1 and right pointer of 9 for our 3x3 table, so the mid guess value 
is 5. We find that there are 6 values in the table less than or equal to 5. Remember that our question is posed as the 
minimum value for which the condition function is True. So when we move the right poiter to mid, our algorithm will also 
find the number 4 which is in our table and also has 6 values that are less than or equal to and that is still not our 
answer. The algorithm will also find 3 which has 5 values that are less than or equal to it, and that will be the answer. 
In otherwords, for any mid value that satisfies our condition but isnt in the table, the algorithm, will also find mid-1 
or mid-2 etc which also satisifies the condition in the same way but which is actually in the multiplication table. Since 
the condition function is O(m), and the binary search is O(log(m*n)), but no space is used, the overall time complexity 
is O(m*log(m*n)) and a space of O(1).
"""


"""Brute Force approach"""
#O(mnlog(mn)) time | O(m*n) space
def findKthNumber(self, m, n, k):
    table = [i*j for i in range(1, m+1) for j in range(1, n+1)]
    table.sort()
    return table[k-1]

"""Merge-sort heap solution"""
#O(k*mlog(m)) time | O(m) space
from collections import heapq
def findKthNumber(self, m, n, k):
    heap = [(i, i) for i in range(1, m+1)]   #(value, rowNumber)
    heapq.heapify(heap)                      

    for _ in range(k):
        val, row = heapq.heappop(heap)     
        nxt = val + row                    
        if nxt <= row * n:                 #m*n table, so n values from each row, if nxt > row*n, nxt not in table
            heapq.heappush(heap, (nxt, row))    
    return val              #we can access val outside for loop because variables are function-scoped not block scoped in Python

"""Binary search optimal solution"""
#O(m*log(m*n)) time | O(1) space
def findKthNumber(m, n, k):
    left, right = 1, m*n

    while left < right:
        mid = left + (right - left) // 2

        if condition(mid, m,n,k):
            right = mid
        else:
            left = mid + 1
    return left

def condition(mid, m, n, k):
    count = 0
    for row in range(1,m+1) :
        count += min(n, mid // row)
    return count >= k
