"""The frequency of an element is the number of times it occurs in an array. You are given an integer array nums and an integer k. In 
one operation, you can choose an index of nums and increment the element at that index by 1. Return the maximum possible frequency of 
an element after performing at most k operations. 1 <= nums.length <= 105 . 1 <= nums[i] <= 105 . 1 <= k <= 105 .

Example 1:
Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4]. 4 has a frequency of 3.

Example 2:
Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

Example 3:
Input: nums = [3,9,6], k = 2
Output: 1

Hint 1 : Note that you can try all values in a brute force manner and find the maximum frequency of that value.
Hint 2 : To find the maximum frequency of a value consider the biggest elements smaller than or equal to this value



So we are given an integer array nums and an integer k, which represents the number of allowable increments. Meaning we can increment
elements of nums at most k times. If we chose to increment a single element k times, that will be the same as adding k to that element. 
The aim is to distribute the k increments in such a way as to have multiple elements become the same repeeated value and to return the 
frequency of the most frequent element after some optimal distribution of at most k increments. So in the first example nums = [1,2,4], 
k= 5 and we can covert all the elements to 4 by incrementing 1 three times, and incrementing 2 two times for a total of 5 increments 
to yield [4,4,4] ie the max frequency is 3. This question reminds me of longestRepeatingCharacterReplacement.py . 

First thing to realize is that we are only allowed increments, not decrements. Meaning for [1.2] we cant get decrease 2 to get 1 but we
can increase 1 to get a 2. In otherwords, for any target value, we can only increment elements that are less than it to get it. Looking
at the constraints, we are told inputs will range from 1 up to 105 ie we are assured of positive non-zero integers only. Okay so when
looking at say [1,2,4], k = 5,  lets say we want to increment elements to reach 4, which of the remaining values do we start with? 
Obviously 2 since its closer to 4 so as to minimize the number of allowed increments k we actually need. If we did the remaining k will 
be 3 since we will need 2 increments to get from 2 to 4. Then we have enough increments, k=3, to convert 1 to 4. 

The key to using sliding is to sort the array in ascending order. Then we have a right pointer point to our current target and our left 
pointer point to the end of our window. Now we know that the length of the window is right + 1  - left. Our aim is to convert every 
element in our window to the target, which is the value at the right pointer. If we did, each element in our window will have a value 
of nums[right] and the total would be nums[r]* windowLength. How do we know that we have k increments to actually convert every element 
in our window to the target. Well we can add up the acutal total of the element in the window and if total[window] + k is  greater than
or equal to our nums[r]*windowLength, then we have enough increments in which case we do a max window length comparison, and then we 
expand our window by moving our right pointer to a new target. If however we determine that we dont have enough increments, then we 
shorten our window for the current target by advancing the left pointer. So we initialize both pointers at index 0, and if our condition 
is valid we try a greater target, if not we shorten our window for the current target. We know that if left every equals right, our
window will be valid because we will be turning the target to itself. When we advance the left pointer to shorten the window we remove
the value at the left pointer from our target. When we advance our right pointer to a new target, we add the new right pointer value to
our total. This way, we only ever do a single O(n) iteration and we dont repeat sums.
"""

"""Optimal approach - we do at most 2n iteration"""
#O(nlog(n)) time | O(1) space
def maxFrequency(nums, k) :
    nums.sort()
    left, right = 0,0
    maxLength, total = 0,0

    while right < len(nums):
        total += nums[right]

        while total + k < nums[right] * (right + 1 - left): #we advance our left pointer whenever our window is invalid
            total -= nums[left]
            left += 1

        maxLength = max(maxLength, right + 1 - left)   #when we find a valid window, track max length seen

        right += 1                                     #when we find a valid window, try the next target.
    
    return maxLength
         








"""Naive solution  - We visit each index up to n times."""
#O(n^2) time | O(1) space
def maxFrequency(nums, k) :
        nums.sort(reverse=True)
        maxLength = 1
        
       
        for left in range(len(nums)) :
            right = left + 1
            
            length = 1
            remaining = k
            
            while right < len(nums) and nums[left] - nums[right] <= remaining :
            
                increments = nums[left] - nums[right]
                
                remaining -= increments

                right += 1
            
            maxLength = max(maxLength, length)
            left += 1
        
        return maxLength
            
        
nums = [1,4,8,13]
k = 5
print(maxFrequency(nums,k))