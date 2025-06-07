"""This question gives a 2-d nxn square matrix made of 0's and 1's and asks to return if there exists an nxn square of zeroes
anywhere in the matrix. The iterative solution treats each position in the matrix as the top left corner of a square and creates 
squares of size 1 to n and has a helper function return if that square represents a square of zeros. Thus there are nxn = n^2 top 
left corners and each has up to n squares extending from it so there are up to n^3 squares in the matrix. A note here is that we 
are looking for squares and not rectangles so the sides of the squares should always be the same in other words the row distance and 
column distance from the top left corner should be equal. The recursive approach generates squares differently it first draws a nxn 
square around the perimeter of the matrix and then pushes each corner inside to form a new square and then pushes in all corners at 
the same time to form another square. This approach will lead to a lot of overlapping squares being drawn and thus requires caching or
memoization as a neccessary addition in order to solve the problem. After squares are generated either iteratively or recursively the
same helper function will determine if these squares have all zeroes, and this is a linear time complexity. In order to make this step
a constant time lookup we create a nxn matrix that includes at each positon a pair of numbers representing the number of zeros below and
to the right of that position, counting the 0 at that position as inclusive. If that position's valaue is a 1 we automatically store 0,0 
in this auxilliary matrix since the prescence of 1 on the border of a square automatically means it cannot be a square of zeroes. Thus
as we generate squares using the iterative approach for example, to test if a certain mxm square from the top left corner is a square
of zeroes we simply check if the topleft corner has m,m zeroes to below and to the right. If it does, we check if the elements m positions
to the right and below have m zeroes below and to the right respectively. Since we make the same three checks, everywhere, this check is
constant time; top left corner has m,m and top right corner has m,* and bottom left corner has *,m zeroes, m,m-below,right zeroes here. """

#Recursive approach with caching but no precomputation (dynamic programming)
#O(n^4) time | O(n^3) space - space because cache size equals and recursive stack at most equal to number of squares
# def squareOfZeroes(matrix):
#     lastIdx = len(matrix) - 1 #index of last row and also index of last column
#     return hasSquareOfZeroes(matrix,0,0,lastIdx,lastIdx,{}) #startRow,startCol,endRow,endCol,cache, endRow=endCol cos matrix is nxn

# def hasSquareOfZeroes(matrix,r1,c1,r2,c2,cache): #recursively generates squares and tests if boundaries are made of 0's
#     if r1 >= r2 or c1 >= c2: #base case, 1x1 square, horizontal line or vertical line, 
#         return False #then return False because not valid squares and if not valid squares cant be squares of zeroes
#     key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2) #generate unique hashable key for cache
#     if key in cache: #check that 
#         return cache[key]
#     cache[key] = (
#         isSquareOfZeroes(matrix,r1,c1,r2,c2) 
#         or hasSquareOfZeroes(matrix,r1+1,c1+1,r2-1,c2-1,cache) #move all rows and columns by 1 in the correct direction
#         or hasSquareOfZeroes(matrix,r1+1,c1+1,r2,c2,cache) #move one row and one column by 1 in the correct direction
#         or hasSquareOfZeroes(matrix,r1+1,c1,r2,c2-1,cache) #move one row and one column by 1 in the correct direction
#         or hasSquareOfZeroes(matrix,r1,c1+1,r2-1,c2,cache) #move one row and one column by 1 in the correct direction
#         or hasSquareOfZeroes(matrix,r1,c1,r2-1,c2-1,cache) #move one row and one column by 1 in the correct direction
#     ) #if current square or generated squares return True, answer is True, if at least one square of 0's exist anywhere

#     return cache[key]

# def isSquareOfZeroes(matrix,r1,c1,r2,c2): #O(n)
#     for row in range(r1,r2+1): #check for all zeroes between r1 and r2 and c1 and c2 are 0's. +1 to include r2 in range
#         if matrix[row][c1] != 0 or matrix[row][c2] != 0: #checking the vertical 0's, if any vertical point isnt 0
#             return False #return 0 because we found 1
#     for col in range(c1,c2+1):
#         if matrix[r1][col] != 0 or matrix[r2][col] != 0: #checking for upper and lower horizontal 0's in tandem, if any isnt 0
#             return False #return 0 because we found 1 somewhere so cant have a square of zeroes
#     return True


