"""Naive approach of testing every possible submatrix for the greatest sum"""
#O(width*height*size^2) time | O(1) space
# def maximumSumSubmatrix(matrix,size):
#     maxSum = float("-inf")
#     maxRow, maxCol = 0,0
#     for row in range(0,len(matrix) - size + 1):#O(w*h)
#         for col in range(0,len(matrix[0]) - size +1):
#             subMatrixSum = getSum(matrix,size,row,col)
#             if subMatrixSum > maxSum:
#                 maxSum = subMatrixSum
#                 maxRow = row
#                 maxCol = col
              
#     return maxSum, getSubmatrix(matrix,maxRow,maxCol,size)

# def getSum(matrix,size,row,col):#O(size^2)
#     sum = 0

#     for i in range(row,row + size):
#         for j in range(col, col + size):
#             sum += matrix[i][j]
#     return sum
    
# #This function isnt included in the complexity analysis, just something i threw in
# def getSubmatrix(matrix,maxRow,maxCol,size):
#     array = []

#     for row in range(maxRow,maxRow + size):
#         array.append(matrix[row][maxCol:maxCol+size])
#     return array


"""Optimal Solution uses extra space to create a sums array so that we can return the sum of size by size in constant-time"""
#O(w*h) time | O(w*h) space
def maximumSumSubmatrix(matrix,size):
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float("-inf")

    for row in range(size - 1, len(matrix)): #note that starting position is size - 1
        for col in range(size -1, len(matrix[row])): #note that starting position is size - 1
            total = sums[row][col] #start with sums[row][col] and check borders of size x size submatrix ending at row,col if subtraction needed
            
            touchesTopBorder = row - size < 0  #check top border
            if not touchesTopBorder: #if size x size submatrix ending at row,col is not on top border 
                total -= sums[row - size][col] #subtract the sums value above size x size submatrix ending at row,col
            
            touchesLeftBorder = col - size < 0 #check left border
            if not touchesLeftBorder:   #if size x size submatrix ending at row,col is not on left border 
                total -= sums[row][col - size]   #subtract the sums value to the left of size x size submatrix ending at row,col

            #if touches both top and left top border
            touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
            if not touchesTopOrLeftBorder: #if not touchesTopBorder and not touchesLeftBorder
                total += sums[row-size][col-size]  #add in the overlapping value of left and top subtractions
            
            maxSubMatrixSum = max(maxSubMatrixSum, total)
    
    return maxSubMatrixSum
            

def createSumMatrix(matrix):
    #initial value 0 repeated col num of times to create 1 row which is then repeated row number of times to create the matrix of 0's
    sums = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))] 
    #update the sums value for the top left corner
    sums[0][0] = matrix[0][0] 
    #next thing is to first fill sums values in the first row 
    for idx in range(1,len(matrix[0])):
        sums[0][idx] = sums[0][idx-1] + matrix[0][idx]
    #then the sums values in first column
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]
    #then the sums values for rest of the matrix
    for row in range(1,len(matrix)):
        for col in range(1,len(matrix[row])): #could also have used matrix[0] since all rows have the same number of columns
            #sums[row][col] = matrix value at row,col + sums to left + sums above - sums diagonal up
            sums[row][col] = matrix[row][col] + sums[row][col - 1] + sums[row -1][col] - sums[row -1][col-1] #constant-time update everywhere
    return sums










matrix=[
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2]
  ]

size=2
print(maximumSumSubmatrix(matrix,size))