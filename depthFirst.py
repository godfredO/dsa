"""The input is a Node class that has a name and an optional children nodes array, as well as an empty array. The question is to write a
method for this class that traverses the tree using the depth-first search approach, from left to right, and stores all of the nodes names
in the input array, and returns it. The first thing is to update the array by appending the current node's name to the array, then loop over 
the children (from left to right), and call the depth-first search method on each child node, passing in the updated array to the method call. 
At the end of the loop, return the array. This will have the effect of appending the root node's name, then the leftmost child of the root, 
then leftmost child of that child etc thus when a leaf node is reached where the children parameter array is empty, then we come back up to 
the leaf's parent and call the method on the next child in the for loop. Even though in the subtrees the return array statement at the end 
doesnt really do anything, when the root node's call is completed ie the for loop for the root's children has terminated, the return statement
will return the filled array as the answer."""


class Node:

    def __init__(self,name):
        self.name = name
        self.children = []

    #upon adding a child's you create a node with that name before appending
    def addChild(self,name):
        self.children.append(Node(name)) 
    
    #O(v+e) time | O(v) space
    def depthFirstSearch(self,array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array) #child is a node
        return array