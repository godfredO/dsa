"""So the general steps for graph problems are
    - visited data structure, could be a single variable (count) or a set or a matrix
    - an outer loop to ensure that we call dfs on every node even if the graph is disconnected, we may filter out some nodes in outer loop
    - inside the dfs function, we initialize a stack with the call node. Dfs runs as long as the stack is non-empty
    - inside the dfs, we check if the current node is visited. If it is we might continue to the next node on the stack or even return
    - if current node is unvisited we mark as visited
    - we use a getNeighbors function to collect the neighbors of the current node and use a for loop to add them to the stack
    - when the dfs stack is empty, we may return something or store something in outside the loop, then back to the outer loop

This input to this question is a two dimensional array containing only 0s and 1s. An island is defined as any number of 1s that are 
horizontally or vertically adjacent (but not diagonallyy adjacent) and that don't touch the border of the matrix. An island can twist 
(hmm like a river can twist in river sizes question, meaning dfs). The question is to write a function that returns a modified version of
the input matrix, where all of the islands are removed. You remove an island by replacing it with 0s. 

This is a great question because it really makes use of the general steps listed above. First the visited matrix is used in a clever way.
The question asks to remove all islands. Another way of saying it is that replace every 1 with a 0 unless that 1 is a non-island. This
way of thinking, 'complement thinking' where you reformulate a question in terms of some sort of complement is useful. So anyway, the
visited matrix will be used to store whether a 1 is a non-island. Meaning is it connected to a border 1. Then when we have the visited
matrix storing True for every non-island, we can then use it to flip every position in the matrix that has a False in the visited to 0.
This will have the effect of flipping 0's to 0's and island 1's to 0's. So we dont actually look for islands, we look for non-islands,
'cover' them with True in the visited matrix and paint every other position with a 0, and then when we remove the cover the only 1s 
remaining will be the non-island ones. Phew that painting metaphor kinda got away from me there!!!

Any way how do we find these non-island 1's. We add some modifications to the outer for loop to only call the dfs function on border 1s.
So we first check if the row,col in the outer loop is not on the border. If it is not continue to the next node. Then we check if the 
border row, col is a 0. If it is we continue. Also quick word about how we ensure that we only call dfs on border 1's. We first check if 
the column is on the border ie col 0 or col len(matrix[row]) - 1. We also check if row is on the border ie row 0 or row len(matrix) - 1. 
The we define a variable that stores both information ie isBorder = rowIsBorder or colIsBorder. Thus at that point we will be left with 1's 
on the border. Then we call the dfs on these.

Inside the dfs we do the same of initializing a new stack with the node from the outer loop. This is the recursive stack. And we keep
running the dfs as long as the stack is non-empty. We again pop, unpack and check if the corresponding node in the visited is True ie
we already visited this node and marked it as a non-island 1. If its already visited we continue to the next node on the stack. Otherwise
we mark it as visited and go get its neighbors. The getNeighbors function is standard for a 2-d array with horizontal and vertical 
movements (but not diagonal). Inside the for loop to add neighbors to the stack, we make a few modifications to solve the problem.
For each neighbor, we check the value. If the neighbor is not a 1, we continue otherwise we append the neighbor to the stack and by that
we mean we append a list [row,col] of neighbor's coordinate. So when the outer loop calls the dfs function on every border 1 and the dfs
function finds and marks every neighbor of a border 1 which is a 1, we have our paint strips in-place covering non-island 1s. 
Now lets paint the island 1s to 0s with the help of this clever visited paint strip matrix.

So outside the outer for loop, we have another for loop that goes through the matrix and at each point checks if the corresponding node
in the visited matrix is a True, for non-island 1. If it is we continue to the next node in the matrix. If its not we set the value in
the matrix to 0. And voila, clever modifications and implementation of the general steps have helped solve this question. This loop 
is optimized by excluding the borders anyway ie row is range(1, len(matrix) - 1), col is range(1, len(matrix[row])-1)

There is another version of this solution, that doesnt use the visited matrix to mark non-island 1's, instead prefering to change the
values of non-island 1's to 2's inside the dfs function. That is the step where we mark a node as True after checking if previously
visited, this solution replaces with a simple step of replacing with a 2. Then inside the for loop for adding we still check if the
neighbor is not a 1 in which case we continue to next neighbor. This will have the added effect of skipping over all the 2's ie 
previously visited nodes hence why no visited matrix and no visited check in the dfs. Then to replace all island 1's we simply say 
that if the node's value in the matrix is 2, make it a 1, otherwise make it a 0 (both 0's and 1's become 0's). In this version of the
solution we go through all positions, we dont skip the borders at all, so that we can change border 2's to 1's. This technically has
the same space complexity because we could have all 1's ie every position is a 1 and connected to a border 1 so the stack in that
case would hold w*h nodes inside the dfs function but since in general we don't expect that we will have a better space complexity.
If you ask me, this version is cute, nothing more, but hey do anything for them coding point man. 

The technique used here, I would call reverse / complement thinking dfs. Another reverse / complement thinking dfs question is 
pacificAtlanticWaterFlow.py . Check out wallsAndGates for reverse / complement thinking bfs. Basically you realize the question is 
an either or situation so you start from the complement situation and use it to get your answer. Here you do a dfs to mark all the
non-island, then go through the matrix later and flip all non-marked positions.


    """

