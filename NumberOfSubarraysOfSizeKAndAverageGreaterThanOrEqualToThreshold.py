"""Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater 
than or equal to threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have 
averages less than 4 (the threshold).

Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.


So this is a fixed width sliding window problem. Basically we move our right pointer until we have a window of size k, and as
we move our right pointer, we add the current right pointer value to a total. So when the window size reaches k, we calculate
the average, and if this average is greater than or equal to the threshold, we increment a result variable. Whether this is
the case or not, we still advance our left pointer by removing the current left value from our total and incrementing the left
pointer.
"""

def numOfSubarrays(arr, k, threshold):
    left = 0
    total = 0
    result = 0

    for right in range(len(arr)):
        total += arr[right]
        
        if right + 1 - left == k :
            avg = total / k
            if avg >= threshold:
                result += 1
            total -= arr[left]
            left += 1

    return result


arr = [11,13,17,23,29,31,7,5,2,3]
k = 3 
threshold = 5
print(numOfSubarrays(arr, k, threshold))