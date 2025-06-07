""" The question asks to write a function that takes in an array of positive integers representing the heights of adjacent buildings and 
returns the area of the largest rectangle that can be created by any number of adjacent buildings, including just one building. All 
buildings have the same width of 1 unit. The width of a created rectangle is the number of buildings used to create the rectangle and 
its height is the height of the smallest building used to create it. Below, a brute force / naive solution which uses a double sweep 
through the array (O(n^2) time) as well as an optimal solution that uses a stack are discussed (O(n) time | O(n) space). Stacks are useful 
in questions that require contiguity.
"""

"""Brute-force solution where we iterate through the array. At each step we take the current building height
as the rectangle height. To find the rectangle width, we iterate to the right and to the left for adjacent buildings
whose height is equal to or greater than the current building height. Once we have the index of the left and right
bounds of the current rectangle we calculate the area and update the max rectangle area. """
#O(n^2) time | O(1) space
def largestRectangleUnderSkyline(buildings):
    maxArea = 0 #initialize return value

    for pillarIdx in range(len(buildings)):
        currentHeight = buildings[pillarIdx]

        furthestLeft = pillarIdx #go left if next building to the left has greater or equal height, stay within bounds
        while furthestLeft > 0 and buildings[furthestLeft - 1] >= currentHeight: #i=0 has no left boundary also bounds
            furthestLeft -= 1
        
        furthestRight = pillarIdx #initialize right boundary at current idx and keep updating if we can extend right
        while furthestRight < len(buildings) -1 and buildings[furthestRight + 1] >= currentHeight:#last, no right bound
            furthestRight += 1 #go right if next building to the right has greater or equal height, stay within bounds

        areaWithCurrentBuilding = (furthestRight - furthestLeft + 1) * currentHeight #add one to width for pillarIdx
        maxArea = max(areaWithCurrentBuilding, maxArea)
    return maxArea

"""Optimal solution where we iterate through the input array and store indices in a stack. Before we append the current iteration index to 
the stack, we check if we have reached the right bound of the stack's peek values' rectangle. This happens if the height at the current index 
in the loop is less than the peek value's height. So we pop the peek value, access the height, calculate the width of its rectangle, calculate 
the area and update max area if needed. To calculate the width, realize that the right bound is the current iterator index and the left bound 
is the peek value that was popped, if the stack is not empty after popping. However if the stack is empty after popping, (because the peek value 
we popped was the only element), it must mean that the rectangle width extends to the beginning of the array of array and so the width is simply 
the current iterator index. This is because since we pop and calculate areas of peek values when the height at the iterator is less, it must 
mean our popped peek value is either the first element in the array or it was lower than all its predecessors all the way to the beginning of 
the array. Either way, the width of its rectangle in that case is simply the current iterator value. Note that we use a while loop to pop, 
calcualate area and update maxArea, for as long as the stack is non-empty and the current building height in the for loop is less than the 
current stack peek value. This means that one building height can pop all the elements of the stack before we add it to the stack. At the end, 
the last element will still be on the stack in addition to any building height that was less than all the heights that came after it. As such 
there are two solutions below with different techniques to handle the remaining indices on the stack. In the first method we use enumerate() 
to access indices and building heights and the input to enumerate is the concatenation of the buildings array and [0] ie an array with 0 height. 
This way we know that 0 will be lower than any building height (and a 0 building height has no area so wont affect our solution), and as such by 
tacking it unto the end of the buildings array the 0 building height entry will pop every remaining index on the stack. The second solution is to
have a secondary while loop after the first for/while loop, to pop and calculate areas and update max area for all indices still on the stack at 
the termination of the first loop."""
#O(n) time | O(n) space
def largestRectangleUnderSkyline(buildings):
    pillarIndices = [] #stack
    maxArea = 0
    for idx,height in enumerate(buildings + [0]):#add a zero-indexed building O(n), to pop all remaining values
        while pillarIndices and height < buildings[pillarIndices[-1]] : #if current height is less than peek value
            pillarHeightIdx = pillarIndices.pop() #compute the area of rectangle of height = peek value, pop peek value
            pillarHeight = buildings[pillarHeightIdx] #access the height
            #if stack is empty then the rectangle of popped value height has a left bound at array start 0 so width of idx - 0
            #this is because in this stack the peak value is greater than all values below it so must have popped all the way to start
            width = idx if len(pillarIndices) == 0 else idx - pillarHeightIdx 
            maxArea = max(width*pillarHeight,maxArea) #update max area

        pillarIndices.append(idx)
    return maxArea


"""Optimal solution but instead of tacking a 0 at the end to clear all remaining building heights that are in ascending order
I do a second pass through the stack to clear the stack and update maxArea when the iterator in the first loop reaches the end
of the array. This means the heights of the remaining indices on the stack are in ascending order.. Particularly the logic for 
calculating the width is the same as above. Time and Space complexity is also the same. This question is also known as the 
Largest Rectangle Under A Histogram"""
#O(n) time | O(n) space
def largestRectangleUnderSkyline(buildings):
    stack = []
    maxArea = 0 #Initialize at 0 because we know that we expect non-negative integers as building heights

    for idx in range(len(buildings)): #idx represents right  boundary and stack[-1] + 1 is the left boundary
        while stack and buildings[idx] <= buildings[stack[-1]]: #idx is right boundary and stack is not empty
            areaIdx = stack.pop() #if the stack has only one element, after popping, stack is empty meaning width is just idx
            areaHeight = buildings[areaIdx]
            areaWidth = idx if not stack else idx - stack[-1] -1
            maxArea = max(maxArea, areaHeight * areaWidth)
        stack.append(idx)
    
    #clear any remaining indices  on stack, now that the iterator of the first loop is at just out of bounds 
    #tacking a [0] at the end of the first loop iterable is an O(n) operation, just as this second loop is O(n)
    idx = len(buildings) #right boundary is now len(buildings), just out of bounds
    while stack:
        areaIdx = stack.pop() #if the stack has only one element, after popping, stack is empty meaning width is just idx
        areaHeight = buildings[areaIdx]
        areaWidth = idx if not stack else idx - stack[-1] -1
        maxArea = max(maxArea, areaHeight * areaWidth)
        
    return maxArea



buildings = [2,1,5,6,2,3]
print(largestRectangleUnderSkyline(buildings))