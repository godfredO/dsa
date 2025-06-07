"""Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. 
That is, no letter appears in a single substring more than once. Return the minimum number of substrings in such a partition.
Note that each character should belong to exactly one substring in a partition. s consists of only English lowercase letters.

Example 1:
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
 

This is a greedy algorithm solution. So basically I am going to use a set to store the unique letters in the current partition.
Thus as we iterate over the string, as long as the current letter is not in the seen set, we add the current letter. If it is,
we just came to the end of a partition, so we increment our result variable by 1, re-initialize a new seen set, before adding
the current character to it. Because we increment our partitions result variable when we get to the next duplicate ie when the
current partition ends, we will not add 1 for the last partition so we return our partitions variable + 1.
"""
def partitionString(s):
    partitions = 0
    seen = set()

    for c in s:
        if c not in seen:
            seen.add(c)
        else:
            partitions += 1
            seen = set()
            seen.add(c)
    
    return partitions + 1