#Iterative solution without precomputaion
#O(n^4) time | O(1) space
# def squareOfZeroes(matrix):
#     n = len(matrix)
#     for topRow in range(n): #choose the row of top left corner
#         for leftCol in range(n): #choose corner of top left corner
#             squareLength = 2 #squareLength goes is 2,3,4 up to len(matrix) -1, squareLength of 1 isn't valid
#             while squareLength <= n - leftCol and squareLength <= n - topRow: #check that square length is valid for topRow,leftCol
#                 bottomRow = topRow + squareLength - 1 #remember that python is 0-indexed hence the -1 to get bottom row index
#                 rightCol  = leftCol + squareLength - 1 #remember that python is 0-indexed hence the -1 to get right column index
#                 if isSquareOfZeroes(matrix,topRow,leftCol,bottomRow,rightCol): #if we find a square of zeroes
#                     return True #return True
#                 squareLength += 1 #test next valid square size
#     return False #othewise return false

# def isSquareOfZeroes(matrix,r1,c1,r2,c2): #O(n)
#     for row in range(r1,r2+1): #check for all zeroes between r1 and r2 and c1 and c2 are 0's. +1 to include r2 in range
#         if matrix[row][c1] != 0 or matrix[row][c2] != 0: #checking the vertical 0's, if any vertical point isnt 0
#             return False #return 0 because we found 1
#     for col in range(c1,c2+1):
#         if matrix[r1][col] != 0 or matrix[r2][col] != 0: #checking for upper and lower horizontal 0's in tandem, if any isnt 0
#             return False #return 0 because we found 1 somewhere so cant have a square of zeroes
#     return True


"""Optimal recursive solution where we precompute the number of zeroes below and to the right of every element,inclusive of the
element and store this information in an auxilliary matrix"""
#O(n^3) time | O(n^3) space - space because cache size equals and recursive stack at most equal to number of squares
def squareOfZeroes(matrix):
    infoMatrix = preComputeNumOfZeroes(matrix) #value, if 0: numOfZerosBelowIncludingSelf, numZeorsToRightIncludingSelf else (if 1) [0.0]
    lastIdx = len(matrix) - 1 #index of last row and also index of last column
    return hasSquareOfZeroes(infoMatrix,0,0,lastIdx,lastIdx,{}) #startRow,startCol,endRow,endCol,cache, endRow=endCol, infoMatrix nxn

def hasSquareOfZeroes(infoMatrix,r1,c1,r2,c2,cache): #recursively generates squares and tests if boundaries are made of 0's
    if r1 >= r2 or c1 >= c2: #base case, 1x1 square, horizontal line or vertical line, 
        return False #then return False because not valid squares and if not valid squares cant be squares of zeroes
    key = str(r1) + "-" + str(c1) + "-" + str(r2) + "-" + str(c2) #generate unique hashable key for cache
    if key in cache: #check that 
        return cache[key]
    cache[key] = (
        isSquareOfZeroes(infoMatrix,r1,c1,r2,c2) 
        or hasSquareOfZeroes(infoMatrix,r1+1,c1+1,r2-1,c2-1,cache) #move all rows and columns by 1 in the correct direction
        or hasSquareOfZeroes(infoMatrix,r1+1,c1+1,r2,c2,cache) #move one row and one column by 1 in the correct direction
        or hasSquareOfZeroes(infoMatrix,r1+1,c1,r2,c2-1,cache) #move one row and one column by 1 in the correct direction
        or hasSquareOfZeroes(infoMatrix,r1,c1+1,r2-1,c2,cache) #move one row and one column by 1 in the correct direction
        or hasSquareOfZeroes(infoMatrix,r1,c1,r2-1,c2-1,cache) #move one row and one column by 1 in the correct direction
    ) #if current square or generated squares return True, answer is True, if at least one square of 0's exist anywhere

    return cache[key]

def isSquareOfZeroes(infoMatrix,r1,c1,r2,c2): #O(1) avoids repeated work of iterating through r1 to r2 and c1 to c2
    squareLength = c2 - c1 + 1 #the length of the square, check if a square of this size is a square of zeroes
    hasTopBorder = infoMatrix[r1][c1]["numZeroesRight"] >= squareLength #from the top left to the top right corner
    hasLeftBorder = infoMatrix[r1][c1]["numZeroesBelow"]>= squareLength #from the top left to the bottom left corner
    hasBottomBorder = infoMatrix[r2][c1]["numZeroesRight"] >= squareLength #from the bottom left to the bottom right corner
    hasRightBorder = infoMatrix[r1][c2]["numZeroesBelow"]  >= squareLength  #from the top right to the bottom right corner
    return hasTopBorder and hasLeftBorder and hasBottomBorder and hasRightBorder

