"""The question gives an input node class where each node has a name and an optional children list and we are 
asked to write a breadth-first search method that takes in an array and adds the names of the nodes. So whenever 
we do a breadth-first search we use a queue so that we can popleft(). When doing dfs we use a stack but since 
Python gives us access to the recursive stack we may not realize that we are using a stack. So when a queue is 
initialized, we add the node on which the method is called to the queue. Then we have a while loop that runs
as long as the queue is non-empty. Inside the queue, we popleft for the current node, append its name to the 
array, and add then in a for loop, add each child to the queue. When the while loop terminates we return the 
array. In Python, to access a queue, we have to do an import 'from collections import deque', initialize an 
empty queue = deque(), to pop from the front, it is node = queue.popleft() and to append to the end it is 
queue.append(node). """

class Node:
    def __init__(self,name):
        self.name = name
        self.children = []
    
    def addChild(self,name):        # addChild is called on Node self, with child name
        self.children.append(Node(name))
    
    #O(v+e) time | O(v) space
    def breadthFirstSearch(self,array):
        queue = [self] #pass in the root node as self
        while len(queue) > 0: #while the queue is not empty
            current = queue.pop(0) #first in first out
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array
