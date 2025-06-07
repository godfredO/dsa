"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8


This question is essentially the same as generateDivTags.py from algoexpert.io only difference is that we replace
opening divs with opening parentheses and closing divs with closing parentheses. Solution I is thus a rewritting of
the solution presented in generateDivTags.py.

The essence of solution II is the same as solution I, but we use a stack, to append and pop either an opening or closing
parentheses instead of concatenating an opening / closing parentheses with the current formed parentheses to yield a new 
cuurrent and then making the recursive call with the new current. This solution captures the recursive soul of this 
solution even more, by using the append and pop operations to demonstrate the backtracking nature of the solution.

"""
def generateParenthesis(n):
    output = []
    getPairs(output,"", n, n)
    return output

def getPairs(output,current, openingTags, closingTags):
    if openingTags > 0:
        newCurrent = current + '('
        getPairs(output, newCurrent, openingTags - 1, closingTags)
        
        
    if closingTags > openingTags:
        newCurrent = current + ')'
        getPairs(output, newCurrent, openingTags, closingTags -1)
    
    if closingTags == 0:
        output.append(current)

#Solution II
def generateParenthesis(n) :
    output = []
    stack = []
    getPairs(output,stack, n, n)
    return output

def getPairs(output,stack, openingTags, closingTags):
    if openingTags > 0:
        stack.append('(')
        getPairs(output, stack, openingTags - 1, closingTags)
        stack.pop()
          
    if closingTags > openingTags:
        stack.append(')')
        getPairs(output, stack, openingTags, closingTags -1)
        stack.pop()
    
    if closingTags == 0:
        output.append("".join(stack))
        
        