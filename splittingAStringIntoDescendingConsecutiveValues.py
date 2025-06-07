"""You are given a string s that consists of only digits. Check if we can split s into two or more non-empty substrings such that the 
numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings 
is equal to 1. For example, the string s = "0090089" can be split into ["0090", "089"] with numerical values [90,89]. The values are in 
descending order and adjacent values differ by 1, so this way is valid. Another example, the string s = "001" can be split into 
["0", "01"], ["00", "1"], or ["0", "0", "1"]. However all the ways are invalid because they have numerical values [0,1], [0,1], and [0,0,1] 
respectively, all of which are not in descending order. Return true if it is possible to split s​​​​​​ as described above, or false otherwise.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "1234"
Output: false
Explanation: There is no valid way to split s.

Example 2:
Input: s = "050043"
Output: true
Explanation: s can be split into ["05", "004", "3"] with numerical values [5,4,3].
The values are in descending order with adjacent values differing by 1.

Example 3:
Input: s = "9080701"
Output: false
Explanation: There is no valid way to split s.



We want to split the string into at least two sub-strings such at the numerical values of the substrings are in descending order and
adjacent values differ by exactly 1. If there is such a split of sub-strings, we need to return True. So this is going to use backtracking
and the moment we hit the True case, we need to bubble it up  otherwise if we all possibilities fail return False. 

How will a decision tree be like? The first for paths could be a slices of 1 digit, 2 digits, 3 digits, 4 digits all the way to n digits.
Thus the first layer will have n branches. Then the second layer will also contain n branches. Now we will have pruning to make our calls
efficient as possible. So say that s = '4321' then the first layer will be 4, 43, 432, 4321. And then for the path starting from '4',
the remaining digits is 321 so the second layer for that path will be 3, 32, 321 and so on. Each time, we pass in the value of the previous 
layer so that we can only continue down a path if its prevValue - 1. So for the first layer of 4, only a second layer choice of 3 will do.
Then the third layer for that path will be 2, 21 and again only will workd and the last layer of that path will be 1 and when we call our
function with an index that equals the length of the string, we know that we found a solution. Each subsequent call will be made with 
endIdx + 1 and we loop from startIdx to len(digits). 

So we will actually need an outer loop since we have no restricitons on the first layer values, and so we will have to consider all possible 
slices from 1 digit to n-1 digits and that becomes the value against which the choices are made against (outer loop like a 2-d matrix grid 
problem). We go up to n-1 digits because we need to split our string into at least two separate numbers. However the backtracking portion
will be looping from startIdx to the end of the string.


"""


def splitString(s) :
    for i in range(len(s) - 1):
        value = int(s[:i+1])
        if dfs(s,i+1, value):
            return True
    return False

def dfs(s,idx, prev):
    if idx == len(s):
        return True
    
    for j in range(idx, len(s)):
        current = int(s[idx:j+1])
        if current == prev - 1 and dfs(s, j+1, current):
            return True
    return False