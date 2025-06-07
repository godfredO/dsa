"""You are given an m x n grid where each cell can have one of three values: 0 representing an empty cell, 1 representing a fresh orange, 
or 2 representing a rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

This is giving me simultaneous bfs like minimumpasses.py. So we initialize our queue with all the positions that have rotten oranges, ie
value 2. Then we do a bfs with time initialized to 0. And inside the bfs, we process each rotten orange's valid and unvisited neighbors
that are fresh oranges by changing the value a the neighbor to 2 and adding the newly rotten orange to the queue. We take the size of the
queue, decrement this variable whenever we process a rotten oranges neighbors. When this size variable reaches 0, we increment the time
variable by 1. Now if we ever get to a point where no rotten orange has a fresh orange neighbor, we will do one pass through the matrix
without adding a newly rotten orange position to the queue. As such, there will be one additional pass and time increment than is needed.
So we return time - 1 but only after we check that there are no remaining fresh oranges in which case we return -1, because we couldnt 
flip all fresh oranges. Before we even initialize our queue however, we need to handle the case where the entire matrix is full of empty
space. In this case we return time = 0 otherwise our algorithm would return time 0 - 1 = -1 which would be wrong. The time and space 
complexity is O(n*m) due to the bfs step and visited matrix. Now we can make an optimization, by first keeping track of all the fresh
oranges in the matrix, and whenever we flip a fresh orange to a rotten orange, we decrement this value. This will save us the trouble of
having to go through our matrix a second time because if this fresh orange count is greater than 0, we know to return -1. We can 
incorporate this in addition to checking the edge case of only empty space to the initial queue. Now another optimization that simplifies
our solution further. We can simply tweak the while loop to run when as long as the queue is non-empty and the freshCount > 0. This ensures
that we dont need to return time - 1 because we will remove that additional pass when there are no fresh oranges but there are coordinates
on the stack, and as such we dont need to keep track of the allEmpty boolean. This is because if the matrix only has empty space, the queue
will be empty and freshCount will also be empty and in this fully optimized version, we just return time instead of time - 1 since we avoid
the last unnecessary pass. 

So we started by adapting the solution from minimumPasses.py, found where that solution failed and then improved it further. In fact the 
solution here can also be used to improve minimumPassesOfMatrix.py.

# Simultaneous BFS
"""
from collections import deque
# O(n*m) time | O(n*m) space
def orangesRotting(grid):
    rows , cols = len(grid), len(grid[0])

    allEmpty = True
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != 0:
                allEmpty = False
    
    if allEmpty:
        return 0

    #initialize queue with positions of the intially rotten oranges
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append([row,col])
    
    #bfs step, initialize time, and visited matrix
    time = 0
    visited = [[False for i in range(cols)] for j in range(rows)]
    while queue:
        size = len(queue)
        while size > 0:
            row, col = queue.popleft()
            if visited[row][col]:
                continue
            visited[row][col] = True
            directions = [[1,0], [-1, 0], [0,1], [0,-1]]
            for direction in directions:
                deltaX, deltaY = direction
                nrow, ncol = row + deltaX, col + deltaY
                if nrow < 0 or ncol < 0 or nrow >= rows  or ncol >= cols : #if invalid or visited
                    continue
                if visited[nrow][ncol]: #if not a fresh orange
                    continue
                if grid[nrow][ncol] != 1:
                    continue
                grid[nrow][ncol] = 2  #turn fresh orange into rotten orange
                queue.append([nrow,ncol]) #add newly rotten orange to queue
            size -= 1 #decrease size by 1, since we finished processing one rotten orange's neighbors
        time += 1

    #second iteration through the matrix, to find any remaining 1's.
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                return -1
    return time - 1
    
"""Solution II- mid-optimized coding solution """
def orangesRotting(grid):
    rows , cols = len(grid), len(grid[0])

    freshCount = 0
    allEmpty = True
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append([row,col])
                allEmpty = False
            elif grid[row][col] == 1:
                freshCount += 1
                allEmpty = False
    
    if allEmpty:
        return 0
            
    #bfs step, initialize time, and visited matrix
    time = 0
    visited = [[False for i in range(cols)] for j in range(rows)]
    while queue:
        size = len(queue)
        while size > 0:
            row, col = queue.popleft()
            if visited[row][col]:
                continue
            visited[row][col] = True
            directions = [[1,0], [-1, 0], [0,1], [0,-1]]
            for direction in directions:
                deltaX, deltaY = direction
                nrow, ncol = row + deltaX, col + deltaY
                if nrow < 0 or ncol < 0 or nrow >= rows  or ncol >= cols : #if invalid or visited
                    continue
                if visited[nrow][ncol]: #if not a fresh orange
                    continue
                if grid[nrow][ncol] != 1:
                    continue
                grid[nrow][ncol] = 2  #turn fresh orange into rotten orange
                freshCount -= 1 #decrement count to avoid second iteration through matrix
                queue.append([nrow,ncol]) #add newly rotten orange to queue
            size -= 1 #decrease size by 1, since we finished processing one rotten orange's neighbors
        time += 1

    return -1  if freshCount > 0 else time - 1
    

"""Solution III - fully-optimized solution"""
def orangesRotting(grid):
    rows , cols = len(grid), len(grid[0])

    freshCount = 0
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 2:
                queue.append([row,col])
                
            elif grid[row][col] == 1:
                freshCount += 1
                         
    #bfs step, initialize time, and visited matrix
    time = 0
    visited = [[False for i in range(cols)] for j in range(rows)]
    while queue and freshCount > 0:
        size = len(queue)
        while size > 0:
            row, col = queue.popleft()
            if visited[row][col]:
                continue
            visited[row][col] = True
            directions = [[1,0], [-1, 0], [0,1], [0,-1]]
            for direction in directions:
                deltaX, deltaY = direction
                nrow, ncol = row + deltaX, col + deltaY
                if nrow < 0 or ncol < 0 or nrow >= rows  or ncol >= cols : #if invalid or visited
                    continue
                if visited[nrow][ncol]: #if not a fresh orange
                    continue
                if grid[nrow][ncol] != 1:
                    continue
                grid[nrow][ncol] = 2  #turn fresh orange into rotten orange
                freshCount -= 1 #decrement count to avoid second iteration through matrix
                queue.append([nrow,ncol]) #add newly rotten orange to queue
            size -= 1 #decrease size by 1, since we finished processing one rotten orange's neighbors
        time += 1

    return -1  if freshCount > 0 else time 



# grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output = 4

# grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1

grid = [[0,2]]
# Output: 0
print(orangesRotting(grid))