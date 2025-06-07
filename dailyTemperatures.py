"""Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] 
is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which 
this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:
1 <= temperatures.length <= 105 ; 30 <= temperatures[i] <= 100 ;

So this is another question that is an application of the next greater element algorithm in monotonicStacks.py. The only'
difference is that if there is no next greater element for the value at any index, we store 0 instead of -1. As such we
initialize our output array with 0's instead of -1's. Next, the final array is supposed to contain the number of days till
the next greater temperature, which simply means the difference in the indices between any value's index and the index of
its next greater temeperature. So while the index that is the stack's peek value is less than the current loop index's value,
the current loop index value is the next greater temperature for the stack peek value, so we pop, calculate the difference
in indices and update the output array at the popped index with the difference. We repeat these operations as long as the
value at index on top of the stack is less than the value at the current loop index and the stack is non-empty. If either
of these is no longer the case, we append the current loop index to the stack.
"""
#O(n) time | O(n) spaces
def dailyTemperatures(temperatures) :
    stack = []
    result = [0]*len(temperatures)
    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            peek = stack.pop()
            diff = i - peek
            result[peek] = diff
        stack.append(i)
    return result