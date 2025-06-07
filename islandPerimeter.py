""" You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water. Grid cells are 
connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or 
more connected land cells). The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell 
is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]         Output: 16    
Input: grid = [[1]]                                             Output: 4
Input: grid = [[1,0]]                                           Output: 4
Explanation: Draw it out to see the perimeter of the single island.

So this question builds on the numberOfIslands question which is itself a 2d version of the numberOfConnectedComponents.py question and an 
island is any group of connected 1's. We are assured that this question will have exactly one island. We can detect this island by starting
a dfs from an unvisited 1 in the outer loop and marking every connected 1 as visited. So the question here is to determine the perimeter of
an island once we discover it. The perimeter is the continuous line forming the boundary of the island. From the visited set we can know the
locations of all the grids that constitute this island, but how do we determine the perimeter? If you take an island consisting of 4 squares
2 on top and 2 below, making one perfect square, the perimeter will be the sum of the sides of all squares in this island that border water,
so in this case the perimeter is 8 because each square has two sides bordering water, and two sides bordering other island squares. If instead
the island was made up of four squares lined up horizontally, then the squares on the ends will have 3 sides bordering water and the two inner
squares will have 2 sides bordering water giving a perimeter of 10. So, the perimeter of an island depends on how the squares of the island
are connected which determines the number of sides that are exposed to water. So a square that is bordered on all sides by island squares and
no water will contribute nothing to the entire perimeter, imagine here the center square of an open cardboard box. We are also told that the
entire matrix is surrounded by water, so any border island squares is at least exposed to water too but again its total perimeter contribution
will depend on what borders the other non-border sides. 
Each square has four sides, the left side, the right side, the bottom side, and the right side. The contribution each side makes to a square's
total perimeter contribution depend on whether on not that side borders water on land.
- When does the top side border water ? When the row = 0 or [row - 1][col] == 0
- When does the bottom side border water ? When the row = lastRow or [row + 1][col] == 0
- When does the left side border water ? When the col = 0 or [row][col - 1] == 0
- When does the right side border water ? When the col = lastCol or [row][col + 1] == 0

So my approach is to first detect the connected ones that comprise this singular island and mark them as visited in the visited matrix. Then
initialize a perimeter variable and go through this visited matrix and for each position that is marked True ie island square, send its
coordinates to another helper function that will return the total perimeter contribution of the sides of this island square and this value
will range from 0, for completely landlocked square to 4 for a singular island. With the perimter contribution of each island square, we
increment the perimeter variable by this value and at the end we return the perimeter. In this implementation when doing the dfs, I take care
of the invalid cases first so as to incorporate getNeighbors function into the dfs. However the getPerimeterContribution function is an clever
modification of the getNeighbors function. Also if the questions asked for area instead, then would just count the number of visited island
squares and return that number, since each square is 1*1= 1 unit^2 area irrespective of what borders it, so area =  1 unit^2 * numIslandSquares
giving area = numIslandSquares unit^2.

So great we can simplify dfs because we are told that there is only one island. This means every 1 in this grid, has to be connected to all the
other 1's in order for all of the 1's to form a single island. So no need to even do a dfs search. We can just go through the grid and if the
position is 1, we mark it as visited. Solution two implements this solution which is the more optimal approach and non-naive. I imagine that 
instead of even implementing a getPerimeterContribution function using the grid values, we can use the visited matrix itself. If the row is 0 
or not visited[row - 1][col], then we know that the top border is bordering water. Hmm are there any optimizations we can do with 
getPerimeterContributions()?

Well we can go back to using dfs to calculate the perimeter directly, so in this sense we modify numberOfIslands.py to return the perimeter
directly. In the outer loop, we go through the grid, looking for unvisited 1's or really any 1 since we know that all 1's are connected. 
The we start our dfs from such a position. The idea is that we look at the neighbors and if the neighbor is land we call dfs on it and the aim
of this is to get perimeter contributions and add it all up for the perimeter count. If a neighbor is out of bounds or is water we add 1 to ur 
perimeter count. We need to keep track of the visited lands so that we dont double count. So to do this I implement a class PerimeterCount 
which takes in a value. Then we go through the outer loop, skipping all visited 1's and 0's and if we find an unvisted 1, we start a dfs. In
the dfs we check if the positon is out of bound or is 0 then we return a PerimeterCount object with a value of 1. Next if the positon is a
visited 1, we return a PerimeterCount object with a value of 0, this is to simply the recursive case below. So at this point in the recursive
case we have an unvisited 1 so we mark it as visited and get its perimeter contribution. In solution 4 below, we initialize this value at 0,
then increment it with all of the values stored in the PerimeterCount object returned by calling dfs on its neighbors, then with this updated
perimeter contribution tempValue, we return a Perimeter Count object with this value. In the outer loop, we just return the sum stored in the
value of the received object.

So we started with what we know, explored the problem, made observations, implemented naive solutions and then optimized this solution. I 
would say that solution 2/3 is the best solution, because it directly uses the single island observation and calculates the perimeter 
iteratively, and even though it has the same space complexity and technically the same time complexity as solution 4, it will have a better 
average complexity overall. Solution 4 is more impressive technically and for some questions that style will be the only approach available.
"""