def preComputeNumOfZeroes(matrix): #O(n)
    infoMatrix = [[x for x in row] for row in matrix] #initialize the infoMatrix to be same size nxn

    n = len(matrix) #number of rows, number of columns
    for row in range(n): #first initalize to the number of zeroes at a position,a value of one at each 0 and zero at each 1
        for col in range(n):
            numZeroes = 1 if matrix[row][col] == 0 else 0
            infoMatrix[row][col] = {
                "numZeroesBelow": numZeroes,
                "numZeroesRight": numZeroes,
            }

    #now using dynammic programming count from the last row upwards and backwards, the number of 0's below and to the right
    #like a getNeighbors function last row and last col dont have below and right 0's to add
    lastIdx = len(matrix) - 1 #endRow and endCol index since this is a nxn square matrix
    for row in reversed(range(n)): #start at the bottom right corner, ie last row upwards and backwards, backwards=right to left
        for col in reversed(range(n)): #start from bottom right corner, ie last row upwards and backwards, bottom to top,right to left
            if matrix[row][col] == 1: #for 1's. their numZeroesBelow and numZeroesRight stay 0, which is also served to neighbors
                continue #if 1, do nothing to numZeroesBelow and numZeroes, just move on
            if row < lastIdx: #elements in last row will never have below 0's to add
                infoMatrix[row][col]["numZeroesBelow"] += infoMatrix[row+1][col]["numZeroesBelow"]
            if col < lastIdx:
                infoMatrix[row][col]["numZeroesRight"] += infoMatrix[row][col+1]["numZeroesRight"]

    return infoMatrix


"""Iterative solution with precomputaion"""
#O(n^4) time | O(1) space
def squareOfZeroes(matrix):
    infoMatrix = preComputeNumOfZeroes(matrix) #precomputation
    n = len(matrix)
    for topRow in range(n): #choose the row of top left corner
        for leftCol in range(n): #choose corner of top left corner
            squareLength = 2 #squareLength goes is 2,3,4 up to len(matrix) -1, squareLength of 1 isn't valid
            while squareLength <= n - leftCol and squareLength <= n - topRow: #check that square length is valid for topRow,leftCol
                bottomRow = topRow + squareLength - 1 #remember that python is 0-indexed hence the -1 to get bottom row index
                rightCol  = leftCol + squareLength - 1 #remember that python is 0-indexed hence the -1 to get right column index
                if isSquareOfZeroes(infoMatrix,topRow,leftCol,bottomRow,rightCol): #if we find a square of zeroes
                    return True #return True
                squareLength += 1 #test next valid square size
    return False #othewise return false

def isSquareOfZeroes(infoMatrix,r1,c1,r2,c2): #O(1) avoids repeated work of iterating through r1 to r2 and c1 to c2
    squareLength = c2 - c1 + 1 #the length of the square, check if a square of this size is a square of zeroes
    hasTopBorder = infoMatrix[r1][c1]["numZeroesRight"] >= squareLength #from the top left to the top right corner
    hasLeftBorder = infoMatrix[r1][c1]["numZeroesBelow"]>= squareLength #from the top left to the bottom left corner
    hasBottomBorder = infoMatrix[r2][c1]["numZeroesRight"] >= squareLength #from the bottom left to the bottom right corner
    hasRightBorder = infoMatrix[r1][c2]["numZeroesBelow"]  >= squareLength  #from the top right to the bottom right corner
    return hasTopBorder and hasLeftBorder and hasBottomBorder and hasRightBorder

def preComputeNumOfZeroes(matrix): #O(n)
    infoMatrix = [[x for x in row] for row in matrix] #initialize the infoMatrix to be same size nxn
    n = len(matrix) #number of rows, number of columns
    for row in range(n): #first initalize to the number of zeroes at a position,a value of one at each 0 and zero at each 1
        for col in range(n):
            numZeroes = 1 if matrix[row][col] == 0 else 0
            infoMatrix[row][col] = {
                "numZeroesBelow": numZeroes,
                "numZeroesRight": numZeroes,
            }
    #now using dynammic programming count from the last row upwards and backwards, the number of 0's below and to the right
    #like a getNeighbors function last row and last col dont have below and right 0's to add
    lastIdx = len(matrix) - 1 #endRow and endCol index since this is a nxn square matrix
    for row in reversed(range(n)): #start at the bottom right corner, ie last row upwards and backwards, backwards=right to left
        for col in reversed(range(n)): #start from bottom right corner, ie last row upwards and backwards, bottom to top,right to left
            if matrix[row][col] == 1: #for 1's. their numZeroesBelow and numZeroesRight stay 0, which is also served to neighbors
                continue #if 1, do nothing to numZeroesBelow and numZeroes, just move on
            if row < lastIdx: #elements in last row will never have below 0's to add
                infoMatrix[row][col]["numZeroesBelow"] += infoMatrix[row+1][col]["numZeroesBelow"]
            if col < lastIdx:
                infoMatrix[row][col]["numZeroesRight"] += infoMatrix[row][col+1]["numZeroesRight"]
    return infoMatrix


matrix = [
    [0, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 1]
]
print(squareOfZeroes(matrix))