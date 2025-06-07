"""Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next 
greater number for every element in nums. The next greater number of a number x is the first greater number to its 
traversing-order next in the array, which means you could search circularly to find its next greater number. If it 
doesn't exist, return -1 for this number.

Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]
 

Constraints:
1 <= nums.length <= 104 ;  -10^9 <= nums[i] <= 10^9 ; 

So this question like nextGreaterElementI.py is an extension of the next greater element algorithm in monotonicStacks.py,
so read that first. The only addition to this question is to treat the input array as a circular array. To handle the
circular array portion, we simply scan through the indices of the array twice. This means the for loop goes through
2*len(nums). Then once we have the index, we modulo divide it by the length of of the array to yield a valid index with
which to access the values in the input array. This way we ensure that after index len(array) - 1, the next index we 
visit is len(array) % len(array) ie index 0. After that, the rest is pretty straightforward. While the peek element is
less than the current loop element (accessed by the result of modulo divisiion), we know that the current loop element 
is the next greater element for the stack peek element so we pop the peek element (we store indices on the stack), and
update the output array at the popped index with the value of the current loop element. We will keep this pop and update
operation going as long as the stack is non-empty and the stack peek element is less than the current loop element. After
this operation comes to an end, we add the current loop index (the result of the modulo division) to the end of the stack.
"""
#O(n) time | O(n) space
def nextGreaterElements(nums) :
    stack = []
    answer = [-1]*len(nums)
    for i in range(2*len(nums)):
        j = i % len(nums)
        while stack and nums[stack[-1]] < nums[j]:
            peek = stack.pop()
            answer[peek] = nums[j]
        stack.append(j)
    return answer
                