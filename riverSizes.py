"""
So the general steps for dfs graph problems  are
    - visited data structure, could be a single variable (count) or a set or a matrix
    - an outer loop to ensure that we call dfs on every node even if the graph is disconnected
    - inside the dfs function, we initialize a stack with the call node or use the recursive stack. Dfs runs as long as stack is non-empty
    - inside the dfs, we check if the current node is visited. If it is we might continue to the next node on the stack or even return
    - if current node is unvisited we mark as visited
    - we use a getNeighbors function to collect the neighbors of the current node and use a for loop to add them to the stack
    - when the dfs stack is empty, we may return something or store something in outside the loop, then back to the outer loop
    
The input is a 2-d array containing only 0's and 1's. Each 0 represents land, each represents part of a river. A river consists of any
number of 1s that are either horizontally or vertically adjacent but not diagonally adjacent. The number of adjacent 1s forming a river
determines its size. A river can twist, it can be horizontal, veritcal or L-shaped. The question is to write a function that returns an 
array of the sizes of all rivers represented in the input matrix in any order.

So first of all, we need a sizes array to keep track of all river sizes. Also we always need a visited matrix or set or count to tell 
help us avoid being stuck in cycles. In this question, being stuck in a cycle, simply means that we are double counting 1s which have
already been counted as part of a previous river. Because the input is a matrix, the keep track of visited node's using a matrix, which
is initialized to false at each node in the graph. Then we need an outer loop that is going to go through every node in the graph (matrix)
in the case of a disconnected graph. Again just like the visited data structure, the meaning this outer loop takes will depend on the 
question being asked. Here in the outer loop, we skip a node if was previously visited, Otherwise, we pass the matrix, the visited data
structure, the node coordinates and the sizes array into a helper function to traverse the graph and calculate the sizes of rivers.

Inside the traverseNode function we first initialize the current river size to 0 and add the current node's coordinates into a stack.
This is because we are about to conduct a depth first search of the graph to find river sizes. In depth first search we always use a
stack though for some problems, the in-built recursive stack is enough, for other problems, such as conducting a dfs on a matrix-graph,
we need to use our own stack. This also means that the dfs will not be recursive. Depth-first search need not be recursive it only
needs a stack ie either the recursive stack when the question lends itself to recursion like tree traversal or a custom stack like 
a matrix graph traversal. Also note that we initialize a new stack for each new node, passed by the outer loop. The visited is the 
same for all dfs calls, but the stack is always re-initialized with each new dfs call.

Inside the while loop for the dfs, we pop from the stack for the current node, unpack the node's coordinates and check if the 
corresponding boolean at the same coordinates in the visited matrix is True. This is how we check if a node has previously been
visited by relating the coordinates of the node to the coordinates of the visited matrix. Note here that we mark every node, whether
0 or 1 as visited once we actually unpack. Also notices the standard technique of first checking if node is visited (and continuing 
if it has or return some sort of result) before actually marking the node as visited. First check if visited, then mark as visited.
The result of the visited check will depend on the question ; in some questions, we return a value or boolean, or we detect a
cycle or we simply continue. So if the node has not been previously visited, we mark it as visited. Then we check the value of the
node. If it is a 0 we continue otherwise if it is a 1 we go on. Again we can do this value check in the outer loop but we would also
have to mark the node as visited. In the code we actually do a visited check in the outer loop but that doesnt really change any thing
just a tiny optimization, because we always initialize a stack, enter the dfs while loop, pop, unpack and check for visited.

So the current value is a 1 and was previously unvisited and just marked as visited. We then increment the current river size by 1.
We go get the (unvisited) neighbors with the standard get neighbors function. Again here in the code, we use collect only unvisited
neighbors, but that is also not necessary. We could just have correctly addded all neighbors and and skipped over those that have 
been visited. So with the neighbors from the getNeighbors function,we use a for loop to append them to the stack. The dfs while loop
will terminate when the stack is empty so outside the loop, if the current river size is greater than 0, we append it to the sizes
array that we passed in from the outer loop.

 """

def riverSizes(matrix):
    sizes = []  #output / solution array
    #auxilliary boolean matrix for visited node, dict can be used too
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)): #number of rows
        for j in range(len(matrix[i])): #number of columns in row
            if visited[i][j]: #if True in aux matrix
                continue
            traverseNode(i,j,matrix,visited,sizes) #otherwise traverse node
    return sizes

