"""Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray 
[numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 
0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Because all the integers are positive, if we keep adding elements of a subarray, the sum will keep increasing. So first off the
longest subarray we could consider is the array itself. And so the only situation under which we return 0 is if the sum of the
entire array is less than the target. Otherwise, the answer will be some subarray in the array. So obviously this is a variable
width sliding window problem with added optimization. So we start with a window with left and right pointer initialized at 0 and
a total also at 0. Then inside our loop we add the current right element and check if our updated total is greaer than or equal
to our target. If it is, we check the length of the current subarray window, do a minimum length check with the stored minLength
(which is initialized at +inf for easy minimum comparison), and then remove the current left value from our total before shifting
the length pointer forward. Whether or not our current total passes the target comparison check, we update the right pointer. In
otherwords, we expand our window, adding up the right pointer elements until we have a valid window, and then we proceed to 
search for a minimized valid widow by shifing our left boundary, only after comparing our current length to the stored value and
removing the current left element from our total. There are two solutions below, where we use a while loop to and a for loop to
generate the right pointer index.

This is a variable width sliding window question where we move the left pointer to optimize our window property unitl the window
property is broken, then we move the right pointer to achieve the window property ie, the total of the subarray inside the
window is greater than or equal to target.

"""

def minSubArrayLen(target, nums):
    left, total = 0, 0
    minLength = float('inf')

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            length = right + 1 - left
            minLength = min(minLength, length)

            total -= nums[left]
            left += 1

    return minLength if minLength != float("inf") else 0





def minSubArrayLen(target, nums):
    result = float('inf')

    left, right = 0,0

    total = 0
    while right < len(nums):
        total += nums[right]

        while total >= target :
            length = right + 1 - left
            result = min(result, length)
            total -= nums[left]
            left += 1
        right += 1
        print(total)

    
    return result if result != float("inf") else 0



target = 7 
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))