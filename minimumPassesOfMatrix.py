""" The input is an matrix of integers and the question is to write a function that returns the minimum number of passes required to
convert all negative integers in the matrix to positive integers. A negative integer in the matrix can only be converted to a positive
integer if one or more its adjacent elements is positive. An adjacent element is an element that is to the left, right, above, below 
the current element in the matrix. Converting a negativ to a positive simply involves multiplying it by -1. Note that 0 is neither 
positive nor negative, meaning that a 0 cannot convet an adjacent negative to postive. A single pass through the matrix involves 
converting all the negative integers that can be converted at a particular point in time. For example consider the following input
matrix.

The first observation is that this is a graph problem where each position in the 2-d matrix is a node. The second thing to realize is
that at the start of each pass, we need to collect all the positions that have positive numbers and for each positive number position
in the current pass, we need to get its adjacent neighbors, see if there are negative number neighbors and convert them. The next 
observation is quite crucial. After any adjacent negative numbers are converted for a particular position, that position cannot 
convert anymore; in fact the newly converted negative-to-positive numbers are the ones that can convert other negative numbers. And this
is how we differentiate between passes. At the beginning of each pass we collect all the positive positions, convert their adjacent 
negative positions, and we are done with the pass and those positive positions, we will never have to look at them or their neighbors
again. Then we collect the positions of the just converted negative-to-positive numbers and begin another pass. Because we have to process
all the adjacent positions for the positive positions at the beginning of each pass, this question is a breadth-first search graph problem,
not the typical depth first search. In dfs, we usually go back up the recursive stack, but here once we are done processing a particular
positive position, its entirely out of contention for the next pass. And since this is breadth first search, we use a queue. Now in between
passes, how do we differentiate which positive positions are from the old pass and which positive positions are new. In the code, one
solution uses two queues. That is as we go through the adjacent positions of a current positive integer we add the position of any 
converted negative numbers to the second queue. The second option is to take store the size of queue at the start of each pass and as
we convert negative numbers, each time we finish with the neighbors of the current positive node, we decrement this size variables so that
when this variable becomes 0, we know that we have completed one pass, so we increment the passes variable, and go back to the top of the
bfs while loop take the size of the queue again, and enter an inner while loop to pop and process exactly size nodes, and when the size
variable reaches 0, we increment passes go back to the top and take size again.

So obviously we will need a getNeighbors() helper function, we will also need a function to go through the matrix at the beginning and 
get all the initial positive nodes to initialize the queue. After that initial sweep, we just add to the queue (the same queue with the
size method) the position of any recently converted negative number. And finally, we will need to complete at least one pass even if we
dont have any negative numbers so when the bfs helper function returns passes,  the actual answer returned from the main function is 
passes - 1. Finally the question also says to return -1 if its impossible to convert all negative after breadth-first search concludes
we should return -1. Therefore we need to have a final sweep in the updated matrix for negative numbers. If there arent any, we return
passes - 1 otherwise -1.

This is one such question where we actually dont need a visited matrix, due to the nature of the question and the bfs implementation.
We initialize the queue with positive positions, look for negative neighbors, flip them to positive, then add the newly flipped 
positions to the queue. From the newly added positions we look for neighbors that are negative, and as such we will not visit the 
positive positions that flipped them again. So we don't need a visit matrix per se. But the space complexity is the same because of
the queue. Another question that by its nature doesnt need a visited matrix is longestIncreasingPathInMatrix.py. 

"""



# #O(w*h) time | O(w*h) space
# def minimumPassesOfMatrix(matrix):
#     passes = convertNegatives(matrix)
#     return passes - 1 if not containsNegative(matrix) else -1

# def convertNegatives(matrix):
#     nextPassQueue = getAllPositivePositions(matrix)

#     passes = 0

#     while len(nextPassQueue) > 0:
#         #the outer while loop switches the current and next Pass Queues
#         currentPassQueue = nextPassQueue
#         nextPassQueue = []
#         while len(currentPassQueue) > 0:
#             currentRow,currentCol = currentPassQueue.pop(0) #popping a value from the beginning of a list is O(N)
#             adjacentPositions = getAdjacentPositions(currentRow,currentCol,matrix)
#             for position in adjacentPositions:
#                 row,col = position