"""Solution one, repurposes the numberOfIslands.py solution and is naive because it doesnt use the fact of a single island"""
# O(w*h) time | O(w*h) space
def islandPerimeter(grid):
    numRows , numCols = len(grid), len(grid[0])
    visited = [[False for i in range(numCols)] for j in range(numRows)]

    for row in range(numRows):
        for col in range(numCols):
            if visited[row][col]:
                continue
            if grid[row][col] != 1:
                continue
            explore(row, col, grid, visited, numRows, numCols)
    
    perimeter = 0
    for row in range(numRows):
        for col in range(numCols):
            if visited[row][col]:
                perimeter += getPerimeterContribution(row,col,grid, numRows, numCols)
    return perimeter

def explore(row, col, grid, visited, numRows, numCols):
    if row < 0 or col < 0 or row >= numRows or col >= numCols:
        return

    if visited[row][col] or grid[row][col] != 1:
        return
    visited[row][col] = True
    explore(row - 1, col, grid, visited, numRows, numCols)
    explore(row + 1, col, grid, visited, numRows, numCols)
    explore(row, col - 1, grid, visited, numRows, numCols)
    explore(row, col + 1, grid, visited, numRows, numCols)

def getPerimeterContribution(row, col, grid, numRows, numCols):
    perimeterContribution = 0
    if row == 0 or grid[row - 1][col] == 0:
        perimeterContribution += 1
    if row == numRows - 1 or grid[row + 1][col] == 0:
        perimeterContribution += 1
    if col == 0 or grid[row][col - 1] == 0:
        perimeterContribution += 1
    if col == numCols - 1 or grid[row][col + 1] == 0:
        perimeterContribution += 1
    return perimeterContribution


"""Solution two recognizes that we actually don't need a dfs since we are told that there is a single island and that happens only
in the case where all the 1's in the grid are connected."""
def islandPerimeter(grid):
    numRows , numCols = len(grid), len(grid[0])
    visited = [[False for i in range(numCols)] for j in range(numRows)]

    for row in range(numRows):
        for col in range(numCols):
            if grid[row][col] != 1:
                continue
            visited[row][col] = True
            
    perimeter = 0
    for row in range(numRows):
        for col in range(numCols):
            if visited[row][col]:
                perimeter += getPerimeterContribution(row,col,grid, numRows, numCols)
    return perimeter


def getPerimeterContribution(row, col, grid, numRows, numCols):
    perimeterContribution = 0
    if row == 0 or grid[row - 1][col] == 0:
        perimeterContribution += 1
    if row == numRows - 1 or grid[row + 1][col] == 0:
        perimeterContribution += 1
    if col == 0 or grid[row][col - 1] == 0:
        perimeterContribution += 1
    if col == numCols - 1 or grid[row][col + 1] == 0:
        perimeterContribution += 1
    return perimeterContribution
    
"""Solution three builds on solution two and uses only the visited matrix to determine perimeter contributions"""
def islandPerimeter(grid):
    numRows , numCols = len(grid), len(grid[0])
    visited = [[False for i in range(numCols)] for j in range(numRows)]

    for row in range(numRows):
        for col in range(numCols):
            if grid[row][col] != 1:
                continue
            visited[row][col] = True
            
    perimeter = 0
    for row in range(numRows):
        for col in range(numCols):
            if visited[row][col]:
                perimeter += getPerimeterContribution(row,col,visited, numRows, numCols)
    return perimeter

def getPerimeterContribution(row, col, visited, numRows, numCols):
    perimeterContribution = 0
    if row == 0 or not visited[row - 1][col] :
        perimeterContribution += 1
    if row == numRows - 1 or not visited[row + 1][col] :
        perimeterContribution += 1
    if col == 0 or not visited[row][col - 1] :
        perimeterContribution += 1
    if col == numCols - 1 or not visited[row][col + 1] :
        perimeterContribution += 1
    return perimeterContribution
    

"""Solution four where we use dfs to calculate the perimeter directly. Because of the visted matrix, which we need always,
the recursive stack doesnt worsen time complexity making this the most optimal solution."""
class PerimeterCount:
    def __init__(self,value):
        self.value = value

def islandPerimeter(grid) :
        numRows , numCols = len(grid), len(grid[0])
        visited = [[False for i in range(numCols)] for j in range(numRows)]
        
        for row in range(numRows):
            for col in range(numCols):
                if visited[row][col]:
                    continue
                if grid[row][col] != 1:
                    continue
                perimeterSum = explore(row, col, grid, visited, numRows, numCols)
    
        return perimeterSum.value
    
def explore(row, col, grid, visited, numRows, numCols):
    if row < 0 or col < 0 or row >= numRows or col >= numCols or grid[row][col] != 1: #bordering water either out of bounds or actual water
        return PerimeterCount(1) #return 1 for 1 side bordering water

    if visited[row][col] : #if visited, return 0, because they belong to the same island 
        return PerimeterCount(0)

    visited[row][col] = True #mark current island as True
    
    tempValue = 0 #initialize value for the perimeter count, then get the values for all four sides
    tempValue += explore(row - 1, col, grid, visited, numRows, numCols).value #go up , 0 if part of island; 1 if water or border
    tempValue += explore(row + 1, col, grid, visited, numRows, numCols).value #go down , 0 if part of island; 1 if water or border  
    tempValue += explore(row, col - 1, grid, visited, numRows, numCols).value #go left , 0 if part of island; 1 if water or border
    tempValue += explore(row, col + 1, grid, visited, numRows, numCols).value #go right , 0 if part of island; 1 if water or border
    
    
    return PerimeterCount(tempValue) #return perimeter contribution


    
    