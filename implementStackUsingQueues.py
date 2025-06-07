"""Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions 
of a normal stack (push, top, pop, and empty).

Implement the MyStack class:
void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.

Notes:
You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty 
operations are valid. Depending on your language, the queue may not be supported natively. You may simulate a queue using a 
list or deque (double-ended queue) as long as you use only a queue's standard operations.
 
Example 1:
Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 

Constraints:
1 <= x <= 9  ;  At most 100 calls will be made to push, pop, top, and empty  ;  All the calls to pop and top are valid.
 

So first off, this solution is going to implement the Mystack class with a single queue (instead of two). So what is this
ridiculous question telling us. Well a stack uses the LIFO priciple, a queue uses a FIFO principle. So the question is 
asking us to use the FIFO principle to achieve the LIFO principle. The reason why this is important is that if we use a
deque in Python, we are able to append and pop from either side of thhe deque, but a deque is a double ended queue not a
regular queue. We could much easily impleement a stack with a deque ; we would appendleft(), the top of the queue will 
always be at index 0, and we popleft(), and all these operations will be O(1) like in a stack. But in a queue, we append() 
to the end (ie right not left), you popleft(), and the top of the queue will be end of the array. That is to say when we
use a queue to implement a stack, we would have to go from the front of the array to the end in order to pop. Thus we are
restricting ourselves to using only the operations that are native to a queue to achieve operations that are native to the
stack. You see this question's main aim is to test if you know the differences between a stack and a queue. For the top()
method however, it turns out looking at the value at the end of a queue is native to the queue data structure. So the main
difference is in the pop operation, which now becomes a O(n) instead of O(1) time. So how do we actually implement the 
pop() method with only the queue's native popleft()? Say the queue has 3 values ie len(queue) = 3. Then, we popleft() and 
append len(queue) - 1 times. After this, the previous last value will now be at the front of the queue ie the queue's 
elements will be shifted. Then we popleft() one last time and return that value. So if we have [1,2,3], we get [2,3,1],
[3,1,2] then we popleft() one time and return 3. In the step where we popleft() and append, we can just call our push
method, ie popleft() and push just reuse code.
"""

from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()
    
    def push(self,x):
        self.stack.append(x)
    
    def pop(self):
        n = len(self.stack)
        for i in range(n-1):
            self.push(self.stack.popleft())
        return self.stack.popleft()

    def top(self):
        return self.stack[-1]
    
    def empty(self):
        return len(self.stack) == 0



"""If we were allowed to use a deque's appendleft() feature"""
class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.appendleft(x)

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack)  == 0