#                 value = matrix[row][col]
#                 if value < 0:
#                     matrix[row][col] = value * -1
#                     nextPassQueue.append([row,col])
#         passes += 1
#     return passes


# def getAllPositivePositions(matrix):
#     positivePositions = []

#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             value = matrix[row][col]
#             if value > 0:
#                 positivePositions.append([row,col])
#     return positivePositions


# def getAdjacentPositions(row,col,matrix):
#     adjacentPositions = []
#     if row > 0: #all rows except the first row have above neighbor
#          adjacentPositions.append([row-1,col])
#     if row < len(matrix) - 1: #all rows except last row have below neighbor
#         adjacentPositions.append([row+1,col])
#     if col >0: #all columns except the first column have a left neighbor
#         adjacentPositions.append([row,col-1])
#     if col < len(matrix[row]) - 1: #all columns except the last column have a right neighbor
#         adjacentPositions.append([row,col+1])
#     return adjacentPositions

# def containsNegative(matrix):
#     for row in matrix:
#         for value in row:
#             if value < 0:
#                 return True
#     return False


"""Taking the number of negative numbers and using it to avoid the last unnecessary pass"""

#O(w*h) time | O(w*h) space
def minimumPassesOfMatrix(matrix):
    passes, numNeg = convertNegatives(matrix)
    return -1 if numNeg > 0  else passes

#th
def convertNegatives(matrix):
    queue, numNeg = getAllPositivePositions(matrix)
    passes = 0

    #this while loop keeps running until all passes are complete
    while len(queue) > 0 and numNeg > 0:
        #the outer determinses size to delimit passes
        currentSize = len(queue)
        
        #this while loop is where 1 pass occurs at the end of which we increment passes
        while currentSize > 0:
            currentRow,currentCol = queue.pop(0) #popping a value from the beginning of a list is O(N)
            adjacentPositions = getAdjacentPositions(currentRow,currentCol,matrix)
            #this for loop processes one positive positon and its adjacent positions, decrement currentSize after it
            for position in adjacentPositions:
                row,col = position

                value = matrix[row][col]
                if value < 0:
                    matrix[row][col] = value * -1
                    queue.append([row,col])
                    numNeg -= 1
            currentSize -= 1
        passes += 1

    return passes, numNeg


def getAllPositivePositions(matrix):
    positivePositions = []
    numNeg = 0
    

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            value = matrix[row][col]
            if value > 0:
                positivePositions.append([row,col])
            elif value < 0:
                numNeg += 1
    return positivePositions, numNeg


def getAdjacentPositions(row,col,matrix):
    adjacentPositions = []
    if row > 0: #all rows except the first row have above neighbor
         adjacentPositions.append([row-1,col])
    if row < len(matrix) - 1: #all rows except last row have below neighbor
        adjacentPositions.append([row+1,col])
    if col >0: #all columns except the first column have a left neighbor
        adjacentPositions.append([row,col-1])
    if col < len(matrix[row]) - 1: #all columns except the last column have a right neighbor
        adjacentPositions.append([row,col+1])
    return adjacentPositions


from collections import deque
def minimumPassesOfMatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])

    queue = deque()
    numNegs = 0
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] > 0:
                queue.append([row,col])
            elif matrix[row][col] < 0:
                numNegs += 1
    
    passes = 0
    while queue and numNegs > 0:
        size = len(queue)
        while size > 0:
            row, col = queue.popleft()

            directions = [[1,0], [-1, 0], [0,1], [0,-1]]
            for direction in directions:
                deltaX, deltaY = direction
                nrow, ncol = row + deltaX, col + deltaY
                if nrow < 0 or nrow >= rows or ncol < 0 or ncol >= cols:
                    continue
                if matrix[row][col] < 0:
                    matrix[row][col] *= -1
                    numNegs -= 1
                    queue.append([nrow, ncol])
            size -= 1
        passes += 1
    
    return -1 if numNegs > 0 else passes

    






matrix = [
    [0, -1, -3, 2, 0],
    [1, -2, -5, -1, -3],
    [3, 0, 0, -4, -1]
  ]


print(minimumPassesOfMatrix(matrix))