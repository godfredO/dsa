"""A string is good if there are no repeated characters. Given a string s. return the number of good substrings of length three in s.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted. A substring is a contiguous 
sequence of characters in a string.

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".


This solution builds on the set solution of longestSubstringWithoutRepeatingCharacters.py. In that solution, whenever we encountered
a duplicate of the current right pointer character,  we used a while to keep popping the current left pointer character and advancing 
the left pointer until the duplicate was not in the duplicate set, before adding the current character to the set. We do the same 
here but in additoin we are asked to only look for substrings of size 3 that have no duplicates. So if our current substring which at
this point has no duplicates is also of size three, we increment our result variable, then we advance our left pointer a single time
so that we can get the next substring of size 3. Thus there are two instances and two ways of advancing the left pointer. With a while
loop and with an if statement. This is a good example of a question that uses both fixed width sliding window and variable width 
sliding window. In a variable width sliding window, you move the left pointer to re-establish the window property. In a fixed width
sliding window, you move the left pointer whenever the fixed width is reached. Thus moving the left pointer to ensure that our window
contains only unique characters (no duplicates of current right pointer character) is an example of variable width sliding window since
that window is bounded by a property ie uniqueness or non-duplication. Moving the left pointer when the window size equals 3 is an 
example of fixed width.

An alternative way of solving the question is to use a count hashmap instead of a set. In this solution, we go through the string and
add increment the count of the current right pointer element. Then when the substring is of size 3 and the keys in the count hashmap 
is also 3, we know that there are exactly 3 unique elements in that window, so we increment the result variable by 1. Whether there 
are three unique keys in the window or there are duplicates, we remove the current left pointer letter from the count hashmap. This 
involves decrementing the count of the current left pointer letter and if after the decrement, the count of the current left pointer
letter is 0, it means that letter doesnt occur in the new window, so we pop that key from the hashmap. Then we increment the left
pointer variable to reflect the new window left boundary. Making sure to pop keys whenever the count reaches 0, is the reason why
we can use the len(dup.keys()) as a test of number of unique characters in the substring. """

def countGoodSubstrings(s):
    dup = set()
    left = 0
    result = 0

    for right in range(len(s)):
        char = s[right]
            
        while char in dup:                  # variable width sliding window
            dup.remove(s[left])
            left += 1
            
        dup.add(char)
            
        if right  + 1 - left == 3:          # fixed width sliding window
            result += 1
            dup.remove(s[left])
            left += 1     
        
    return result


def countGoodSubstrings(s):
    left = 0
    dup = {}
    result = 0

    for right in range(len(s)):
        increaseCount(dup, s[right])

        if right + 1 - left == 3:
            if len(dup.keys()) == 3:
                result += 1   
            decreaseCount(dup,s[left])
            left += 1    
    return result

def increaseCount(dup,char):
    if char not in dup:
        dup[char] = 0
    dup[char] += 1

def decreaseCount(dup,char):
    dup[char] -= 1
    if dup[char] == 0:
        dup.pop(char)