def traverseNode(i,j,matrix,visited,sizes):

    currentRiverSize = 0
    nodesToExplore = [[i,j]] #using depth-first search, so use stack, for breadth-first , use queue

    while len(nodesToExplore):
        currentNode = nodesToExplore.pop() #stack
        i = currentNode[0]
        j = currentNode[1]
        #check if visited
        if visited[i][j]:
            continue
        visited[i][j] = True   # mark as visited
        #if a piece of land
        if matrix[i][j] == 0:
            continue
        #if not land(0) must be river, so increase current river size
        currentRiverSize +=1 #unvisited river, encountered increase current river size
        unvisitedNeighbors = getUnvisitedNeighbors(i,j,matrix,visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor) #graph traversal, depth-first search method
    
    # while loop terminates once nodesToExplore is empty
    if currentRiverSize > 0 :
        sizes.append(currentRiverSize)


def getUnvisitedNeighbors(i,j,matrix,visited):
    unvisitedNeighbors = []
    #check for valid neighbors, nodes at corners of matrix some neighbors don't exist
    #above node , first row i==0 dont have above
    if i > 0 and not visited[i-1][j]: #for nodes not in first row and above node is not visited
        unvisitedNeighbors.append([i-1,j]) #append above node
    #below node , last row i==len(array) -1  dont have below node   
    if i < len(matrix) -1 and not visited[i+1][j]: # for nodes not in last row, and below node is not visited
        unvisitedNeighbors.append([i+1,j]) #append left node
    #nodes on left border dont have a left node
    if j > 0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i,j-1]) #aopend left node
    #nodes on right border(j=len(matrix[0])-1) dont have right node  
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        unvisitedNeighbors.append([i,j+1])
    return unvisitedNeighbors
    

"""Solution two, same idea as before but realizing that if we just count all the connected 1's we have the river size.  So I use an 
object, RiverSize to store the size of the current river throughout the recursive calls, after marking a connected unvisited 1 as 
visited. Also I use the recursive stack instead of implementing an actual stack and implementing dfs iteratively. I also just skip 
the 0's in the outer loop. I also include the getNeighbors function into the recursive dfs function."""

class RiverSize:
    def __init__(self,value):
        self.value = value

#O(n*m) time | O(n*m) space
def riverSizes(matrix):	
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    sizes = []
    for row in range(rows):
        for col in range(cols):
            if visited[row][col] or matrix[row][col] != 1: #only start dfs from unvisited 1's
                continue
            area = RiverSize(0)
            explore(row, col, matrix, visited, rows, cols, area)
            sizes.append(area.value)
    return sizes

def explore(row, col, grid, visited, rows, cols, area):
    if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] != 1:
        return
    
    visited[row][col] = True
    area.value += 1
    explore(row - 1, col, grid, visited, rows, cols, area)
    explore(row + 1, col, grid, visited, rows, cols, area)
    explore(row, col - 1, grid, visited, rows, cols, area)
    explore(row, col + 1, grid, visited, rows, cols, area)


        
""""Solution III, where I dont use and increment the value of a custom object in order to use the recursive stack, but instead add up 
the length of the river starting from all the connected ones and return them up the recursive tree. So that if we have 1-1-1, the first
one will wait for the answeer from the second 1 which will wait for an answer from the last 1. The last 1 will initialize its size as 1,
then receive 0's from its neighbor calss (assume all the 1's are surrounded by 0's) then it returns size = 1 to the second connected 1,
which will add it to its own initial size of 1, to get size = 2, return this to the first connected 1, which will add it to its own
initial size of 1 to get 3 and return this to the outer loop where it will be appended to the size array. So while solution II calculates
the size in a top-down manner by updating a custom object value, this solution uses a truly recursive bottom up approach. Some solutions
require a top-down approach, other require a bottom-up approach. Knowing how to think differently is thus useful. """
def riverSizes(matrix):	
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for i in range(cols)] for j in range(rows)]

    sizes = []
    for row in range(rows):
        for col in range(cols):
            if visited[row][col] or matrix[row][col] != 1: #only start dfs from unvisited 1's
                continue
            size = explore(row, col, matrix, visited, rows, cols)
            sizes.append(size)
    return sizes

def explore(row, col, grid, visited, rows, cols):
    if row < 0 or row >= rows or col < 0 or col >= cols or visited[row][col] or grid[row][col] != 1:
        return 0
    
    visited[row][col] = True
    currentSize = 1
    currentSize += explore(row - 1, col, grid, visited, rows, cols)
    currentSize += explore(row + 1, col, grid, visited, rows, cols)
    currentSize += explore(row, col - 1, grid, visited, rows, cols)
    currentSize += explore(row, col + 1, grid, visited, rows, cols)
    return currentSize



matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
  ]
print(riverSizes(matrix))