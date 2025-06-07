"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how 
much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this 
case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:
n == height.length ; 1 <= n <= 2 * 104  ; 0 <= height[i] <= 105

This question is the same as the algoexpert waterArea.py. This here is the name of the question on leetcode. So we
start by realizing that the total amount trapped in simply the sum of the amount trapped above each height. To find
this value, we treat the height at each index as the bottom of the trap and the top of the trap is the minimum of 
the maximum to the left and the maximum to the right of an index. Say we have [1,5,3,6,4], for index 2, the bottom 
of the trap has a height of 3, the top of the trap has a height min(5,6) ie 5, meaning the height of water trapped 
above index 2 is 5-3=2. If we had [7,5,3,6,4], the height of water trapped above index 2 is min(7,6) - 3 = 3. If we 
have [7,5,8,6,4], then the height of water trapped above index 2 is min(8,8) - 8 = 0. Yup, the height at index 2 is 
its own maximum height to the left and maximum height to the right. So in the first solution, we iterate from left 
to right for the current height, then expand leftward to find the greatest value to its left (including the current),
expand rightward to find the greatest value to its right (including the current), then determine the height of the
water trapped above the current height using min(leftMax, rightMax) - currentHeight, summing up all water heights.
This is an O(n^2) time, O(1) space complexity but since we are expanding leftward and rightward, we know that we can 
use dynamic programming to store the left max and right max for each index. Basically we are storing the maximum value 
for the left subarray and right subarray ending at each element ie [0,idx],[idx,len(heights)-1]. We realize then that 
for index 0, the only option for left max is height[0] , for index len(height) - 1, the only option for right max is 
height[len(height)-1]. Otherwise, for the left maxes we iterate from left to right starting from index 1 and we say 
that the maximum to the left of each index is the maximum of the previous left max and the current height. Similarly, 
for the right maxes we iterate from right to left, starting from the penultimate value and we say that the maximum to 
the right of each index is the maximum of the next right max and the current height. This solution is O(n) time and 
space. If the input is [7,5,3,6,4] leftMax = [7,7,7,7,7], rightMax = [7,6,6,6,4] and then the height of water above
each index ie water= min(leftMax,rightMax) - height[i], we would have [0,1,3,0,0] for a total trapped water of 4 and
the reason is because to convert from height to area, we multiply the water trapped above each index by a width of 1.

A cleaner approach is with the use of a stack. But instead of working with the leftMaxHeight and rightMaxHeight, we
can use the standard stack algorithms, next greater and previous greater, (read monotonicStacks.py). So we keep the
array in a strictly decreasing order. This means by the time we append the current index to the stack, if the stack
is non-empty, then the top of the stack will be occupied by a value that is greater than the current index. In 
othewords the stack type depends on the type of property we want maintained between the stack peek (if stack is non
empty) and the current index; stack type being described as strictly increasing, increasing with equals (ascending 
sorted order), strictly decreasing, decreasing with equals (descending sorted order). In otherwords, when we append
do we want the our value graph to slope down, ie decreasing? This would mean that the current index should be less
than the peek at appending said differently the peek should be greater than the current index at appending. To 
achieve this property, we pop of any peek value that is less than or equal the current index, and by so doing we
either leave the stack empty or by the time we append the current index, the peek value is greater than the current
index. Keeping a graph of ascending and descending slopes will make it easier to visualize this information , figure 
out the property to be maintained, and the popping actions needed to achieve said property. And how do we achieve 
this property? By popping the current top if its relationship with the current index dont fit the pattern. 
Greater indicates decreasing order, previous greater being strictly decreasing, next greater being decreasing with 
equals. Smaller indicates increasing order, previous smaller being strictly increasing, next smaller being increasing
with equals. 

