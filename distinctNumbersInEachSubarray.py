"""Given an integer array nums and an integer k, you are asked to construct the array ans of size n-k+1 where ans[i] is the 
number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]]. Return the array ans.

Example 1:
Input: nums = [1,2,3,2,2,1,3], k = 3
Output: [3,2,2,2,3]
Explanation: The number of distinct elements in each subarray goes as follows:
- nums[0:2] = [1,2,3] so ans[0] = 3
- nums[1:3] = [2,3,2] so ans[1] = 2
- nums[2:4] = [3,2,2] so ans[2] = 2
- nums[3:5] = [2,2,1] so ans[3] = 2
- nums[4:6] = [2,1,3] so ans[4] = 3

Example 2:
Input: nums = [1,1,1,1,2,3,4], k = 4
Output: [1,2,3,4]
Explanation: The number of distinct elements in each subarray goes as follows:
- nums[0:3] = [1,1,1,1] so ans[0] = 1
- nums[1:4] = [1,1,1,2] so ans[1] = 2
- nums[2:5] = [1,1,2,3] so ans[2] = 3
- nums[3:6] = [1,2,3,4] so ans[3] = 4


So we have a fixed window width of k and for each window of size k in an original array we are to store the number of unique 
elements in the window and return an output of the number of unique elements of course arranged from the first to the last
subarray of size k. This is a fixed width sliding window question. Now because there can be repeated values in a window,
we cant use a set to track our unique elements we have to use a count hashmap. This way, shifting the left pointer involves
decrementing the count of the left pointer value and if after decrementing the count is 0, we pop since that number doesnt
occur in our current window. The number of unique elements in the window will simply be the number of keys after the right
pointer value has been added to our count hashmap, w

"""
def distinctNumbers(nums,k):
    output = []

    counts = {}
    for i in range(k):
        addCount(counts,nums[i])

    output.append(len(counts.keys()))
    
    left = 0
    for right in range(k,len(nums)):
        decreaseCount(counts, nums[left])

        addCount(counts,nums[right])

        output.append(len(counts.keys()))
    return output


def addCount(counts, rightChar):
    if rightChar not in counts:
        counts[rightChar] = 0
    counts[rightChar] += 1

def decreaseCount(count, char):
    count[char]  -= 1 
    if count[char] == 0: 
        count.pop(char)  

nums = [1,1,1,1,2,3,4] 
k = 4
print(distinctNumbers(nums,k))