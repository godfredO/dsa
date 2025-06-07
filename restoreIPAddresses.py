"""A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and 
cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" 
and "192.168@1.1" are invalid IP addresses. Given a string s containing only digits, return all possible valid IP addresses that can 
be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses 
in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
1 <= s.length <= 20
s consists of digits only.


This question is solved iteratively in valid_ip_addresses.py so I will put the iterative down below. This here is about solving the
question with backtracking (aka recursion). Since each of the four integers will need to be a subsequence of the original string and
we are not concerned about duplicates here, an n-ary decision tree is in order, in particular a ternary decision tree. This means each
node of our decision tree has three children signifying the different values for the current level given previous choices. Each level
in this tree also signifies the current integer section. I have a solution below, which is my method of implementing the iterative 
solution using backtracking. The time complexity is O(3^4) ie a max of 3 children and 4 levels so constant time O(1) and the depth of 
the tree will always be 4 so that is also constant space. 

First a note about leading zeros , 0 is valid but 01 ie if we are going to have 0 start a section it can only be 0 not 01 or 023 or 
having something come after the 0. Second note is that after we have a valid value for the third section, append this valid string
and make a call for the fourth section, we have our base case. That is if the section is 4, then the remaining elements must be the
last section, so endIdx is len(s) and if this section is valid, we append, join the current array of section strings with dots, 
append the resulting string to the results array and pop the last section we added like we would do if we were backtracking from a
call. It this last section is valid or not, we know that our a valid ip address can only have four sections so we cant go on further
and thus we return. The alternate valid helper function is a direct copy from valid_ip_addresses.py so read that to understand. The
first valid helper function first checks numeric validity and for the leading zero check says that the slice cant start with a 0
unless its a single 0 ie endIdx is exactly startIdx + 1. We could also add an edge case of returning an empty array if the length of 
the input string is greater than 12 (read valid_ip_addresses.py, where we are assured that input string is length 12 or less) and 
that will depend on how we write the solution
"""

#O(1) time | O(1) space
def restoreIpAddresses(s) :
    # if len(s) > 12:
    #     return []
    results = []
    current = []
    dfs(1, 0, s,current, results)
    return results


def dfs(section, startIdx, s, current, results):
    if section == 4:                            #   max depth of tree is 4
        endIdx = len(s)                         #   so slice between start and end of string is our last section
        if valid(s, startIdx, endIdx):          #   if slice between start and end of string is valid
            current.append(s[startIdx:endIdx])  #   append this slice to current
            copy = ".".join(current)            #   join current strings with '.' to form a valid ip address
            results.append(copy)                #   append valid ip string to results
            current.pop()                       #   pop the last section since we wont have another call to backtrack from and pop
        return                                  #   whether last section valid or invalid, don't continue just return
             
    
    for endIdx in range(startIdx + 1 , min(startIdx + 4, len(s))):   #  we can have slice of length 1-3 for current section
        if valid(s, startIdx, endIdx):                               #  test for ip section valididty, if valid
            current.append(s[startIdx:endIdx])                       #  append slice of current section 
            dfs(section + 1, endIdx , s, current, results)           #  go down tree to find next section
            current.pop()                                            #  backtrack by popping appended section   


def valid(s, start, end):
    slice = s[start:end ]
    num = int(slice)
    if num > 255:   #numeric value 0-255
        return False
    
    return end == start + 1 or s[start] != "0"


"""Alternate check for numeric and leading 0 validity based on valid_ip_addresses.py"""
def valid(s, start, end):
    slice = s[start:end ]
    num = int(slice)
    if num > 255:   #numeric value 0-255
        return False
    return len(str(num)) == len(slice)   #leading 0's




def restoreIpAddresses(s) :
    # if len(s) > 12:
    #     return []
    results = []
    current = []
    dfs(1, 0, s,current, results)
    return results


def dfs(section, startIdx, s, current, results):
    if section == 4:                            #   max depth of tree is 4
        endIdx = len(s)                         #   so slice between start and end of string is our last section
        if valid(s, startIdx, endIdx):          #   if slice between start and end of string is valid
            current.append(s[startIdx:endIdx])  #   append this slice to current
            copy = ".".join(current)            #   join current strings with '.' to form a valid ip address
            results.append(copy)                #   append valid ip string to results
            current.pop()                       #   pop the last section since we wont have another call to backtrack from and pop
        return                                  #   whether last section valid or invalid, don't continue just return
             
    
    for endIdx in range(startIdx + 1 , min(startIdx + 4, len(s))):   #  we can have slice of length 1-3 for current section
        if valid(s, startIdx, endIdx):                               #  test for ip section valididty, if valid
            current.append(s[startIdx:endIdx])                       #  append slice of current section 
            dfs(section + 1, endIdx , s, current, results)           #  go down tree to find next section
            current.pop()                                            #  backtrack by popping appended section   


def valid(s, start, end):
    slice = s[start:end ]
    num = int(slice)
    if num > 255:   #numeric value 0-255
        return False
    
    return end == start + 1 or s[start] != "0"



