"""Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest 
product. The issue with this question is the situation where we have two negative numbers which will multiply to a positive number
which could yield the maxProduct eg [-2,3,-4,-1]. The answer is 24 for the subarray [-2,3,-4]. So the question is how do we know at
-2 or 3, if there is some negative number coming that would make it worthwhile to extend the subarray. The complication that negative
numbers introduce is that when we have negative numbers the subarray product oscillates between a maximum and a minimum eg for array
[-1,-2, -3, -4], if we just multiplied all the numbers as we go through the array, we would have subarray products of [-1,2,-6, -24].
So how do we use this oscillation to find the maximum subarray product which in this case would actually be the entire array?. Well 
we have to store both the minimum subarray product and the maximum subarray product at each index for the subarray ending at that 
index. 
So in the code we initialize the runningMax and runningMin to both be 1. We also initialize the maxProduct variable to the the 
maximum number in the array. Then we loop over the array, calculate two temporary variables, one multiplies the current number with
the runningMax and the other multiplies the current number with the runningMax. Then to update the runningMax, we update the
comparison with tmp1, tmp2 and array[i], followed by a min comparison of thes same numbers to update runningMin. We add the curent
number because we could have a 0 somewhere in the middle that would reduce the runningMax to 0 but if a positive number occurs after
the 0, that would be the new runningMax. So after updating runningMax, we do a final maximum comparison between maxProduct and 
runningMax, to update maxProduct. Upon termination of the loop, we return maxProduct.
"""

def maxProduct(array):
    runningMax = 1
    runningMin = 1
    maxEver = max(array)
    for i in range(len(array)):
        tmp1 = runningMax * array[i]
        tmp2 = runningMin * array[i]
        runningMax = max(tmp1, tmp2, array[i])
        runningMin = min(tmp1, tmp2, array[i])
        maxEver = max(runningMax, maxEver)
    return maxEver



array = [2,3,0,4]
print(maxProduct(array))