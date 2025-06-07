"""Given a string S, return the number of substrings of length K with no repeated characters.

Example 1:
Input: S = "havefunonleetcode", K = 5
Output: 6
Explanation: 
There are 6 substrings they are : 'havef','avefu','vefun','efuno','etcod','tcode'.

Example 2:
Input: S = "home", K = 5
Output: 0
Explanation: 
Notice K can be larger than the length of S. In this case is not possible to find any substring.

Note:

1 <= S.length <= 10^4
All characters of S are lowercase English letters.
1 <= K <= 10^4

So this questin is an extension of longestSubstringWithoutRepeatingCharacters.py. So we can break the question up into two 
sections namely; find all substrings withoug repeating characters, determine the length and if its equal to k, we increment
a count. To find all substrings without duplicates, we use a set, a left and right pointer and both pointers are initialized
at 0. So inside a loop we access the current right pointer character, then check if its in the set, which will mean its a
duplicate. If it is, we access the current left pointer character, remove it from the set, and increment the left pointer,
we do all this in a while loop until the current right pointer character is no longer in the set. Now we know the set contains
non repeated characters. So we can access the length of the current window by right + 1 - left and check if its equal to k
and if it is, we increment a count. Now one key here is that since we are adding duplicates, we add the current letter after 
we have checked for its duplicate and calculated the length of the substring that contains it. Now another consideration is
what if the longest substring with no repeated characters is actually longer than k. Well they way I prefer it, when we get 
to a substring of no repeated character of size k, after incrementing our count, we shift the left boundary again this time
to remove the leftmost character and shifting the left pointer so that the next substring we consider is the next possible
substring of size k. So we have one case of shifting the left pointer to remove duplicates and another case of shifting the
left pointer to consider the next substring of size k.
"""

def numKLenSubstrNoRepeats(s,k):
    if k > len(s):
        return 0
    dup = set()
    left = 0
    result = 0
    for right in range(len(s)):
        char = s[right]
        while char in dup:
            dup.remove(s[left])
            left += 1
        
        length = right + 1 - left
        if length == k:
            result += 1
            dup.remove(s[left])
            left += 1

        dup.add(char)
    
    return result


s = "havefunonleetcode" 
k = 5
print(numKLenSubstrNoRepeats(s,k))