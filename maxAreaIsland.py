""" You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or 
vertical.) You may assume all four edges of the grid are surrounded by water. The area of an island is the number of cells with a value 1 
in the island. Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

This question is a continuation of numberOfIslands.py. Basically from that question we know that whenever we start a dfs from an unvisited 1, 
we have found the start of a new island and in the dfs, we mark as visited, all the 1's that are connected to the same island horizontally or
vertically (but not diagonally). So this question is asking if we can calculate the area of each island, and return the max island area. The
first thing to realize is that because each square is of 1 unit^2 area, the area of an island is basically the number of 1's * 1 unit sq which
is the number of 1's in an island. So the question is reduced to counting the number of 1's in any island. So to do this I have created an
AreaValue object, which just takes a value, this is so that we can have a mutable object that we can incrment and pass around the recursive 
tree at the same time. So the idea is that before we tart a dfs from unvisited 1's, we initialize an AreaValue object with value 0, and in the
dfs, whenever we are at an invalid neighbor, visited node or a 0 we return. Otherwise, we mark the node as visited in the visited matrix, and
then we increment the count of the number of connected 1's by incrementing value stored in the AreaValue object. At the end of a particular 
dfs, we do a max comparison with the stored maxArea value and the value stored in the updated AreaValue object. At the end of the outer loop,
we return the maxArea variable. Thus this solution as written is a modification of the numberOfIslands.py solution. This is solution I. Also,
another question that is essentially the same question as this , is riverSizes.py where islands become rivers and we are asked to return an
array of riverSizes.

If you compare this solution here to the islandPerimeter.py solution, the main difference is that the base case of a visited neighboring node 
differs in its perimeter contribution to the base case of invalid (border) or water neighboring node since perimeter is determined by the 
number of sides of an island that border water. With that said, we can re-write solution I in a way that resembles the islandPerimeter.py 
solution, with or without the use of a custom object to store the count of connected 1's. Solutions II, III do this but essentially they are 
the exact same solution as Solution I, just different way of coding it out. It must however be said that sometimes its more than convenient 
or clean to use a custom object, especially in tree problems where we need to check and use values returned by a recursive call on a subtree.



"""

class AreaValue:
    def __init__(self,value):
        self.value = value

#O(w*h) time | O(w*h) space - solution I
def  maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    maxArea = 0
    for row in range(rows):
        for col in range(cols):
            if visited[row][col] or grid[row][col] != 1: #only start dfs from unvisited 1's
                continue
            area = AreaValue(0)
            explore(row, col, grid, visited, rows, cols, area)
            maxArea  = max(maxArea, area.value)
    return maxArea



def explore(row, col, grid, visited, rows, cols, area):
    if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] != 1:
        return
    
    visited[row][col] = True
    area.value += 1
    explore(row - 1, col, grid, visited, rows, cols, area)
    explore(row + 1, col, grid, visited, rows, cols, area)
    explore(row, col - 1, grid, visited, rows, cols, area)
    explore(row, col + 1, grid, visited, rows, cols, area)




"""Solution II and III are written to resemble islandPerimeter.py instead of numberOfIslands.py """

class AreaValue:
    def __init__(self,value):
        self.value = value

#O(w*h) time | O(w*h) space - solution I
def  maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    maxArea = 0
    for row in range(rows):
        for col in range(cols):
            if visited[row][col] or grid[row][col] != 1: #only start dfs from unvisited 1's
                continue
            area = explore(row, col, grid, visited, rows, cols, area)
            maxArea  = max(maxArea, area.value)
    return maxArea



def explore(row, col, grid, visited, rows, cols, area):
    if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] != 1:
        return AreaValue(0)
    
    visited[row][col] = True
    area  = AreaValue(1)
    area.value += explore(row - 1, col, grid, visited, rows, cols, area).value
    area.value += explore(row + 1, col, grid, visited, rows, cols, area).value
    area.value += explore(row, col - 1, grid, visited, rows, cols, area).value
    area.value += explore(row, col + 1, grid, visited, rows, cols, area).value
    return area



"""Solution III doesnt use a custom object"""
#O(w*h) time | O(w*h) space - solution III
def  maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    maxArea = 0
    for row in range(rows):
        for col in range(cols):
            if visited[row][col] or grid[row][col] != 1: #only start dfs from unvisited 1's
                continue
            area = explore(row, col, grid, visited, rows, cols)
            maxArea  = max(maxArea, area.value)
    return maxArea

def explore(row, col, grid, visited, rows, cols):
    if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] != 1:
        return 0
    
    visited[row][col] = True
    area = 1
    area += explore(row - 1, col, grid, visited, rows, cols)
    area += explore(row + 1, col, grid, visited, rows, cols)
    area += explore(row, col - 1, grid, visited, rows, cols)
    area += explore(row, col + 1, grid, visited, rows, cols)
    return area
