"""Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return 
the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
1 <= heights.length <= 105   ;   0 <= heights[i] <= 104   ;


This is the same as the algoexpert question largestRectangleSkyline.py. The approach used here is designed to work with
the standard algorithms in monotonicStacks.py. So the first question to ask is that what is the largest rectangle we can
form with the height at any index? We will need to know the left and right boundaries of that rectangle, use those 
boundaries to calculate the width, and multiply the width with the height at that index to get the rectangle area. So
the next thing to ask is, what is the left and right boundaries' relationship with the height at the index of interest.
The left boundary is the previous smaller height, the right boundary is the next smaller height. This means, centered at 
height at any index, we expand leftward until we hit a height that is less, and we expand rightward until we hit a height
that is less or until we are out of bounds. Now suppose we have the same height [2,2], for i=0, expanding leftwards and
rightwards will yield the same area for both heights ie [4,4], but since we are tracking the maximum area calculating the 
same area twice will still result in the correct max area in this brute force solution. If we wanted to ensure that we 
dont double count areas, we can restrict how we deal with equal heights and boundaries. We can say that we can only go left 
if the previous height is strictly greater but we can go right if the next height is greater than or equal to. This means 
for [2,2] , we get [4,2] as the areas. This brute force solution is O(n^2) time and O(1) space.

So how do we use a stack to get a linear time, linear space solution. First we know that the left boundary is the previous
smaller, the right boundary is the next smaller. So the stack type we need is either strictly increasing or ascending order.
Before deciding on the stack type we need, lets first talk initial conditions since it turns out that one of the keys to 
solving this problem is in the initial conditions. We initialize previousSmaller array with -1 everywhere and the nextSmaller 
with n=len(heights) everywhere and then width = nextSmaller[i] - previousSmaller[i] -1. Say we only have a single bar of height 
4. With previousSmaller = -1, nextSmaller = n = 1, width = 1 --1 - 1 = 2-1 = 1. This is essential to get the correct width for 
any height whose rectangle extends the entire base of the histogram.

Other than that, in order to avoid double-counting rectangles, we need to choose the correct stack type. The choice of the 
correct stack type has to do with how we deal with equal heights. Say we have a heights array [2,2,1], do we want the width to 
be [1,2,3] or [2,1,3]? In otherwords, do we want to include equal heights in the previous smaller or in the next smaller? Since 
we are iterating from left to right, we want the correct width to extend from left to right. In otherwords, the rectangle with 
height 2 and index 0 should extend from left to right until it encounters height 1 at index 2; and we want the rectangle with 
height 2 at index 1 to extend from left to right until it encounters height 1 at index 2. In otherwords, we want nextSmaller
to continue through equal heights and stop at strictly smaller heights, but we want the previousSmaller to stop at both equal
and strictly smaller heights. In otherwords, nextSmaller is strictly smaller and previousSmaller is smaller or equal and this
denotes ascending order stack type.  This means when we have [2] on our stack, when we get to the second 2, we know that the 
rectangle for the stack peek 2 hasnt come to an end on the right, but the rectangle for the second 2 has come to an end on the 
left, so we set the previousSmaller[1] = 0. In otherwords, if the incoming height has the same height as current stack peek, 
we can append after updatig the previousSmaller to the index of the equal height on the stack. This means the stack type is 
ascending order. Finally a cleaner way of coding this solution is in largestRectangleSkyline.py. 

The last solutions are my preferred stack solutions where, we use a stack to get the previous/next smaller but we store the
left/right boundary for the current height. That is leftBoundary = previousSmaller + 1 and rightBoundary = nextSmaller - 1.
This way, to calculate the width, we use the same formula as for the left/right boundary exponential solution. This better
demonstrates the links betweent the solutions. We also initialize the left boundary (from prevSmaller) at 0 and right boundary
(from nextSmaller) at len(heights) - 1 ie the first and last indices. We can also use the next and previous smaller indices
directly and that changes the width calculation and the initial conditions.
"""
#O(n^2) time | O(n) space  - storing all left/right boundary values
def largestRectangleArea(heights):
    n = len(heights)

    leftBoundary = [0]*n
    for i in range(n):
        currentHeight = heights[i]
        
        leftIdx = i
        while leftIdx - 1 >= 0 and heights[leftIdx - 1] >= currentHeight:
            leftIdx -= 1
        
        leftBoundary[i] = leftIdx
    
    rightBoundary = [n-1]*n
    for i in range(n):
        currentHeight = heights[i]

        rightIdx = i
        while rightIdx + 1 < n and heights[rightIdx + 1] >= currentHeight:
            rightIdx += 1
        
        rightBoundary[i] = rightIdx
    
    maxArea = 0
    for i in range(n):
        currentHeight = heights[i]
        width = rightBoundary[i] - leftBoundary[i] + 1
        area = width * currentHeight
        maxArea = max(maxArea, area)
    return maxArea


#O(n^2) time | O(1) space
def largestRectangleArea(heights):
    maxArea = 0
    for i in range(len(heights)):
        currentHeight = heights[i]
        leftIdx = i 
        while leftIdx - 1 >= 0 and heights[leftIdx - 1] >= currentHeight: 
            leftIdx -= 1
            
        rightIdx = i
        while rightIdx + 1 < len(heights) and heights[rightIdx + 1] >= currentHeight:
            rightIdx += 1

        width = rightIdx - leftIdx + 1
        area = currentHeight * width
        maxArea = max(maxArea, area) 
    
    return maxArea

#O(n) time | O(n) space
def largestRectangleArea(heights):
    n = len(heights)

    leftBoundary = [0]* n            #note initial values
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()

        if stack:
            leftBoundary[i] = stack[-1] + 1

        stack.append(i)

    rightBoundary = [n-1]*n           #note initial values
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            stackTop = stack.pop()
            rightBoundary[stackTop] = i - 1
        stack.append(i)

    maxArea = 0
    for i in range(len(heights)):
        currentHeight = heights[i]
        width = rightBoundary[i] - leftBoundary[i] + 1   #note width calculation
        area = currentHeight * width
        maxArea = max(area, maxArea)
    return maxArea


#O(n) time | O(n) space 
def largestRectangleArea(heights):
    n = len(heights)

    prevSmaller = [-1]* n
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

        if stack:
            prevSmaller[i] = stack[-1]

        stack.append(i)
    
    nextSmaller = [n]*n
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            stackTop = stack.pop()
            nextSmaller[stackTop] = i
        stack.append(i)
    
    maxArea = 0
    for i in range(len(heights)):
        currentHeight = heights[i]
        width = nextSmaller[i] - prevSmaller[i] - 1
        area = currentHeight * width
        maxArea = max(area, maxArea)
    return maxArea




heights = [2,2,5,6,1,3]
print(largestRectangleArea(heights))