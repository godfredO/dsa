"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m ; nums2.length == n ; 0 <= m <= 1000 ; 0 <= n <= 1000 ; 1 <= m + n <= 2000 ; 
-10^6 <= nums1[i], nums2[i] <= 10^6

So the two gives us two sorted arrays and asks us to return the median of the two sorted arrays. The naive approach
would be to merge the two solutions using merge sort and return the median value. The length of the merged sorted
array will be m+n and if we use two pointers to merge them the time and space complexity of the merge operation will
be O(m+n). If the total length is odd, the median is the value at (m+n)//2 of the merged array ie the middle value.
If the total length is even, the median will be the average of the (m+n)//2 and the ((m+n)//2)-1. That is if total
length is 3, the median is at index 1; if total length is 4, median is the average of index 1 and 2 values of the 
merged arrays.

But do we need to merge the arrays? The answer lies in looking at what the median is. The median is the middle value
of the array, in otherwords, the median divides the array into two halves. If there are 13 elements in the array,
the median will be the 7th value, since it divides the array into two partitions of the same size. The left partition
will have 6 elements, the right partition will also have 6 elements. Now say the array has 12 elements, then when we
partition into two equal size halves, we will have 6 elements in the left partition, 6 elements in the right 
partition and in this case, the median will be the average of the rightmost element in the left partition and the 
leftmost element in the right partition. With this understanding, we can use binary search to simulate partitioning 
the two sorted arrayswithout actually having to merging them first. 

So when we partition the arrays, we want the left partition to be of size total // 2. So if the total length is 13
we want the left partition to be 13//2 , 6. So a very important point about this algorithm is that we have to apply
binary search to the shorter of the two arrays, calculate our mid, which will be the last index of the shorter 
array that goes into the left partition. So if mid=4, then we know that we only need add 2 elements from the longer
array to make up a left partition of 6. Why do need to implement binary search on the shorter array. Well the left
partition could include elements from only the short, only the long, some of the short and some of the long or all 
of the short and some of the long. Thus since the left partitions of both arrays must add up to total // 2, we use
the shorter array for binary search to ensure it works in case where the left partition contains all of the shorter
array and some of the longer array. Also since both arrays are sorted, we know that the left partitions will start
from index 0 to some index in either array. Thus we use binary search to compute mid, the size of the left partition
for the shorter array and subtract that from total // 2 to get the size of the left partition for the longer array.

Now the next question is, how do we know if we found the left partition or not. Well we are simulating partitioning
a merged sorted array without actually merging the arrays. Meaning every element in the left partition must be
less than every element in the right partition. So say that shorter[leftEnd], shorter[rightStart], longer[leftEnd],
longer[rightStart] represents the last elements in the left partitions of either array and the first elements in
the right partitions of either array. Since shorter[leftEnd], shorter[rightStart] are in the same sorted array we 
know that shorter[leftEnd] <= shorter[RightStart], and similarly longer[leftEnd] <= longer[rightStart]. But our
partition is only correct if shorter[leftEnd] <= longer[rightStart] and longer[leftEnd] <= shorter[rightStart]. In
otherwords, the last element of either array's left partition must be less than or equal to the first element of 
either array's right partitions. If this is the case, we know that the partition is correct. In that case if the 
total length is odd, we return the min(shorter[rightStart],longer[rightStart]) since the median will be the value 
that comes after the end of the left partition. If the total length is even, we return the average of the 
max(shorter[leftEnd], longer[leftEnd])  and min(shorter[rightStart], longer[rightStart]) siginifying the last 
element (rightmost) of the left partition and the first element (leftmost) of the right partition. But what if
the partition is incorrect. How do we intelligently move according to sorted order? For this we compare 
shorter[leftEnd] and longer[rightStart]. If shorter[leftEnd] > longer[rightStart], then we need to shorten the 
left partition of the shorter array a bit, so we move the right pointer to mid - 1, otherwise we need to make
it longer by moving left pointer to mid + 1.

A few implementation details. We first need to declare references to the shorter of the two arrays, in the code
here, we have A for shorter and B for longer. Secondly, we are assured to have a median, so we wrap the binary
search logic in while True since we know that we will hit the return statements at some point. Next, when we
calculate mid, we are calculating the index of the last element in the left partition of the shorter array, but
since indices are 0-indexed but the lengths we use for calculating total length are 1-indexed, in order to 
generate the index of the last element in the longer array's left partition we have to do half - mid - 2 where
the -2 takes out the difference of 1 between the last index and the length of an array for both arrays, and
half = totalLength//2. So if shorter is length 6, we know its last index will be 5 and if longer is length 10, 
we know its last index will be 9. So if say our mid is index 3, (index 3 is the fourth element), we get 
(10+6)//2 - 3 - 2 = 3 as the index of the last element of the longer arrays left partition. Also note that when 
we calculate shorter[leftEnd], shorter[rightStart] = shorter[leftEnd + 1] and longer[leftEnd] and 
longer[rightStart] = longer[leftEnd + 1], so just in case we go out of bounds, if leftEnd(shorter) or 
lefEnd(longer) < 0 we assign -inf and similarly if rightStart(shorter) >= len(shorter) or 
rightStart(longer) >= len(longer), we assign +inf to simplify the code logic and comparisons. 





"""
def findMedianSortedArrays(nums1, nums2):
    A = nums1 if len(nums1) <= len(nums2) else nums2    #A is the shorter array
    B = nums1 if len(nums1) > len(nums2) else nums2     #B is the longer array

    total = len(nums1) + len(nums2)
    half = total // 2

    left, right = 0, len(A) - 1
    while True:
        i = (left + right)// 2
        j = half - i - 2     #the -2 is to offset 0-indices for both A, B
        
        Aleft = A[i] if i >= 0 else float("-inf")
        Aright = A[i+1] if i+1 < len(A) else float("inf")
        Bleft = B[j] if j >= 0 else float("-inf")
        Bright = B[j+1] if j+1 < len(B) else float("inf")

        if Aleft <= Bright and Bleft <= Aright:  #if we found valid partitions
            if total % 2:                   #odd
                return min(Aright,Bright)
            else:                           #even
                return ( max(Aleft,Bleft) + min(Aright,Bright) ) / 2
        elif Aleft > Bright:
            right = i - 1
        else:
            left = i + 1