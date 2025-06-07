"""You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:
Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.
For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".


Hint 1 : Note what actually matters is how many 0s and 1s are in odd and even positions
Hint 2 : For every cyclic shift we need to count how many 0s and 1s are at each parity and convert the minimum between them for 
each parity


So we are going to start with the O(n^2) solution, use some clever observations and sliding window, to make it an O(n) solution.
The O(n^2) solution would involve re-creating new strings to represent each new type 1 operation but we dont have to do this.
Now the first thing to realize is that we are allowed to do operation type 1 ,as many times as we want or need to in order to
minimize the number of type 2 operations we need to do, in order to have an alternating string. The next thing to realize is 
that if we do type 1 operations k times, we are esentially moving a suffix of size k and making it a prefix ie from 1100 if we
do type 1 operations 2 times we end up with 0011 (and if we did type 1 operations n times, we end up with the original string).
The main idea is to realize that the type 1 operations can be represented by treating this as a string with circular indices
or wrap around indices. And such questions are solved by appending the original string to its own end, and scanning substrings 
of width equal to the original string length. For example if our string is 1100, the type 1 operations yield 1100, 1001, 0011, 
0110, 1100. To represent this in code we just append 1100 to itself to get 11001100 and scan subarrays of a width equal to the 
original string ie 4 . So when we scan subarrays of size 4 from 11001100, we get 1100, 1001, 0011, 0110, 1100. And these 
represent doing type operations 0 - n times. So by treating the string as though it had circular indices, we can convert the
type 1 operations into a fixed width sliding window problem.

Now say the input is size n, there are always only two alternating strings of size n either starting with 0 or 1. If n is 6,
then we can have 010101 or 101010. If n is 4 we can have 0101 or 1010. Basically we can decide to generate the two alternating
strings of the same size as our expanded string, and determine the number of differences that exist between the alternating 
strings and our expanded string, for each substring / sliding window of size equal to the original string. Once determine how 
many differences there are and take the least number of differences as our answer. This check of comparing our expanded string 
to the two alternating strings of size 2n,takes linear O(n) time. This is thus a fixed width sliding window question with
circular indices, similar to minimumSwapsToGroupAll1'sTogetherII.py. Thus by using circular indices and fixed width sliding
window technique, we are able to optimize type 1 operations ie the window of the expanded string with the minimal differences 
compared to the alternating strings and type 2 operations ie the alternating string with the minimal differences compared to 
the most optimal window of the expanded string  and choose the optimal solution as the minimal number of type 2 operations you
need to perform to make the string alternating after performing the optimal number of type 1 operations. Also just a note, we
use the modulo operation to generate the alternating strings. The differences between the alternating strings and the 
expanded strings within the sliding window represent the number of slips needed to make the substring represented by the
window into an alternating string. In the code below there are two ways of coding it up and each has a different order of how
we advance our left pointer and right pointer. In the first solution, we first compare the first substring of size equal to
the width of our sliding window before comparing the remaining array. The second solution just uses a single for loop to to
build the first window and update the left pointer on the next iteration. I prefer the first, since I find that coding fixed 
width sliding window solutions by first tackling the first window makes it easier for me to wrap my head the solution steps.
around



"""


def minFlips(s):
    width = len(s)
    circularS = s + s

    alt1, alt2 = "", ""
    for i in range(len(circularS)):
        alt1 += "0" if i%2 else "1"
        alt2 += "1" if i%2 else "0"
    
    
    diff1 , diff2 = 0,0
    for j in range(width):
        if circularS[j] != alt1[j]:
            diff1 += 1
        
        if circularS[j] != alt2[j]:
            diff2 += 1

    minDiff = min(diff1,diff2)
    left = 0
    for right in range(width,len(circularS)):
        if circularS[left] != alt1[left]:
            diff1 -= 1
        if circularS[left] != alt2[left]:
            diff2 -= 1
        left += 1

        if circularS[right] != alt1[right]:
            diff1 += 1
        if circularS[right] != alt2[right]:
            diff2 += 1

        minDiff = min(minDiff, diff1, diff2)     #compare the current differences to the minimum differences seen so far
    
    return minDiff



def minFlips(s):
    n = len(s)
    s = s + s

    alt1, alt2 = "", ""
    for i in range(len(s)):
        alt1  += "0" if i%2 else "1"
        alt2  += "1" if i%2 else "0"

    res = len(s)     #maximum number of difference, could also use float("inf")
    diff1, diff2 = 0,0
    left = 0
    for right in range(len(s)):
        if s[right] != alt1[right]:
            diff1 += 1
        if s[right] != alt2[right]:
            diff2 += 1

        if right + 1 - left > n:
            if s[left] != alt1[left]:
                diff1 -= 1
            if s[left] != alt2[left]:
                diff2 -= 1
            left += 1

        if right + 1 - left == n:
            res = min(res, diff1, diff2)
    return res
