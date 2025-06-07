"""Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the 
array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than 
or equal to threshold. Each result of the division is rounded to the nearest integer greater than or equal to that 
element. (For example: 7/3 = 3 and 10/2 = 5). The test cases are generated so that there will be an answer.

Example 1:
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

Example 2:
Input: nums = [44,22,33,11,1], threshold = 5
Output: 44
 
Constraints:
1 <= nums.length <= 5 * 10^4 ; 1 <= nums[i] <= 10^6 ; nums.length <= threshold <= 10^6.

So first off all, we are being asked to round up. We can either use math.ceil(a/b) or 1 + (a-1)//b. Next thing is 
to realize the effect of the chosen divisor on the array of numbers. If numbers is [1,2,5,9] if the divisor is 1, 
the answer will be the sum of all the numbers ie math.ceil(1/1) + math.ceil(2/1) + math.ceil(5/1) + math.ceil(9/1) 
= 1+2+5+9=17. If the divisor is 9, the answer is the length of the array since every division defaults to 1 , ie
math.ceil(1/9) + math.ceil(2/9) + math.ceil(5/9) + math.ceil(9/9)= 1+1+1+1=4. So the range of sums are from
lengthOfNums < sum < sumOfNums if the divisor is max(nums) < divisor < 1. Lets write the other way around, that is
1 < divisor < max(nums) ; sumOfNums < sum < lengthOfNums. In otherwords, as the divisor increases the sum decreases. 
The question is asking us to find the a positive integer divisor such that the result is less than or equal to the
threshold. So let's say we have a divisor whose sum equals the threshold, as we increase this divisor, the sums we
get will be less than the threshold. In otherwords, the answer will be the minimum divisor for which the resulting
sum is less than or equal to the threshold. So that's what we do, we take a guess of the divisor from 1 to max(nums)
and for each guess, we calculate the resulting sum of the round up division, and if the resulting sum is less than
or equal to the threshold, we minimize our guess by moving the right pointer, otherwise we maximize our guess by 
moving the left pointer in a bid to find a divisor that yields a sum that is less than or equal to our threshold.
"""
def smallestDivisor(nums, threshold):
    left, right = 1, max(nums)
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid,nums, threshold):
            right = mid
        else:
            left = mid + 1
    return left


def condition(mid,nums,threshold):
    sum = 0
    for num in nums:
        sum += 1 + (num-1)//mid
    return sum <= threshold