def removeIslands(matrix):
    #initialize boolean matrix to track border 1s and connected-to border 1s
    onesConnectedToBorder = [[False for col in row ]for row in matrix] 

    #find border 1's 
    for row in range(len(matrix)): #select row, list of lists
        for col in range(len(matrix[row])): #go through each col for selected row (list of lists)
            #are we on a border row
            rowIsBorder = row == 0 or row == len(matrix) -1 #top row or bottom row
            #are we on a border column
            colIsBorder = col == 0 or col == len(matrix[row]) -1 # current col in current row
            isBorder = rowIsBorder or colIsBorder #if either on a border row or border col
            #if we ar not on the border, continue
            if not isBorder:
                continue
            #if we are on the border but value is 1, continue
            if matrix[row][col] != 1:
                continue
            #if we found a border 1, use depth-first search to find connected 1s
            findOnesConnectedToBorder(matrix,row,col,onesConnectedToBorder)

    for row in range(1,len(matrix)-1):
        for col in range(1, len(matrix[row])-1):
            if onesConnectedToBorder[row][col]:
                continue
            #set island 1s, (and 0s too) to 0
            matrix[row][col] = 0

    return matrix


# def findOnesConnectedToBorder(matrix,startRow,startCol,onesConnectedToBorder):
#     stack = [(startRow,startCol)]
#     while len(stack)>0:
#         currentPosition = stack.pop()
#         currentRow, currentCol = currentPosition

#         #if already visited, continue
#         alreadyVisited = onesConnectedToBorder[currentRow][currentCol]
#         if alreadyVisited:
#             continue
        
#         #if not, mark as visited, then get neighbors
#         onesConnectedToBorder[currentRow][currentCol] = True
        
#         #get neighbors of current node
#         neighbors = getNeighbors(matrix,currentRow,currentCol)
#         #loop through neighbors and append 1s to the stack
#         for neighbor in neighbors:
#             row, col = neighbor #unpack row and col of current neighbor

#             if matrix[row][col] != 1: #contine if a 0
#                 continue 
#             #append neighboring 1s ie 1s connected to border 1s
#             stack.append(neighbor)


def findOnesConnectedToBorder(matrix,startRow,startCol,onesConnectedToBorder):
    onesConnectedToBorder[startRow][startCol] = True
    neighbors = getNeighbors(matrix, startRow, startCol)
    for neighbor in neighbors:
        row, col = neighbor
        if onesConnectedToBorder[row][col]:
            continue
        if matrix[row][col] != 1:
            continue
        findOnesConnectedToBorder(matrix, row, col, onesConnectedToBorder)

def getNeighbors(matrix,row,col):
    neighbors= []
    numRows = len(matrix)
    numCols = len(matrix[row])

    #append valid neighbors
    if row -1 > 0: #up neighbor, first row doesnt have a neighbor
        neighbors.append((row-1,col))
    if row+1 < numRows: #down neighbor
        neighbors.append((row+1,col))
    if col -1 >= 0: #left neighbor
        neighbors.append((row,col-1))
    if col + 1 < numCols:#right neighbor
        neighbors.append((row,col+1))

    return neighbors


"""Solution III, same idea, just incorporating the getNeighbors function into the dfs and returning from invalid calls"""
def removeIslandsIV(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    for row in range(rows):
        explore(row, 0, matrix, visited, rows,cols)
        explore(row, cols - 1, matrix, visited, rows,cols) 

    for col in range(cols):
        explore(0, col, matrix, visited, rows,cols)
        explore(rows - 1, col, matrix, visited, rows,cols)
    
    for row in range(rows):
        for col in range(cols):
            if visited[row][col]:
                continue
            matrix[row][col] = 0
    return matrix

def explore(row, col, matrix, visited, rows, cols):
    if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or matrix[row][col] != 1:
        return
    
    visited[row][col] = True
    print(row,col)
    explore(row - 1, col, matrix, visited, rows, cols)
    explore(row + 1, col, matrix, visited, rows, cols)
    explore(row, col - 1, matrix, visited, rows, cols)
    explore(row, col + 1, matrix, visited, rows, cols)


matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]
print(removeIslandsIV(matrix))





              

