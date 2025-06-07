"""The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'. For example, "ACGAATTCCG" 
is a DNA sequence. When studying DNA, it is useful to identify repeated sequences within the DNA. Given a string s that 
represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
You may return the answer in any order.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]

The key to this problem is the fixed width sliding window technique or pattern. In that we usually add the current right
pointer element to a total (if its an integer), before checking for the condition under which we advance the left pointer
and if this condition checks out we do just that. So the key idea here is that we only need to consider substrings of size
10. So in my first solution, I use the common technique for sliding window questions of fixed width. To detect duplicate
substrings, I add all generated substrings to a set. And since the same substring could be repeated many many times, the 
result array itself is also a set. So the right pointer goes from index 0 to the end of the array, and I use it to add the
current right pointer elemen to the interim deque. I use a deque instead of an array because when the interim deque is of 
length 10, I join them into a substring, and check the substring is already in the duplicates sets, and if it is, I add it
to the result set, before advancing the left pointer by popping left from the deque. And that's it, at the end I cast the
result set into a list before returning.

Alternatively, we can just directly create all substrings of size 10 and in this case we use a left pointer instead of a
right pointer. We have to make sure that our left pointer goes from 0 to the 10 less than the length of the string so that
we can use it to successfully slice out our substrings. So in order to ensure that we dont get our error, our left pointer 
has to go from range(0 to len(s) - 9_. This way if we have a string of length 10, the last index is 9 and the first index 
is 0 and this should be the only left pointer index we consider, so we need range(10-9) = range(1) = 0. Once we have the 
left pointer index, we can slice from left to left+10, due to the slice end exclusivity ie s[l:l+10]. Again if the slice
is in our duplicates set, we add the slice to our result set, before add the slice to the duplicate set. Again at the end
we cast the result set into a list before returning.
"""
from collections import deque
def findRepeatedDnaSequences(s) :
    interim = deque()
    dup = set()
    result = []
    for right in range(len(s)):
        interim.append(s[right])

        if len(interim) == 10:
            seq = "".join(interim)
            if seq in dup:
                result.append(seq)
            dup.add(seq)
            interim.popleft()
    
    return list(result)



def findRepeatedDnaSequences(s) :
    result = set()
    dup = set()
        
    for left in range(len(s)-9):
        current = s[left:left+10]
        if current in dup:
            result.add(current)
        dup.add(current)
    return list(result)