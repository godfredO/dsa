"""You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).  The rain starts 
to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and 
only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay 
within the boundaries of the grid during your swim. Return the least time until you can reach the bottom right square (n - 1, n - 1) if 
you start at the top left square (0, 0). Each value grid[i][j] is unique.

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation: 
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

The main thing to realize about this problemis that in order for one to swim a position of height of say 4, one would have to wait at least
for at least time t = 4 in order for the water to be high enough to swim from the height of 4. Now lets say you waited for time t = 4 then 
now you can swim to one of the neighboring cells. Lets say the neighboring cells are 5, 2, 6, then at at time t=4, you can go to the cell
with height = 2. But imagine instead the neighboring cells had heights of 14,21,10 then at time t=4 even though you can swim from the start
of height = 4, you cant go anywhere since all the neighboring cells heights are higher than 4. In fact you would have to weight to at least
time t=10 in order for be able to swim to the neighboring cell with height = 10. So the main bottle neck is the heights and not really the 
time, but the heights of the cells. As such the question is about finding a path that minimizes the highest height encountered from the top 
left corner to the bottom right corner, as this path will require the least time.

The solution is a breadth-first search approach that uses a modified version of Djikstra's algorithm.  So we start from the topleft node,
add the minHeap is going to contain the frontier of where we're at. And at each node we choose the neighbor that minimizes the height 
encountered as this will take the least amount of time to swim to and the actual time needed will be the maximum of start height and the
chosen height. Of course we will need to do this maximum comparison too with the stored variable. So lets say the startNode, position (0,0)
has a height of 0, and its neighbors have heights of 1 and 2, we choose the node with height 1 as our new currentNode. The reason is that
to minimize the maximum height along a path, if we choose 1 we know that the maximum height is at least 1 whilst if we choose 2, the max
height is at least 2 and we are interested in minimizing the max height encountered on the path. So we choose the node with height 1 and 
add it to our minHeap, and the modification is that we have to add the height since the minHep is using this to siftUp/siftDown and then
we are also going to add its coordinates ie heapq.heappush(minHeap, (1, 0,1)) where height 1 is in row 0, column 1 (height, row, column).
So we add our startNode to the heap, and inside the while loop, we pop it, add it to the visited set and add its unvisited neighbors to 
the minHeap, which will give us log time access to the neighbor with the minimum height. Then we pop, add to visited, and then unvisited
neighbors to the minHeap. And of course, we need to keep track of the heighest height encountered on any path by doing a max comparison
of the popped height with the time variable which can be initialized as the height of the topLeft node (startNode). At the end, the 
"""
import heapq
def swimInWater(grid):
    rows, cols = len(grid), len(grid[0])
    visited  = [[False for i in range(cols)]for j in range(rows)]
    
    startNode = (grid[0][0], 0, 0)
    minHeap = [startNode]
    heapq.heapify(minHeap)

    time = grid[0][0]
    while minHeap:
        height, row, col = heapq.heappop(minHeap)
        if visited[row][col]:
            continue
        visited[row][col] = True

        time = max(time, height)  #update time, or maximum height encountered in path
        if row == rows - 1 and col == cols - 1: #check if endNode reached
            break

        directions = [[1,0], [-1,0], [0,1], [0,-1]] #directions for finding neighbor nodes
        for direction in directions: 
            deltaX, deltaY = direction #unpack
            nrow, ncol = row + deltaX, col + deltaY #calculate neighbor row, col

            if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols: #invalid neighbors
                continue

            if visited[nrow][ncol]: #skip visited neighbors
                continue
            
            #add valid , unvisited
            heapq.heappush(minHeap, (grid[nrow][ncol], nrow, ncol))
    return time



grid = [[0,1,3], [2,4,1],[1,2,1]]
print(swimInWater(grid))