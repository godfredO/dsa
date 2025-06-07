"""Design a max stack that supports push, pop, top, peekMax and popMax.
push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove 
the top-most one.

Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.

So this question is essentially the same as minStack.py and minMaxStack.py. The only difference is the popMax() method which
retrieves the maximum element in the stack, removes it and returns it, and if the maximum element occurs more than once, we
remove the one that is nearest the top of the stack. So how do we handle this? ForpopMax, we know what the current maximum 
(peekMax) is. We can pop until we find that maximum, then push the popped elements back on the stack.
"""
class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxStack = []
    
    def push(self,val):
        maxVal = max(self.maxStack[-1], val) if self.maxStack else val
        self.maxStack.append(maxVal)
        self.stack.append(val)
    

    def pop(self):
        self.maxStack.pop()
        return self.stack.pop()
    

    def top(self):
        return self.stack[-1]
    
    def peekMax(self):
        return self.maxStack[-1]
    
    def popMax(self):
        maxVal = self.peekMax()
        stackBuffer = []
        maxBuffer = []
        while self.top() != maxVal:
            stackBuffer.append(self.stack.pop())
            maxBuffer.append(self.maxStack.pop())
        
        val = self.stack.pop()
        self.maxStack.pop()

        while stackBuffer:
            self.stack.append(stackBuffer.pop())
            self.maxStack.append(maxBuffer.pop())
        
        return val, self.stack, self.maxStack



stack  =  MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
stack.push(2)
print(stack.top())
print(stack.popMax())
print(stack.pop())
print(stack.popMax())