""" Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

This question is the same as longestSubstringWithoutDuplication.py on alogexpert.io. The title here is leetcode 3. Anyway the brute
force approach would be to generate all possible substrings starting at each index, determine if a substring has a duplicate character
and if in doesnt, check its length and track the largest length. This is an O(n^2) approach. With this approach, the momement we find
a duplicate we know that every substring after that will also contain that duplicate we found, so do we even need to continue? This
is what the optimal solution addresses ie using a sliding window technique. That is we use two pointers and under some condition we
update the start of the window, under other conditions we keep it where its at but in the general case, we always update the end of 
the window.

So in this question, our window will only contain a substring without repeating characters. The moment we encounter a repeated 
character, we need to update the start of our window, to remove all duplicates, to re-establish the condition of our window. The 
indices as used here are slice indices ie start 0, end 1 contains only the letter at index 0. Since we know that a single character
is non-repeating we can initialize our start and end pointers here. (in many sliding window problems we initialize start, end = 0,1).

So how do we keep track of repeating characters? We use a hashmap or a set. How do we use a set to solve this solution. We use the set 
to store the letters in the current substring with non-repeating characters. So if we encounter a character thats already in the set, 
we know that we have a duplicate. So in that case, how do we shift our start pointer to re-establish the window property. We say that 
while the current character is in the set, remove the character at the current start pointer and then increment the start pointer. So 
if we have 'abba' we have start = 0 and {a} then {a, b} then at the second 'b', we remove the element at the current start pointer ie 
set.remove(string[start]) = set.remove(string[0]) = set.remove('a') to get {b} and increment start += 1 = 1. We check again and 'b' is 
in the set so we repeat and now start= 2 and set = {}. Then we calcualte our length, track our max length and add the second b to the 
set {b}. When we get to the second 'a', the set is {b} and start is 2 and 'a' is not in the set so, we just add it to the set {'b','a'}. 

If we use a hashmap the key is the character and the value is the last index we encountered that character. So if have 'aa', we first 
have 'a':0, then 'a':1. So when we encounter a character that is in the map, we know its a duplicate and we update its index. But how 
do we move our start index to re-establish the window property. To remove the duplicate of the current character, the start of the 
window will have to move to 1 index after the current index. That is say we had 'aba', the 'a':0, 'b': 1, when we get to the second a, 
to remove its preceding duplicate, start will have to move to the current value map['a]+ 1 = 0 + 1  = 1. But the is a catch here. If we 
have 'abba', then when we get to the second 'b', start = 1+1 = 2. So, when we get to the second a, start will not be 0 +1 = 1 but will 
still be 2. In otherwords, start = max(start, map[char]+1). Then we calculate the length of the current substring and do a max comparison 
to track the longest without duplicates ie i+1 - start, before updating the current index of the character we encountered. This solution 
is in logestSubstringWithoutDuplication.py also.

Due to the use of the set / hashmap to track duplicates, both solutions take linear time and space. The set method due to the inner while
loop will be at most O(2*n) but its still linear time O(n).


"""

def lengthOfLongestSubstring(s):
    left = 0
    dup = {}
    maxLength = 0
        
    for right in range(len(s)):
            
        while s[right] in dup:
            decreaseCount(dup, s[left])
            left += 1
            
        length = right + 1 - left
        maxLength = max(maxLength, length)
            
        increaseCount(dup,s[right])
        
    return maxLength


def lengthOfLongestSubstring(s):
    left = 0
    dup = {}
    maxLength = 0
        
    for right in range(len(s)):
        char = s[right]
            
        if char in dup:
            left = max(left, dup[char] + 1)

        length = right + 1 - left
        maxLength = max(maxLength, length)
        dup[char] = right
        
    return maxLength



def lengthOfLongestSubstring(s):
    left = 0
    dup = {}
    maxLength = 0
        
    for right in range(len(s)):
            
        while s[right] in dup:
            decreaseCount(dup, s[left])
            left += 1
            
        length = right + 1 - left
        maxLength = max(maxLength, length)
            
        increaseCount(dup,s[right])
        
    return maxLength

def increaseCount(map, char):
    if char not in map:
        map[char] = 0
    map[char] += 1
   
def decreaseCount(map, char):
    map[char] -= 1
    if map[char] == 0:
        map.pop(char)       



def lengthOfLongestSubstring(s):
    startIdx = 0
    duplicates = {}
    maxLength = 0

    for endIdx, char in enumerate(s):

        if char in duplicates:
            startIdx = max(startIdx, duplicates[char] + 1)
        
        length = endIdx + 1 - startIdx
        maxLength = max(maxLength, length)

        duplicates[char] = endIdx
    
    return maxLength
    


