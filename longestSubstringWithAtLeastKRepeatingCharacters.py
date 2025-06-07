"""Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in 
this substring is greater than or equal to k. s consists of only lowercase English letters.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

So obviously we are going to summarize each substring with a hashmap, and the question is saying that a substring is valid if each
key in its hashmap has a value greater than or equal to 3. The substring represented by {a:3} is valid, the substring represented
by {a:3,b:1} is not valid since b has a value less than 3 , the substring repreented by {a:3,b:3} is valid since each value is 3, 
the substring represented by {a:3,b:4} is also valid since each value is greater or equal to 3. The tricky part to this question is
the need to track the longest valid substring. If we are at an invalid substring represented by {a:3,b:2}, how do we know if we a 
valid substring of {a:3,b:4} exists down the string. What if to enough b's we still end up with an invalid string such as 
{a:3,b:3,c:1}. Even more tricky, how do we determine when to shift our left pointer. In other words, what are the conditions for 
expanding / shrinking our window in this variable width sliding window problem. And even more importantly what should we track 
in our window? 

To solve this problem, we utilize a technique that was used in substringWithConcatenationOfAllWords.py where we broke up the set
of possibilities into subsets based on possible starting positions of a valid answer and found all the valid substrings in each 
subset. So what subsets do we use and track in each window. The answer is, we track the max number of allowed unique characters. 
First what is the upper bound of the max number of allowed unique characters? It will be the number of unique characters in the 
original string. Meaning if the input string has 4 unique characters, we break our solution into subsets where the max number of 
allowed unique characterrs can be 1,2,3,4. So we first find all valid substrings with 1 unique character such as "aaaaa", "bbb",
then two unique characters such as "aaabbbbbbbbbb", then three unique characters such as "aaabbbccc". How does this help our
conundrum. Say maxUniqueCharsAllowed = 1, and we have "aaabb", we can count the 3 a's or the 2 b's but not both in our current 
iteration since to do that max uniuqe chars count will be 2. So how do move our left / right pointers ? So we use our right 
pointer to update counts, and if we are ever in a situation where the keys in our substring hashmap is more then the current 
maxUniqeCharsAllowed, we shift our left pointer until it matches our current subset. Then in order to certify that our current
subset substring is valid we need to ensure that the minimum key is 3. This technique is more accurately called brute force
over sliding window. We create a new hashmap for each maxAllowedUniqueChars, and start a new sliding window.

Now in the code, how can we methodically track the number of unique characters in the current window. We use an approach similar 
to the numFound variable in minimumWindowSubstring.py. After incrementing a count, we check if the count equals 1. If it is, we 
increment a currentUniqueChars variable by 1. This way the loop for shifing the left pointer runs as long as currentUniqueChars
> maxAllowedUniqueChars. This would involve removing the left pointer letter and decrementing the left pointer character count
and if the count of the left pointer is 0 after decrement, we pop that key, and reduce the currentUniqueChars by 1. Keeping
track of currentUniqueChars is better I guess than just counting the number of keys each time in our substring hashmap. Then
we have the last check of looking if the minimum value in our hashmap is greater than or equal to 3. If that is the case, we
have a valid substring so we check the length, and track the maximum length seen so far. Since we are assured that our string
only consists of English lowercase letters, 1 <= maxAllowedUniqueChars <= 26 meaning that our solution is O(26*n) or O(n) time.
since we repeat the linear sliding window portion at most 26 times but in reality we repeat it for as many unique characters
there are in the string, the upper bound of which is 26 so O(26*n) to O(n) actually holds.

"""

def longestSubstring(s, k) :
    chars = set()
    for char in s:
        chars.add(char)
    totalUnique = len(chars)   #number of unique charactes in s
    

    maxLength = 0
    for allowedUnique in range(1,totalUnique + 1):  #break solution into subsets
        
        counts = {}
        currentUnique = 0
        left = 0

        for right in range(len(s)):       #for each subset perform a sliding window over the string

            rightChar = s[right]
            if rightChar not in counts:
                counts[rightChar] = 0
            counts[rightChar] += 1

            if counts[rightChar] == 1:
                currentUnique += 1
            
            while currentUnique > allowedUnique  and left <= right:

                leftChar = s[left]
                counts[leftChar] -= 1

                if counts[leftChar] == 0:
                    counts.pop(leftChar)
                    currentUnique -= 1
                
                left += 1
            
            if min(counts.values()) >= k:
                length = right + 1 - left
                
                maxLength = max(maxLength, length)
        
    return maxLength




s= "ababbc"
k = 2
print(longestSubstring(s,k))




