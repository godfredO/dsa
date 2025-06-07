"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. 
There is only one repeated number in nums, return this repeated number. You must solve the problem without 
modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
 
Constraints:
1 <= n <= 105 ; nums.length == n + 1 ; 1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


So the thing about this question is that if we were allowed to modify the input array or use extra space, then we
could use the solution in first_duplicate_value.py, since both questions have the unique requirement that the array
contains values between 1 to n, where n is the length of the array. Since we are also told that there is only one
duplicate number then unlike first_duplicate_value.py, we can sort the array, hence modifying the array, and then
iterate through the sorted array, comparing each number to the previous number and the first time those two numbers
equal one another, we return that value.  So how do we solve this question whilst meeting the constraints?

The first solution that meets the constraints uses binary search. Consider an array that has nnn distinct numbers in 
the range [1,n]. For example: [1,2,3,4,5]. If we pick any one of these 5 numbers and count how many numbers are less 
than or equal to it, the answer will be equal to that number. So in [1,2,3,4,5], if you pick the number 4, there's 
exactly 4 numbers that are less than or equal to 444. If you pick 3, there's exactly 3 numbers that are less than or 
equal to 3, and so on. However, when you have duplicates in the array, this count will exceed the number at some point. 
For example: in [4,3,4,5,2,4,1], 3 has 3 numbers less than or equal to it, 2 has 2 numbers less than or equal to it,
1 has 1 number less than or equal to it. However, for the duplicate number, the count of numbers less than or equal to 
it, will actually be greater than the duplicate itself. In this example, 4, which is the duplicate, has 6 numbers that 
are less than or equal to it. But this also affects the numbers that come after 4. 5 will have 7 numbers that are less
than or equal to it. Hence, the smallest number that satisfies this property is the duplicate number. Binary search 
allows us use this information to solve the question in O(nlog(n)) instead of O(n^2) using linear scan. And the reason
why we know that binary search will work is because we can observe monotonicity in the counts ie is the count is
always greater than the value for the duplicate and numbers that come after it. Read binarySearchII.py. 

The optimal solution involves reducing this question to linkedListCycleII.py or even findLoop.py ie a linked list cycle
detection question that can be solved using the fast/slow pointer technique. The idea is that if we use the function
f(x) = nums[x] to construct the sequence, x, nums[x], nums[nums[x]], nums[nums[nums[x]]], and we start from x=nums[0],
the sequence will produce a linked list with a cycle. that is each new element in the sequence is an element in nums 
at the index of the previous element. So if we have [2,6,4,1,3,1,5], then we construct our nodes using f(x) = nums[x]
and starting from x=0, we have 2 -> 4 - > 3 -> 1 -> 6 -> 5 -> 1. So the origin of the loop, 1 is the duplicate. That is,
since we are assured of a duplicate, once we realize that the head node is the node at index 0, and that values can be
treated as next pointers or random pointers, so when we read the value at any index, we are reading the node its pointer
goes to, we can use linked list cycle detection to solve this problem in O(n) time and constant space.

"""
#O(nlog(n)) time | O(1) space
def findDuplicate(nums):
    left = 1
    right = len(nums) - 1 #n+1 values, so n = len(nums) - 1 ie n+1-1=n

    while left < right:
        mid = left + (right - left) // 2

        if count(mid, nums):  
            right = mid 
        else:
            left = mid + 1
    return left

def count(mid, nums):
    count = 0
    for num in nums:
        if num <= mid:
            count += 1
    return count > mid



#O(n) time | O(1) space
def findDuplicate(nums):
    head = nums[0]
    slow, fast = head, head         # head is an integer so need to clearly assign it.
    slow = nums[slow]               # initial advancement before going into first while loop
    fast = nums[nums[fast]]

    while fast != slow:             # read findLoop.py, advance at 1x and 2x speed till they cross
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    slow = head                     # set slow back to head node
    while fast != slow:             # iterate to find origin of loop
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

