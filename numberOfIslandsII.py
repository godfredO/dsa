"""Read numbeOfIslands.py for the description of the solution. Here, I will write the breadth-first search solution."""

def numIslands(grid):
    if not grid: #if the grid is empty
        return 0
    numRows, numCols = len(grid), len(grid[0])
    visit = [[False for i in numCols] for j in numRows]