"""Given an array of building heights ie positive non-zero integers and a direction that all of the buildings face, return an array of the 
indices of the buildings that can see the sunset. A building can see the sunset if its strictly taller than all of the buildings that come 
after it in the direction that it faces. The building at index i has height denoted by buildings[i] and all the buildings face the same
direction, as given in the direction input and its either 'EAST' or 'WEST' and in relation to the input, these are intepreted as right
for east and left for west. As such the direction will affect the startingIdx and step ie 0 or len(buildings) -1 and +1 or -1 respectively.
Also the indicies in the output array should be sorted in ascending order. There are two solutions discussed below, read both lol.
The first solution starts iterating from the first building in a direction; the second solution uses a stack and starts iterating from the
last building in a direction."""

"""
The first solution uses a running Maxium and the direction for traversing the array in the direction the buildings face ie end of array for 
east, start of array for west. At each step of the iteration we ask if the current building height is higher than the running maximum. if it 
is, append its index to the output array and update the runningMaximum, since every building that comes after would have to be taller to see
the sunset. This running Maximum starts of at 0 because the first building in the direction the buildings face will always see the sunset.
Then the second in the direction the buildings face will have to taller than the first and if it is indeed taller will become the new
running maximum since every building after that will have to be taller to see the sunset and so on and so forth. This running maximum 
approach reminds me of the array of products calculatio where we realize that on the left the leftProduct starts of as 1 and on the right, 
the rightProducts starts of as 1 and after using it to update the output at that index, we update the running leftProduct/rightProduct with 
the value at that index to be the new left/rightProduct for the next value in the list. Here we only do the update when a building is taller 
than the running maximum in the direction we face, remembering to add the index to the output before or after. Also since the loop condition 
will change based on direction since startingIdx and step change due to direction, we must write the condition in a way that handles both 
possiblities. Also as far as the sortedness of the output array, we keep the output as is if direction is WEST since we iterate in sorted
order of indices. If direction is EAST we reverse before returning since we iterate in reversed sorted order of indices ie descending order.
"""

#O(n) time | O(n) space, where n is the length of buildings array
def sunsetViews(buildings, direction):
	buildingIndices = []
	runningMaximum = 0
	
	startingIdx = 0 if direction == "WEST" else len(buildings) - 1
	step = 1 if direction == "WEST" else - 1
	
	while startingIdx >= 0 and startingIdx < len(buildings) :
		
		if buildings[startingIdx] > runningMaximum:
			buildingIndices.append(startingIdx)
			runningMaximum = buildings[startingIdx]
		startingIdx += step
	
	if direction == "EAST":
		return buildingIndices[::-1]
	return buildingIndices
		
"""
This solution uses a stack and since it doesnt use a running Maximum, the direction for traversing the array of buildings is flipped in 
order to start in the direction of the tallest building that could see the sun in a direction.This is start of array for EAST, end of array 
for WEST.Thus assuming each building can see the sun and the direction is east the tallest building will be index 0. Another way of saying
this is that if direction is WEST, then for the building at buildings[len(buildings)-1] has to be taller than every building for it to
see the sun. Similarly if direction is EAST, then the building at buildings[0] has to be taller than every building for it to see the sun.
This is the reverse of the previous solution where we knew that the first building in the direction always sees the sun. Here we start at
the last building in the direction and that only sees the sun if it is the tallest. At each step in the iteration we add the building index 
to the stack. Before we add each element we ask if the last element in the stack will be blocked by the new stack addition. It will be blocked 
if its height is equal to or less than the new stack addition. If the last stack building will blocked, then pop it before adding the current 
building to the stack. Like most stack questions we use a while loop ie we keep checking the new peek height and comparing it to the current
loop building height and keep popping as long as the height on top of the stack is less than or equal to the stack or the stack is empty.
This means that when we this inner while loop finally terminates and we add the current building height to the stack, it will be shorter than
all the remainig buildings on the stack and becomes the new peek value of the stack. Thus at any point in time, the heights on the stack are
always in descending order in terms of height from the tallest at the bottom of the stack to the shortest at the top of the stack and the 
indices will be in sorted order or reversed sorted order based on the way we iterate.Since we start from the last building in a direction,
we revers the stack elements before returning the stack as the output if direction is 'WEST' since in that case we start iterateing from 
len(buildings) - 1. Also note that the startingIdx and step will be reversed compared with the previous solution.
"""
#O(n) time | O(n) space, where n is the length of buildings array
def sunsetViewsII(buildings, direction):
	buildingIndices = [] #stack
	startingIdx = 0 if direction == "EAST" else len(buildings) - 1
	step = 1 if direction == "EAST" else -1
	
	while startingIdx >= 0 and startingIdx < len(buildings):
		
		while len(buildingIndices) > 0 and buildings[buildingIndices[-1]] <= buildings[startingIdx] :
			buildingIndices.pop()
			
		buildingIndices.append(startingIdx)
		
		startingIdx += step
	
	
	if direction == "WEST":
		return buildingIndices[::-1]
	return buildingIndices


"""This last solution uses the next greater element algorithm in monotonicStacks.py the only difference is that since a buildings
view is also blocked by an equal height building in the direction in which it faces hence the stack maintains a strictly increasing
property. This solution is basically the same as in buildingsWithAnOceanView.py, and is actually the exact same as solution II
above, just that instead of cleverly avoiding repeated code using startingIdx and step, like was done in solution II I well repeat 
code for simpler understanding."""
def sunsetViews(buildings, direction):
    stack = []
    if direction == "EAST":
        for i in range(len(buildings)):
            while stack and buildings[stack[-1]] <= buildings[i]:
                stack.pop()
            stack.append(i)
    else:
        for i in reversed(range(len(buildings))):
            while stack and buildings[stack[-1]] <= buildings[i]:
                stack.pop()
            stack.append(i)
    return stack if direction == "EAST" else stack[::-1]
    