"""You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island 
is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells. An island 
in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2. Return 
the number of islands in grid2 that are considered sub-islands.

Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
       grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3

Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], 
       grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 

So the idea of sub-islands is that if you find an island in grid2, there is a corresponding island in grid1 ie every single cell of the grid2 
island is also contained in a single island of grid1. This part of ensuring that every single cell of any grid2 island be contained in a 
single island of grid1 is essential. On the flip side a single island in grid1 can be broken up into multiple islands in grid2 because eveen 
in that case, every single cell of the grid2 islands is contained in a single island in grid1. . This also means that if an island in grid2 
does not have a corresponding island in grid1, it does not count as a sub-island. It is also possible that an island in grid1 has some of its 
1's present in grid2 but in grid2 they dont necessarily correspond to a single island but rather are broken up into mini-islands. Example if 
we had 1,1,1 in grid1 but 1,0,1 in grid2, the single island in grid1 has become 2 sub-islands in grid2. And finally we can have an island in 
grid 2 but only some of its 1's are present in grid1 in which case that island is not a sub-island since all of its cells are contained in a 
single island in grid1. For example, if in grid1, we have 1,0,1 and in grid2 we have 1,1,1, then even though the first and last 1 of grid2's 
island is present in grid1, the entire island is not contained in a single island of grid1.

So the naive way of solving this question will be to find the islands in grid1, store the coordiantes of the 1's that make up any island in
grid2 say in a list of coordinates, and then find the islands in grid2 and for each island check if all of its coordiantes is in any of 
grid1's list of coordiantes. The more efficient solution will be to do a simultaneous dfs where we start a dfs for grid2 and every time we 
find a 1, we check if that position is also a 1 in grid1. We use a True / False backtracking techinque to determine if we need to continue 
down a path or not. So when we finish discovering a island in grid2 and for each 1 in this island, we found a corresponding 1 in grid1, we 
return True so that can increment our subIsland variable by 1. But if we find a contiguous 1 in grid2 and that position is 0 in grid1, then 
we know that island in grid2 cannot be a sub-island of grid1 so return False so that we can continue down the next path. Of course we will 
keep a visit set / matrix for grid2 so that we dont visit the same coordinate multiple times. So what we are effectively doing is taking the 
algorithm for finding islands and modifying it to find sub-islands in grid2. So if we find a contiguous 1 in grid2 and the same position is 
also a 1 in grid 1, we continue till we reach the bounds of the island in grid2 then return 1. Otherwise if a contiguous 1 in grid2 does not 
have a corresponding 1 in grid1, we terminate the search and return 0. The intuition is similar the sameTrees.py. The time and space complexity 
is O(n.m) where n,m are the dimensions of the grids.

In the code, I use an outer loop and skip over all visited 1's and positions that are 0 in grid2 and if we come to an unvisited 1, we start
a depth-first search to find subIslands and when a subIsland is found we increment the subIsland variable by 1. So in the depth first search
we will if the position is out of bounds, is visited or is 0 in grid2 we return True and this actually corresponds not to the outer loop dfs 
call but rather from the neighbor calls below. Otherwise if the corresponding position in grid1 is 0 we return False, and this can correspond
both to the neighbor calls and the outer loop call. Otherwise we have a valid, unvisited 1 in grid 2 with a corresponding 1 in grid1, so we
mark the position as visited. It is important to place this here  before we start the neighbor calls for up, down , left and right and return
the result of up and down and left and right dfs calls ie if they all return True we return True but if any of them returned False we return
False up the recursive tree up to the outer loop.
"""

def countSubIslands(grid1, grid2):
    rows, cols  = len(grid1) , len(grid1[0])
    visited = [[False for col in range(cols)]for row in range(rows)]

    subIslands = 0
    for row in range(rows):
        for col in range(cols):
            if visited[row][col]: #we start dfs from unvisited positions
                continue
            if grid2[row][col] == 0:
                continue 
            if foundSubIsland(row, col, grid2, visited, grid1, rows, cols):  #start dfs from univisited 1's 
                subIslands += 1
    return subIslands


def foundSubIsland(row, col, grid2, visited, grid1, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols or visited[row][col] or grid2[row][col] == 0: #for neighbor calls
        return True  #if we reach the bounds of an island in grid2
    
    #at this point we have a valid, unvisited, 1 in grid2 so lets check if grid1 has corresponding 1
    if grid1[row][col] == 0 :
        return False

    #at this point we have a valid, unvisited, 1 in grid2 with a corresponding 1 in grid 1 so lets visit it
    visited[row][col] = True

    #the start dfs on its neighbors, if a neighbor goes out of bounds, is visited or has 0, we receive True
    up = foundSubIsland(row -1, col, grid2, visited, grid1, rows, cols) 
    down = foundSubIsland(row +1, col, grid2, visited, grid1, rows, cols) 
    left = foundSubIsland(row, col - 1, grid2, visited, grid1, rows, cols) 
    right = foundSubIsland(row , col + 1, grid2, visited, grid1, rows, cols) 
    return up and down and left and right #check that we received True for all neighbors
    


grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
print(countSubIslands(grid1, grid2))