#O(n) time | O(n) space
def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0  #initially,there is nothing to the left of first index,so 0
    
    for i in range(len(heights)): #loop for creating the maximum height to the left of current index
        height = heights[i]    #height at current index
        maxes[i] = leftMax #set the left max for current index before updating, ensuring that left max at index 0 is 0
        leftMax = max(leftMax,height) #updating the leftmax

    rightMax = 0  #initial right max for last value in array since there is nothing to the right of len(array) - 1
    for i in reversed(range(len(heights))): #loop in reverse, to determine maximum pillar height to the right of each index
        height = heights[i]
        minHeight = min(rightMax,maxes[i]) #set the min height between right max and left max at index
        if height < minHeight: #if there is space abover our current index, when the pillar , if any, is shorter than left/right max
            maxes[i] = minHeight - height #height of water stored above current index
        else:
            maxes[i] = 0  #if current index's pillar is higher than pillars on either end, no water will be stored there
        rightMax = max(rightMax,height) #finally update rightmax
    
    return sum(maxes)

"""Optimal solution, same time complexity, better space complexity, basically, using two pointers left and right, initialized at ends
of array and comparing the height at each pointer. which ever pointer is lower, move it, then update the left max and right max with
the maximum between the previous value and the height at the current index. Finally update the surface area by subtracting the right or 
left max from the height at the current index.Also you have to handle the edge case that the input array is empty"""
#O(n) time | O(1) space
def waterArea(heights):
    if len(heights) == 0: #edge case , empty input array
        return 0 #has a 0 surface area
    
    leftIdx = 0                     #initialize left pointer , to start of array
    rightIdx = len(heights) - 1     #initialize right pointer, to end of array
    leftMax = heights[leftIdx]      #initialize leftMax to value at start of array
    rightMax = heights[rightIdx]   #initialize rightMax to value at end of array
    surfaceArea = 0               #initialize surface are to 0

    while leftIdx < rightIdx:    #loop condition, keep moving left and right pointers until the meet
        if heights[leftIdx] < heights[rightIdx]: #choose the minimum height, if leftIdx is minimum
            leftIdx += 1         #update current idx iterator on the left
            leftMax = max(leftMax,heights[leftIdx])    #update the left max height
            surfaceArea += leftMax - heights[leftIdx]  #find the area stored at current idx, ie updated left idx
        else:                                        #else if right idx is minimum
            rightIdx -= 1                               #update current idx iterator on the right
            rightMax = max(rightMax,heights[rightIdx])  #update the right max height
            surfaceArea  += rightMax - heights[leftIdx]  #find the area stored at current idx, ie updated right idx
    return surfaceArea






heights = [4, 0, 6, 0, 10]
print(waterArea(heights))