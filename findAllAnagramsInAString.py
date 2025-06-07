"""Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any 
order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the 
original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 
Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.

So first off, you might want to revise group_anagrams.py before this question. Anyway, an anagram is a word or phrase is formed by 
rearranging the letters of a different word or phrase. In othewords, if we got a count hashmap of two strings that are anagrams, 
the counts will be the same; they would have the same keys and each key will have the same count. 

This is a sliding window problem. How do we use sliding window to find the start indices of anagrams of one string in another. First 
what does it mean for a substring of one string to be an anagram of another string. It means that the length (width) of the substring 
equals the length (width) of the other string. It also means that the count hashmap of the window is the same as the count hashmap of 
the other string; same keys and the keys have same values. So say the other string is of length 3, then one idea will be to get a
count hashmap of all substrings of length 3 of the main string.

So first of since we know that all anagrams of string p will have the same length as string p, so the first thing to realize is that 
our window in this sliding window technique, will only contain substrings of string s of a fixed width, ie the width of string p. So 
we first handle our first base case that if string s is shorter than string p, then no anagram of string p can occur in string s, so
we return an empty list. Next we get a count map of string p and the first 'len(p)' substring of string s ie the first substring 
starting from index 0 that is of the same length of string p. So width these two count hashmaps, we can decide if index 0 is a valid 
anagram ie if the count hashmaps are equal. This is a constant time operation since there are at most 26 keys(we are assured that the 
strings only contain lowercase English letters. So if they are, we append a left/start index of 0. We also realize that there is only 
one such substring starting from index 0.Then we need to check the next substring of width = len(p). 

The next substring of that length will start from index 1 ie (s[1:len(p)+1]). So we use a for loop to generate the right/ end indices 
starting from len(p) and ending at the last index of s. Then to ensure that the count hashmap of s is representative of this substring, 
we move the left pointer by decrementing the count of the letter at index 0 by 1 and if after reduction, the count is 0, then it means 
this letter doesnt occur between in the substring s[1:width + 1]. So if the count is 0 after decrementing, we pop that key. Next we 
update the count of the new letter in our window, ie the letter at the right pointer ie s[endIdx] . And updating its count means that
if its not in the count initializing a count of 0 before increamenting by 1 to 1, if it exists already we just increment by 1. Then we
update our left / start index by incrementing to reflect the current substring that our count hashmap is representing. Note the order
here, we remove the letter at the previous left pointer, add the letter at the new right pointer, before we advance the left pointer
itself. So now we check again if the updated hashmaps are equal. If they are we append the updated leftIdx to the output. Since we are 
assured that our inputs only contain lowercase English letters and there are 26 of those, our hashmaps are going to have a constant max 
keys of 26 and as such this check is O(26) or constant time.

The key thing here is to first check if the substring at index 0 is a valid anagram of p. That greatly simplifies the code and the
thinking process. Also, since our window represents a substring of fixed width, we move our left/start index at every iteration to 
re-establish the window property as right/end index moves.

The window property is a fixed width of subststring contained in the window. We move the left pointer on each iteration to re-establish 
this width, and when the window property is established we check if the count frequency of the window substring is the same as string p, 
we add the left pointer index to our result.

This is an example of a fixed width sliding window problem.
"""



def findAnagrams(s, p) :
    if len(s) < len(p):
        return []
        
    width = len(p)
    countP, countS = {}, {}
    for idx in range(width):   
        addChar(countS, idx, s)
        addChar(countP, idx, p)
        
    startIdx = 0
    output = []
    if countS == countP:
        output.append(startIdx)
    
    for endIdx in range(width, len(s)):
        removeChar(countS, startIdx, s)
        addChar(countS, endIdx, s)
            
        startIdx += 1
        if  countS == countP:
            output.append(startIdx)

    return output
                
    
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
