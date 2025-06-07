"""Given an array, rotate the array to the right by k steps, where k is non-negative.
Example 1:                                                              Example 2:
Input: nums = [1,2,3,4,5,6,7], k = 3                                    Input: nums = [-1,-100,3,99], k = 2
Output: [5,6,7,1,2,3,4]                                                 Output: [3,99,-1,-100]
Explanation:                                                            Explanation: 
rotate 1 steps to the right: [7,1,2,3,4,5,6]                            rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [6,7,1,2,3,4,5]                            rotate 2 steps to the right: [3,99,-1,-100]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

This is the array version of the linked list question, shiftLinkedList.py. Review the notes on that question. So the naive approach is to
use extra space in the form of an auxilliary array and copy each element in the input array to its final position in that auxilliary array.
So for example 1, index 0 of the input will end up at index 0 + k; 0 + 3 = 3 of the auxilliary array. The same logic holds for index 1, 
which goes to index 1 which goes to index 1 + 3 = 4, index 2 which goes to index 2 + 3 = 5 and index 3 which goes to index 3 + 3 = 6 of the
auxilliary arrray. But at index 4, this calculation will yield index 4 + 3 = 7 but this is obviously out of bounds and what we want is to 
get index 0 as the answer ie we want the shifted array to wrap around itself. Whenever we need an index to wrap around we modulo divide by
the length of the input array so index (4+3) % 7 = 7 % 7 = 0. And of course this yields the right answer for the previous calculations also,
ie index (0 + 3) % 7 = 3. So that is the naive approach. We go through the array, calculate the new index for each value, copy it to that 
new index of an auxilliary array and at the end, we can copy from the auxilliary array to the input array as a way of modifying the input
array. But do we need to use an auxilliary array? The answer is no. 

The optimal solution improves the space complexity by doing the shifting in place. The first observation is that if we reverse the array,
by swapping the values, with a left, right pointer while loop, we get [7,6,5,4,3,2,1]. Now this is not the final answer but we can realise
that the first k elements and the remaining elements are reversed when compared to the actual answer ie 7,6,5 vs 5,6,7 for the first k 
elements and 4,3,2,1 vs 1,2,3,4 for the remeaining elements. So we have to reverse the first k elements ie index 0 to k - 1 of the reversed
array and then we have to reverse the remaining elements ie from index k to len(array) - 1 of this reversed array. And just like that we
have the answer [5,6,7,1,2,3,4]. And just as a reminder we still have to get the actual offset by modulo dividing k by the length of array.

A final thing here, is that we are assured that k will be non-negative integer ie 0 or positive. What changes if k could be negative?
Take inspiration from shiftedLinkedList.py where k is simply an integer. Next try leetcode questions (or use lintcode for question)
Rotate List , Reverse Words in a String , Reverse Words in a String II. 

"""
#O(n) time | O(n) space - Naive or brute force approach
def rotateArray(nums, k):
    numsLen = len(nums)
    auxilliary = [None]*numsLen

    for i in range(len(nums)):
        j = (i+k) % numsLen
        auxilliary[j] = nums[i]
    
    for i in range(len(auxilliary)):
        nums[i] = auxilliary[i]
    


def rotateArray(nums, k):
    k = k % len(nums)             #calculate the actual shift distance or offset
    swap(nums, 0, len(nums) - 1)  #reverse the whole array
    swap(nums, 0, k - 1)          #reverse the first k elements of the reversed array
    swap(nums, k, len(nums)- 1)   #reverse the remaining elements of the reversed array

def swap(array, startIdx, endIdx):
    leftIdx = startIdx
    rightIdx = endIdx
    while leftIdx < rightIdx:
        array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]   # this one line code is whats great about Python lol
        leftIdx  += 1
        rightIdx -= 1