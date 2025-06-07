"""There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left 
and top edges, and the Atlantic Ocean touches the island's right and bottom edges. The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c). 
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring 
cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean. Return a 
2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and 
Atlantic oceans.

Input:                                 Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
heights = [                            Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
            [1,2,2,3,5],               [0,4]: [0,4] -> Pacific Ocean                        [1,3]: [1,3] -> [0,3] -> Pacific Ocean
            [3,2,3,4,4],                      [0,4] -> Atlantic Ocean                              [1,3] -> [1,4] -> Atlantic Ocean
            [2,4,5,3,1],               [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean      [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean      
            [6,7,1,4,5],                      [1,4] -> Atlantic Ocean                              [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
            [5,1,1,2,4]                [3,0]: [3,0] -> Pacific Ocean                        [3,1]: [3,1] -> [3,0] -> Pacific Ocean
            ]                                 [3,0] -> [4,0] -> Atlantic Ocean                     [3,1] -> [4,1] -> Atlantic Ocean
Note that there are other paths                                                             [4,0]: [4,0] -> Pacific Ocean 
from these cells to the Pacific and Atlantic oceans.                                               [4,0] -> Atlantic Ocean

The solution to this question is similar to the removeIslands.py where we start from our positions of interest and work our way backwards.
The question says that water can flow from a cell to its neighbor if the neighbor height is less than or equal to the current cell's height.
This means that for water to flow into a border cell from any current cell, the current cell height has to be greater than or equal to the 
border cell height, where the border cell is the neighboring cell. Another way of saying this is that, if a current cell height is less than
the bordering cell, then water cannot flow from it to the border cells. Now at this point this applies to the cells that are adjacent to the
border cells. If a cell's water cant flow into a particular border cell then there is no point in continuing to search if its own adjacent
cells can flow through it to the particular border cell in question. If however its own water can flow into a particular border cell, then
its own neighbors' water can flow through it to the border if its neighbor's height is not less ie, the adjacent cell becomes the new border
against which we compare its neighbors. So instead of starting a depth first search from every position in the graph and figure out if water 
can flow from it to both the pacific and atlantic ocean , we actually start from the borders and start a dfs and in this depth first search, 
we keep going as long as the neighboring cell's water can floow into the border cells. So for the top row, which borders the pacific ocean, 
we go through its columns and for each column get its neighbors and to determine if the neighbor's water can flow into the top row column, 
we say that if the neighbor cell height is less than the top row column, then it cant flow into the top border column, since the question 
states that the top row border has to be equal or less. We keep separate visited data strucutures for the pacific and atlantic, meaning 
when we start a dfs for the leftmost column and the top row we use the pacific visited data structure. And when we start a dfs from the
bottom or rightmost column, we use the atlantic visited data structure. At the end we loop through the entire matrix, and if the position
is in both data strucutures, we add it to the output array. Also because we update the comparison height to an adjacent cell if it can
flow into a border cell, we pass in a previous height, which starts out as the border cell height and keeps getting updated. The solution
as presented below is extremely verbose and redundant but its so written to amplify the nuances of the question. For example, we can use
the same for loop for the top row pacific dfs and the bottom row atlantic dfs, and then another for loop for left pacific dfs and right
atlantic dfs. Also we can clean up the dfs really well, combine the return situations and even incorporate the base cases inside the 
base cases, by passing in numRows and numCols into the dfs calls and from each point, making all four neighbor calls and returning from
invalid calls. In that case its important to write the case for invalid calls first before checking if visited or
"""
#O(w*h) time | O(w*h) space
def pacificAtlantic(heights):
    numRows, numCols = len(heights) , len(heights[0])
    pacific = [[False for i in range(numCols)] for j in range(numRows)]
    atlantic = [[False for i in range(numCols)] for j in range(numRows)]
        
    for col in range(numCols): #dfs from top row for pacific
        explore(0, col, pacific, heights[0][col], heights)
        
    for row in range(numRows):
        explore(row, 0, pacific, heights[row][0], heights)
        
    for col in range(numCols):
        explore(numRows - 1, col, atlantic, heights[numRows - 1][col], heights)
        
    for row in range(numRows):
        explore(row, numCols - 1, atlantic, heights[row][numCols - 1], heights)
        
    output = []
    for i in range(numRows):
        for j in range(numCols):
            if pacific[i][j] and atlantic[i][j]:
                output.append([i,j])
    return output

def explore(row, col, visited, prevHeight, heights):
    if visited[row][col]:
        return
    if heights[row][col] < prevHeight:
        return
    visited[row][col] = True
    neighbors = getNeighbors(row, col, heights)
    for neighbor in neighbors:
        nrow, ncol = neighbor
        if visited[nrow][ncol]:
            continue
        if heights[nrow][ncol] < heights[row][col]:
            continue
        explore(nrow, ncol, visited, heights[row][col], heights)

def getNeighbors(row, col, heights):
    neighbors = []
    if row > 0:
        neighbors.append([row - 1, col])
    if row < len(heights) - 1:
        neighbors.append([row+1, col])
    if col > 0:
        neighbors.append([row, col - 1])
    if col < len(heights[0]) - 1:
        neighbors.append([row, col + 1])
    return neighbors
        

"""Cleaner simpler re-writting, where we include getNeighbors function in base cases, to avoid invalid nodes, then check for
visited status before checking if water can flow into prevHeight cell. """
#O(w*h) time | O(w*h) space
def pacificAtlantic(heights):
    numRows, numCols = len(heights) , len(heights[0])
    pacific = [[False for i in range(numCols)] for j in range(numRows)]
    atlantic = [[False for i in range(numCols)] for j in range(numRows)]
        
    for col in range(numCols): #dfs from top row for pacific
        explore(0, col, pacific, heights[0][col], heights, numRows, numCols)
        explore(numRows - 1, col, atlantic, heights[numRows - 1][col], heights, numRows, numCols)
        
    for row in range(numRows):
        explore(row, 0, pacific, heights[row][0], heights, numRows, numCols)
        explore(row, numCols - 1, atlantic, heights[row][numCols - 1], heights, numRows, numCols)
        
    #loop to go through both visited sets for pacific and atlantic and choosing those that can reach both pacific and atlantic    
    output = []
    for i in range(numRows):
        for j in range(numCols):
            if pacific[i][j] and atlantic[i][j]:
                output.append([i,j])
    return output

def explore(row, col, visited, prevHeight, heights, numRows, numCols):
    if row < 0 or col < 0 or row == numRows or col == numCols or visited[row][col] or heights[row][col] < prevHeight :
        return
    
    visited[row][col] = True #if valid, unvisited and can flow into prevHeight, mark as visited

    #then call on all neighbors, the base case will handle the invalid calls, then the visited calls, then the water cant flow calls
    explore(row-1, col, visited, heights[row][col], heights, numRows, numCols)  #call on up neighbor, with current height as prevHeight
    explore(row+1, col, visited, heights[row][col], heights, numRows, numCols)  #call on down neighbor, with current height as prevHeight
    explore(row, col - 1, visited, heights[row][col], heights, numRows, numCols) #call on left neighbor, with current height as prevHeight
    explore(row, col + 1, visited, heights[row][col], heights, numRows, numCols) #call on right neighbor, with current height as prevHeight


