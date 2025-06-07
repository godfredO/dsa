"""You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer 
array removable containing a subset of indices of s (s is also 0-indexed). You want to choose an integer k 
(0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, 
p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, 
then remove all marked characters and check if p is still a subsequence. Return the maximum k you can choose such 
that p is still a subsequence of s after the removals. A subsequence of a string is a new string generated from the 
original string with some characters (can be none) deleted without changing the relative order of the remaining 
characters.

Example 1:
Input: s = "abcacb", p = "ab", removable = [3,1,0]
Output: 2
Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".
If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.
Hence, the maximum k is 2.

Example 2:
Input: s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
Output: 1
Explanation: After removing the character at index 3, "abcbddddd" becomes "abcddddd".
"abcd" is a subsequence of "abcddddd".

Example 3:
Input: s = "abcab", p = "abc", removable = [0,1,2,3,4]
Output: 0
Explanation: If you remove the first index in the array removable, "abc" is no longer a subsequence.
 

Constraints:
1 <= p.length <= s.length <= 105  ; 0 <= removable.length < s.length ; 0 <= removable[i] < s.length ; p is a 
subsequence of s ; s and p both consist of lowercase English letters ; The elements in removable are distinct.


Interesting question. So let's try to brute-force this. First off, how do we tell if a string p, is a subsequence 
of another string s. In order for p to be a subsequence of s, we have to find a substring in s such that the letters
in p appear in the same order in this substring as they appear in p. The question valid_subsequence.py question solves 
this problem but for an array of integers ie determining if one array of integers is a valid subsequence of another 
array of integers. Now for  1 <= k <= len(removable), we will attempt to remove letters in s at indices removable[0]- 
removable[k-1] (note that k is 1-indexed) and check if p is still a valid subsequence of the resulting substring. The 
subsequece check is O(n) where n is the length of the longer string, so this brute force approach is O(n*k) time. So 
how does the valid subsequence function work? Generally we use two pointers one for (the substring of) s and the other 
for p. The idea is to find the first letter of p in (the substring of) s, and then the second letter then the third 
letter, etc. Now, to ensure we are only accessing valid indices, we ensure that neither string pointer goes out of 
bounds, in the while loop. This way if we are able to find all the letters of p in s and in the order they appear in p, 
we know our the string p pointer will be equal to len(p). So generally if the string p pointer letter is equal to the 
string s pointer letter, we move both pointers otherwise we only advance the string s pointer to check if the next 
letter equals the current string p pointer letter. Now how do we rig this solution to skip the letters at the first k 
elements of removed. We keep a set of the first k elements in removed, and in our subsequence check function we say 
that if the string s pointer index is in this removed set or the string s pointer letter doesnt match the string, 
advance the string s pointer otherwise, the current string s pointer is not to be removed and it matches the string p 
pointer letter, so advance both. Thus we are able to cleverly and cleanly remove the first k letters and validate a 
subsequence.

We can however improve this solution, using binary search over the removable array. Why is this possible? Because
we are to remove the first k characters, so we can reframe the question as finding the maximum k for which p is
still a subsequence of the resulting substring after removing the first k characters of s. Note that k is 1-indexed 
so k=1 if we only remove the letter at s[removable[0]]. This binary search option yields O(n*log(k)) time complexity.
In otherwords, isSubseq() our subsequence becomes the condition function. The binary search pattern here is thus
the maximum value for which the condition returns True and for each mid value, we add all indices up to that to our
removed set.
"""

"""Brute Force solution"""
#O(n*k) time | O(k) space
def maximumRemovals(s,p, removable):
    k = 0
    removed = set()
    for i, idx in enumerate(removable):
        removed.add(idx)
        if isSubseq(s,p,removed):
            k = i + 1
    return k

def isSubseq(s,subseq, removed):
    i, j = 0, 0                                     #pointers for s, p
    while i < len(s) and j < len(subseq):
        if i in removed or s[i] != subseq[j]:
            i += 1
            continue
        i += 1
        j += 1
    return j == len(subseq)



"""Binary search solution"""
#O(n*log(k)) time | O(k) space
def maximumRemovals(s,p, removable):
    k = 0
    left, right = 0, len(removable) - 1
    while left < right:
        mid = left + (right - left) // 2
        removed = set(removable[:mid+1])            #O(k) space
        if isSubseq(s,p, removed):
            k = mid + 1                             #this is because k is 1-indexed so if mid=0, k=1
            left = mid + 1                          #this is an index
        else:
            right = mid - 1
    return k

def isSubseq(s,subseq, removed):
    i, j = 0, 0                                     #pointers for s, p
    while i < len(s) and j < len(subseq):
        if i in removed or s[i] != subseq[j]:
            i += 1
            continue
        i += 1
        j += 1
    return j == len(subseq)







s = "abcacb" 
p = "ab" 
removable = [3,1,0]
print(maximumRemovals(s,p, removable))