"""Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, and /. 
Each operand may be an integer or another expression. Note that division between two integers should truncate 
toward zero. It is guaranteed that the given RPN expression is always valid. That means the expression would always 
evaluate to a result, and there will not be any division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 
Constraints:
1 <= tokens.length <= 104  
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].



Reverse Polish notation (RPN), also known as reverse Łukasiewicz notation, Polish postfix notation or simply postfix notation, 
is a mathematical notation in which operators follow their operands, in contrast to Polish notation (PN), in which operators 
precede their operands. It does not need any parentheses as long as each operator has a fixed number of operands. For instance, 
to add 3 and 4 together, one would write 3 4 + rather than 3 + 4. If there are multiple operations, operators are given 
immediately after their final operands (often an operator takes two operands, in which case the operator is written after the 
second operand); so the expression written 3 - 4 + 5 in conventional notation would be written 3 4 - 5 + in reverse Polish 
notation: 4 is first subtracted from 3, then 5 is added to it. The concept of a stack, a last-in/first-out construct, is 
integral to these actions.

Now concerning the question here, we are told that if there is a division between two integers, we should truncate toward zero,
so that is something we need to make sure to handle in Python. We are also assured that the RPN expression will be valid. So we 
know that each operator will apply to the previous two values on the stack. So if we have 2 1 +, we will add the previous  two
values on the stack [2,1], add them together and add the result to the stack, so [3]. So if the full expression is 2 1 + 3 *, 
then with the stack containing the result of the previous operation [3], we add 3, [3,3] and when we get to * we again apply it
to the two previous values on the stack so 3*3=9 and that goes onto the stack [9] which in this case is the final answer. So a
major key to writing the code here is to recognize that if the current token is an operator, we will be popping exactly two times
from the stack. Hence the solution more closely resembles using a stack for a string problem, and hence will contain if statements
instead of while statements (read simplifyPath.py). Also note that we are given a bunch of strings so we need to ensure we convert
to an integer before appending to the stack. Now finally, how do we truncate the division towards 0 in Python. We simply convert
the result of decimal division to an integer ie int(). Take -3 2 / . The division -3/2 yields -1.5. If we use floor division -3//2
this will yield -2. However if we convert the result to an integer int(-1.5), we get -1, which is truncating towards zero.


"""
def evalRPN(tokens):
    stack=[]
    for c in tokens:
        if c == '+':
            operandTwo = stack.pop()
            operandOne = stack.pop()
            result = operandOne + operandTwo
            stack.append(result)
        elif c == '-':
            operandTwo = stack.pop()
            operandOne = stack.pop()
            result = operandOne - operandTwo
            stack.append(result)
        elif c == '*':
            operandTwo = stack.pop()
            operandOne = stack.pop()
            result = operandOne * operandTwo
            stack.append(result)
        elif c == '/':
            operandTwo = stack.pop()
            operandOne = stack.pop()
            result = operandOne / operandTwo
            stack.append(int(result))
        else:                                   
            stack.append(int(c))
    return stack[0]