So how does the stack help us solve this question. Instead of finding the leftMax and rightMax, we use width information
together with next greater and previous greater. Basically we keep a strictly decreasing stack type, meaning that we
append when the peek is greater than the current index; we pop when the peek is less than or equal to the current index.
So when we pop because the peek is less than or equal to the current index, the new peek is the previous greater of
the popped value, the current index being the next greater of the popped value. Using these we calculate the width of
water as i - stack[-1] - 1. Then the height is the min(height[stack[-1]], height[i]) - height[stackTop]) where stackTop
is stack.pop(). The area of water added is width*height. Now how does the inclusion of width bridge this solution with
the intuition of finding the left and right maxes. Take [7,5,3,6,4] leftMax = [7,7,7,7,7], rightMax = [7,6,6,6,4] and 
then the height of water above each index ie water= min(leftMax,rightMax) - height[i], we would have [0,1,3,0,0]. For
the same question, if we use nextGreater, prevGreater (inclduing the current index) and width information, we have 
prevGreater as [7,7,5,7,6] and nextGreater = [7,6,6,6,4], and height = [0, 1, 2, 0, 0 ], width = [0,2,1,2,3] (width
values are calculated using the indices of the values in prevGreater and nextGreater at each index. In the code
below, we store only indices and use them to access the height values for nextGreater and previousGreater). The area
array is [0,2,2,0,0] for a total of 4. So it seams like by using nextGreater and prevGreater instead of leftMax and
rightMax, our calculation shifts I unit of water from 3, to 5. Because in this case, we are effectively asking how
longer a particular water extends horizontally. Note that in order to reduce to 0, the positions that cant store
water, we say that if an index doesnt have a next greater or previous greater, we store the same value at that
index. In the code, we initialize a list of indices for nextGreater and prevGreater. This way if something doesnt
get update, we know it doesnt have a next or previous greater. Inside the while loop, when we update either of these
arrays, at any index, we store the index of its next greater and previous greater. This way we have access to the
information we need to determine width, use these indices to access. So that the horizontal column of water formula
min(height[stack[-1]], height[i]) - height[stackTop]), becomes min(height[prevGreater[i]], height[nextGreater[i]]) 
- height[i]. We determine width as width = prevGreater[i] - nextGreater[i] - 1.  

The last solution, a two pointer solution is a simplification of the dynamic programming solution. First we realize
that from the formula area += min(leftMax, rightMax) - currentHeight, we can say that water above each height will
depend on the lower of the leftMax, or rightMax. That if leftMax < rightMax, area += leftMax - currentHeight, else
area += rightMax - currentHeight. So we initialize two pointers from left, right pointers at index 0 and index 1 
and we advance them inward so as long as left < right . Anyway, as we move the pointers if the current left pointer's
height value is greater than the leftMax, it time to update the leftMax to the pointer value and if the current right 
pointer's height value is gteater than the rightMax it time to update the rightMax to the pointer value. This allows
us to both track the update of leftMax, rightMax as well as allow us to use the updated values in area of water above
a column calculation. Also, when calculating the water height above an index, current height will be the left pointer 
height or right pointer height depending (on which pointer value was found to be minimim). This crystallization of the
dynamic programming solution which was itself a simplification of the left, right boundary solution is so clean. It
also gives you linear time and space complexity.


"""
# #O(n^2) time | O(1) space
# def trap(height):
#     area = 0
#     for i in range(len(height)):
#         leftMax = 0
#         leftIdx  = i
#         while leftIdx >= 0:
#             leftMax = max(leftMax, height[leftIdx])
#             leftIdx -= 1
            
#         rightMax = 0
#         rightIdx  = i
#         while rightIdx < len(height):
#             rightMax = max(rightMax, height[rightIdx])
#             rightIdx += 1
                
#         area += min(rightMax, leftMax) - height[i]
#     return area
                
# def trap(height) :
        
#     leftMaxes = [0]*len(height)
#     leftMaxes[0] = height[0]
#     for i in range(1,len(height)):
#         leftMaxes[i] = max(leftMaxes[i-1], height[i])
            
#     rightMaxes = [0]*len(height)
#     rightMaxes[-1] = height[-1]
#     for i in reversed(range(len(height)-1)):
#         rightMaxes[i] = max(rightMaxes[i+1], height[i])
           
#     area = 0
#     for i in range(len(height)):
#         area += min(rightMaxes[i], leftMaxes[i]) - height[i]
        
#     return area


# def trap(height):
#     stack = []
#     nextG = list(range(len(height)))
#     prevG = list(range(len(height)))

#     for i in range(len(height)):
#         while stack and height[stack[-1]]  <= height[i]:
#             stackTop = stack.pop()   #next greater of invalid peek
#             nextG[stackTop] = i
#         if stack:
#             prevG[i] = stack[-1]  #prev greater of current is current peek
#         stack.append(i)

#     area = 0
#     for i in range(len(height)):
#         width = nextG[i] - prevG[i] - 1
#         curHeight = min(height[nextG[i]] , height[prevG[i]]) - height[i]
#         area += width * curHeight
#     return area
    
    

def trap(height):
    area = 0
    left, right = 0 , len(height) - 1
    leftMax, rightMax = 0 , 0
    while left < right:
        if height[left] < height[right]:         # if trap top is to the left
            if height[left] >= leftMax:          # first update leftMax
                leftMax = height[left]
            area += leftMax - height[left]      #  then calculate area for current left pointer
            left += 1                           #  advance left pointer
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            area += rightMax - height[right]
            right -= 1
    return area
        

        
            
height = [4,2,0,3,2,5]
print(trap(height))