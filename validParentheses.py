"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.



This question is the same as balancedBrackets.py from algoexpert.io. Anyway, '()', '()[]{}]' are valid. ')()' is invalid 
since it starts with a closing bracket. '(]' is invalid because different type brackets are matching one another. So we
use a stack to solve this problem. We are able to use a stack because matching opening and closing brackets happens in 
a contiguous manner, since a closing bracket is always going to match the most recent bracket. What does our stack store? 
It stores the unmatched opening brackets in order from left to right as we iterate the input string. So if our current 
character is an opening bracket we append to the top of the stack. If its a closing bracket, we check if it matches the 
opening bracket on top of the (non-empty) stack, and if it matches, we know pop the stack peek. If the closing bracket 
doesnt match we return False. If the stack is empty when we come upon a closing bracket, then there is no opening bracket 
to match so we return False. To solve this question we store a hashmap that matches closing brackets to opening brackets. 
If the current character is a key in this hashmap, then its a closing bracket otherwise its an opening bracket (we are 
assured string only contains '(',')','{','}','[',']'). At the end of the loop, we want to check that every opening bracket 
was matched, which will be the case if the stack is empty at the end of the for loop. So if the stack is empty, the string 
was valid, otherwise its not.  The solution is O(n) time and space.
"""
#O(n) time | O(n) space
def isValid(s):
    stack = []
    matching = {')':'(','}':'{', ']':'['}

    for i in range(len(s)):
        char = s[i]
        if char in matching:
            if stack and stack[-1] == matching[char] :
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    return not stack