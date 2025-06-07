"""You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent 
and equal letters and removing them. We repeatedly make duplicate removals on s until we no longer can. Return the final 
string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  
The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay"
 
Constraints:
1 <= s.length <= 105  ; s consists of lowercase English letters.



So this is a foundational question for stacks. Basically, if the current character is the same as the stack peek value, we
pop from the stack without appending the current character, otherwise we append the curernt character. At the end, we join
the contents of the stack and return the result. Read removeAllAdjacentDuplicatesInString.py for using a vital summarizing
technique when this question is generalized to only append when there are k duplicates.
"""
def removeDuplicates(s) :
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
            
    return "".join(stack)