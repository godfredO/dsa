"""Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise. In other words, return true if one 
of s1's permutations is the substring of s2. 1 <= s1.length, s2.length <= 104. s1 and s2 consist of lowercase English letters.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
Hint 1 : Obviously, brute force will result in TLE. Think of something else.
Hint 2 : How will you check whether one string is a permutation of another string?
Hint 3 : One way is to sort the string and then compare. But, Is there a better way?
Hint 4 : If one string is a permutation of another string then they must one common metric. What is that?
Hint 5 : Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to 
store frequencies?
Hint 6 : What about hash table? An array of size 26?

This question is in essence the same as findAllAnagramsInAString.py. That is because the set of all permutations of a string can also
be called the set of all anagrams of the string. So the question is asking if there are any anagrams of one string in another but in this 
case we are to return a boolean instead of an array of all anagram starting indices. In otherwords, we only need to find one occurrence 
of the anagram. So whenever we find a first occurence of an anagram (an anagram is simply one of the permutations of a string), we return
True. Otherwise if we go through s1 and never find an anagram of s2, we return False. 

This is a fixed width sliding window problem.
"""

def checkInclusion(s1, s2) :
        if len(s2) < len(s1):
            return False
        
        width = len(s1)
        count1 = {}
        count2 = {}
        for idx in range(width):
            addChar(count1, idx, s1)
            addChar(count2, idx, s2)
         
        startIdx = 0
        if count1 == count2:
            return True
        
        for endIdx in range(width, len(s2)):
            removeChar(count2, startIdx, s2)
            addChar(count2, endIdx, s2)
            
            startIdx += 1
            if  count1 == count2:
                return True
        return False
                
    
def removeChar(count, idx, s):
    char = s[idx]
    count[char]  -= 1
    if count[char] == 0:
        count.pop(char)
    
def addChar(count, idx, s):
    char = s[idx]
    if char not in count:
        count[char] = 0
    count[char] += 1