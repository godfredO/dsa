"""Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome 
partitioning of s. A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

This question is clearly in the palindrome family of questions. So we are to return list of partitions where each partition is an
array that contains sub-strings that are all palindromes. So of course a partition where each substring is a single letter of the 
input string qualifies as a palindrome.

So we are going to brute-force this with backtracking. That is, we are going to create every single possible way we can partition
the input string and if a partition forms palindromes, we are going to add it to the result. So if input string is "aab", how do
we use backtracking to generate all types of partitions and check if these partitions yield palindromes.

So say the input string is 'aab', then we can partition as 'a' ('ab' remaining), 'aa', ('b' remaining) and 'aab' ("" remaining).
Now of these partitions, 'aab' is not a palindrome so we don't even continue down that path. So for the 'a' path, we do another
partition 'a' ('b' remaining) and 'ab' ("" remaining). Again we realize that 'ab' is not a palindrome so we dont go down that
path. Then for the 'a' then 'a' path, the remaining can only be a partitioned as 'b' and is a palindrome so we add that to our
result ie [['a','a','b']]. We backtrack to the first layer 'aa' ('b' remaining) and again we have 'b' as a palindrome so we add
the substrings of that path to the result [['a','a','b'],['aa','b']].

So how do we represent this idea in code, we know that the first layer is going to be generating subtrings of the input strings
so from start index of 0, we generate end indices, check if the substring between start and end indices is a palindrome using a
helper function. If it, we slice out the palindrome, concatenate with the partition array thus far and make a recursive call
with the updated partition (concatenation) for the sub-string starting from endIdx + 1. So whenever we find a substring that is
a palindrome we make the next call with a starting index which is our endIdx + 1 until we go out of bounds ie until we make
a call with a startIdx equal to the length of the string. Then we will backtrack and keep generating substrings for another 
partition.
"""
def partition(s):
    result = []
    part = []
    dfs(s, part, result, 0)
    return result


def dfs(s, part, result, startIdx):
    if startIdx >= len(s):
        result.append(part[:])
        return
    
    #generate all partitions from starting index to end of string
    for endIdx in range(startIdx, len(s)):
        if isPalindrome(s, startIdx, endIdx):
            palindrome = s[startIdx:endIdx + 1]
            updated = part.a[palindrome]
            dfs(s, updated, result, endIdx + 1)

def isPalindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True