"""The question asks to write a function that takes in an array of integers representing a stack and recursively sorts the stack in place.
The array must be treated as a stack, with the end of the array as the top of the stack, and as such the only allowable operations are
only pop, push and peek. The solution is first of all recursive and based on the fact that an empty array is considered sorted. So there
are two main helper functions, sortStack(stack) which is the main function and insertInSortedOrder(stack, value). When we make a recursive
call to sortStack, the first thing it does is pop the value at the top of the stack and store a reference to this, here the variable used
is top. Then it recursively calls sortStack(stack) ie calls itself on the remaining stack. It keeps doing this ie pop and recursive call
on the remaining stack until the base case which is an empty stack, at which point it returns the stack. So if the the array is 
[-5,-7,-2,4,3,2], will pop and store each number and when the stack has -5, that is popped and stored as top then the next call with the
empty array will return the array. So when that happens the second helper function insertInSortedOrder(stack, top) is called ie
insertInSortedOrder([], -5). The base case of this is if the stack is empty or the value is equal to or greater than the peek value of
the stack ie would come after the peek value in sorted array, in which case, we append the value to the stack and return to sortStack,
then sortStack will return the returned stack with value inserted in sorted order. That is sortInStack will return [-5] to the call with
top = -7. When this receives the returned stack, that recursive function will then call insertInSortedOrder([-5],-7). Clearly the stack
is not empty neither is -7 greater than or equal to the peek value, -5. So the recursive case in insertInSortedOrder() is to pop the stack,
store a reference to the popped value and re-call itself recursively to insert value in sorted order. Thus inside 
insertInSortedOrder([-5],-7), we get top = -5 ie top = stack.pop() followed by insertInSortedOrder([],-7). This call will hit the base case 
of an empty stack, append -7 and return. But this time it would be returning to a previous call of insertInSortedOrder ie the original 
insertInSortedOrder([-5],-7), but this time stack is [-7] and top = -5. Now the next step is to append the top value to the sorted stack 
ie [-7,-5] and since this append is the last line in insertInSortedOrder(), execution is returned to sortStack which will then call 
insertInSortedOrder([-7,-5],-2). This function starts with n calls of sortStack() and each of these calls will make a call to 
insertInSortedOrder. If that call hits the base case, it will be constant time ie append and return but if not the recursive calls will 
pop at most every element of and have up n recursive calls of insertInSortedOrder, leading to a time complexity of O(n^2) and a space 
complexity of O(n) due to the use of the recursive stack."""

# O(n^2) time | O(n) space
def sortStack(stack):
    if len(stack) == 0:
        return stack
    
    top = stack.pop()

    sortStack(stack)

    insertInSortedOrder(stack,top)

    return stack

def insertInSortedOrder(stack,value):
    if len(stack) == 0 or stack[len(stack) - 1] <= value:
        stack.append(value)
        return
    
    top = stack.pop()

    insertInSortedOrder(stack,value)

    stack.append(top)



stack = [-5,2,-2,4,3,1]
print(sortStack(stack))