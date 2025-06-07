"""Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands. An island is 
surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water.

Example 1:                                          Example 2:
Input: grid = [                                     Input: grid = [
  ["1","1","1","1","0"],                                ["1","1","0","0","0"],
  ["1","1","0","1","0"],                                ["1","1","0","0","0"],
  ["1","1","0","0","0"],                                ["0","0","1","0","0"],
  ["0","0","0","0","0"]                                 ["0","0","0","1","1"]
]                                                       ]
Output: 1                                           Output: 3

This question is basically the 2-d version of numberOfConnectedComponents.py, because an island, as defined here is any group of connected 1's. 
We need to note that the definition of an island used here is slightly different from removeIslands.py question, but both are generalizations 
of the numberOfConnectedComponents.py pattern.
So we use a visited matrix to match the 2-d input and we initialize this visited matrix with False eveywhere. Then we have an outer loop that 
goes through each row and for each row goes through each column and before this outer loop we initialize the numberOfIslands variable. Inside 
the outer loop, We first check if the current position has been visited, so that we dont double count 1's that are part of previously discovered
islands. If True, we continue to the top of the outer loop. Next we check if the value at the current position is a 0, in which case we again 
continue to the top of the outer loop again, because a 0 cant be part of an island so why bother. Otherwise the current positon is an unvisited 
1 so we have found the start of a new island, so we increment the number of islands variable by 1 and then start a dfs from the current position 
to mark all the connected 1s in this island as True in the visited matrix, so that we skip all of those whenever we reach them in the outer loop, 
to avoid counting the same island multiple times. 
So in the dfs the first thing we check is that if the current position is visited, we return. This happens because each position has four 
neighbors and each of those neighbors will have the current position as a neighbor, so if we go down the dfs tree and mark a position as True 
and we recurse back to the top of the tree and call dfs again on this node we visited while going down the tree we just want to return. 
Otherwise, we mark the current position as True, then get its neighbors using a getNeighbors function. This pattern of marking a node as visited
before going through its edges is the crux of the numberOfConnectedComponents pattern. It helps as avoid interminable loops arising from doing
repeated work or getting stuck in cyles. With the neighbors in hand, we unpack each neighbor and again we check if the neighbor is visited or 
not and whether its a 1 or not; in either case we go back to the top of the neighbor loop. It is important to note that in this question, the 
1's and 0's are strings so we have to stringify 1 or 0 to check for equality ( ie value == str(1) or alternatively value != str(0), since value 
is either 0 or 1). If we dont continue to the top of the neighbors for loop, then we have found an unvisited 1 neighbor, we call a dfs from it 
to find all of its neighboring 1s and mark them as True in the visited  map, thus going down the dfs tree. We visit each node at most once so 
this is O(n) where n = mxn, the number of nodes in the 2-d input matrix. 

This question, in addition to numberOfConnectedComponents.py, graphValidTree.py can also be solved with Unio Find algorithm. Check out the
Union Find tag on leetcode.
"""

"""Solution one uses depth-first search for graph traversal function markIslands"""

def numIslands(grid):
    numCols = len(grid[0])
    numRows = len(grid)
    visited = [[False for i in range(numCols)] for j in range(numRows)]
        
    numberOfIslands = 0
    for row in range(numRows):
        for col in range(numCols):
            if visited[row][col]:
                continue
            if grid[row][col] != str(1):
                continue
            numberOfIslands += 1
            markIslands(grid, row, col, visited, numRows, numCols)
    return numberOfIslands

    
def markIslands(grid, row, col, visited, numRows, numCols):
    if visited[row][col]:
        return
    visited[row][col] = True
    neighbors = getNeighbors(grid, row, col, numRows, numCols)
    for neighbor in neighbors:
        nrow, ncol = neighbor
        if visited[nrow][ncol]:
            continue
        if grid[nrow][ncol] != str(1):
            continue
        markIslands(grid, nrow, ncol, visited, numRows, numCols)

    
def getNeighbors(grid, row, col, numRows, numCols):
    neighbors = []
    if row > 0:
        neighbors.append([row-1, col])
    if row < numRows - 1:
        neighbors.append([row+1, col])
    if col > 0:
        neighbors.append([row, col - 1])
    if col < numCols - 1:
        neighbors.append([row, col + 1])
    return neighbors

"""In this solution, I incorporate the getNeighbors function into the depth-first search"""
def numIslandsII(grid):
    numCols = len(grid[0])
    numRows = len(grid)
    visited = [[False for i in range(numCols)] for j in range(numRows)]
        
    numberOfIslands = 0
    for row in range(numRows):
        for col in range(numCols):
            if visited[row][col]:
                continue
            if grid[row][col] != str(1):
                continue
            numberOfIslands += 1
            markIslandsII(grid, row, col, visited, numRows, numCols)
    return numberOfIslands

    
def markIslandsII(grid, row, col, visited, numRows, numCols):
    if row < 0 or col < 0 or row >= numRows or col >= numCols:
        return
    if visited[row][col] or grid[row][col] != str(1):
        return
    visited[row][col] = True
    
    markIslandsII(grid, row - 1, col, visited, numRows, numCols)
    markIslandsII(grid, row + 1, col, visited, numRows, numCols)
    markIslandsII(grid, row , col - 1, visited, numRows, numCols)
    markIslandsII(grid, row , col + 1, visited, numRows, numCols)


from collections import deque
def numIslandsIII(grid):
    numCols = len(grid[0])
    numRows = len(grid)
    visited = [[False for i in range(numCols)] for j in range(numRows)]
        
    numberOfIslands = 0
    for row in range(numRows):
        for col in range(numCols):
            if visited[row][col]:
                continue
            if grid[row][col] != str(1):
                continue
            numberOfIslands += 1
            markIslandsIII(grid, row, col, visited, numRows, numCols)
    return numberOfIslands

    
def markIslandsIII(grid, row, col, visited, numRows, numCols):
    queue = deque()
    queue.append((row,col))
    while queue:
        row, col = queue.popleft()
        if visited[row][col]:
            continue
        visited[row][col] = True
        directions = [[1,0], [-1,0], [0, 1], [0,-1]]
        for direction in directions:
            nrow, ncol = row + direction[0] , col + direction[1]
            if nrow < 0 or ncol< 0 or nrow >= numRows or ncol >= numCols:
                continue
            if visited[nrow][ncol] or grid[nrow][ncol] != str(1):
                continue
            queue.append([nrow, ncol])


# grid = [                                     
#   ["1","1","1","1","0"],                                
#   ["1","1","0","1","0"],                                
#   ["1","1","0","0","0"],                                
#   ["0","0","0","0","0"]                                 
# ]                                                       
# Output: 1                                           



grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]

print(numIslandsIII(grid))