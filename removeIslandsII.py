def removeIslands(matrix):
    

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
            changeBorderConnectedOnesToTwos(matrix,row,col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            color = matrix[row][col]
            if color == 1: #island, a 1 unconnected to border
                matrix[row][col] = 0
            elif color == 2:
                matrix[row][col] = 1

    return matrix


def changeBorderConnectedOnesToTwos(matrix,startRow,startCol):
    stack = [(startRow,startCol)]
    while len(stack)>0:
        currentPosition = stack.pop()
        currentRow, currentCol = currentPosition

        matrix[currentRow][currentCol] = 2
        #get neighbors of current node
        neighbors = getNeighbors(matrix,currentRow,currentCol)
        #loop through neighbors and append 1s to the stack
        for neighbor in neighbors:
            row, col = neighbor #unpack row and col of current neighbor

            if matrix[row][col] != 1: #contine if a 0
                continue 
            #append neighboring 1s ie 1s connected to border 1s
            stack.append(neighbor)


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



matrix = [
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1]
  ]
print(removeIslands(matrix))





              

