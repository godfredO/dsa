"""Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after 
removing k digits from num.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 
Constraints:
1 <= k <= num.length <= 105 ; num consists of only digits. ; num does not have any leading zeros except for the zero itself.



So this is a question best explained by examples. If we have unique digits in descending order say 54321, then to minimize the
result we remove the most significant number. So if k=1, we remove 5 to get 4321, if k=2 we remove 5,4 to get 321. What if we
have unique digits in ascending order say 12345, then in this case we would remove the least significant number ie 5 to get
1234 instead of removing 1 which will give 2345. What if the digits are not unique. Say 9991, since the digits are in descending
order, we remove the most significant to yield 991 instead of 999. And if the values are 1999, again since the digits are in
ascending order, we remove the least significant digit to yield 199 instead of 999. So how do we use a stack to solve this 
problem. We use a monotonic ascending stack. If the value on the stack top is greater than the current value, then we know that
the greater peek value is also a greater significant number, and as such we remove it. Otherwise, we add the current value. If 
say the number is in in perfectly ascending order, then at the end we would have added all the digits so we pop exactly k times.
In otherwords, we want to keep track of the number of pops we have done so far. If we get to the end with less than k pops then
we will make the additional pops. When we have done all k pops, we are ready to return the answer. If the stack is empty after
all k pops, we return "0", otherwise we join the values on the stack into a string ie "".join(stack), though this could lead
to leading zeroes eg 0200. To remove leading zeroes we convert to an integer and re-convert to a string before returning.
"""

#O(n) time | O(n) space
def removeKdigits(num,k):
    stack = []
    
    for c in num:
        while stack and k > 0 and c < stack[-1]:
            stack.pop()
            k -= 1
        stack.append(c)
    
    while k > 0:
        stack.pop()
        k -= 1
    
    return str(int("".join(stack))) if stack else "0"