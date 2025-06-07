"""Given a binary array data, return the minimum number of swaps required to group all 1's present in the array together 
in any place in the array.

Example 1:
Input: [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.

Example 2:
Input: [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.

Example 3:
Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].

Note:
1 <= data.length <= 10^5
0 <= data[i] <= 1

A simple solution is to first count total number of 1's in the array. The reason is that if the 1's were all grouped together then 
a subarray of only 1's would be of a size equal to the total number of 1's in the array. Suppose this count is x, now we need to 
find the subarray of length x of this array with maximum number of 1's. And minimum swaps required will be the number of 0's in the 
subarray of length x with maximum number of 1's which we can obtain by subtracting the maximum number of 1's (in subarray of size x) 
from the total number of 1's ie numberOfZeroes = x - maxOnes. Look at longestRepeatingCharacterReplacement.py for a similar question.
This is a fixed width sliding window question with some reverse thinking. Instead of getting the maxOnes in a sliding window of x and
then subtracting it from the totalOnes (which is the width of our sliding window), we could get the minimum number of 0's in our 
sliding window and the return that number directly.
"""
def minSwaps(data):
    width = 0                #the width of the window
    for val in data:
        if val != 1:
            continue
        width += 1
   
    ones = 0
    for i in range(width):
        val = data[i]
        if val != 1:
            continue
        ones += 1
        
    
    maxCount = ones
    left = 0
    for right in range(width,len(data)):
        if data[left] == 1:
            ones -= 1
        left += 1

        if data[right] == 1:
            ones += 1
        
        maxCount = max(maxCount, ones)
    
    return width - maxCount
    


def minSwaps(data):
    width = 0                #the width of the window
    for val in data:
        if val != 1:
            continue
        width += 1
   
    zeros = 0                   #counting the number of 0's
    for i in range(width):
        val = data[i]
        if val != 0:
            continue
        zeros += 1
        
    
    minCount = zeros
    left = 0
    for right in range(width,len(data)):
        if data[left] == 0:
            zeros -= 1
        left += 1

        if data[right] == 0:                        #counting number of 0's
            zeros += 1
        
        minCount = min(minCount, zeros)
    
    return minCount
    
data = [1,0,1,0,1,0,0,1,1,0,1]
print(minSwaps(data))