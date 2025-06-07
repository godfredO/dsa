"""Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:
FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 
Example 1:
Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].


So this solution is rather interesting. We need to know the element with the highest frequency, and if there is a tie for
max frequency we need to know which of the tie elements is closer to the top of the stack. To do this, we keep two hashmaps
and a maxFreq variable on the class definition.

The maxFreq variable will just store the maximum frequency of any element in our class. The two dictionaries will be the 
frequency dictionary and the group dictionary. The first one will store value:freq and the second will store freq:[va1,val2].
Hence if we add 5, freq[5] = 1, groups[1]=[5], add 7 freq[7]=1, groups[1]=[5,7], add 5 freq[5]=2, groups[2]=[5]. Note that
at this point we have freq= {5:2,7:1}, groups= {1:[5,7],2:[5]}, and maxFreq = 2. In otherwords, when we push an element, we
first increment the frequency of that element in the frequency dictionary, and then store the current frequency. Then we 
check if that current frequency is greater than maxFrequency, in which case we update maxFrequency to be the frequency of 
the element we just pushed. Then finally, we append the element to that frequency's key in the groups hashtable.


So if we want to pop, we access the group with maxFreq as key and pop from the end, and storing the popped number. Then we 
access the popped number's key in the freq dictionary and decrement it by 1. Also, if after popping the maxFreq key in groups 
is empty, we reduce maxFrequency by 1, before returning the popped element
"""

class FreqStack():
    def __init__(self):
        self.freq = {}
        self.groups = {}
        self.maxFreq = 0
    

    def push(self,x):
        
        if x not in self.freq:
            self.freq[x] = 0
        self.freq[x] += 1

        f = self.freq[x]
        
        if f > self.maxFreq:
            self.maxFreq = f
        
        if f not in self.groups:
            self.groups[f] = []
        self.groups[f].append(x)
    

    def pop(self):
        x = self.groups[self.maxFreq].pop()
        self.freq[x] -= 1
        if not self.groups[self.maxFreq]:
            self.maxFreq -= 1
        return x


        