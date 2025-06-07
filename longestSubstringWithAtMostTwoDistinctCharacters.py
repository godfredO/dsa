"""Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.

So the idea here is what is a valid substring and what isn't. A substring with 1 unique character is valid. A substring with 2
unique characters is valid. A substring with more than 2 unique characters is invalid. So we will use our right pointer to 
add to a count hashmap where the key is the right pointer character. And as long as there is 1 or 2 keys we know that there is
1 or 2 unique characters in the substring represented by the hashmap, ie a valid substring and so we take the length of the
substring using left and right pointers. However if the number of keys is more than 2, then we shif the left pointer until 
the substring represented by the hashmap is valid.  This is a variable width sliding window question, as evidenced by the while
loop used to shift the left pointer until the substring represented is valid. 
"""


def lengthOfLongestSubstringTwoDistinct(s):
    left = 0
    maxLength = 0
    dup = {}

    for right in range(len(s)):
        increaseCount(dup,s[right])
        
        while len(dup.keys()) > 2 and left <= right:
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


s = "ccaabbb"
print(lengthOfLongestSubstringTwoDistinct(s))