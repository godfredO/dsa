"""Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

So this question is literally the same as longestSubstringWithAtMostTwoDistinctCharacters.py. The only difference is that instead
of shifting the left pointer when the (unique) keys in our count hashmap is greater than 2, we now shift when its greater than
k. So we add the count of the right pointer letter, check if we need to shift the left pointer, which involves decrementing the
left pointer letter count before incremeting the left pointer itself. Decrementing the left pointer count is simply subtracting
1 but if after subtraction, the count is 0, we pop that letter (key) from the count hashmap. When we are assured that the current
window has at most k distinct characters, we take the length, and track the longest such length seen. At the end we return the
longest such length seen. As such this is a variable width sliding window problem where we shift our left pointer to re-establish
our property. 
"""

def lengthOfLongestSubstringKDistinct(s,k):
    left = 0
    maxLength = 0
    dup = {}

    for right in range(len(s)):
        increaseCount(dup,s[right])
        
        while len(dup.keys()) > k and left <= right:
            decreaseCount(dup, s[left])
            left += 1
 
        length = right + 1 - left
        maxLength = max(maxLength, length)

    return maxLength
        


def increaseCount(map, char):
    if char not in map:
        map[char] = 0
    map[char] += 1
   
def decreaseCount(map, char):
    map[char] -= 1
    if map[char] == 0:
        map.pop(char)    

    

s = "aa"
k = 1

print(lengthOfLongestSubstringKDistinct(s,k))