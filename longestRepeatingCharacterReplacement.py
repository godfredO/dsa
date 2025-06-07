"""You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
English character. You can perform this operation at most k times. Return the length of the longest substring containing the 
same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length


So we are given a string of letters and an integer k. We are told that we can do a character replacement operation k times. We are 
then asked to return the length of the longest substring containing the same repeated letter after the operations. So though poorly 
worded, we want in each operation, we want to change some letter to another letter so that we can have a series of repeated letter 
so if 'ABA' then in our first operation we want to change 'B' to 'A' to yield 'AAA'. In example 1 above s = 'ABAB' , k = 2 and we 
could replace both A's with B's to get 'BBBB' or replace both B's with A's to get 'AAAA' and either way, we have a longest repeated 
character substring of 4.

So this is a sliding window problem. So the first question we want to ask is what does our window represent. Here the window will
represent a substring of our string. And how does that help us solve the question? We will be creating and updating a character
count representing the counts letters within our current window. So we know how to find the length of the current window, which is
length = right + 1 - left. So as we go through, we want find the character that occurs the most in our window and subtract that
value from length of the window. This subtraction will represent the number of character replacement operations needed to make our
substring contain repeated characters of the most frequent letter ie the max value in our counts map. That is if we replaced every 
other letter in our window to the most frequent letter we would have a substring of repeated characters where the character would 
be the most frequent character in our window. Now why do we want to replace all other characters to the most occuring character? 
We do this to minimize the number of operations we need to get a substring of repeated characters. Now does this mean that every 
window will be valid? No. A window is valid only if the number of operations needed to convert every other character into its most 
frequent character is less than or equal to k. If a window is valid we want to track if its the longest such window we've seen. 
So this is the logic we carry out as we widen our window. 

When and how do we shrink our window? We shrink our window if the current window is invalid ie if the minimum number of character
replacement operations needed to yield a substring of repeated characters is greater than k. We shift our left pointer until our 
window until the substring represented by the window becomes valid once again ie number of character replacement operations needed
is less than or equal to k.

In the code we initialize our left pointer at index 0, and use a for loop to generate our right pointer. Then we access the letter
at the right pointer and we increment its count in our counts hashtable. Then we check if our current window is invalid and as 
long as its invalid, we get the current left pointer letter, decrement its count (to remove it from the new window) and increase the 
left pointer (to represent the new window). When we break out of this loop, our window will be valid, so and so if the current window 
length is greater than our stored window length we update our stored window length. At the end we return the maxLength which we 
initialized at 0. This question becomes easier once you understand the conditions involved.

So the time complexity is O(n), since right pointer will be doing a O(n) traversal and the left pointer is also going to do a O(n)
traversal. This is because, once we find an invalid window, we move left till its valid again and then go back to moving right.
Also max(counts.values()), is an O(1) operation because since our string only contains upperCase English letters the max number of 
keys is 26 so max(counts.values()) is O(26) constant O(1) time. Alternatively we could store a maxFrequency variable. After 
incrementing a count, we update this variable if the new count of the current right pointer letter is a greater frequency. 
Interestingly when we shrink our window, we don't need to change this. Why? We are increasing left pointer until the number of
operations needed is equal or less than k. So if we dont update maxFrequency, we will only stop the movement of the left pointer
sooner but then when our maxFrequency is next updated, we can make up those steps we didnt take last iteration. All of this to
say, this optimization is unnecessary and not doesnt even improve the time complexity per se. Phew!!!!
"""


#O(n) time | O(1) space
def characterReplacement(s, k) -> int:
    counts = {}
    left = 0
    maxLength  = 0

    for right in range(len(s)):
        rightChar = s[right]
        addCount(counts , rightChar)


        while right + 1 - left - max(counts.values()) > k and left <= right:
            leftChar = s[left]
            decreaseCount(counts, leftChar)
            left += 1
        
        if right + 1 - left > maxLength:
            maxLength = right + 1 - left
            
    return maxLength



def characterReplacement(s, k) :
    counts = {}
    left = 0
    maxLength  = 0
    maxFrequency = 0

    for right in range(len(s)):
        rightChar = s[right]
        addCount(counts , rightChar)
        if counts[rightChar] > maxFrequency:
            maxFrequency = counts[rightChar]

        while right + 1 - left - maxFrequency > k and left <= right:
            leftChar = s[left]
            decreaseCount(counts, leftChar)
            left += 1
        
        if right + 1 - left > maxLength:
            maxLength = right + 1 - left
            
    return maxLength


def addCount(counts, rightChar):
    if rightChar not in counts:
        counts[rightChar] = 0
    counts[rightChar] += 1

def decreaseCount(count, char):
    count[char]  -= 1 #decrement the character count
    if count[char] == 0: #if after decrement the character count is 0, character is not in current window
        count.pop(char)  #so pop it., last two steps dont affect solution but good for map to accurately represent current window
