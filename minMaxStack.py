""" The question asks to write a MinMaxStack class for a Min Max Stack. The class should support pushing and popping values on and off
the stack, peeking at the value on top of the stack, getting both the minimum and maximum values in the stack at any point in time. 
All the class methods, when considered independently, should run in constant time and with constant space. Now a stack is a data 
structure that supports the last in first out (LIFO) principle. The push() method adds a value to the top of the stack, the peek() 
method shows the value on top of the stack, the pop() removes the value on top of the stack ie last item added. All these methods can 
be handled with a regular array stack ie array.append(), array[-1], array.pop() and are all constant time. The getMin() method should 
return the minimum value in the stack and the getMax() method should return the maximum value in the stack. Using array methods to get 
the min and max values would involve iterating through the array ie linear time, so how do we find the min and max without traversing. 
One option would be to track the min and max values using class attributes but in that case if we pop the element stored in the min/max
attribute, then we have an incorrect value stored on the class. An improvement on this idea is to store the min and max values at each 
point of the stack using an array of dictionary values. That way when we pop an element from the end of the stack, we also pop the 
corresponding dictionary object but we will still have an object corresponding to the new peek value. This way, the min and max will 
always return the min and max at the current point of the stack and still achieve O(1) access. So that is what we do here, the class 
instantiation method has a stack and a minMaxStack which are both arrays. When we push a number, we create a new dicitonary object with 
the number as the value for the min and max keys in this dictionary object. If this is the first first element then it the correct min 
and max at that point in the stack, so we add the number to the stack attribute array and the dictionary to the minMaxStack attribute 
array. If there are elements on the stack already, then to update to the actual min,max we just compare with the peek value of the 
minMaxStack attribute array chose the minimum of the number and the peek's min key value  and do the same with the max key before adding
the number to the stack attribute array and the dictionary to the minMaxStack attribute array. Since looking at peek values is constant
time, we are able to handle all the methds in constant time. Then to return the min, max value we just look at the min,max key values in
the peek element of the minMaxStack. 
"""


class MinMaxStack:

    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # O(1) time | O(1) space
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space
    def push(self,number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack): # check if the minMaxStack list of objects is empty
            lastMinMax = self.minMaxStack[len(self.minMaxStack)-1]
            newMinMax["min"] = min(lastMinMax["min"],number)
            newMinMax["min"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["min"]

    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["max"]
