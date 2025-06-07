"""You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from 
s and removing them, causing the left and the right side of the deleted substring to concatenate together. We repeatedly 
make k duplicate removals on s until we no longer can. Return the final string after all such duplicate removals have been 
made. It is guaranteed that the answer is unique.

Example 1:
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Example 2:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Example 3:
Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 
Constraints:
1 <= s.length <= 105  ; 2 <= k <= 104  ; s only contains lowercase English letters.


This question is really interesting. It uses a stack summarizing technique first introduced in onlineStockSpan.py optimal
approach. Anyway, how do we use this to summarize the string on a stack so that we know when we have 3 consecutive 
duplicates. Well, on the stack we push [char,count]. So we first check if the current char is the same as the char at index 
0 of the stack peek value. If it is, we increment the count of hte stack peek value by 1. Otherwise, we push [char,1]. Again 
note that since this is a string application of stack we have an if statement instead of a while loop.  Then we check if the 
current stack peek value has a count that equals k. If it does, we pop that value from the stack, and this is how we remove k 
consecutive chars. After we have summarized the entire string, we go through the stack and build our output string.
"""
def removeDuplicates(s,k):
    stack = []

    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
        else:
            stack.append([c,1])
        
        if stack[-1][1] == k:
            stack.pop()
    

    output = []
    for char,count in stack:
        output.append(char*count)
    return "".join(output)