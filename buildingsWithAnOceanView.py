"""
Tags: Stack; Monotonic Stack; Previous Greater; Medium

There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the
buildings in the line. The ocean is to the right of the buildings. A building has an ocean view if the building can see
the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller
height. Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

Example 1:
Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.

Example 2:
Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.

Example 3:
Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.

Example 4:
Input: heights = [2,2,2,2]
Output: [3]
Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.

Constraints:
1 <= heights.length <= 10^5  ; 1 <= heights[i] <= 10^9 ;

Okay, this is an application of the next greater element algorithm in monotonicStacks.py. So here our input array contains
the heights of buildings. We iterate through the array before we append the current index to the stack, we check if the
height at the index on top of the stack is less than or equal than the current loop element (and the stack is non-empty).
If yes, we have found a building that blocks the view of the building at the peek index so we pop from the top of the stack.
We keep doing this as long as the stack is non-empty and the peek index's height is less than or equal to the current loop
index height. At the end of this operation we append the current loop index to the stack. This means that after we loop
through the building heights, the stack will contain the indices of the buildings that whose ocean view are not blocked in
sorted ascending order since we loop from left to right, so the stack is our output array. Note that the stack maintains
a strictly descending property (due to <= instead of <)to ensure that all buildings on the stack can see the ocean view.
In otherwords, at the end, the indices left on the stack represent those building heights that dont have any next greater
or equal element after them.
A similar question to this is the algoexpert.io sunset_views.py.

"""


def findBuildings(heights):
    stack = []

    for i in range(len(heights)):   # iterate left to right
        while stack and heights[stack[-1]] <= heights[i]:  # if previous will be blocked by current
            stack.pop()  # remove blocked building
        stack.append(i)  # append current building
    return stack


heights = [1, 3, 2, 4]
print(findBuildings(heights))
