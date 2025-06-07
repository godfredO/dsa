"""You are given an n x n binary matrix grid where 1 represents land and 0 represents water. An island is a 4-directionally connected 
group of 1's not connected to any other 1's. There are exactly two islands in grid. You may change 0's to 1's to connect the two islands 
to form one island. Return the smallest number of 0's you must flip to connect the two islands.

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


In asking how many 0's we can flip to connect the two islands in the matrix, the question is asking what is the shortest path between the 
two islands. Now when you think about shortest path, you think about algorithms like Djikstra's and Bellman-Ford which are used for  graphs 
with weighted edegs. What do these techniques have in common? They are both breadth-first search algorithms. You may not have realized it,
but breadth-first search is actually a shortest path algorithm for graphs with unweighted edges. So what the graph is asking as to do
is to use breadth-first search to determine the shortest path or shortest transformation from one island to the other island.

The first question to ask is that how do we measure this path? From either island, which of the connected 1's do we use as our 
starting point to measure out. The good thing is that this question reeks of bfs . And bfs can be applied to multiple sources and multiple 
destinations ie simultaneous bfs. By simultaneous bfs, I mean that we initialize our queue with more than one position, and then we use our
bfs algorithm to take one step from all these positions, and then two steps and then three and so on until we find what we are looking for. 
That is we can start a bfs from the connected 1's of one island and determine the shortest distance to the other island aka the smallest 
number of 0's we can flip. To do this we initialize our bfs queue with all the positions of one island's connected 1's and then check all 
the positions that are one layer away from these positions, ie neighboring nodes that are one removed from the island's 1's, if these 
positions contain the other island's 1's. Of course since the two islands are distinct we expect to see at least one buffer layer of 0's 
between them so we expect that the first layer of neighbors will contain only 0's . So we add these to our stacks and increment our flips 
variable by 1. Then we collect all the neighbors of the first layer nodes and ask if any of them is a 1. Now we need to keep track of the 
visited nodes in each step. But the idea is that the first time we find a neighboring layer node that is a 1, since we started from one 
island, that 1 must belong to the second island and we return the flips variable because we have determined the shortest unweighted path 
between the two islands.

Now we need to first find one of the islands so we actually need a dfs for that. So we search the input matrix, for the first position that 
contains a 1, then we start a dfs from it to mark all of its connected 1's using the visited matrix. We convert the marked positions in this 
visited matrix or set into the initial positions in the queue. Then since we don't want to visit trip over ourselves and mistakenly think the
first island 1's are the second island 1's, we use the same visited matrix from the dfs as the visited matrix or set for the bfs. Because of
this unique situation, and since we are starting from one island 1's we need to make sure the solution is coded up in a particular way in 
order to avoid mistakes. We take the size of the queue so that we can decrement it for each node we pop and process. This way whenever size
reaches 0, we know that we have processed an entire layer of nodes. So we pop from the queue, get all the neighbors of the popped position, 
we do not check visited or if the value is 1 here since that will lead to a mistake, again because we are using the visited set from our dfs
so our first queues will be visited and 1's. Ideally, I guess you can add the valid neighbors of the marked 1's of the first island to the
queue as initial positions and initialize the flips variable to 1 so that you can code this up like a typical bfs where you check visited
status, mark visited status, then check if a position is 1 before adding only unvisited neighbors, but this way is simpler. So when we get 
the neighbors of the popped positions, we discard any invalid or visited neighbors, then we check if the neighbor's is 1. If it is it must 
belong to the second island so we return flips variable. If its not, we mark it as visited and add the neighbor position as visited. Now 
since the dfs and bfs follow one another instead of being nested, the time and space complexity is still O(n*n), since we are given an nxn 
binary matrix. Now in the code, we do the one dfs, follow it up with the bfs and return the answer from the bfs so the outer for loop doesnt
get to run a second dfs. If we don't code it up like this will need to break out of the two for loops that make up the outer loop and we 
will need to use a flag for that and so on and so forth. All I am saying is that coding this question's solution, is slightly trickier than 
it seems from looking at the idea.
"""

""" Solution I- optimal solution"""
#O(n*m) time | O(n*m) space
from collections import deque
def shortestBridge(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for i in range(cols)] for j in range(rows)] #this is the visited matrix for the dfs

    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                dfs(row, col, grid, visited, rows, cols)
                return bfs( rows, cols, grid, visited)
                  
def initializeQueue(visited,rows,cols):
    queue = deque()
    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                queue.append([row, col])
    return queue
    
    
def dfs(row, col, grid, visited, rows, cols):
    if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0 or visited[row][col]:
        return
    visited[row][col]= True
    dfs(row - 1, col, grid, visited, rows, cols)
    dfs(row + 1, col, grid, visited, rows, cols)
    dfs(row, col - 1, grid, visited, rows, cols)
    dfs(row, col + 1, grid, visited, rows, cols)


def bfs( rows, cols, grid, visited):
    queue = initializeQueue(visited,rows,cols) 
    flips = 0
    while queue:
        size = len(queue)
        while size > 0 :
            row, col = queue.popleft()
            directions = [[1,0],[-1, 0], [0,1],[0,-1]]
            for direction in directions:
                deltaX, deltaY = direction
                nrow, ncol = row + deltaX, col + deltaY 
                if nrow < 0 or ncol < 0 or nrow >= rows or ncol >= cols or visited[nrow][ncol]:
                    continue
                if grid[nrow][ncol]:
                    return flips
                queue.append([nrow, ncol])
                visited[nrow][ncol] = True
            size -= 1
        flips += 1




grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
print(shortestBridge(grid))